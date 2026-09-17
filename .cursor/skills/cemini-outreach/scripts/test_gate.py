#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GATE = HERE / "gate.py"


def run_csv(text: str, campaign: str) -> tuple[int, dict]:
    p = Path(tempfile.mkdtemp()) / "t.csv"
    p.write_text(text)
    r = subprocess.run(
        [sys.executable, str(GATE), "--csv", str(p), "--campaign", campaign],
        capture_output=True,
        text=True,
    )
    return r.returncode, json.loads(r.stdout)


ATTO_URL = "https://youratto.com/?utm_source=email&utm_medium=outreach&utm_campaign=atto"
GW_URL = "https://guruwatcher.com/?utm_source=email&utm_medium=outreach&utm_campaign=gw"


def test_atto_pass():
    code, out = run_csv(
        "name,contact,draft_subject,draft_body,status\n"
        "Firm,a@example.com,subj,"
        f'"Hi\\n\\nYour page names the six-month estratto. Atto is a local folder. {ATTO_URL}\\nClaudio Barone\\nyouratto.com",human\n',
        "atto",
    )
    assert code == 0, out
    assert out["ok_to_send"] == ["a@example.com"]


def test_atto_com_banned():
    code, out = run_csv(
        "name,contact,draft_subject,draft_body,status\n"
        "Firm,a@example.com,subj,"
        '"See atto.com please. Claudio Barone\\nyouratto.com",human\n',
        "atto",
    )
    assert code == 1
    assert "atto.com_domain" in out["fail"][0]["reasons"]


def test_form_not_fail():
    code, out = run_csv(
        "name,contact,draft_subject,draft_body,status\n"
        "Firm,https://example.com/contact,subj,body,draft\n",
        "atto",
    )
    assert code == 0, out
    assert out["rows"][0]["verdict"] == "form"


def test_youratto_allowed():
    code, out = run_csv(
        "name,contact,draft_subject,draft_body,status\n"
        "Firm,a@example.com,subj,"
        f'"Hi\\n\\nDetail. {ATTO_URL}\\nClaudio Barone\\nyouratto.com",human\n',
        "atto",
    )
    assert code == 0, out


def test_missing_tracked_url_fails():
    code, out = run_csv(
        "name,contact,draft_subject,draft_body,status\n"
        "Firm,a@example.com,subj,"
        '"Hi\\n\\nDetail. Claudio Barone\\nyouratto.com",human\n',
        "atto",
    )
    assert code == 1
    assert "missing_tracked_url" in out["fail"][0]["reasons"]


def test_gw_tracked_url():
    code, out = run_csv(
        "name,public_email,draft_subject,draft_body,status\n"
        "Writer,b@example.com,subj,"
        f'"Hi\\n\\nOne public print. {GW_URL}\\nClaudio Barone\\nguruwatcher.com",human\n',
        "gw",
    )
    assert code == 0, out
    assert out["ok_to_send"] == ["b@example.com"]


if __name__ == "__main__":
    test_atto_pass()
    test_atto_com_banned()
    test_form_not_fail()
    test_youratto_allowed()
    test_missing_tracked_url_fails()
    test_gw_tracked_url()
    print("ok")
