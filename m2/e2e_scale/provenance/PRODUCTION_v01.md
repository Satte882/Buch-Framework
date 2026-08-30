# PROVENANCE – M2 PRODUCTION SPERRFRIST v0.1

status: draft
artifact: GitHub Actions artifact `m2-sperrfrist-production/SPERRFRIST_v01.html`
artifact_ref: sha256:233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb
generated_via: `scripts/build_html.py`
action: build_from_G4_approved_manuscript
date: 2026-08-30
purpose: Reproduzierbares minimales Produktionsartefakt für Human Gate G5.
gate_basis: G4 APPROVE
review_status: awaiting_human_G5

## Upstream refs

- `MANUSCRIPT_v01.md` — blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`
- `gates/G4.md` — blob `0d462e477fceb319ed7db9146e1c56f66b1fa6ef`
- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`
- `production/BUILD_MANIFEST.md` — candidate blob `7eb86e36cd1c3fc8be15c8de7197e92828e8dbf3`

## Build-Identität

- Framework Validation Run #48 / ID `33315932510` — **success**
- Build-Commit: `f7425fa0cccdb960722d80fd34780b33290d223c`
- GitHub Actions Artifact: `m2-sperrfrist-production`
- Artifact-ID: `9733432615`
- HTML SHA-256: `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`
- Artifact-ZIP SHA-256: `ba326c8de39a3580e7f66221788769e20d3338f13882beae865cc7a1543d15f8`
- G4-Source-Blob-Check: **PASS**
- byte-für-byte deterministischer Build: **PASS**
- Tests: **60/60 PASS**

## Speicher-/Reproduzierbarkeitsgrenze

Das konkrete GitHub-Actions-Artefakt läuft laut GitHub-Metadaten am 2026-11-28 aus. Seine Identität ist durch Artifact-ID und Hash dokumentiert. Der gleiche HTML-Output ist aus dem referenzierten G4-Manuskript und Builder reproduzierbar.

## Gültigkeit

Dieser Produktionsstand ist real gebaut und deterministisch verifiziert, aber noch nicht durch Human Gate G5 `accepted`. Bis dahin bleibt der Provenienzstatus `draft`.

Eine Änderung des G4-Manuskript-Blobs blockiert diesen Produktionsstand und erfordert Backtracking zu G4. Eine reine Produktionsänderung erzeugt einen neuen Output-Hash und benötigt eine neue G5-Entscheidung.
