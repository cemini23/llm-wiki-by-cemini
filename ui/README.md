# Cemini AI — chat UI

Local browser front-end for the Cemini AI gateway running on `cemini-egress-fi:8088`.

## How it fits

```
browser  ->  http://127.0.0.1:9000/                   (this folder: serve.py + index.html)
                       |
                       |  /chat, /health proxied to
                       v
             http://127.0.0.1:8088/...                 (SSH tunnel)
                       |
                       v
             cemini-egress-fi:8088 (FastAPI gateway)
```

The proxy exists so the browser and the gateway share an origin — the gateway has no
CORS middleware and we don't want to modify it just for a dev UI.

## Run

Open the SSH tunnel (backgrounded; uses local port `8288` to avoid clashes
with `8088 → cemini-librarian:8080` (stash) and `8188 → ComfyUI`):

```sh
ssh -fN -L 8288:127.0.0.1:8088 cemini-egress-fi
```

Start the UI server:

```sh
python3 ui/serve.py
```

Then open <http://127.0.0.1:9000/>.

Python 3.11+, no dependencies. Override ports with `CEMINI_AI_GATEWAY_PORT`
(default `8288`) and `CEMINI_AI_UI_PORT` (default `9000`).

Close the tunnel later with:

```sh
pkill -f "ssh.*8288:127.0.0.1:8088.*cemini-egress-fi"
```

## Features

- Chat thread with user / AI bubbles, Enter to send (Shift+Enter for newline).
- Live `/health` badge polling every 10 s — overall status + per-component dots
  (kb_server, stash, conductor, deepseek). Falls to red with "tunnel?" if the
  proxy can't reach the gateway.
- Per-response trace footer: elapsed time, kb sources, stash episodes, conductor route.
- Surfaces `proposed_action` payloads when the gateway emits them.

## Limits / future work

- Single-turn `/chat` (the gateway has no `conversation_id` yet — Phase 3 item).
- No streaming — gateway returns the full JSON body on completion (~3–12 s).
- No auth — internal-only, locked to `127.0.0.1` listen address.
- If we later host the UI on `cemini-egress-fi` itself, mount `index.html` as
  FastAPI static files and retire this proxy.
