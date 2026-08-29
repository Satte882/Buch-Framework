# RESEARCH_REGISTER

register_status: ready

Dieses Register enthält nur Recherchefragen, die für Plot, Figurenhandlung, Plausibilität oder konkrete Szenenentscheidungen relevant sind.

| ID | Frage | Betroffene Szene(n) | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung |
|---|---|---|---|---|---|---|
| R-001 | Welche vereinfachte Alarm-/Verifikationskette ist für ein modernes Forschungs-/Laborgebäude plausibel, ohne eine formale Brandmeldeanlage falsch darzustellen? | S1; S2; S3 | high | resolved | DIN 14675-1 (Aufbau und Betrieb von Brandmeldeanlagen); DIN VDE 0833-2 (Festlegungen für Brandmeldeanlagen); DIN-Fachinformation zu Anschlussbedingungen für BMA (2023); DIN-Fachinformation zu Übertragung/Fernzugriff (2025) | FEHLALARM behauptet bewusst **keine** manuell verzögerbare, feuerwehraufgeschaltete Haupt-Brandmeldeanlage. Das anfängliche Signal ist eine interne technische Rauch-/Prozesswarnung des Forschungsbereichs, die eine lokale Verifikation auslöst. Sobald Mara vor Ort konkrete Gefahrenindikatoren erkennt, startet sie die separate volle interne Alarm-/Evakuierungskette. Ob und wie eine öffentliche Feuerwehr automatisch aufgeschaltet wäre, wird im M1-Text nicht spezifiziert. |

## Recherchebegründung R-001

Die DIN-Quellen zeigen, dass reale Brandmeldeanlagen in Deutschland normativ geregelt sind und die konkrete Aufschaltung zusätzlich objektspezifischen Anschlussbedingungen unterliegt. DIN weist zudem darauf hin, dass Alarmübertragungsinformationen an eine Empfangsstelle erst nach dem Hauptalarm übertragen werden; daraus lässt sich keine beliebige manuelle „erst mal zurücksetzen“-Logik für eine formale aufgeschaltete BMA ableiten.

Für den Mini-Testfall wird deshalb eine bewusst einfachere und plausiblere Ebene gewählt: ein internes technisches Warnsignal im Forschungsbetrieb. Mara entscheidet zunächst über lokale Verifikation versus interne Volleskalation. Damit bleibt der dramaturgische Mechanismus erhalten, ohne technische Sicherheitsnormen als frei disponierbar darzustellen.

## Gate-Regel

`register_status: ready` bedeutet: Die bekannte plotrelevante Recherchefrage ist erfasst und für die geplanten Szenen aufgelöst. Die Szenen dürfen keine detailliertere reale Feuerwehr-/BMA-Prozedur erfinden, die über diese Entscheidung hinausgeht.