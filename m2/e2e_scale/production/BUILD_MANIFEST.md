# BUILD MANIFEST – SPERRFRIST M2

status: READY_FOR_BUILD_VALIDATION
date: 2026-08-30
format: standalone HTML reading/print artifact
artifact_name: `SPERRFRIST_v01.html`
distribution: GitHub Actions artifact `m2-sperrfrist-production`

## Freigegebene Quelle

- `MANUSCRIPT_v01.md` — G4-approved blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`
- `gates/G4.md` — blob `0d462e477fceb319ed7db9146e1c56f66b1fa6ef`

## Builder

- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`
- Aufruf: `python scripts/build_html.py m2/e2e_scale/MANUSCRIPT_v01.md m2/e2e_scale/production/SPERRFRIST_v01.html`

## Deterministische Produktions-QA

CI muss vor G5 nachweisen:

1. `git hash-object MANUSCRIPT_v01.md` entspricht exakt dem G4-approved Blob,
2. HTML wird ausschließlich mit dem bestehenden Builder aus diesem Manuskript erzeugt,
3. erzeugtes HTML entspricht byte-für-byte `build_document(source)`,
4. SHA-256 des erzeugten HTML wird als Begleitdatei ausgegeben,
5. HTML + SHA-256 werden gemeinsam als GitHub-Actions-Artefakt hochgeladen.

## Scope

M2 baut bewusst keine DOCX/PDF/KDP-Pipeline. Das HTML dient wie in M1 als minimales reales Produktionsartefakt für Reproduzierbarkeit, Provenienz und G5.

## G5

Human Gate G5 bleibt bis zum erfolgreichen realen CI-Build offen. Nach dem Build werden Run, Artifact-ID und HTML-SHA-256 in diesem Manifest ergänzt.
