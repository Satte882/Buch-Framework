# G5 Review Request – FEHLALARM v0.2

status: AWAITING_HUMAN_G5_DECISION
gate_name: Produktion
prior_gate: `m1/e2e_minibook/gates/G4.md`
prior_gate_ref: `8c4181e878c0f64d233c2bdaeaf73a218a1ab5ac`

## Zweck

G5 ist der letzte Human Gate des M1-Laufs. Er prüft nicht mehr Story, Szenen oder Prosaqualität, sondern genau den finalen **Produktionsstand**, der aus dem G4-freigegebenen Manuskript abgeleitet wurde.

## G4-Quelle

- `m1/e2e_minibook/MANUSCRIPT_v02.md`
- blob: `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
- G4: **APPROVE**

Der Produktionsschritt darf diesen Text nicht inhaltlich verändern.

## Zu prüfendes Produktionsartefakt

- `m1/e2e_minibook/production/FEHLALARM_v02.html`
- blob: `1add4d45fea3e552521041ae5d6120fba717d214`
- Format: eigenständiges HTML-Lese-/Printartefakt
- Provenienz: `m1/e2e_minibook/provenance/v02/PRODUCTION.md` — blob `702de0928e351ceb2a312ac3ec82418764efb4ee`
- Build Manifest: `m1/e2e_minibook/production/BUILD_MANIFEST.md` — blob `607cf29c259e211d796fbe57092ac99ac1f4e68a`

## Produktionsmerkmale

Der Output ist ein echter abgeleiteter Produktionsstand und keine umbenannte Markdown-Datei:

- HTML-Dokumentstruktur,
- Titelblattdarstellung,
- strukturierte Szenenüberschriften,
- responsive Lesetypografie,
- A5-Print-CSS,
- definierte Seitenumbrüche für Druck,
- keine externe Runtime-/CDN-Abhängigkeit.

## Reproduzierbarkeit

Builder:

- `scripts/build_html.py` — blob `05adc654d1dffcdd219e7cf80301537f51428122`

Rebuild:

```text
python scripts/build_html.py \
  m1/e2e_minibook/MANUSCRIPT_v02.md \
  m1/e2e_minibook/production/FEHLALARM_v02.html
```

Regressionstest:

- `tests/test_build_html.py` — blob `7d0bf4d7d592b4cad42fec29953c6fef93b205e8`
- verlangt byte-genaue Gleichheit zwischen Rebuild und committed Produktionsartefakt.

## Fehlerfall im realen M1-Lauf

Der erste Produktions-Rebuild-Test schlug **absichtlich nicht still fehl**: Er erkannte, dass die erste HTML-Datei aus einem minimal älteren S3-Zwischenstand gebaut worden war.

Daraufhin wurde ausschließlich das Produktionsartefakt aus dem bereits G4-freigegebenen Manuskript neu gebaut. `MANUSCRIPT_v02.md` blieb unverändert auf blob `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`.

Der korrigierte Produktionsstand ist blob `1add4d45fea3e552521041ae5d6120fba717d214`.

## Deterministische QA

Finaler GitHub-Actions-Nachweis:

- Workflow: `Framework Validation`
- Run #32 / ID `33306864034`
- Head: `55e128aaba91744ebe277134d04b6a7b978769c8`
- Ergebnis: **success**

Der erfolgreiche Lauf umfasst insbesondere:

- byte-genauen Produktions-Rebuild,
- Provenienz-/Invalidierungstests,
- Pipeline-v0.2-Tests,
- Scene-Readiness-Tests,
- Prosa-Audit-Tests,
- vollständigen NORMALFALL-Rauschtest.

## Invalidierungsnachweis

- `m1/e2e_minibook/INVALIDATION_TEST.md`
- Ergebnis: **PASS**

Geprüft wurde isoliert und deterministisch:

`accepted + geänderter Upstream-Blob → BLOCK → sichtbares stale → STALE_OK`

Damit musste für den Test kein real freigegebener FEHLALARM-Upstream künstlich geändert und durch G2–G4 zurückgeführt werden.

## G5-Reviewfragen

1. Ist das HTML als echter finaler M1-Produktionsoutput ausreichend und nicht nur eine Dateikopie des Manuskripts?
2. Ist die Ableitung klar auf genau den G4-freigegebenen Manuskript-Blob zurückgeführt?
3. Ist die Produktionsdarstellung für den M1-Zweck ausreichend: lesbar am Bildschirm und druckbar als A5-artiger Output?
4. Ist akzeptabel, dass M1 bewusst HTML statt DOCX/PDF/KDP als minimales Produktionsformat verwendet?
5. Ist der zuerst gefundene Produktions-Drift sauber behoben und durch den byte-genauen Regressionstest ausreichend abgesichert?
6. Würdest du genau Output-Blob `1add4d45fea3e552521041ae5d6120fba717d214` als finalen Produktionsstand des M1-Tests freigeben?

## Nächste menschliche Entscheidung

- `G5-APPROVE` — genau `production/FEHLALARM_v02.html` blob `1add4d45fea3e552521041ae5d6120fba717d214` wird als finaler M1-Produktionsstand akzeptiert. Danach werden G5-Record, M1-Abschlussbericht und Fixture-Freeze geschrieben und Issue #8 kann bei Gesamt-PASS geschlossen werden.
- `G5-REWORK` — ausschließlich konkrete Produktions-/Formatbefunde überarbeiten; eine Manuskriptänderung erfordert Backtracking zu G4.
- `G5-STOP` — M1 an dieser Stelle beenden.

**Wichtig:** Der erfolgreiche Build und die CI ersetzen nicht die menschliche Produktionsfreigabe. G5 bleibt eine bewusste Entscheidung über genau den oben referenzierten Output.