# BEATS

version: v0.2
events_version: v0.2
beats_status: ready

## Zweck

Diese Datei bricht die durch `G1 = APPROVE` freigegebene FEHLALARM-Event-Kette horizontal in erlebbare Beat-Schritte herunter. Sie führt keine neue Storylogik ein. Jeder Beat ist auf genau ein freigegebenes Event zurückgeführt und einer geplanten Szene zugeordnet.

| beat_id | event_id | planned_scene_id | POV | Auslöser / beobachtbarer Schritt | Reaktion / Entscheidung | Druckverschiebung | Informationsverschiebung | Konsequenz | character_state_impact | research_refs |
|---|---|---|---|---|---|---|---|---|---|---|
| BT001 | E001 | S1 | Mara Voss | Das interne Rauch-/Prozesswarnsignal aus dem bekannten Problembereich erscheint erneut in der Sicherheitszentrale. | Mara nimmt das Signal aktiv auf und behandelt es weder als bestätigte Gefahr noch als automatisch harmlosen Wiederholungsfehler. | Aus routinemäßiger Nachtschicht wird eine unklare Sicherheitslage. | Ein neues Signal liegt vor; seine Bedeutung ist noch offen. | Mara muss den aktuellen Fall neu bewerten statt nur die Vorgeschichte fortzuschreiben. | Mara aktiviert ihre Sicherheitsrolle, trägt aber die bisherige Fehlalarm-Erfahrung weiter mit. | R-001 |
| BT002 | E002 | S1 | Mara Voss | Mara versucht die Lage über die Flurkamera und den Belegungsstand zu verifizieren; die Kamera liefert kein verwertbares Bild, der Bereich ist offiziell leer. | Sie hält die Leerbelegung als beruhigenden Hinweis fest, erkennt aber zugleich die fehlende Sichtkontrolle. | Sicherheit und Entwarnung bleiben gleichzeitig unvollständig. | Der Leser erhält dieselbe widersprüchliche Datenlage wie Mara: kein Bild, aber scheinbar niemand vor Ort. | Eine rein technische Fernklärung ist nicht möglich. | Maras Skepsis gegenüber dem Alarm bleibt nachvollziehbar, ohne zur Gewissheit zu werden. | R-001 |
| BT003 | E003 | S1 | Mara Voss | Nils Berger macht die mehrfachen Fehlalarme und den sicheren Verlust des empfindlichen Nachtversuchs bei voller Eskalation konkret. | Mara hört den betrieblichen Einwand an und gewichtet ihn als realen Schaden, nicht als bloßen Druck von außen. | Der Preis eines vorsorglichen Vollalarms wird unmittelbar und messbar. | Die Gegenposition erhält einen legitimen Grund: Versuchsschutz bei unklarer Gefahrenlage. | Die Entscheidung kann nicht als simple Regelbefolgung behandelt werden. | Mara und Nils bleiben fachlich verbunden, gewichten aber das Risiko unterschiedlich. | R-001 |
| BT004 | E004 | S1 | Mara Voss | Die vorhandenen Daten liefern weiterhin weder Entwarnung noch bestätigte Gefahr. | Mara entscheidet: noch keine volle Alarm-/Evakuierungskette; sie übernimmt selbst die lokale Verifikation und hält die Eskalation verfügbar. | Die Unsicherheit wird in persönliche Verantwortung und Zeitdruck übersetzt. | Der Leser weiß, dass die Verzögerung bewusst und begründet gewählt ist. | Mara verlässt die Sicherheitszentrale und bindet die nächste Entscheidung an reale Vor-Ort-Evidenz. | Mara trägt die informelle Routine aktiv mit; Nils ist nicht alleiniger Verursacher der Abkürzung. | R-001 |
| BT005 | E005 | S2 | Mara Voss | Mara erreicht den betroffenen Bereich; zunächst ist kein offener Brand sichtbar und die Umgebung wirkt ruhiger als das Warnsignal erwarten lässt. | Sie prüft den Bereich weiter statt die anfängliche Ruhe sofort als Entwarnung zu nehmen. | Der Druck fällt kurz ab, ohne die Lage zu schließen. | Die alte Fehlalarm-Hypothese bleibt für einen Moment plausibel. | Mara gewinnt keinen belastbaren Grund, die Prüfung abzubrechen. | Maras Erwartung neigt kurz wieder zum bekannten Fehlalarm-Muster. | none |
| BT006 | E005 | S2 | Mara Voss | Eine frische Anwesenheitsspur zeigt, dass der offiziell leere Bereich sehr wahrscheinlich doch benutzt wurde. | Mara verwirft die Leerbelegung als belastbare Entwarnung und sucht gezielt nach weiteren Widersprüchen. | Aus technischer Unsicherheit wird zusätzlich ein mögliches Personenrisiko. | Ein konkreter Fakt widerspricht dem bisherigen Belegungsstand. | Die Annahme „niemand gefährdet“ kann nicht mehr verwendet werden. | Mara verschiebt ihre Risikogewichtung; Lea wird als mögliche reale Betroffene vorbereitet, ohne bereits bestätigt zu sein. | none |
| BT007 | E006 | S2 | Mara Voss | In Richtung des Technik-/Laborbereichs nimmt Mara einen konkreten Rauch-/Hitzehinweis wahr. | Sie behandelt den Hinweis als unabhängigen Gegenbeleg zum bisherigen Fehlalarm-Muster und nähert sich nicht weiter unkritisch. | Der Gefahrenverdacht steigt deutlich; weiteres Zögern wird selbst riskanter. | Zur falschen Leerannahme kommt erstmals ein physischer Gefahrenhinweis. | Die bisherige lokale Prüfroutine verliert einen wesentlichen Teil ihrer Rechtfertigung. | Maras Überzeugung kippt von „wahrscheinlich wieder harmlos“ zu „muss als reale Gefahr behandelt werden, sofern kein starker Gegenbeleg kommt“. | R-001 |
| BT008 | E007 | S2 | Mara Voss | Mara meldet die veränderte Lage; Nils bittet ausgehend von Fehlalarm-Vorgeschichte und offiziellem Belegungsstand um wenige weitere Sekunden Verifikation. | Mara prüft den Einwand gegen die jetzt vorliegenden Gegenindikatoren, statt ihn wegen des Konflikts persönlich abzuwerten. | Die letzte plausible Gegenoption bleibt sichtbar, während ihre Tragfähigkeit sinkt. | Nils verfügt weiterhin nicht über verborgenes Wissen; seine Position stammt aus derselben früheren Datenlage. | Die finale Entscheidung muss aus der Beleglage entstehen, nicht aus Antipathie oder Heldeninstinkt. | Die fachliche Beziehung bleibt intakt, aber Maras aktuelle Lagekenntnis überholt Nils' Risikogewichtung. | R-001 |
| BT009 | E007 | S2 | Mara Voss | Mara stellt die drei aktuellen Befunde gegeneinander: Warnsignal, unzuverlässige Leerbelegung, physischer Gefahrenhinweis. | Sie entscheidet, dass weitere lokale Verifikation keinen ausreichenden Erkenntnisgewinn mehr gegenüber dem Verzögerungsrisiko bietet. | Die verbleibende Entscheidungszeit kollabiert; aus Abwägung wird Handlungszwang. | Nicht ein einzelnes Indiz, sondern die kumulierte Evidenz überschreitet die bisherige Schwelle. | Die informelle Routine ist für diesen konkreten Fall beendet. | Mara übernimmt die Verantwortung, ihre eigene frühere Abkürzung zu widerrufen. | R-001 |
| BT010 | E008 | S2 | Mara Voss | Mara aktiviert die volle interne Alarm-/Evakuierungskette. | Sie setzt die Eskalation trotz des sicheren Verlusts des Nachtversuchs um. | Der Sicherheitskonflikt wird irreversibel entschieden; die Kosten sind nicht mehr vermeidbar. | Die Storyfrage verschiebt sich von „eskalieren oder weiter prüfen?“ zu „war die Neubewertung rechtzeitig und berechtigt?“. | Räumung und Sicherheitsreaktion beginnen; der Nachtversuch wird aufgegeben. | Mara bindet sich an die Sicherheitsentscheidung; Nils muss die neue Lage akzeptieren, ohne dadurch rückwirkend zum Schuldigen zu werden. | R-001 |
| BT011 | E009 | S3 | Mara Voss | Während die Alarm-/Evakuierungskette läuft, wird bestätigt, dass tatsächlich noch eine Person aus dem betroffenen Bereich herauskommen muss bzw. herausgeführt wird. | Mara ordnet die Restanwesenheit als reale Konsequenz der zuvor falschen Belegannahme ein und bleibt bei der koordinierten Sicherheitsreaktion. | Aus möglichem Personenrisiko wird konkrete menschliche Betroffenheit. | Leas Anwesenheit ist nun Fakt statt indirekter Spur. | Die Entscheidung zur Eskalation erhält eine unmittelbar menschliche Relevanz. | Mara erkennt, dass ihre frühere Risikorechnung auf unvollständigen Organisationsdaten beruhte; Lea wird von möglicher zu bestätigter Betroffener. | none |
| BT012 | E009 | S3 | Mara Voss | Lea erreicht den sicheren Bereich beziehungsweise wird durch die laufende Haus-/Sicherheitsorganisation dorthin gebracht. | Mara führt keine heroische Einzelrettung aus, sondern hält die richtige Eskalations- und Koordinationsentscheidung aufrecht. | Akute Personengefahr sinkt, während die Bewertung der Verzögerung bestehen bleibt. | Lea ist in Sicherheit; ihre Restanwesenheit hatte einen banalen betrieblichen Grund und war keine Plotfalle. | Die menschliche Konsequenz wird real, ohne einen neuen Nebenplot zu eröffnen. | Mara und Lea bleiben funktional verbunden; persönliche Nähe wird nicht nachträglich zur Motivationsabkürzung. | none |
| BT013 | E010 | S3 | Mara Voss | Der technische Vorfall bestätigt sich als real und ausreichend gefährlich, um den Alarm und die Evakuierung zu rechtfertigen. | Mara ordnet die neue Tatsache gegen die Serie früherer Fehlalarme ein. | Die Unsicherheit über den aktuellen Alarm endet, die methodische Frage bleibt. | Der aktuelle Alarm war berechtigt; die früheren Fehlalarme werden dadurch nicht rückwirkend umgeschrieben. | Die zentrale Umdeutung ist faktisch abgesichert. | Maras Überzeugung verschiebt sich von Routinevertrauen zu bewusster Begrenzung dieser Routine. | R-001 |
| BT014 | E010 | S3 | Mara Voss | Gleichzeitig steht fest, dass der Nachtversuch durch die Eskalation verloren ist. | Mara akzeptiert den betrieblichen Schaden als reale Folge einer unter neuer Evidenz notwendigen Sicherheitsentscheidung. | Die richtige Entscheidung bleibt teuer und wird nicht nachträglich risikolos gemacht. | Nils' vorheriger Gegenanreiz erweist sich als real, auch wenn er die finale Entscheidung nicht mehr tragen konnte. | Der Konflikt wird nicht moralisch vereinfacht: Sicherheit gewann, aber der Preis existiert. | Mara und Nils können dieselben Fakten anerkennen, obwohl ihre frühere Gewichtung unterschiedlich war. | R-001 |
| BT015 | E010 | S3 | Mara Voss | Aktuelle Gefahr, Leas Anwesenheit und Verlust des Versuchs liegen als gemeinsame Konsequenz vor. | Mara zieht die operative Grenze: Frühere Erfahrung darf künftige Signale informieren, aber nicht als automatische Entwarnung fungieren, wenn neue Gegenbelege entstehen. | Der äußere Zeitdruck endet; die Bedeutung der Entscheidung wird sichtbar. | Die Story beantwortet die Leitfrage nicht mit einer starren Regel, sondern mit der Notwendigkeit, Evidenz neu zu gewichten. | Der Mini-Fall endet ohne zusätzlichen Twist oder Schuldigen. | Mara übernimmt die Verantwortung für die Grenze der Routine; Nils bleibt nachvollziehbare Gegenposition; Lea bleibt konkrete Konsequenz. | R-001 |

