from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import prosa_audit  # noqa: E402
import provenance_check  # noqa: E402


class M2ManuscriptIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.project = ROOT / "m2" / "e2e_scale"
        self.drafts = self.project / "drafts" / "v01"
        self.manuscript = self.project / "MANUSCRIPT_v01.md"

    def test_manuscript_is_exact_concatenation_of_ten_drafts(self) -> None:
        parts = [
            (self.drafts / f"S{i}.md").read_text(encoding="utf-8").strip()
            for i in range(1, 11)
        ]
        expected = (
            "# SPERRFRIST\n\n"
            "M2 10-Szenen-Manuskript v0.1\n\n"
            + "\n\n---\n\n".join(parts)
            + "\n"
        )
        actual = self.manuscript.read_text(encoding="utf-8")
        self.assertEqual(expected, actual)

    def test_full_manuscript_has_no_deterministic_prose_fail(self) -> None:
        text = self.manuscript.read_text(encoding="utf-8")
        config = prosa_audit.load_config(ROOT / "config" / "prosa_rules.yml")
        findings = prosa_audit.audit_text(text, config)
        totals = prosa_audit.counts(findings)
        print(
            f"M2 FULL MANUSCRIPT AUDIT: FAIL={totals['FAIL']} "
            f"REVIEW={totals['REVIEW']} INFO={totals['INFO']}"
        )
        for finding in findings:
            print(
                f"M2 MANUSCRIPT FINDING: {finding.severity} "
                f"{finding.rule_id} {finding.chapter} {finding.excerpt}"
            )
        self.assertEqual(0, totals["FAIL"])

    def test_full_manuscript_does_not_leak_framework_labels(self) -> None:
        text = self.manuscript.read_text(encoding="utf-8")
        forbidden = ("Quelle A", "Quelle B", "T/K", "BT001", "BT0")
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, text)

    def test_all_ten_prose_manifests_match_current_upstream(self) -> None:
        manifests = {
            1: self.project / "provenance" / "g3_sample" / "S1.md",
            2: self.project / "provenance" / "g3_scaled" / "S2.md",
            3: self.project / "provenance" / "g3_scaled" / "S3.md",
            4: self.project / "provenance" / "g3_scaled" / "S4.md",
            5: self.project / "provenance" / "g3_sample" / "S5.md",
            6: self.project / "provenance" / "g3_scaled" / "S6.md",
            7: self.project / "provenance" / "g3_scaled" / "S7.md",
            8: self.project / "provenance" / "g3_sample" / "S8.md",
            9: self.project / "provenance" / "g3_scaled" / "S9.md",
            10: self.project / "provenance" / "g3_scaled" / "S10.md",
        }
        for scene_id, manifest in manifests.items():
            with self.subTest(scene=scene_id):
                result = provenance_check.evaluate_provenance(self.project, manifest)
                self.assertEqual("OK", result.status, "\n".join(result.mismatches))
                self.assertFalse(result.mismatches)

    def test_manuscript_provenance_matches_current_draft_blobs(self) -> None:
        manifest = self.project / "provenance" / "MANUSCRIPT_v01.md"
        result = provenance_check.evaluate_provenance(self.project, manifest)
        self.assertEqual("OK", result.status, "\n".join(result.mismatches))
        self.assertFalse(result.mismatches)


if __name__ == "__main__":
    unittest.main()
