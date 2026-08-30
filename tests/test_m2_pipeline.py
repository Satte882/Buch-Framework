from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import pipeline_check  # noqa: E402
import scene_readiness  # noqa: E402


class M2PipelineIntegrationTest(unittest.TestCase):
    def test_sperrfrist_is_ready_for_prose_after_human_g2(self) -> None:
        pipeline_config = pipeline_check.load_config(ROOT / "config" / "pipeline_contract.yml")
        scene_config = scene_readiness.load_config(ROOT / "config" / "scene_readiness.yml")

        result = pipeline_check.evaluate_project(
            ROOT / "m2" / "e2e_scale",
            pipeline_config,
            scene_config,
        )

        self.assertEqual("READY_FOR_PROSE", result.status, "\n".join(result.issues))
        self.assertEqual(10, len(result.active_scenes))
        self.assertFalse(result.issues)


if __name__ == "__main__":
    unittest.main()
