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
    def test_all_accepted_scene_manifests_block_after_relevant_upstream_drift(self) -> None:
        project = ROOT / "m2" / "e2e_scale"
        manifests = sorted((project / "provenance" / "v02").glob("S*.md"))

        self.assertEqual(10, len(manifests))
        blocked = 0
        for manifest in manifests:
            with self.subTest(manifest=manifest.name):
                result = provenance_check.evaluate_provenance(project, manifest)
                self.assertEqual("BLOCK", result.status)
                self.assertTrue(
                    any("CHARACTERS.md" in item for item in result.mismatches),
                    "Expected CHARACTERS.md blob drift to be visible",
                )
                blocked += 1

        self.assertEqual(10, blocked)


if __name__ == "__main__":
    unittest.main()
