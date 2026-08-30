# BUILD MANIFEST – SPERRFRIST M2

status: G5_APPROVED
date: 2026-08-30
format: standalone HTML reading/print artifact
artifact_name: `SPERRFRIST_v01.html`
distribution: GitHub Actions artifact `m2-sperrfrist-production`
human_gate: G5 APPROVE
gate_ref: `89f4cb5d84d0fb3b2935f3dc7dc33d5604f763be`

## Freigegebene Quelle

- `MANUSCRIPT_v01.md` — G4-approved blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`
- `gates/G4.md` — blob `0d462e477fceb319ed7db9146e1c56f66b1fa6ef`

## Builder

- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`
- Aufruf: `python scripts/build_html.py m2/e2e_scale/MANUSCRIPT_v01.md m2/e2e_scale/production/SPERRFRIST_v01.html`

## Kanonischer Produktionsnachweis

Framework Validation Run #48 / ID `33315932510`:

- Build-Commit: `f7425fa0cccdb960722d80fd34780b33290d223c`
- Framework-Tests: 60/60 PASS
- G4-Manuskript-Blob-Match: PASS
- bytegenauer deterministischer HTML-Build: PASS
- Artifact-ID: `9733432615`
- HTML SHA-256: `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`
- Artifact-ZIP SHA-256: `ba326c8de39a3580e7f66221788769e20d3338f13882beae865cc7a1543d15f8`
- Artifact-Größe: 17,256 Bytes
- Actions-Ablaufdatum: 2026-11-28 14:05:55 UTC

Final-State-Check Run #49 / ID `33316104195`: PASS. Der Run bestätigte erneut exakt den G4-Manuskript-Blob, den bytegenauen Builder-Output und denselben HTML-SHA-256 `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`.

## Produktionsidentität

Der durch G5 freigegebene Produktionsstand ist nicht durch eine dauerhaft eingecheckte HTML-Datei definiert, sondern durch:

1. den G4-approved Manuskript-Blob,
2. den versionierten Builder,
3. den reproduzierten HTML-SHA-256,
4. den realen Build-Nachweis in Run #48 und den Wiederholungsnachweis in Run #49.

Damit bleibt der Produktionsstand auch nach Ablauf des konkreten Actions-Artefakts reproduzierbar.

## Scope

M2 baut bewusst keine DOCX/PDF/KDP-Pipeline. Das HTML dient wie in M1 als minimales reales Produktionsartefakt für Reproduzierbarkeit, Provenienz und Human Gate G5.
