# Scene Readiness v0.2

## Zweck

Scene Readiness ist die fachliche Prüfung am Ende der **Szenen-Architektur** vor systematischer Prosa.

Sie ist ab v0.2 Bestandteil von **G2 – Prose Ready** und kein eigener zusätzlicher Gate-Typ pro Szene.

Die verbindliche Arbeitsweise steht in `ARBEITSWEISE.md`:

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Szenen → Beats → Prosa`

Die Szenenlandschaft wird zuerst horizontal über das gesamte Buch geschlossen; anschließend werden die Beats innerhalb dieser Szenen ausreichend konkretisiert.

## Warum Scene Readiness relevant bleibt

Scene Readiness soll zwei Fehlerklassen früh sichtbar machen:

1. Eine Szene wirkt plot-funktional vollständig, lässt aber noch relevante Entscheidungen offen oder trägt ihr narratives Gewicht nur als Zusammenfassung.
2. Viele Szenen sind einzeln korrekt, verwenden aber über längere Strecken denselben dramaturgischen Träger und erzeugen dadurch erst im Vollmanuskript Monotonie.

Der zweite Punkt wurde im Real-Pilot `Satte882/ABWEICHUNG` bestätigt: semantisch saubere Szenen und Beats bestanden lokale Reviews, während Whole-Manuscript-Reviews eine wiederkehrende Meeting-/Governance-Choreografie als Major sichtbar machten. Ein reiner Prosa-Rework reichte nicht; erst ein kontrollierter Scene-/Beat-Backtrack löste die Ursache.

## Was der Checker entscheidet – und was nicht

`scripts/scene_readiness.py` entscheidet nur:

- **BLOCK** – Pflichtinformationen fehlen, enthalten Platzhalter oder eine explizite Abhängigkeit ist noch offen.
- **READY_FOR_HUMAN_GATE** – mechanische Vollständigkeit ist erreicht; ein Mensch muss die Szenenarchitektur im G2-Review weiterhin mit `APPROVE`, `REWORK` oder `STOP` bewerten.

Der Checker entscheidet ausdrücklich **nicht**:

- ob eine Szene spannend ist,
- ob emotionale Wirkung ausreicht,
- ob Dialog gut ist,
- ob die geplante Länge passt,
- ob die Szene literarisch „gut“ ist,
- ob die Verteilung der Szenenformen über das ganze Buch ermüdend wirkt.

Eine semantische Selbstprüfung derselben KI ist ebenfalls kein unabhängiger Review.

## Abhängigkeiten vor G2

Vor einer G2-Freigabe müssen für die betroffenen Szenen mindestens vorhanden sein:

1. G1-freigegebene Story-Architektur,
2. vollständige Szenenlandschaft,
3. ausreichende horizontale Beat-Abdeckung,
4. szenenbezogene Character States, soweit im Projekt geführt,
5. geschlossene Recherchefragen, die eine aktuelle Beat-/Szenen-/Informations-/Konsequenzentscheidung verändern können.

Recherche ist nur dann blockierend, wenn sie gemäß `ARBEITSWEISE.md` tatsächlich eine jetzt zu treffende relevante Entscheidung verändern kann. Austauschbare Oberflächendetails dürfen offen bleiben.

## Pflichtbereiche einer prose-ready Szene

### 1. Storyfunktion

- POV, Ort/Zeit, Ziel und Gegenkraft sind konkret.
- relevante Entscheidung und Konsequenz sind festgelegt.
- die Szene ist auf konkrete Beats zurückführbar.
- es gibt keine offene Storyentscheidung, die beim Schreiben improvisiert werden müsste.

### 2. Informationsarchitektur

- Leserwissen vor/nach der Szene ist klar.
- nicht zu verratende Informationen sind benannt oder begründet nicht relevant.
- Character-State-Referenzen sind vorhanden, falls das Projekt diese separat führt.

### 3. Recherche/Plausibilität

- aktuell blockierende Recherche ist `resolved` oder nachweislich `not_applicable`.
- austauschbare Oberflächendetails dürfen später recherchiert werden, solange sie keine Kausalität, Handlung oder Figurenentscheidung verändern.

### 4. Erlebnisplanung

Die Szene muss nicht ausformuliert sein, aber die tragenden Romanebenen brauchen konkrete Träger:

- `pressure_progression` – wie verändert sich der Druck innerhalb der Szene?
- `observable_actions` – welche sichtbaren Prüfungen, Handlungen oder Interaktionen tragen die Entwicklung?
- `alternatives_in_scene` – welche Gegenoption oder Gegenlesart bleibt real?
- `consequence_carrier` – woran wird die Konsequenz konkret sichtbar/spürbar?
- `space_or_procedure_anchors` – welche räumlichen/prozeduralen Tatsachen sind fest?
- `relationship_or_psychology_carrier` – wodurch wird eine psychologische oder relationale Veränderung erlebbar?

Nicht jede Dimension ist in jeder Szene relevant. `n/a` ist möglich, aber nur mit Begründung.

## Whole-Book Scene-Shape Review

Scene Readiness endet nicht mehr mit 40 isolierten Einzel-PASSes. Vor G2 wird die **gesamte Szenenfolge** zusätzlich als Verteilung betrachtet.

### Primary Dramatic Carrier

Jede Szene erhält für die Review-Sicht genau einen dominanten `Primary Dramatic Carrier`. Diese Klassifikation ist eine **nicht-kanonische Review-Projektion** und muss nicht als neue Pflichtdatei im Buchrepo gespeichert werden.

Mögliche Carrier:

- `clinical_action`
- `resource_conflict`
- `personal_confrontation`
- `solo_analysis`
- `data_review`
- `governance_design`
- `audit_investigation`
- `relationship_scene`
- `implementation_test`
- `aftermath`

Die Liste ist erweiterbar. Entscheidend ist nicht das Label, sondern die erkennbare dramaturgische Hauptform.

### Verteilungsheuristiken

Warnsignale:

- mehr als **2 direkt aufeinanderfolgende Szenen** mit praktisch demselben Carrier,
- in einem Fenster von **8 Szenen mehr als 4** mit Hauptform Meeting/Review/Governance/Data Discussion,
- mehrere Regel-/Governance-Stufen hintereinander, ohne dass ihre Wirkung zunächst als Anwendung, Folge, Konflikt oder Beziehung erlebt wird,
- wiederholt dieselbe Erkenntnismechanik wie `Daten/Regel → Prüfung → Gegenposition → Klärung`.

Diese Werte sind **keine automatischen Blocker**. Ein Überschreiten verlangt nur eine bewusste semantische Prüfung:

> Entsteht aus der Verteilung reale Ermüdung/Redundanz, oder ist die Wiederholung dramaturgisch begründet und in der konkreten Ausführung ausreichend verschieden?

Nur ein belastbarer Befund führt zu `REWORK`.

## G2-Gate-Fragen

Ein G2-Review beantwortet künftig beide Fragen:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

und:

> **Ist die Szenenfolge als Leseerlebnis ausreichend variiert, oder wiederholt die Architektur über längere Strecken denselben dramaturgischen Träger?**

Wenn eine relevante Storyentscheidung offen ist: `REWORK`.

Wenn die Whole-Book-Verteilung einen bestätigten strukturellen Major zeigt: ebenfalls `REWORK`.

## G2-Batching

Bei einem kleinen M1-Testfall können alle Szenenkarten gemeinsam geprüft werden. Bei einem langen Roman darf G2 in mehrere Review-Batches aufgeteilt werden.

Das erzeugt keine neuen Gate-Typen. Nach den Teilreviews folgt zwingend ein **Gesamtcheck über alle Batch-Grenzen hinweg**, inklusive Scene-Shape-Verteilung.

---

# Retrospektive Validierung an NORMALFALL

## Methode

Für v0.1 wurden acht Kapitel gewählt, die in der historischen Ausbau-Matrix deutlich nachbearbeitet werden mussten. Verglichen wurden die damaligen Szenenkarten mit den später dokumentierten Ausbauaufträgen. Die Fälle sind unveränderlich in `tests/corpus/scene_readiness_normalfall.json` abgelegt.

Das ist **kein Benchmark** und keine statistische Güteaussage. Es ist ein retrospektiver Plausibilitätstest an einem echten Entwicklungsverlauf.

## Ergebnis

| Kapitel | Szene | Ist → Ausbauziel | Retrospektives Readiness-Ergebnis | Kernbefund |
|---|---|---:|---|---|
| 1 | `02_01_01` | 594 → 1.600 | **BLOCK** | Ort/Arbeitskontext noch als später zu recherchieren markiert; konkrete Prüfhandlungen später nachgerüstet |
| 11 | `03_04_01` | 557 → 1.750 | **BLOCK** | genaue äußere Ereignisform ausdrücklich noch offen |
| 14 | `04_01_01` | 478 → 1.800 | **BLOCK** | konkrete Daten-/Identifikatorart noch alternativ formuliert; später auf begrenzten Kennzeichenabgleich fixiert |
| 24 | `05_04_02` | 497 → 1.750 | **BLOCK** | konkrete Folge für den falsch Belasteten noch als Auswahl mehrerer Möglichkeiten offen |
| 29 | `06_03_01` | 584 → 1.900 | **HUMAN REVIEW** | Plot sehr vollständig; Problem lag vor allem in Gewicht, Abwägung und ausgespielter Konsequenz |
| 34 | `07_01_01` | 858 → 1.700 | **BLOCK** | falsche Auslassungshypothesen noch nicht konkret als erlebbare Prüfschritte festgelegt |
| 38 | `08_01_01` | 790 → 1.800 | **BLOCK** | Art der zweiten unabhängigen Bestätigung noch alternativ/offen |
| 40 | `08_03_01` | 581 → 2.000 | **PASS – bekannte False Negative** | Szenenkarte bereits außergewöhnlich konkret; späterer Ausbau betraf vor allem Zeitlupe/Pacing und Nachwirkung |

### Interpretation

Die bisherige Readiness-Logik hätte sechs der acht Fälle wegen echter offener Entscheidungen blockiert, einen Fall zwingend in einen qualitativen Human Review gegeben und Kapitel 40 wahrscheinlich passieren lassen.

Der letzte Fall bleibt absichtlich im Korpus. Er zeigt eine Grenze:

> **Scene Readiness kann verhindern, dass unfertige Storyentscheidungen in Prosa wandern. Es kann nicht garantieren, dass eine fertig geplante Szene in der ersten Prosa-Fassung bereits ihr volles narratives Gewicht erhält.**

ABWEICHUNG ergänzt eine zweite Grenze:

> **Lokale Scene Readiness garantiert nicht automatisch eine gute Whole-Book-Verteilung der Szenenformen.**

Daraus folgt kein neues Wortzahl- oder automatisches Scene-Shape-Gate. G2 muss den Whole-Book-Verlauf semantisch prüfen; G3 testet anschließend echten Sequenzrhythmus in Prosa.

## Keine nachträgliche Schönkalibrierung

Die Kriterien werden nicht so erweitert, dass historische Fälle rückwirkend künstlich zum BLOCK werden. Neue Kriterien dürfen nur entstehen, wenn echte Projektverläufe denselben vermeidbaren Fehler zeigen und die Regel zukünftige Arbeit besser macht, statt nur einen Datensatz perfekt zu erklären.

## Nutzung

```bash
python scripts/scene_readiness.py project/scenes/03_04_01.md
```

Nur `READY_FOR_HUMAN_GATE` erlaubt, die Szene in ein G2-Review-Paket aufzunehmen. Die endgültige Freigabe bleibt menschlich.
