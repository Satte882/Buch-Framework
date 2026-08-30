# M2 Observations – SPERRFRIST

status: IN_PROGRESS
m2_issue: `#10`
date: 2026-08-30
scope: Beobachtungen bis einschließlich Human Gate G2, deterministischem READY_FOR_PROSE-Nachweis und kontrolliertem Invalidierungstest

## Messbarer Umfang bisher

- Story Blocks: 12
- Events: 30
- Beats: 42
- Szenen: 10
- Character States: 31
- G2 Batch 1: 5 Szenen / 21 Beats / 13 Character States
- G2 Batch 2: 5 Szenen / 21 Beats / 18 Character States
- Human Gates abgeschlossen: G0, G1, G2
- interne G2-Batches menschlich akzeptiert: 2/2
- Cross-Batch-Probleme im Gesamtcheck: 0
- Human-Rework in den beiden G2-Batches: 0
- deterministischer Pipeline-Status nach G2: `READY_FOR_PROSE`
- kontrollierter Invalidierungstest: PASS

## O-01 – fünf Szenen sind als Review-Batch grundsätzlich handhabbar

Beide 5-Szenen-Batches konnten als kompakte Review-Pakete ohne Rückfrage und ohne Human-Rework akzeptiert werden.

Das ist **kein allgemeiner Standard `5 Szenen`**. Für diesen 10-Szenen-Fall war die Größe praktikabel. Ein belastbarer Zeitwert in Minuten wurde nicht erhoben und wird nicht erfunden.

## O-02 – Volltext aller Character States ist bereits Kontextmüll

31 Character-State-Dateien direkt vorzulegen wäre unergonomisch. Tatsächlich nützlich waren ad hoc, nicht als neues Tooling:

1. Scene-Batch-Sicht: Funktion, Entscheidung, Leserwissen, Beziehungsverschiebung je Szene.
2. Information/Reveal-Sicht: getrennte T-/K-Entwicklung.
3. Character-/Relationship-Sicht: Nora↔David, Nora↔Jonas, Nora↔Quelle A und Nebenbeziehungen.

Eine separate Research Dependency View war bisher nicht nötig; R-01/R-02 ließen sich innerhalb der Szenen-/Batch-Prüfung ausreichend kontrollieren.

## O-03 – die Batch-Grenze braucht einen expliziten Übergabezustand

Für S5→S6 war ein kompakter Übergabezustand wesentlich nützlicher als erneutes Lesen aller 13 Batch-1-State-Dateien:

- T unabhängig gestützt, letzte RC-Brücke fehlt,
- K deutlich geschwächt,
- Quelle A geschützt, aber verunsichert,
- Quelle B geschützt,
- Jonas fachlich im Fall, externe Autonomie eingeschränkt,
- Nora↔David Timingkonflikt offen,
- kein Publikationsbeschluss.

## O-04 – Gesamtlogik blieb über zwei Batches erhalten

Der Gesamt-Self-Review S1–S10 fand nach den beiden akzeptierten Batches **0 neue Cross-Batch-Widersprüche**.

Geprüft wurden Chronologie, T, K, Nora↔Jonas, Nora↔David, Nora↔Quelle A, Quelle-B-Schutz und Recherchegrenzen. Der Review erfolgte im selben Chat-/Modellkontext und ist daher kein Nachweis unabhängiger semantischer QA.

## O-05 – semantischer Self-Review fand einen echten Methodenfehler

Vor G1 war der geplante Story-Reversal zunächst fälschlich als Framework-Invalidierung interpretiert worden. Der Fehler wurde vor G1 korrigiert und in `SEMANTIC_REVIEW_LOG.md` dokumentiert.

Das ist ein realer semantischer Fund, aber **kein** Beleg für eine validierte unabhängige Review-Methode, weil Erzeugung und Review aus demselben Kontext kamen.

## O-06 – deterministische Prüfungen fanden reale Metadatenprobleme

Zwei unterschiedliche mechanische Probleme wurden sichtbar:

1. G0/G1-Gate-Records enthielten zunächst `artifacts:` nicht vertragskonform. Die Metadaten wurden korrigiert; Story blieb unverändert.
2. Nach G2 blockierte CI Run #33 den M2-Stand wegen BT009: Das Wort `unklar` in einer legitimen Informationsbeschreibung wurde als Placeholder erkannt.

