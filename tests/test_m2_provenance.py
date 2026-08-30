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
    def test_all_g2_accepted_scene_manifests_match_current_blobs(self) -> None:
        project = ROOT / "m2" / "e2e_scale"
        manifests = sorted((project / "provenance" / "v02").glob("S*.md"))

        self.assertEqual(10, len(manifests))
        for manifest in manifests:
            with self.subTest(manifest=manifest.name):
                result = provenance_check.evaluate_provenance(project, manifest)
                self.assertEqual("OK", result.status, "\n".join(result.mismatches))
                self.assertFalse(result.mismatches)


if __name__ == "__main__":
    unittest.main()
