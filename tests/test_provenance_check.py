from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.provenance_check import (
    evaluate_provenance,
    extract_markdown_slice,
    git_blob_sha,
)


class ProvenanceInvalidationTests(unittest.TestCase):
    def test_changed_upstream_blocks_accepted_downstream_until_marked_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            upstream = root / "upstream.txt"
            artifact = root / "artifact.txt"
            provenance = root / "provenance.md"

            upstream.write_text("alpha\n", encoding="utf-8")
            artifact.write_text("derived\n", encoding="utf-8")

            upstream_sha = git_blob_sha(upstream.read_bytes())
            artifact_sha = git_blob_sha(artifact.read_bytes())

            provenance.write_text(
                "\n".join(
                    [
                        "# Provenienz",
                        "",
                        "artifact: `artifact.txt`",
                        f"artifact_ref: `{artifact_sha}`",
                        "status: accepted",
                        "",
                        "## Upstream",
                        "",
                        f"- `upstream.txt` — blob `{upstream_sha}`",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            initial = evaluate_provenance(root, provenance)
            self.assertEqual("OK", initial.status)
            self.assertEqual((), initial.mismatches)

            upstream.write_text("beta\n", encoding="utf-8")
            changed = evaluate_provenance(root, provenance)
            self.assertEqual("BLOCK", changed.status)
            self.assertTrue(any("blob mismatch: upstream.txt" in item for item in changed.mismatches))

            provenance.write_text(
                provenance.read_text(encoding="utf-8").replace("status: accepted", "status: stale"),
                encoding="utf-8",
            )
            stale = evaluate_provenance(root, provenance)
            self.assertEqual("STALE_OK", stale.status)
            self.assertTrue(stale.mismatches)

    def test_unchanged_stale_manifest_is_not_silently_promoted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            upstream = root / "upstream.txt"
            artifact = root / "artifact.txt"
            provenance = root / "provenance.md"

            upstream.write_text("alpha\n", encoding="utf-8")
            artifact.write_text("derived\n", encoding="utf-8")
            upstream_sha = git_blob_sha(upstream.read_bytes())
            artifact_sha = git_blob_sha(artifact.read_bytes())

            provenance.write_text(
                "\n".join(
                    [
                        "artifact: `artifact.txt`",
                        f"artifact_ref: `{artifact_sha}`",
                        "status: stale",
                        f"- `upstream.txt` — blob `{upstream_sha}`",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            result = evaluate_provenance(root, provenance)
            self.assertEqual("OK", result.status)
            # The checker verifies hash consistency; it never upgrades the declared status.
            self.assertIn("upstream.txt", result.checked_refs)

    def test_slice_ref_ignores_unselected_table_row_but_blocks_selected_row(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            characters = root / "CHARACTERS.md"
            artifact = root / "scene.md"
            provenance = root / "provenance.md"

            characters.write_text(
                "\n".join(
                    [
                        "# CHARACTERS",
                        "",
                        "| Figur | Funktion |",
                        "|---|---|",
                        "| Nora Feld | POV |",
                        "| Jonas Rehm | Reporter |",
                        "",
                        "### A2 – Nora ↔ Jonas",
                        "",
                        "- Start: hohes Vertrauen.",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            artifact.write_text("scene\n", encoding="utf-8")

            selector = "table-row:Jonas Rehm"
            slice_sha = git_blob_sha(
                extract_markdown_slice(characters.read_text(encoding="utf-8"), selector).encode("utf-8")
            )
            artifact_sha = git_blob_sha(artifact.read_bytes())
            provenance.write_text(
                "\n".join(
                    [
                        "artifact: scene.md",
                        f"artifact_ref: {artifact_sha}",
                        "status: accepted",
                        f"- `CHARACTERS.md` — slice `{selector}` — blob `{slice_sha}`",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            initial = evaluate_provenance(root, provenance)
            self.assertEqual("OK", initial.status)

            characters.write_text(
                characters.read_text(encoding="utf-8").replace(
                    "| Nora Feld | POV |", "| Nora Feld | Investigativ-Leitung |"
                ),
                encoding="utf-8",
            )
            unrelated = evaluate_provenance(root, provenance)
            self.assertEqual("OK", unrelated.status)

            characters.write_text(
                characters.read_text(encoding="utf-8").replace(
                    "| Jonas Rehm | Reporter |", "| Jonas Rehm | Reporter mit Freigabepflicht |"
                ),
                encoding="utf-8",
            )
            selected = evaluate_provenance(root, provenance)
            self.assertEqual("BLOCK", selected.status)
            self.assertTrue(any("slice mismatch: CHARACTERS.md" in item for item in selected.mismatches))

            provenance.write_text(
                provenance.read_text(encoding="utf-8").replace("status: accepted", "status: stale"),
                encoding="utf-8",
            )
            stale = evaluate_provenance(root, provenance)
            self.assertEqual("STALE_OK", stale.status)

    def test_heading_slice_tracks_only_named_section(self) -> None:
        text = """# CHARACTERS

### A1 – Nora ↔ David

- Timingkonflikt.

### A2 – Nora ↔ Jonas

- Autonomievertrauen.

## Global

- Ende.
"""
        fragment = extract_markdown_slice(text, "heading:A2 – Nora ↔ Jonas")
        self.assertEqual(
            "### A2 – Nora ↔ Jonas\n\n- Autonomievertrauen.\n\n",
            fragment,
        )

    def test_unknown_or_ambiguous_slice_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source.md"
            artifact = root / "artifact.md"
            provenance = root / "provenance.md"
            source.write_text("| A | one |\n| A | two |\n", encoding="utf-8")
            artifact.write_text("x\n", encoding="utf-8")
            artifact_sha = git_blob_sha(artifact.read_bytes())
            provenance.write_text(
                "\n".join(
                    [
                        "artifact: artifact.md",
                        f"artifact_ref: {artifact_sha}",
                        "status: accepted",
                        "- `source.md` — slice `table-row:A` — blob `0000000000000000000000000000000000000000`",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            result = evaluate_provenance(root, provenance)
            self.assertEqual("BLOCK", result.status)
            self.assertTrue(any("slice is ambiguous" in item for item in result.mismatches))


if __name__ == "__main__":
    unittest.main()