BT009 wurde semantisch identisch formuliert als: `Bezug zum relevanten Release ist noch nicht belegt.`

Danach bestätigte Framework Validation Run **#34** den vollständigen M2-Stand mit `READY_FOR_PROSE`.

Der zweite Fund zeigt zugleich eine Grenze des Placeholder-Scanners: fachlich legitime Unsicherheit kann bei bestimmten Triggerwörtern False Positives erzeugen.

## O-07 – G2-Provenienz funktioniert unter 10-Szenen-Last

Nach G2 wurden zehn `accepted` Szenen-Provenienzmanifeste angelegt. Auf unverändertem `main` bestätigte Framework Validation Run **#35**:

- 10/10 Provenienzmanifeste `OK`.

Damit ist die bestehende M1-Provenienzmechanik erstmals auf zehn aktive Szenen angewandt.

## O-08 – kontrollierte Upstream-Änderung invalidiert zuverlässig

Auf der separaten, nie gemergten Test-Branch `m2-invalidation-test` wurde Jonas’ kanonische Governance-Baseline relevant verändert: externe Kontakte wären von Beginn an freigabepflichtig. Dadurch wäre die bestehende S5-Fehlerlogik fachlich nicht mehr unverändert tragfähig.

Ergebnis:

- Phase 1: 10/10 `accepted`-Manifeste → `BLOCK`; PR-CI Run **#36** PASS, weil BLOCK erwartet wurde.
- Phase 2: dieselben 10 Manifeste explizit `stale` → 10/10 `STALE_OK`; PR-CI Run **#38** PASS.
- Mismatch blieb in beiden Phasen sichtbar.
- Draft-PR #15 wurde geschlossen und nicht gemergt.

Vollständige Dokumentation: `M2_INVALIDATION_TEST.md`.

## O-09 – file-level Provenienz erzeugt einen zu großen technischen Blast Radius

Die Teständerung betraf semantisch primär Jonas’ Governance-/Vertrauensbogen. Der bestehende Provenienzchecker inferiert bewusst keine semantische Relevanz.

Da alle Szenenmanifeste den gesamten `CHARACTERS.md`-Blob referenzieren, führte die Änderung technisch zu:

**10/10 Szenen stale.**

Das ist konservativ sicher, aber bei größeren Büchern potenziell teuer. Der tatsächliche fachliche Rework-Radius wäre voraussichtlich kleiner als der technische Invalidierungsradius.

Konsequenz für M2: Dies ist ein **real beobachtetes Skalierungsproblem**, aber noch kein Auftrag, sofort neue Granularität oder Impact-Analyse zu implementieren. Die Entscheidung dazu gehört in den M2-Abschlussbericht.

## O-10 – bisher kein ungeplanter Framework-Funktionsausbau nötig

Bis einschließlich Invalidierungstest wurden keine neuen Checker, semantischen Scores, Agenten, Human Gates oder Produktionspfade gebaut.

Hinzu kamen lediglich:

- M2-Testartefakte,
- ad-hoc Review-Zusammenfassungen,
- zwei kleine Integrationstests, die die **bestehenden** Pipeline-/Provenienzchecker gegen den realen M2-Bestand ausführen.

Neue Framework-Funktionen ungeplant erforderlich: **keine**.

## Noch offen für M2

- G3 Prosa-Stil mit realem repräsentativem Prosa-Batch.
- vollständige Prosa / G4 Manuskript.
- G5 Produktion.
- Review-Aufwand bis G4/G5 weiter dokumentieren.
- finale Bewertung der Review-Sichten.
- M2-Abschlussbericht mit sieben Prüffragen und Entscheidung: echter Buchlauf vs. M3 vs. gezielter QA-/Review-Ausbau.

## Zwischenfazit nach G2 + Invalidierung

Die Pipeline skaliert von 3 auf 10 Szenen mechanisch und fachlich besser als vor M2 belegt. Der erste klare Engpass ist nicht die reine Szenenzahl, sondern **Review- und Abhängigkeitsgranularität**:

- Human Review braucht verdichtete Sichten statt Volltext aller Zustände.
- Provenienz schützt zuverlässig vor stillem Drift, ist auf Datei-Blob-Ebene aber zu grob und kann unnötig viele Downstreams invalidieren.

Beides ist jetzt beobachtet statt nur vermutet. Ob daraus festes Tooling entsteht, wird erst nach dem vollständigen M2-Lauf entschieden.