## Horizontale Abdeckung

- `E001` → BT001
- `E002` → BT002
- `E003` → BT003
- `E004` → BT004
- `E005` → BT005–BT006
- `E006` → BT007
- `E007` → BT008–BT009
- `E008` → BT010
- `E009` → BT011–BT012
- `E010` → BT013–BT015

## Geplante Szenenabdeckung

- **S1 – Kontrollraum / bewusste Abkürzung:** BT001–BT004
- **S2 – Vor Ort / Evidenz kippt / Eskalation:** BT005–BT010
- **S3 – Konsequenz / Umdeutung:** BT011–BT015

Die Szenenzuordnung konkretisiert die bereits in `STORY_PACKAGE.md` angelegte Drei-Szenen-Struktur. Die Aktivierung der vollen Eskalation bleibt als Endentscheidung von S2 erhalten; S3 trägt deren reale Folgen und die Umdeutung.

## Horizontaler Gesamtcheck

- Alle zehn freigegebenen Events besitzen mindestens einen Beat.
- Die Beats konkretisieren Handlung, Wahrnehmung, Entscheidung, Informationsverschiebung oder Konsequenz; kein Beat führt eine neue Storyentscheidung außerhalb der G1-Architektur ein.
- Maras POV bleibt durchgehend die Entscheidungsachse.
- Nils bleibt bis zum Kipppunkt eine reale Gegenoption und erhält kein verborgenes Wissen.
- Lea wird erst über einen Gegenbeleg vorbereitet und später als reale Person bestätigt; sie ist keine künstliche Rettungsmission.
- Der Druck verläuft über die drei Szenen von unklarer Warnung → bewusster Abkürzung → widersprechender Evidenz → kollabierender Entscheidungszeit → irreversibler Eskalation → realer Konsequenz.
- R-001 wird dort referenziert, wo Alarm-/Verifikations- oder Sicherheitslogik die Beat-Ausgestaltung begrenzt.

## Offene Prose-Ready-Punkte

- none auf Beat-Ebene; Szenenkarten und Character States müssen die Beats jetzt konkret tragen, ohne neue relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidungen einzuführen.

**Arbeitsregel:** Erst nachdem diese Beat-Ebene horizontal über den gesamten Mini-Fall geschlossen ist, werden die drei Szenenkarten und die zugehörigen Character States systematisch neu für v0.2 abgeleitet. Es gibt zwischen Beats und Szenenkarten keinen zusätzlichen Human Gate.