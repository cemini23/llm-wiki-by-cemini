import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.agent_reach_daily_social import run_agent_reach_social_pass


class AgentReachDailySocialTests(unittest.TestCase):
    def test_daily_social_pass_normalizes_fake_opencli_yaml(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "config").mkdir()
            (repo / "config" / "agent_reach_daily_sources.example.json").write_text(
                json.dumps(
                    {
                        "allowed_sources": ["manual_snapshot"],
                        "allowed_domains": ["x.com"],
                        "allowed_author_or_channel": ["*"],
                    }
                ),
                encoding="utf-8",
            )
            command = [
                sys.executable,
                "-c",
                "print('- author: test_author\\n  text: Synthetic social discovery row.\\n  url: https://x.com/test_author/status/1')",
            ]
            cfg = {
                "agent_reach_social": {
                    "enabled": True,
                    "timeout_seconds": 10,
                    "max_items_per_query": 5,
                    "allowlist": "config/agent_reach_daily_sources.example.json",
                    "queries": [
                        {
                            "cluster": "fake-x",
                            "platform": "twitter",
                            "command": command,
                        }
                    ],
                }
            }

            result = run_agent_reach_social_pass(repo, cfg, date(2026, 7, 3))

            self.assertTrue(result.enabled)
            self.assertTrue(result.ok)
            self.assertTrue(result.output_path and result.output_path.exists())
            payload = json.loads(result.output_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["mode"], "DRY_RUN")
            self.assertEqual(payload["items"][0]["operator_review"], True)
            self.assertIn("Agent Reach social pass", "\n".join(result.lines))


if __name__ == "__main__":
    unittest.main()
