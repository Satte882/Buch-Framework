# STORY_BLOCKS

version: v0.2
story_package_version: v0.1
blocks_status: ready

## Zweck

Diese Datei zerlegt den bestehenden FEHLALARM-Storykern horizontal in dramaturgische Makro-Bausteine. Sie führt keine neue Handlung ein und ersetzt nicht `STORY_PACKAGE.md`; sie macht dessen Kausalität vor der Event- und Beat-Ebene explizit prüfbar.

| block_id | Funktion im Gesamtbogen | Ausgangslage | zentrale Verschiebung / Druck | relevante Entscheidung | Konsequenz | Leserfunktion | Figurenkern | Rechercheabhängigkeiten |
|---|---|---|---|---|---|---|---|---|
| B01 | Gewöhnung und erneutes Warnsignal etablieren | Derselbe Bereich hat mehrfach folgenlos gewarnt; die Nachtschicht behandelt das Signal deshalb mit erlernter Skepsis. | Ein neues internes Rauch-/Prozesswarnsignal trifft auf ausgefallene Flurkamera und einen offiziell leer gemeldeten Bereich. | Noch keine finale Eskalationsentscheidung; Mara muss bestimmen, wie ernst das Signal unter der bekannten Fehlalarm-Vorgeschichte genommen wird. | Der neue Alarm bleibt plausibel harmlos, kann aber wegen der Informationslücken nicht belastbar entkräftet werden. | Der Leser versteht, warum Nicht-Eskalation nicht sofort als Dummheit erscheint. | Mara trägt Erfahrungswissen und Sicherheitspflicht gleichzeitig. | R-001 |
| B02 | Die vernünftige Abkürzung als bewusste Entscheidung setzen | Der Alarm ist ungeklärt; der empfindliche Nachtversuch würde durch volle Eskalation sicher verloren gehen. | Nils macht den realen betrieblichen Preis sichtbar und stützt sich auf dieselbe Fehlalarm-Erfahrung und denselben Belegungsstand wie Mara. | Mara entscheidet sich gegen sofortige Volleskalation und für persönliche lokale Verifikation bei weiter bestehender Eskalationsbereitschaft. | Sie verlässt den Kontrollraum und übernimmt selbst das Risiko, die Lage vor Ort zu klären. | Der Leser soll Maras Entscheidung als riskant, aber nachvollziehbar akzeptieren. | Mara und Nils vertreten unterschiedliche Risikogewichtungen ohne versteckte Agenda. | R-001 |
| B03 | Die Harmlosigkeitsannahme durch einen konkreten Widerspruch beschädigen | Vor Ort wirkt der Bereich zunächst ruhig und liefert keinen offenen Brandbefund. | Eine frische Anwesenheitsspur widerspricht dem offiziellen Belegungsstand. | Mara muss die Annahme „Bereich leer, daher wahrscheinlich wieder Fehlalarm“ neu gewichten. | Der Fehlalarm-Erfahrung fehlt erstmals eine tragende Voraussetzung: die erwartete Leerbelegung. | Der Leser erhält denselben Gegenbeleg wie Mara und kann die Unsicherheit neu bewerten. | Lea wird als reale, aber zunächst nur indirekt sichtbare menschliche Konsequenz vorbereitet. | none |
| B04 | Entscheidungsschwelle durch zusammenlaufende Evidenz kippen | Anwesenheit ist plausibel geworden, der technische Alarm ist aber noch nicht eindeutig bestätigt. | Ein konkreter Rauch-/Hitzehinweis kommt hinzu; Nils bittet aus weiterhin nachvollziehbaren Gründen um wenige weitere Sekunden. | Mara entscheidet, dass die Kombination aus Warnsignal, falschem Belegungsstand und physischem Gefahrenhinweis die bisherige Abkürzung nicht mehr trägt. | Die informelle Routine verliert ihre Rechtfertigung für diesen konkreten Fall. | Der Leser erlebt den Kipppunkt als Belegverschiebung statt als plötzlichen Heldeninstinkt. | Mara übernimmt Verantwortung; Nils bleibt legitime Gegenposition, nicht Antagonist. | R-001 |
| B05 | Die Routine sichtbar brechen und den Preis der Entscheidung real machen | Mara verfügt nun über genügend konkrete Gegenindikatoren, während die betrieblichen Kosten unverändert hoch bleiben. | Die Zeit für weitere lokale Verifikation wird selbst zum Risiko. | Mara löst die volle interne Alarm-/Evakuierungskette aus. | Der Nachtversuch wird verloren; gleichzeitig beginnt die sichere Räumung des betroffenen Bereichs. | Der Leser sieht, dass die richtige Sicherheitsentscheidung einen echten Preis hat und deshalb nicht trivial war. | Maras Kernhandlung ist Eskalation, keine heroische Rettungsaktion. | R-001 |
| B06 | Konsequenz und Umdeutung abschließen | Die volle Sicherheitsreaktion läuft; die Frage nach realer Gefahr und tatsächlicher Anwesenheit ist noch offen. | Lea erreicht den sicheren Bereich bzw. wird aus dem betroffenen Bereich geführt; der aktuelle Alarm bestätigt sich als berechtigt. | Keine neue Plotentscheidung; die Figuren müssen die Bedeutung der vorherigen Routine einordnen. | Frühere Fehlalarme bleiben wahr, verlieren aber ihren Status als Entwarnungsbeweis für neue Signale; Nils bleibt fachlich nachvollziehbar, der Versuch ist trotzdem verloren. | Der Leser erhält die zentrale Umdeutung ohne Twist: Erfahrung war relevant, aber übergeneralisiert. | Mara akzeptiert die Grenze der Routine; Nils wird nicht zum Schuldigen; Lea bleibt konkrete Konsequenz statt Nebenplot. | R-001 |

## Horizontaler Gesamtcheck

- Anfang: B01 macht Fehlalarm-Gewöhnung und aktuelle Unsicherheit gleichzeitig sichtbar.
- Eskalation: B02 setzt die nachvollziehbare Abkürzung; B03 und B04 entziehen ihr schrittweise die Grundlage.
- Kipppunkt: B04 verändert die Gewichtung durch kombinierte Evidenz, nicht durch neue Geheimkenntnis.
- Finale Entscheidung: B05 enthält die eigentliche irreversible Handlung.
- Nachhall/Umdeutung: B06 bestätigt reale Gefahr, ohne die früheren Fehlalarme rückwirkend umzuschreiben.
- Konflikt und Leitfrage aus `STORY_PACKAGE.md` bleiben über alle sechs Bausteine erhalten.
- Keine neue Figur, kein Täter, keine Verschwörung und kein zusätzlicher Twist wurden eingeführt.

## Offene Architekturpunkte

- none

**Arbeitsregel:** Erst nach vollständiger Event-Abdeckung aller sechs Bausteine ist das FEHLALARM-G1-Paket v0.2 review-fähig. Zwischen STORY_BLOCKS und EVENTS entsteht kein zusätzlicher Human Gate.
