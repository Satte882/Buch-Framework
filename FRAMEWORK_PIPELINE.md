# Framework-Pipeline v0.1

Diese Datei definiert die **dünne End-to-End-Wirbelsäule** des Buch-Frameworks. Sie ist dem unveränderlichen Ziel aus `ZIEL.md` untergeordnet.

> Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.

## Warum die nächste Vertiefung bei Szenen liegt

Die Priorisierung ist nicht nur eine Einschätzung. Die historische Ausbau-Matrix von `NORMALFALL` (`Satte882/Buch`, Commit `be6a8881f8cfd5ff79e9ce6730b9d58f680eec0c`) dokumentiert nach einer bereits **vollständigen Story** eine Manuskriptfassung von 27.370 Wörtern und einen zusätzlichen Ausbauplan von 49.630 Wörtern. Die Diagnose dort lautet ausdrücklich: Das Problem lag in der **systematischen Verdichtung auf Szenenebene**; Konflikt, psychologische Konsequenz, Figurenreaktion, Suspense und situatives Erleben waren oft zu knapp ausgespielt.

Daraus folgt für v0.1:

> Vor weiteren tiefen Spezialscannern wird zuerst verhindert, dass eine nur plot-komplette, aber noch nicht prose-ready Szene in teure Prosa übersetzt wird.

Diese Priorität ist empirisch für `NORMALFALL` begründet, aber noch keine allgemeine Aussage über jedes Buchprojekt.

## Pipeline und verbindliche Artefakte

| Stufe | Input | Verbindliches Arbeitsartefakt | Menschlicher Gate | Tiefe v0.1 |
|---|---|---|---|---|
| 0 Idee | Buchidee | `project/BOOK_IDEA.md` nach `templates/BOOK_IDEA.md` | **G0 – Idee freigeben** | **Contract + Pipeline-Check implementiert** |
| 1 Story | freigegebene Idee | `project/STORY_PACKAGE.md` nach `templates/STORY_PACKAGE.md` | **G1 – Storyarchitektur freigeben** | **Contract + Pipeline-Check implementiert** |
| 2 Figuren + Recherche-Basis | Story Package | `project/CHARACTERS.md` + `project/RESEARCH_REGISTER.md` | **G2 – Voraussetzungen für Szenen freigeben** | **Minimal-Baseline + Pipeline-Check implementiert** |
| 3 Szenen | Story + Figuren-/Recherche-Basis | `project/scenes/<scene_id>.md` nach `templates/SCENE_PLAN.md` + szenenbezogene Character States | **G3 – Scene Readiness** | **v0.1 implementiert + Upstream-Referenzen geprüft** |
| 4 Prosa | freigegebene Szene(n) | kanonisches Manuskript / Prosa-Batch | **G4 – Prosa-Stichprobe bzw. Batch freigeben** | Contract definiert |
| 5 Qualität | Manuskript | Prosa-Audit-Report + später semantischer Review | **G5 – Manuskriptqualität freigeben** | Prosa-Audit v0.1 implementiert |
| 6 Produktion | freigegebenes Manuskript | DOCX/PDF/KDP-Produktionsartefakte | **G6 – Veröffentlichung freigeben** | Contract definiert, tiefe Produktion später |

Jeder Gate wird mit `templates/GATE_RECORD.md` dokumentiert. Ein Gate ist eine **menschliche Entscheidung**, kein automatisch erzeugtes Score-Feld.

## Ausführbarer Upstream-Pfad

`scripts/pipeline_check.py` prüft den Pfad von G0 bis vor G3 als zusammenhängende Kette. Dabei werden nicht nur einzelne Dateien auf Pflichtfelder geprüft, sondern auch Übergänge und Referenzen:

- G0, G1 und G2 müssen als menschliche `APPROVE`-Records vorliegen;
- `working_title` muss zwischen Idee und Story Package konsistent sein;
- `CHARACTERS.md` muss auf die aktuelle Story-Package-Version zeigen;
- offene Recherche darf im Register bestehen, aber eine von der konkreten Szene referenzierte Recherche muss `resolved` oder `not_applicable` sein;
- `character_state_refs` müssen auf reale, zur Szene passende Character-State-Dateien zeigen;
- eine mechanisch vollständige Szene erhält nur `READY_FOR_G3`, niemals automatisch `APPROVE`.

Damit existiert erstmals ein echter End-to-End-Test der frühen Framework-Kette statt nur einzelner Methodenbeschreibungen.

## Regel für Human Gates

Ein Gate darf nur drei Entscheidungen festhalten:

- `APPROVE` – nächste Stufe darf beginnen.
- `REWORK` – definierte Punkte müssen vor dem nächsten Gate behoben werden.
- `STOP` – Projekt/Stufe wird bewusst nicht fortgeführt.

Offene irreversible Storyentscheidungen dürfen nicht durch den Gate hindurch in die nächste, teurere Stufe geschoben werden.

## Abhängigkeitsreihenfolge vor Scene Readiness

Die frühere Reihenfolge „Szenen zuerst, Figurenmodell danach“ wäre zirkulär, weil Scene Readiness bereits Wissen, Glauben, Beziehungen und Informationsgrenzen der Figuren braucht. Deshalb gilt ab v0.1:

1. Story Package freigeben.
2. Minimalen Figuren-Baseline-Stand und Recherche-Register anlegen.
3. Pro Szene den **Character-State-Stub** ausfüllen.
4. Erst dann Scene Readiness prüfen.

Das ist bewusst **noch kein tiefes Figuren-Konsistenzsystem**. Es liefert nur die Informationen, die eine Szene benötigt, damit beim Schreiben keine relevanten Figuren- oder Wissensentscheidungen improvisiert werden müssen.

## Vertiefungsregel für das Framework

Neue Automatisierung wird nur gebaut, wenn sie mindestens eine dieser Bedingungen erfüllt:

1. Sie verhindert nachweisbar teures Downstream-Rework.
2. Sie ersetzt wiederholbare, häufige Handarbeit.
3. Sie schützt eine irreversible oder schwer rückholbare Qualitätsentscheidung.
4. Sie schließt eine konkrete Lücke auf dem Weg zu `ZIEL.md`.

Ein Baustein wird **nicht** deshalb vertieft, weil er technisch leicht automatisierbar ist.

## Aktueller Schwerpunkt nach v0.1

Der Upstream-Pfad **Idee → G0 → Story → G1 → Figuren/Recherche → G2 → erste Szene → READY_FOR_G3** ist jetzt technisch geschlossen und durch einen synthetischen End-to-End-Test abgesichert.

Der nächste Ausbau sollte deshalb nicht wieder innerhalb G0–G3 neue Detailtiefe erzeugen. Der nächste strukturell offene Übergang ist **G3 → Prosa → G4**: Wie wird aus einer freigegebenen Szene ein kontrollierter Prosa-Batch, dessen narratives Gewicht früh geprüft werden kann, bevor ein kompletter Roman zu dünn oder methodisch übererklärt geschrieben wird?
