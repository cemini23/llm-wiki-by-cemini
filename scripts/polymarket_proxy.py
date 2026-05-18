#!/usr/bin/env python3
"""CONNECT-tunneling forward proxy — routes HTTPS through Surfshark IP.

Supports CONNECT method so clients can use it as a standard HTTPS proxy
(curl --proxy, https_proxy env var, requests.Session.proxies, etc.).

Run on laptop while connected to Surfshark (non-US server).
Share port back to cemini-prod via: ssh -R 8888:localhost:8888 cemini-prod -N
"""
import socket
import threading
import select
import sys

LISTEN = ("127.0.0.1", 8888)
BUFSIZE = 65536

def relay(src, dst, name):
    """Bidirectional byte relay between two sockets."""
    try:
        while True:
            ready, _, _ = select.select([src], [], [], 30)
            if not ready:
                break
            data = src.recv(BUFSIZE)
            if not data:
                break
            dst.sendall(data)
    except Exception:
        pass
    finally:
        try:
            src.close()
        except Exception:
            pass
        try:
            dst.close()
        except Exception:
            pass

def handle(conn):
    """Handle one client connection. Read CONNECT line, tunnel to target."""
    try:
        req = b""
        while b"\r\n\r\n" not in req:
            chunk = conn.recv(BUFSIZE)
            if not chunk:
                conn.close()
                return
            req += chunk

        line = req.split(b"\r\n")[0].decode()
        method, target, _ = line.split()
        host, port = target.split(":")
        port = int(port)

        if method != "CONNECT":
            conn.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            conn.close()
            return

        print(f"[proxy] CONNECT {host}:{port}", flush=True)
        remote = socket.create_connection((host, port), timeout=10)
        conn.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")

        # Bidirectional relay
        t1 = threading.Thread(target=relay, args=(conn, remote, "c2r"), daemon=True)
        t2 = threading.Thread(target=relay, args=(remote, conn, "r2c"), daemon=True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except Exception as e:
        print(f"[proxy] error: {e}", flush=True)
        try:
            conn.close()
        except Exception:
            pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(LISTEN)
    sock.listen(32)
    print(f"[proxy] CONNECT tunnel proxy → clob.polymarket.com", flush=True)
    print(f"[proxy] listening on {LISTEN[0]}:{LISTEN[1]}", flush=True)

    while True:
        try:
            conn, addr = sock.accept()
            threading.Thread(target=handle, args=(conn,), daemon=True).start()
        except KeyboardInterrupt:
            break
    sock.close()
    print("\n[proxy] stopped", flush=True)

if __name__ == "__main__":
    main()
