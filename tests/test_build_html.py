from __future__ import annotations

import unittest
from pathlib import Path

from scripts.build_html import build_document


REPO_ROOT = Path(__file__).resolve().parents[1]


class HtmlBuildTests(unittest.TestCase):
    def test_fehlalarm_v02_production_artifact_rebuilds_byte_for_byte(self) -> None:
        manuscript = REPO_ROOT / "m1/e2e_minibook/MANUSCRIPT_v02.md"
        output = REPO_ROOT / "m1/e2e_minibook/production/FEHLALARM_v02.html"

        rebuilt = build_document(manuscript.read_text(encoding="utf-8"))
        committed = output.read_text(encoding="utf-8")

        self.assertEqual(committed, rebuilt)

    def test_builder_preserves_prose_text_while_changing_markup(self) -> None:
        source = "# Titel\n\n## S1\n\nMara & Nils.\n"
        result = build_document(source)

        self.assertIn("<h1>Titel</h1>", result)
        self.assertIn("<h2>S1</h2>", result)
        self.assertIn("<p>Mara &amp; Nils.</p>", result)
        self.assertNotIn("# Titel", result)


if __name__ == "__main__":
    unittest.main()
