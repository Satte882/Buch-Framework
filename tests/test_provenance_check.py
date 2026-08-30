from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.provenance_check import evaluate_provenance, git_blob_sha


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


if __name__ == "__main__":
    unittest.main()
