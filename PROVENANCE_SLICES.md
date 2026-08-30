# Provenienz-Slices – feingranulare explizite Abhängigkeiten

## Zweck

M2 zeigte ein reales Skalierungsproblem: Eine Änderung in einem Teil von `CHARACTERS.md` invalidierte technisch 10/10 Szenen, weil jede Szene den vollständigen Datei-Blob referenzierte.

Provenienz-Slices reduzieren diesen Blast Radius, **ohne semantische Relevanz automatisch zu erraten**.

## Grundprinzip

Ein Downstream kann statt des gesamten Datei-Blobs einen explizit benannten Markdown-Ausschnitt referenzieren.

Beispiel:

```md
- `CHARACTERS.md` — slice `table-row:Jonas Rehm` — blob `<40-char-git-blob-sha>`
- `CHARACTERS.md` — slice `heading:A2 – Nora ↔ Jonas` — blob `<40-char-git-blob-sha>`
```

Der Manifest-Autor entscheidet, **welche** Abhängigkeit relevant ist. Der Checker entscheidet nur deterministisch, ob genau dieser Ausschnitt seit der Ableitung verändert wurde.

## Unterstützte Selector-Typen

### `table-row:<first cell>`

Extrahiert genau eine Markdown-Tabellenzeile, deren erste Zelle exakt dem Schlüssel entspricht.

Geeignet für:

- einzelne Figuren-Baselines,
- einzelne Event-/Beat-Zeilen, falls künftig sinnvoll.

### `heading:<heading text>`

Extrahiert den benannten Markdown-Abschnitt vom Heading bis zum nächsten Heading gleicher oder höherer Ebene.

Geeignet für:

- Beziehungsentwicklungen,
- klar abgegrenzte Regel-/Storyabschnitte.

### `line-prefix:<prefix>`

Extrahiert genau eine Zeile, deren getrimmter Inhalt mit dem Prefix beginnt.

Nur verwenden, wenn die Zeile eindeutig und stabil benannt ist.

## Sicherheitsregeln

- 0 Treffer → `BLOCK`/`STALE_OK` wie normaler Drift.
- >1 Treffer → ebenfalls blockieren; ein Slice darf nicht mehrdeutig sein.
- unbekannter Selector-Typ → blockieren.
- Slice-Hash ist ein Git-Blob-Hash des extrahierten Fragmenttexts.
- Die Statussemantik bleibt unverändert:
  - `accepted/draft + Drift → BLOCK`
  - `stale/invalidated + Drift → STALE_OK`
  - unverändert → `OK`

## Was Slices ausdrücklich nicht tun

Der Checker inferiert nicht:

- welche Figur semantisch betroffen ist,
- welche Szenen „wahrscheinlich“ Rework brauchen,
- ob eine Änderung wichtig genug ist,
- ob ein LLM-Fund korrekt ist.

Diese Abhängigkeit muss explizit im Manifest stehen.

## M2-Hardening-Nachweis

Der ursprüngliche M2-Test änderte Jonas' Governance-Baseline. Mit vollständigem `CHARACTERS.md`-Blob wurden technisch 10/10 Szenen stale.

Der Hardening-Regressionsfall verwendet dieselbe Änderung mit explizitem `table-row:Jonas Rehm`-Slice nur für Szenen, die einen Jonas-Character-State besitzen:

- betroffen: S2, S3, S5, S6, S8, S10 = 6/10
- nicht betroffen: S1, S4, S7, S9 = 4/10

Damit entspricht der technische Prüfradius dem im M2-Abschluss bereits als fachlich plausibel benannten Jonas-Radius wesentlich besser, ohne die Entscheidung zu automatisieren.

## Einsatzregel für neue Romanprojekte

Whole-file-Refs bleiben der KISS-Default, solange die Datei klein oder global relevant ist.

Slices verwenden, wenn **beides** gilt:

1. eine Datei enthält mehrere unabhängig veränderbare kanonische Einheiten,
2. M2-/Projekt-Erfahrung zeigt, dass Whole-file-Drift unnötig viele Downstreams invalidiert.

> **Granularität nur dort erhöhen, wo realer Rework gespart wird.**
