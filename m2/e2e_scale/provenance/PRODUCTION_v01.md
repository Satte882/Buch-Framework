# PROVENANCE – M2 PRODUCTION SPERRFRIST v0.1

status: accepted
artifact: GitHub Actions artifact `m2-sperrfrist-production/SPERRFRIST_v01.html`
artifact_ref: sha256:233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb
generated_via: `scripts/build_html.py`
action: build_from_G4_approved_manuscript
date: 2026-08-30
purpose: Reproduzierbares minimales Produktionsartefakt für M2.
gate_basis: G5 APPROVE
gate_ref: 89f4cb5d84d0fb3b2935f3dc7dc33d5604f763be
review_status: human_G5_approved

## Upstream refs

- `MANUSCRIPT_v01.md` — blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`
- `gates/G4.md` — blob `0d462e477fceb319ed7db9146e1c56f66b1fa6ef`
- `gates/G5.md` — blob `89f4cb5d84d0fb3b2935f3dc7dc33d5604f763be`
- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`
- `production/BUILD_MANIFEST.md` — G5-final blob `72f4c747702090250e9a0685cc53f81b7aa8dc09`

## Build evidence

- kanonischer Produktionslauf: Framework Validation Run #48 / ID `33315932510`
- Build-Commit: `f7425fa0cccdb960722d80fd34780b33290d223c`
- Artifact-ID: `9733432615`
- HTML SHA-256: `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`
- Artifact-ZIP SHA-256: `ba326c8de39a3580e7f66221788769e20d3338f13882beae865cc7a1543d15f8`
- Final-State-Wiederholung: Run #49 / ID `33316104195` = PASS; identischer HTML-SHA-256

## Gültigkeit

Dieser konkrete Produktionsstand ist durch Human Gate G5 `accepted`. Eine Änderung des G4-Manuskript-Blobs macht ihn fachlich ungültig und erfordert Backtracking zu G4. Eine reine Änderung am Produktionsmarkup erzeugt einen anderen Output-Hash und benötigt eine neue G5-Entscheidung.

Das zeitlich befristete Actions-Artefakt ist nicht die alleinige Source of Truth. Die Produktionsidentität bleibt über Manuskript-Blob + Builder + HTML-Hash reproduzierbar.
