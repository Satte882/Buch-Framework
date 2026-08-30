# H1 Result – Provenienzgranularität / Impact-Disposition

status: PASS
issue: #16
date: 2026-08-30

## Ausgangsproblem aus M2

Der kontrollierte M2-Invalidierungstest änderte Jonas Rehms Governance-Baseline in `CHARACTERS.md` relevant. Da alle zehn Szenenmanifeste den vollständigen `CHARACTERS.md`-Blob referenzierten, ergab sich technisch:

- betroffen laut Checker: **10/10 Szenen**
- tatsächlich fachlich plausibler Jonas-Prüfradius laut M2-Befund: S2, S3, S5, S6, S8, S10

Die Sicherheit war hoch, die Granularität zu grob.

## Hardening-Lösung

`scripts/provenance_check.py` unterstützt jetzt zusätzlich **explizite Provenienz-Slices**.

Beispiel:

```md
- `CHARACTERS.md` — slice `table-row:Jonas Rehm` — blob `<sha>`
```

Der Checker inferiert weiterhin **keine semantische Relevanz**. Der Manifest-Autor benennt den relevanten Ausschnitt explizit; der Checker prüft nur dessen Git-Blob-Hash.

Unterstützt:

- `table-row:<first cell>`
- `heading:<heading text>`
- `line-prefix:<prefix>`

Mehrdeutige, fehlende oder unbekannte Slices blockieren konservativ.

## Reale M2-Regression

`tests/test_hardening_provenance_slices.py` verwendet:

- das reale M2-`CHARACTERS.md`,
- die realen zehn M2-Szenenkarten,
- die real vorhandenen Jonas-Character-State-Zuordnungen,
- dieselbe Jonas-Governance-Teständerung wie beim ursprünglichen M2-Invalidierungstest.

Ergebnis mit expliziten Character-Slices:

| Szene | Jonas-State vorhanden | Ergebnis nach Jonas-Änderung |
|---|---:|---|
| S1 | nein | OK |
| S2 | ja | BLOCK |
| S3 | ja | BLOCK |
| S4 | nein | OK |
| S5 | ja | BLOCK |
| S6 | ja | BLOCK |
| S7 | nein | OK |
| S8 | ja | BLOCK |
| S9 | nein | OK |
| S10 | ja | BLOCK |

**Technischer Blast Radius: 10/10 → 6/10.**

Nach expliziter `stale`-Markierung liefern genau diese sechs Szenen `STALE_OK`; die vier nicht abhängigen bleiben `OK`.

Die Zustandslogik bleibt damit:

```text
explizit abhängiger accepted Downstream + Slice-Drift → BLOCK
explizit abhängiger stale Downstream + Slice-Drift    → STALE_OK
nicht referenzierter Slice ändert sich                → OK
```

## CI

Framework Validation Run **#55**:

- 64 Tests ausgeführt
- 64/64 PASS
- neuer H1-M2-Regressionsfall PASS
- bestehende M1/M2-Provenienztests PASS
- bestehender M2-Manuskript-/Produktionspfad weiterhin PASS

## Bewertung

H1-Akzeptanz aus Issue #16:

- pauschale 10/10-Invalidierung reduziert: **PASS – 6/10**
- tatsächlich explizit abhängige Szenen blockieren: **PASS**
- nicht abhängige Szenen bleiben unverändert: **PASS**
- keine automatische semantische LLM-Impact-Entscheidung: **PASS**
- bestehende `OK → BLOCK → STALE_OK`-Sicherheit erhalten: **PASS**

## Einsatzregel

Whole-file-Refs bleiben der KISS-Default. Slices werden nur dort eingesetzt, wo eine kanonische Datei mehrere unabhängig veränderbare Einheiten enthält und Whole-file-Invalidierung real unnötiges Rework erzeugt.

**H1 Gesamt: PASS.**
