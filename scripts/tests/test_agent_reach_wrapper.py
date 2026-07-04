import tempfile
import unittest
from pathlib import Path

from scripts.agent_reach_wrapper import SourceAllowlist, load_snapshot, process_captures
from scripts.agent_reach_wrapper.cli import main as cli_main
from scripts.agent_reach_wrapper.schema import SchemaError, validate_capture_schema


FIXTURE_DIR = Path("fixtures/agent_reach_wrapper")
ALLOWLIST = Path("config/agent_reach_sources.example.json")


class AgentReachWrapperTests(unittest.TestCase):
    def test_accepts_benign_snapshot_and_requires_operator_review(self):
        allowlist = SourceAllowlist.from_file(ALLOWLIST)
        captures = load_snapshot(FIXTURE_DIR / "benign_snapshot.json")

        result = process_captures(captures, allowlist)

        self.assertTrue(result.ok)
        self.assertEqual(len(result.items), 2)
        self.assertTrue(all(item["operator_review"] is True for item in result.items))
        self.assertTrue(all(item["content_hash"].startswith("sha256:") for item in result.items))

    def test_rejects_prompt_injection_fixture(self):
        allowlist = SourceAllowlist.from_file(ALLOWLIST)
        captures = load_snapshot(FIXTURE_DIR / "malicious_prompt_injection.json")

        result = process_captures(captures, allowlist)

        self.assertFalse(result.ok)
        self.assertEqual(result.rejections[0].reason, "PROMPT_INJECTION_REJECTED")

    def test_rejects_unknown_domain_fixture(self):
        allowlist = SourceAllowlist.from_file(ALLOWLIST)
        captures = load_snapshot(FIXTURE_DIR / "unknown_domain.json")

        result = process_captures(captures, allowlist)

        self.assertFalse(result.ok)
        self.assertEqual(result.rejections[0].reason, "ALLOWLIST_REJECTED")

    def test_rejects_duplicate_content_fixture(self):
        allowlist = SourceAllowlist.from_file(ALLOWLIST)
        captures = load_snapshot(FIXTURE_DIR / "duplicates.json")

        result = process_captures(captures, allowlist)

        self.assertFalse(result.ok)
        self.assertEqual(result.rejections[0].reason, "SNAPSHOT_REJECTED")

    def test_rejects_empty_capture_fixture(self):
        allowlist = SourceAllowlist.from_file(ALLOWLIST)
        captures = load_snapshot(FIXTURE_DIR / "empty_capture.json")

        result = process_captures(captures, allowlist)

        self.assertFalse(result.ok)
        self.assertEqual(result.rejections[0].reason, "EMPTY_CAPTURE")

    def test_rejects_cookie_or_session_fields(self):
        with self.assertRaises(SchemaError):
            validate_capture_schema(
                {
                    "source": "manual_snapshot",
                    "source_url": "https://x.com/osint_fixture/status/5001",
                    "author_or_channel": "@osint_fixture",
                    "captured_at": "2026-07-03T18:30:00Z",
                    "raw_text": "Synthetic fixture.",
                    "license_or_terms_note": "Synthetic fixture for local validation only.",
                    "cookies": "do-not-commit",
                }
            )

    def test_cli_writes_local_output_and_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp)
            out = workspace / ".local" / "agent-reach-wrapper" / "normalized-social-items.json"
            audit = workspace / ".local" / "agent-reach-wrapper" / "audit.jsonl"

            code = cli_main(
                [
                    "--snapshot",
                    str(FIXTURE_DIR / "benign_snapshot.json"),
                    "--allowlist",
                    str(ALLOWLIST),
                    "--out",
                    str(out),
                    "--audit",
                    str(audit),
                    "--workspace",
                    str(workspace),
                ]
            )

            self.assertEqual(code, 0)
            self.assertTrue(out.exists())
            self.assertTrue(audit.exists())

    def test_cli_rejects_output_outside_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = Path(tmp) / "workspace"
            workspace.mkdir()

            code = cli_main(
                [
                    "--snapshot",
                    str(FIXTURE_DIR / "benign_snapshot.json"),
                    "--allowlist",
                    str(ALLOWLIST),
                    "--out",
                    str(Path(tmp) / "outside.json"),
                    "--audit",
                    str(workspace / ".local" / "audit.jsonl"),
                    "--workspace",
                    str(workspace),
                ]
            )

            self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
