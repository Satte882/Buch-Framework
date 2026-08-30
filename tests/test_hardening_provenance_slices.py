from __future__ import annotations

import re
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.provenance_check import (
    evaluate_provenance,
    extract_markdown_slice,
    git_blob_sha,
)

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "m2" / "e2e_scale"


def scene_sort_key(scene_id: str) -> int:
    return int(re.fullmatch(r"S(\d+)", scene_id).group(1))


class HardeningProvenanceSliceIntegrationTest(unittest.TestCase):
    def test_m2_jonas_change_reduces_blast_radius_without_losing_blocks(self) -> None:
        jonas_scenes = {
            path.name.split("_", 1)[0]
            for path in (PROJECT / "character_states").glob("S*_JONAS.md")
        }
        self.assertEqual({"S2", "S3", "S5", "S6", "S8", "S10"}, jonas_scenes)

        scene_ids = [f"S{number}" for number in range(1, 11)]

        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "scenes").mkdir()
            (project / "provenance").mkdir()
            shutil.copy2(PROJECT / "CHARACTERS.md", project / "CHARACTERS.md")

            for scene_id in scene_ids:
                shutil.copy2(PROJECT / "scenes" / f"{scene_id}.md", project / "scenes" / f"{scene_id}.md")

            characters_text = (project / "CHARACTERS.md").read_text(encoding="utf-8")
            jonas_selector = "table-row:Jonas Rehm"
            nora_selector = "table-row:Nora Feld"
            jonas_sha = git_blob_sha(
                extract_markdown_slice(characters_text, jonas_selector).encode("utf-8")
            )
            nora_sha = git_blob_sha(
                extract_markdown_slice(characters_text, nora_selector).encode("utf-8")
            )

            manifests: dict[str, Path] = {}
            for scene_id in scene_ids:
                scene_rel = f"scenes/{scene_id}.md"
                scene_sha = git_blob_sha((project / scene_rel).read_bytes())
                manifest = project / "provenance" / f"{scene_id}.md"
                manifests[scene_id] = manifest

                refs = [
                    f"- `CHARACTERS.md` — slice `{nora_selector}` — blob `{nora_sha}`"
                ]
                if scene_id in jonas_scenes:
                    refs.append(
                        f"- `CHARACTERS.md` — slice `{jonas_selector}` — blob `{jonas_sha}`"
                    )

                manifest.write_text(
                    "\n".join(
                        [
                            f"# HARDENING PROVENANCE – {scene_id}",
                            "",
                            "status: accepted",
                            f"artifact: {scene_rel}",
                            f"artifact_ref: {scene_sha}",
                            "",
                            "## Character dependencies",
                            "",
                            *refs,
                        ]
                    )
                    + "\n",
                    encoding="utf-8",
                )

            baseline = {
                scene_id: evaluate_provenance(project, manifest).status
                for scene_id, manifest in manifests.items()
            }
            self.assertEqual({scene_id: "OK" for scene_id in scene_ids}, baseline)

            changed = characters_text.replace(
                "fachlich stark, schnell, neigt unter Zeitdruck zu zu konkreten Verifikationsanfragen",
                "fachlich stark; externe Kontakte sind von Beginn an nur nach expliziter Freigabe durch Nora erlaubt",
            )
            self.assertNotEqual(characters_text, changed, "M2 Jonas test injection no longer matches fixture")
            (project / "CHARACTERS.md").write_text(changed, encoding="utf-8")

            after_change = {
                scene_id: evaluate_provenance(project, manifest).status
                for scene_id, manifest in manifests.items()
            }
            blocked = {scene_id for scene_id, status in after_change.items() if status == "BLOCK"}
            still_ok = {scene_id for scene_id, status in after_change.items() if status == "OK"}

            self.assertEqual(jonas_scenes, blocked)
            self.assertEqual(set(scene_ids) - jonas_scenes, still_ok)
            self.assertEqual(6, len(blocked))
            self.assertEqual(4, len(still_ok))
            self.assertLess(len(blocked), 10)

            for scene_id in blocked:
                manifest = manifests[scene_id]
                manifest.write_text(
                    manifest.read_text(encoding="utf-8").replace(
                        "status: accepted", "status: stale"
                    ),
                    encoding="utf-8",
                )

            after_stale = {
                scene_id: evaluate_provenance(project, manifest).status
                for scene_id, manifest in manifests.items()
            }
            for scene_id in scene_ids:
                expected = "STALE_OK" if scene_id in jonas_scenes else "OK"
                self.assertEqual(expected, after_stale[scene_id], scene_id)


if __name__ == "__main__":
    unittest.main()
