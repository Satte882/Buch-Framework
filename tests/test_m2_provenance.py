from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import provenance_check  # noqa: E402


class M2SceneProvenanceIntegrationTest(unittest.TestCase):
    def test_all_explicitly_stale_scene_manifests_report_stale_ok(self) -> None:
        project = ROOT / "m2" / "e2e_scale"
        manifests = sorted((project / "provenance" / "v02").glob("S*.md"))

        self.assertEqual(10, len(manifests))
        stale_ok = 0
        for manifest in manifests:
            with self.subTest(manifest=manifest.name):
                result = provenance_check.evaluate_provenance(project, manifest)
                self.assertEqual("STALE_OK", result.status)
                self.assertTrue(
                    any("CHARACTERS.md" in item for item in result.mismatches),
                    "Expected CHARACTERS.md drift to remain visible after stale marking",
                )
                stale_ok += 1

        self.assertEqual(10, stale_ok)


if __name__ == "__main__":
    unittest.main()
