# RESEARCH_REGISTER

register_status: ready

Dieses Register enthält nur Recherchefragen, die für Plot, Figurenhandlung, Plausibilität oder konkrete Szenenentscheidungen relevant sind. Recherche ist im v0.2-Workflow ein Querschnittsartefakt und besitzt keinen eigenen Human Gate.

| ID | Frage | Betroffene Ebene / Artefakte | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung | blocking_now |
|---|---|---|---|---|---|---|---|
| R-001 | Welche vereinfachte Alarm-/Verifikationskette ist für ein modernes Forschungs-/Laborgebäude plausibel, ohne eine formale Brandmeldeanlage falsch darzustellen? | STORY_BLOCKS.md; EVENTS.md; spätere BEATS/SCENE_PLAN-Artefakte | high | resolved | DIN 14675-1 (Aufbau und Betrieb von Brandmeldeanlagen); DIN VDE 0833-2 (Festlegungen für Brandmeldeanlagen); DIN-Fachinformation zu Anschlussbedingungen für BMA (2023); DIN-Fachinformation zu Übertragung/Fernzugriff (2025) | FEHLALARM behauptet bewusst **keine** manuell verzögerbare, feuerwehraufgeschaltete Haupt-Brandmeldeanlage. Das anfängliche Signal ist eine interne technische Rauch-/Prozesswarnung des Forschungsbereichs, die eine lokale Verifikation auslöst. Sobald Mara vor Ort konkrete Gefahrenindikatoren erkennt, startet sie die separate volle interne Alarm-/Evakuierungskette. Ob und wie eine öffentliche Feuerwehr automatisch aufgeschaltet wäre, wird im M1-Text nicht spezifiziert. | no |

## Recherchebegründung R-001

Die DIN-Quellen zeigen, dass reale Brandmeldeanlagen in Deutschland normativ geregelt sind und die konkrete Aufschaltung zusätzlich objektspezifischen Anschlussbedingungen unterliegt. DIN weist zudem darauf hin, dass Alarmübertragungsinformationen an eine Empfangsstelle erst nach dem Hauptalarm übertragen werden; daraus lässt sich keine beliebige manuelle „erst mal zurücksetzen“-Logik für eine formale aufgeschaltete BMA ableiten.

Für den Mini-Testfall wird deshalb eine bewusst einfachere und plausiblere Ebene gewählt: ein internes technisches Warnsignal im Forschungsbetrieb. Mara entscheidet zunächst über lokale Verifikation versus interne Volleskalation. Damit bleibt der dramaturgische Mechanismus erhalten, ohne technische Sicherheitsnormen als frei disponierbar darzustellen.

## Blockierstatus

R-001 ist `resolved`. `blocking_now: no` bedeutet hier nicht, dass die Frage unwichtig ist, sondern dass die für G1 benötigte Storyentscheidung bereits festgelegt ist. Nachgelagerte Beats und Szenenkarten müssen innerhalb dieser Entscheidung bleiben und dürfen keine detailliertere Feuerwehr-/BMA-Prozedur erfinden.

## Gate-Bezug

- G1 prüft, dass die Story-Architektur keine offene blockierende Rechercheabhängigkeit enthält.
- G2 prüft erneut, dass keine Beat-/Szenenentscheidung eine noch offene `blocking_now: yes`-Frage voraussetzt.
