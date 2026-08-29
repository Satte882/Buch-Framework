# Scene Readiness v0.1

## Zweck

Scene Readiness ist das Gate zwischen **Szenenplanung** und **Prosa**.

Es soll den teuersten Fehler aus der NORMALFALL-Entwicklung früher sichtbar machen: Eine Szene kann plot-funktional vollständig wirken und trotzdem noch zu viele relevante Entscheidungen oder zu wenig erlebte Ausgestaltung für belastbare Romanprosa enthalten.

Die historische Begründung steht in der Ausbau-Matrix von `Satte882/Buch`, Commit `be6a8881f8cfd5ff79e9ce6730b9d58f680eec0c`: Nach einer bereits vollständigen Story lag das Manuskript bei 27.370 Wörtern; diagnostiziert wurde eine systematische Verdichtung auf Szenenebene und ein Ausbauplan von 49.630 Wörtern.

## Was der Checker entscheidet – und was nicht

`scripts/scene_readiness.py` entscheidet nur:

- **BLOCK** – Pflichtinformationen fehlen, enthalten Platzhalter oder eine explizite Abhängigkeit ist noch offen.
- **READY_FOR_HUMAN_GATE** – mechanische Vollständigkeit ist erreicht; ein Mensch muss G3 trotzdem noch mit `APPROVE`, `REWORK` oder `STOP` entscheiden.

Der Checker entscheidet ausdrücklich **nicht**:

- ob eine Szene spannend ist,
- ob emotionale Wirkung ausreicht,
- ob Dialog gut ist,
- ob die geplante Länge passt,
- ob die Szene literarisch „gut“ ist.

Diese Trennung verhindert, dass eine subjektive Checkliste als objektiver Score ausgegeben wird.

## Abhängigkeiten

Vor G3 müssen drei Dinge vorhanden sein:

1. freigegebene Storyarchitektur,
2. szenenbezogene Character States,
3. geschlossene plotrelevante Recherche-Blocker.

Damit wird die zirkuläre Abhängigkeit aufgelöst: Scene Readiness fragt nicht nach einem erst später zu bauenden vollständigen Figuren-System, sondern nach einem kleinen `CHARACTER_STATE`-Stub, der Wissen, Glauben, Ziel, Beziehung und Informationsgrenzen der relevanten Figur festhält.

## Pflichtbereiche einer prose-ready Szene

### 1. Storyfunktion

- POV, Ort/Zeit, Ziel und Gegenkraft sind konkret.
- relevante Entscheidung und Konsequenz sind festgelegt.
- es gibt keine offene Storyentscheidung, die beim Schreiben improvisiert werden müsste.

### 2. Informationsarchitektur

- Leserwissen vor/nach der Szene ist klar.
- nicht zu verratende Informationen sind benannt oder begründet nicht relevant.
- Character-State-Referenzen sind vorhanden.

### 3. Recherche/Plausibilität

- plotrelevante Recherche ist `ready` oder nachweislich `not_applicable`.
- austauschbare Oberflächendetails dürfen später recherchiert werden, solange sie keine Kausalität, Handlung oder Figurenentscheidung verändern.

### 4. Erlebnisplanung

Die Szene muss nicht ausformuliert sein, aber die tragenden Romanebenen brauchen konkrete Träger:

- `pressure_progression` – wie verändert sich der Druck innerhalb der Szene?
- `observable_actions` – welche sichtbaren Prüfungen, Handlungen oder Interaktionen tragen die Entwicklung?
- `alternatives_in_scene` – welche Gegenoption oder Gegenlesart bleibt real?
- `consequence_carrier` – woran wird die Konsequenz konkret sichtbar/spürbar?
- `space_or_procedure_anchors` – welche räumlichen/prozeduralen Tatsachen sind fest?
- `relationship_or_psychology_carrier` – wodurch wird eine psychologische oder relationale Veränderung erlebbar?

Nicht jede Dimension ist in jeder Szene relevant. `n/a` ist deshalb möglich, aber nur mit Begründung.

## Gate-Frage

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

Wenn nein: `REWORK`.

Wenn ja, prüft der Mensch zusätzlich:

> **Ist das dramaturgische Gewicht der Szene ausreichend als erlebbare Handlung geplant – oder besteht die Gefahr, dass die Prosa nur Plot zusammenfasst?**

Diese zweite Frage ist absichtlich nicht automatisiert.

---

# Retrospektive Validierung an NORMALFALL

## Methode

Für v0.1 wurden acht Kapitel gewählt, die in der historischen Ausbau-Matrix deutlich nachbearbeitet werden mussten. Verglichen wurden die damaligen Szenenkarten mit den später dokumentierten Ausbauaufträgen. Die Fälle sind unveränderlich in `tests/corpus/scene_readiness_normalfall.json` abgelegt.

Das ist **kein Benchmark** und keine statistische Güteaussage. Es ist ein retrospektiver Plausibilitätstest an einem echten Entwicklungsverlauf.

## Ergebnis

| Kapitel | Szene | Ist → Ausbauziel | Retrospektives G3-Ergebnis | Kernbefund |
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

Die v0.1-Logik hätte sechs der acht Fälle wegen echter offener Entscheidungen blockiert, einen Fall zwingend in einen qualitativen Human Review gegeben und Kapitel 40 wahrscheinlich passieren lassen.

Der letzte Fall bleibt absichtlich im Korpus. Er zeigt eine Grenze des Gates:

> **Scene Readiness kann verhindern, dass unfertige Storyentscheidungen in Prosa wandern. Es kann nicht garantieren, dass eine fertig geplante Szene in der ersten Prosa-Fassung bereits ihr volles narratives Gewicht erhält.**

Daraus folgt **kein** neues Wortzahl-Gate. Die spätere Prosa-Batch-Freigabe G4 muss Gewicht/Pacing anhand echten Texts prüfen.

## Keine nachträgliche Schönkalibrierung

Die Kriterien werden nicht so erweitert, dass Kapitel 40 rückwirkend künstlich zum BLOCK wird. Neue Kriterien dürfen nur entstehen, wenn mehrere echte Fälle denselben vermeidbaren Fehler zeigen und die Regel zukünftige Arbeit besser macht, statt nur den historischen Datensatz perfekt zu erklären.

## Nutzung

```bash
python scripts/scene_readiness.py project/scenes/03_04_01.md
```

Nur `READY_FOR_HUMAN_GATE` erlaubt, einen G3-Gate-Record vorzubereiten. Die endgültige Freigabe bleibt menschlich.
