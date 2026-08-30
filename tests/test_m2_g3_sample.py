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


class M2G3SampleIntegrationTest(unittest.TestCase):
    def test_sperrfrist_g3_sample_has_no_deterministic_prose_fail(self) -> None:
        project = ROOT / "m2" / "e2e_scale"
        paths = [project / "drafts" / "v01" / name for name in ("S1.md", "S5.md", "S8.md")]
        text = "\n\n".join(path.read_text(encoding="utf-8") for path in paths)

        config = prosa_audit.load_config(ROOT / "config" / "prosa_rules.yml")
        findings = prosa_audit.audit_text(text, config)
        totals = prosa_audit.counts(findings)
        print(f"M2 G3 SAMPLE AUDIT: FAIL={totals['FAIL']} REVIEW={totals['REVIEW']} INFO={totals['INFO']}")
        for finding in findings:
            print(f"M2 G3 FINDING: {finding.severity} {finding.rule_id} {finding.chapter} {finding.excerpt}")

        self.assertEqual(0, totals["FAIL"])

    def test_sperrfrist_g3_draft_provenance_matches_current_upstream(self) -> None:
        project = ROOT / "m2" / "e2e_scale"
        manifests = [project / "provenance" / "g3_sample" / name for name in ("S1.md", "S5.md", "S8.md")]

        for manifest in manifests:
            with self.subTest(manifest=manifest.name):
                result = provenance_check.evaluate_provenance(project, manifest)
                self.assertEqual("OK", result.status, "\n".join(result.mismatches))
                self.assertFalse(result.mismatches)


if __name__ == "__main__":
    unittest.main()
