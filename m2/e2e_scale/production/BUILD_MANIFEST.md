# BUILD MANIFEST – SPERRFRIST M2

status: READY_FOR_HUMAN_G5
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

## Reale Build-Ausführung

- Framework Validation: Run **#48** / ID `33315932510` — **PASS**
- Build-Commit: `f7425fa0cccdb960722d80fd34780b33290d223c`
- Tests: **60/60 PASS**
- G4-Source-Blob-Check: **PASS** (`55753bb0ce177a80886343a8ac4e23a71de05c4a`)
- HTML-Build: **PASS**
- byte-für-byte Vergleich mit `build_document(source)`: **PASS**

## Konkretes Produktionsartefakt

- Artifact-Name: `m2-sperrfrist-production`
- GitHub Actions Artifact-ID: `9733432615`
- enthaltene Dateien:
  - `SPERRFRIST_v01.html`
  - `SPERRFRIST_v01.sha256`
- HTML SHA-256: `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`
- Artifact-ZIP SHA-256: `ba326c8de39a3580e7f66221788769e20d3338f13882beae865cc7a1543d15f8`
- Artifact-Größe: 17,256 Bytes
- erstellt: 2026-08-30 14:06:07 UTC
- GitHub-Actions-Ablaufdatum: 2026-11-28 14:05:55 UTC

Das konkrete Actions-Artefakt ist damit zeitlich befristet gespeichert. Der Produktionsoutput bleibt darüber hinaus reproduzierbar, solange der G4-Manuskript-Blob und der Builder unverändert verfügbar sind.

## Deterministische Produktions-QA

Nachgewiesen:

1. `git hash-object MANUSCRIPT_v01.md` entspricht exakt dem G4-approved Blob — **PASS**,
2. HTML wurde ausschließlich mit dem bestehenden Builder aus diesem Manuskript erzeugt — **PASS**,
3. erzeugtes HTML entspricht byte-für-byte `build_document(source)` — **PASS**,
4. SHA-256 des HTML wurde erzeugt — **PASS**,
5. HTML + SHA-256 wurden gemeinsam als GitHub-Actions-Artefakt hochgeladen — **PASS**.

## Scope

M2 baut bewusst keine DOCX/PDF/KDP-Pipeline. Das HTML dient wie in M1 als minimales reales Produktionsartefakt für Reproduzierbarkeit, Provenienz und G5.

## G5

Human Gate G5 ist vorbereitet, aber noch nicht erteilt. Ein `G5-APPROVE` akzeptiert exakt den durch Run #48 erzeugten HTML-Output mit SHA-256 `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb` als M2-Produktionsstand.
