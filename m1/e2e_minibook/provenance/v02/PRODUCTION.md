# Provenienz – FEHLALARM v0.2 Produktion

artifact: `m1/e2e_minibook/production/FEHLALARM_v02.html`
artifact_ref: `1add4d45fea3e552521041ae5d6120fba717d214`
generated_via: deterministic_builder
action: generated
date: 2026-08-30
purpose: Den G4-freigegebenen Mini-Manuskriptstand als eigenständiges HTML-Lese- und Printartefakt ableiten.
gate_basis: G4 APPROVE
status: draft

## Upstream

- `m1/e2e_minibook/MANUSCRIPT_v02.md` — blob `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
- `m1/e2e_minibook/gates/G4.md` — blob `8c4181e878c0f64d233c2bdaeaf73a218a1ab5ac`
- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`

## Build

```text
python scripts/build_html.py \
  m1/e2e_minibook/MANUSCRIPT_v02.md \
  m1/e2e_minibook/production/FEHLALARM_v02.html
```

Der Builder verwendet ausschließlich Python-Standardbibliothek. Er wandelt Titel und Szenenüberschriften in HTML-Struktur um, escaped Prosa sicher und ergänzt responsive sowie A5-Print-CSS. Er ändert keine Manuskriptformulierung.

## Produktionscharakter

Das Artefakt ist keine umbenannte Markdown-Kopie:

- eigenständiges HTML-Dokument,
- Titelblattdarstellung,
- strukturierte Szenenüberschriften,
- Lesetypografie,
- responsive Darstellung,
- A5-Print-CSS mit Seitenumbrüchen.

## Deterministische QA

`tests/test_build_html.py` enthält einen byte-genauen Regressionstest: `build_document(MANUSCRIPT_v02.md)` muss exakt dem committed `FEHLALARM_v02.html` entsprechen.

Der erste Lauf dieses neuen Tests hat einen echten Driftfehler gefunden: Das HTML war aus einem minimal älteren S3-Zwischenstand gebaut. Das Produktionsartefakt wurde daraufhin ausschließlich aus dem bereits G4-freigegebenen Manuskript neu gebaut; der G4-Manuskripttext selbst blieb unverändert.

Die endgültige CI-Freigabe wird im G5-Review-Paket auf den erfolgreichen Rebuild-Test referenziert.

## Gültigkeit

Bis zum menschlichen `G5-APPROVE` bleibt das Produktionsartefakt `draft`. Eine Änderung des G4-Manuskript-Blobs invalidiert diesen Output; reine Build-/CSS-Änderungen erzeugen einen neuen Produktionsstand und müssen erneut über G5 geprüft werden.