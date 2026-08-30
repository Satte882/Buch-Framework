# BEATS

version: v0.1
events_version: v0.1
beats_status: ready

## Zweck

Diese Datei bricht die durch `G1 = APPROVE` freigegebene SPERRFRIST-Ereigniskette horizontal in erlebbare Beat-Schritte herunter. Jeder Beat ist auf genau ein freigegebenes Event zurückgeführt und bereits einer der genau zehn geplanten Szenen zugeordnet. Es werden keine neuen G1-Plotentscheidungen eingeführt.

| beat_id | event_id | planned_scene_id | POV | Auslöser / beobachtbarer Schritt | Reaktion / Entscheidung | Druckverschiebung | Informationsverschiebung | Konsequenz | character_state_impact | research_refs |
|---|---|---|---|---|---|---|---|---|---|---|
| BT001 | E001 | S1 | Nora Feld | Quelle A übergibt Nora das interne Prüfungsdossier. | Nora nimmt das Material an, behandelt es aber ausdrücklich als Recherchegrundlage statt als fertigen Beweis. | Aus einem normalen Redaktionstag wird eine potenziell zeitkritische Recherche. | T und K erscheinen zunächst gekoppelt, sind aber noch nicht geprüft. | Nora bindet Zeit und Teamkapazität an die Verifikation. | Nora↔Quelle A startet mit hohem Arbeitsvertrauen. | R-01, R-02 |
| BT002 | E002 | S1 | Nora Feld | Quelle A verlangt Vertraulichkeit und Sperrfrist bis 18 Uhr. | Nora akzeptiert die Schutzbedingung und begrenzt die interne Nutzung auf das notwendige Team. | Die Recherche erhält eine externe Deadline und eine Schutzrestriktion. | Keine neue Sachwahrheit; Nutzbarkeit der Informationen wird eingeschränkt. | Jede spätere Anfrage muss Quellenschutz mitdenken. | Nora übernimmt persönlich Verantwortung für Quelle A. | R-01 |
| BT003 | E003 | S1 | Nora Feld | In den Unterlagen tauchen kurzfristige Rollouttermine bei kommunalen Nutzern auf. | Nora erkennt, dass auch Nicht-Veröffentlichen eine reale Konsequenz haben kann. | Die Sperrfrist kollidiert mit möglicher Aktualität. | T erhält potenzielles öffentliches Gewicht, ohne technisch bestätigt zu sein. | Die Recherche kann nicht beliebig vertagt werden. | Noras Ziel verschiebt sich von bloßer Prüfung zu belastbarer Entscheidung vor Deadline. | R-02 |
| BT004 | E003 | S1 | Nora Feld | Nora legt Dossier, Sperrfrist und Rollouttermine nebeneinander. | Sie setzt als Arbeitsregel: keine Dossier-Gesamtgeschichte übernehmen; zuerst tragende Behauptungen isolieren. | Aus diffusem Alarm wird strukturierter Prüfauftrag. | Der Leser weiß, dass Zeitwert und Belegbarkeit gleichzeitig zählen. | S2 beginnt mit Behauptungszerlegung statt mit voreiliger Storyfassung. | Nora hält Vertrauen in Quelle A und Skepsis gegenüber ihrer Interpretation gleichzeitig. | R-01, R-02 |
| BT005 | E004 | S2 | Nora Feld | Nora und Jonas markieren, welche Dokumente T und welche K tragen sollen. | Sie trennen T = technischer Befund von K = Wissen/Verantwortung und führen zwei Evidenzketten. | Die Recherche wird methodisch anspruchsvoller, aber kontrollierbarer. | Ein wahrer T-Befund kann K nicht automatisch beweisen. | Jede spätere Information muss gegen beide Stränge separat geprüft werden. | Nora strukturiert; Jonas übernimmt die technische Dokumentkette. | R-01, R-02 |
| BT006 | E005 | S2 | Nora Feld | Jonas zeigt ein intern konsistentes Testprotokoll mit kritischem Failover-/Auslieferungsbefund. | Nora akzeptiert den Befund als ersten T-Beleg, verweigert aber die Gleichsetzung mit dem Rolloutstand. | T gewinnt Substanz. | „Problem existierte in einem Teststand“ wird plausibel; aktuelle Relevanz bleibt offen. | Die technische Spur wird priorisiert. | Jonas gewinnt fachliche Sicherheit, Nora hält die Beleggrenze fest. | R-02 |
| BT007 | E006 | S2 | Nora Feld | David meldet, dass eine Konkurrenzredaktion denselben Themenkomplex prüft. | Nora hält an der Prüfung fest, akzeptiert aber, dass verlorene Zeit nun einen publizistischen Preis hat. | Der abstrakte Zeitdruck wird Wettbewerb. | Keine Sachwahrheit ändert sich. | Die Redaktion braucht Zwischenentscheidungen statt unbegrenzter Recherche. | Nora↔David geraten erstmals in einen echten Timingkonflikt. | none |
| BT008 | E007 | S2 | Nora Feld | David verlangt bis zum internen Nachmittagstermin eine belastbare Kernthese statt die komplette Dossierstory. | Nora akzeptiert diesen Arbeitskorridor. | Der Konflikt verschiebt sich von „Tempo gegen Sorgfalt“ zu „welcher Kern ist rechtzeitig belastbar?“. | Publizierbarkeit wird von Vollständigkeit getrennt. | S3 muss Versionen und Gegenposition schnell klären. | Nora erkennt David als legitimen Gegenpol, nicht als bloßen Druckmacher. | none |
| BT009 | E008 | S3 | Nora Feld | Jonas entdeckt unterschiedliche Build-/Release-Kennungen in den Dokumenten. | Nora stoppt jede weitere T-Zuspitzung bis zur Versionszuordnung. | Der bislang stärkste Sachstrang wird fragiler. | Testbefund ja; Bezug zum relevanten Release unklar. | Die Redaktion verliert scheinbar gewonnenen Boden. | Jonas muss seine frühe technische Sicherheit korrigieren. | R-02 |
| BT010 | E009 | S3 | Nora Feld | Dokumentkopf/Metadaten zeigen, dass mindestens eine hervorgehobene Seite älter als die Freigabeübersicht ist. | Nora trennt Vertrauen in Quelle A von Vertrauen in die Dossierzusammenstellung. | Zweifel trifft nun auch die Quelle-Interpretation. | Ein veralteter Teilbefund ist real möglich. | Veröffentlichung auf Basis dieser Seite scheidet aus. | Nora↔Quelle A bleibt geschützt, aber epistemisch weniger unkritisch. | R-02 |
| BT011 | E010 | S3 | Nora Feld | Mira hilft, eine konkrete Anfrage zu Testfehler, Versionsstand und behauptetem Vorwissen zu formulieren. | Nora gibt nur die für faire Stellungnahme nötigen Details preis. | Die Redaktion öffnet bewusst einen Gegeninformationskanal. | Das Unternehmen erfährt den Kern der Prüfung. | Quellenschutz und Stellungnahme müssen gleichzeitig gehalten werden. | Nora↔Mira arbeiten erstmals operativ an derselben Behauptungsgrenze. | R-01 |
| BT012 | E011 | S3 | Nora Feld | Die Pressestelle antwortet schnell: zentrale Seiten seien überholt. | Nora wertet die Antwort als überprüfbaren Einwand statt als PR-Rauschen. | Versionsdruck steigt. | Der Einwand bestätigt, dass Dokumentstände zentral sind, widerlegt T aber noch nicht. | Die Versionskette wird zwingende Voraussetzung. | Nora akzeptiert Gegeninformation auch gegen die eigene Arbeitshypothese. | R-01, R-02 |
| BT013 | E012 | S3 | Nora Feld | Das Unternehmen bestreitet das konkrete Vorwissen der ins Auge gefassten Führungsperson. | Mira markiert K als derzeit nicht ausreichend gesichert; Nora hält K offen. | Persönliche Verantwortungszuschreibung wird riskanter als T. | T und K driften sichtbar auseinander. | S4 braucht unabhängige Quelle und Chronologie. | Nora akzeptiert, dass die spektakulärere K-These schwächer sein kann. | R-01 |
| BT014 | E013 | S4 | Nora Feld | Quelle B bestätigt unabhängig den kritischen technischen Befund. | Nora wertet die Bestätigung als zweite T-Stütze, nicht als Beweis für K. | T stabilisiert sich nach dem Versionsschock. | Der technische Kern stammt nicht nur aus Quelle A. | Die Redaktion kann T weiterverfolgen. | Nora gewinnt Vertrauen in T zurück. | R-02 |
| BT015 | E014 | S4 | Nora Feld | Quelle B legt die tatsächliche Testchronologie dar: der relevante Managementtermin lag vor Abschluss der späteren Testserie. | Nora nimmt K deutlich zurück. | K verliert einen zentralen Zeitanker. | Die konkrete Führungsperson kann den späteren Befund nicht allein aus dem Dossier vor dem Termin gekannt haben. | Die ursprüngliche Dossierdeutung ist nicht mehr tragfähig. | Nora trennt Quelle-As Ehrlichkeit von deren Schlussfolgerung. | R-01, R-02 |
| BT016 | E015 | S4 | Nora Feld | Quelle B verlangt, ein identifizierendes internes Detail nicht zu veröffentlichen. | Nora akzeptiert die Bedingung, sofern der Kern anderweitig belegbar bleibt. | Belegbarkeit und Publizierbarkeit fallen auseinander. | Ein Detail kann wahr und dennoch nicht verwendbar sein. | Die spätere Story muss abstrahieren. | Nora übernimmt auch gegenüber Quelle B konkrete Schutzverantwortung. | R-01 |
| BT017 | E015 | S4 | Nora Feld | Nora bilanziert nach dem Gespräch: T stärker, K schwächer, Quellenauflagen enger. | Sie priorisiert für den nächsten Arbeitsblock Belegkette und Schutz statt größere Story. | Die Geschichte wird weniger spektakulär und zugleich belastbarer. | Zwei Evidenzstränge haben jetzt klar unterschiedliche Reifegrade. | S5 beginnt unter engeren Kontakt- und Schutzbedingungen. | Nora hält die eigene Linie gegen Zeitdruck aufrecht. | R-01, R-02 |
| BT018 | E016 | S5 | Nora Feld | Nora erfährt, dass Jonas für die Versionsverifikation eine sehr präzise Rückfrage an einen internen Ansprechpartner gesendet hat. | Sie erkennt zunächst den fachlichen Nutzen, aber noch nicht das konkrete Ausmaß des Risikos. | Recherchegeschwindigkeit kollidiert mit Quellenschutz. | Kein neuer Sachbeleg; mögliche Informationsleckage entsteht. | Die Arbeitsweise selbst wird zur Risikoquelle. | Nora↔Jonas kippen von rein fachlichem Vertrauen in Kontrollbedarf. | R-01 |
| BT019 | E017 | S5 | Nora Feld | Quelle A meldet alarmiert, dass intern nach dem Ursprung bestimmter Unterlagen gesucht wird. | Nora verbindet die Reaktion mit der konkreten Anfrage und stoppt weitere detailreiche Direktkontakte. | Aus abstraktem Schutzrisiko wird reale Konsequenz. | Recherchehandlungen verändern die Informationslage. | Quelle A erwägt Kontaktabbruch; Geschwindigkeit sinkt. | Nora↔Quelle A Vertrauen leidet; Nora übernimmt Verantwortung statt Jonas vorzuschieben. | R-01 |
| BT020 | E018 | S5 | Nora Feld | Nora entscheidet über Jonas' Rolle nach dem Fehler. | Sie nimmt ihn nicht aus dem Fall, beschränkt aber seine externe Kontaktaufnahme. | Die Redaktion zahlt mit langsamerer Recherche für kontrollierteren Quellenschutz. | Keine Sachlage ändert sich; Governance ändert sich. | Jonas bleibt für Versionsarbeit verantwortlich, verliert aber Autonomie nach außen. | Nora↔Jonas: Vertrauen beschädigt, nicht beendet. | R-01 |
| BT021 | E018 | S5 | Nora Feld | Jonas akzeptiert die Grenze und bleibt an der internen Dokumentkette. | Nora bindet seine Rehabilitation an saubere Arbeit, nicht an Entschuldigung. | Der Beziehungskonflikt wird in eine überprüfbare Arbeitsregel übersetzt. | Leser wissen, dass Jonas weder ausgeschieden noch folgenlos davongekommen ist. | Batch 1 endet mit verändertem Teamzustand und engeren Informationswegen. | Nora führt durch Begrenzung statt Bestrafung; Jonas bleibt fachlich relevant. | R-01 |
| BT022 | E019 | S6 | Nora Feld | Mira ordnet T und K mit Nora neu: T kann bei sauberer Versionierung Tatsachenkern werden; K derzeit höchstens offene Verdachtsebene. | Nora akzeptiert zwei unterschiedliche Aussageformen. | Aus „eine Story“ werden zwei publizistische Belegreichweiten. | Unsicherheitsgrad wird explizit statt versteckt. | Die spätere Fassung kann enger werden, ohne ganz zu stoppen. | Nora↔Mira verschieben sich von Reibung zu gemeinsamer Eingrenzung. | R-01 |
| BT023 | E020 | S6 | Nora Feld | Mira verlangt substantielle Wiedergabe der Unternehmensantwort und Transparenz über veraltete Dokumentstände. | Nora und David akzeptieren diese Bedingungen für eine mögliche T-Fassung. | Eine polemisch stärkere Version fällt weg. | Leser sollen Gegenposition und Versionsunsicherheit erkennen können. | Der Textbau wird bereits durch Sorgfaltsanforderungen begrenzt. | David zeigt, dass er Tempo unter Bedingungen akzeptiert. | R-01 |
| BT024 | E021 | S6 | Nora Feld | Jonas findet Rolloutunterlagen, die kurzfristigen Einsatz eines Release Candidate derselben Versionslinie zeigen. | Nora priorisiert sofort die genaue RC-Zuordnung. | T bekommt aktuellen Öffentlichkeitswert. | Der technische Befund könnte roll-out-relevant sein. | Vollständige K-Klärung wird für die erste Publikation weniger zwingend. | Nora↔David nähern sich in der Priorisierung an. | R-02 |
| BT025 | E021 | S6 | Nora Feld | Nora legt Rolloutunterlage und bisherigen Testbefund nebeneinander, erkennt aber die noch fehlende eindeutige Kette. | Sie verweigert die Formulierung „betroffener Release“ solange diese letzte Zuordnung fehlt. | Hoher Aktualitätsdruck trifft auf eine einzelne noch fehlende Brücke. | Relevanz ist plausibel, nicht abschließend bewiesen. | S8 braucht einen belastbaren Release-/Freigabenachweis. | Nora bleibt trotz Annäherung an David bei derselben Belegschwelle. | R-02 |
| BT026 | E022 | S6 | Nora Feld | Quelle B bestätigt die praktische Relevanz des Teilpfads und warnt vor der Formulierung eines vollständigen Systemausfalls. | Nora engt T auf den tatsächlich belegten kritischen Teilpfad ein. | T wird gleichzeitig stärker und weniger spektakulär. | „kritischer Teilpfad kann unter definierten Bedingungen fehlschlagen“ ersetzt „System versagt“. | Die finale Story bekommt eine technische Schutzgrenze. | Nora akzeptiert Präzision als Gewinn, nicht als Abschwächung. | R-02 |
| BT027 | E023 | S7 | Nora Feld | Nora konfrontiert Quelle A mit Chronologie- und Versionswiderspruch. | Sie verlangt Trennung zwischen eigener Beobachtung und eigener Interpretation. | Das ursprüngliche Vertrauensverhältnis wird fachlich belastet. | Quelle A kann T stützen, K aber nicht aus eigener Kenntnis bestätigen. | Die umfassende Dossierthese verliert ihre wichtigste Quelle. | Nora↔Quelle A wechseln von Übernahmevertrauen zu kontrolliertem Vertrauen. | R-01 |
| BT028 | E023 | S7 | Nora Feld | Quelle A räumt ein, die konkrete K-Verknüpfung aus mehreren Dokumenten erschlossen zu haben. | Nora hält fest, dass diese Interpretation nicht als Tatsache in den Text darf. | Die moralisch plausible Erklärung verliert Beweisstatus. | K bleibt offen, Quelle A ist damit nicht automatisch unzuverlässig. | Quellenschutz bleibt bestehen. | Nora schützt die Person, ohne deren Schlussfolgerung zu übernehmen. | R-01 |
| BT029 | E024 | S7 | Nora Feld | Quelle A drängt dennoch auf die größere Verantwortungsstory. | Nora widerspricht inhaltlich und verweist auf getrennte Belegketten. | Der Konflikt verschiebt sich von Vertrauen zu Zweck der Veröffentlichung. | Moralische Verantwortung ersetzt keinen konkreten Vorwissensbeleg. | Eine spektakulärere Fassung wird bewusst verworfen. | Nora↔Quelle A erreicht die stärkste Spannung. | R-01 |
| BT030 | E024 | S7 | Nora Feld | Nora bestätigt Quelle A trotzdem die zugesagte Vertraulichkeit. | Sie trennt Schutzversprechen von redaktioneller Zustimmung. | Der Konflikt wird begrenzt, ohne harmonisiert zu werden. | Quelle A weiß, dass Ablehnung der These nicht Verrat an der Quelle bedeutet. | S8 kann evidenzorientiert weiterarbeiten. | Nora hält Beziehung und Behauptungsgrenze gleichzeitig. | R-01 |
| BT031 | E025 | S8 | Nora Feld | Jonas bringt einen authentischen Verteiler-/Freigabenachweis aus dem bestehenden Dokumentpfad. | Nora lässt den Beleg vor jeder Storyänderung separat gegen T und K prüfen. | Nach dem Quellenschutzfehler liegt eine mögliche fachliche Rehabilitation vor. | Ein Beleg kann beide Stränge unterschiedlich verändern. | Der zentrale Reversal wird prüfbar. | Nora↔Jonas bewegen sich vorsichtig zurück zu fachlichem Vertrauen. | R-01, R-02 |
| BT032 | E025 | S8 | Nora Feld | Nora und Jonas ordnen Testzeit, Release Candidate und Verteiler chronologisch. | Sie halten die Kette erst nach übereinstimmenden Zeit-/Versionsmerkmalen für belastbar. | Die fehlende Brücke aus S6 schließt sich. | Rolloutbezug und Kenntniszeitpunkt können nun getrennt gelesen werden. | Die Redaktion erreicht erstmals eine veröffentlichbare technische Kette. | Jonas' Stärke in der Versionsarbeit wird sichtbar, ohne den früheren Fehler zu löschen. | R-01, R-02 |
| BT033 | E026 | S8 | Nora Feld | Der Nachweis zeigt, dass der kritische technische Befund bis in den roll-out-relevanten Release Candidate dokumentiert war. | Nora setzt T als final tragfähigen Publikationskern. | Der größte technische Unsicherheitsblock fällt. | T wird deutlich stärker und aktuell. | Veröffentlichung wird grundsätzlich möglich. | Nora gewinnt Entscheidungsfähigkeit zurück. | R-02 |
| BT034 | E027 | S8 | Nora Feld | Derselbe Nachweis zeigt, dass die konkrete Führungsperson den relevanten Befund erst nach dem maßgeblichen Freigabezeitpunkt erhielt. | Nora streicht die persönliche Vorwissensbehauptung aus der geplanten Fassung. | Die spektakulärere Verantwortungsstory bricht genau im Moment technischer Sicherheit weg. | T stark; konkrete K-Zuschreibung widerlegt. | Story muss enger werden, nicht gestoppt. | Nora muss Belegdisziplin gegen den Wunsch nach einer großen Auflösung behaupten. | R-01 |
| BT035 | E027 | S8 | Nora Feld | Nora teilt David und Mira die asymmetrische Beleglage mit. | Sie bindet die Freigabe an T, Versionskontext, Stellungnahme und das explizite Weglassen der konkreten K-Zuschreibung. | Aus Recherche wird finale Redaktionsentscheidungsvorbereitung. | Der spätere Publikationsrahmen ist vollständig. | S9 prüft nur noch, ob äußerer Konkurrenzdruck diese Grenze verändert. | Nora↔David sind näher, aber der Timingkonflikt bleibt. | R-01, R-02 |
| BT036 | E028 | S9 | Nora Feld | Die Konkurrenz veröffentlicht zuerst eine breitere Geschichte mit stärkerer Verantwortungszuschreibung. | Nora liest nur so weit, wie nötig, um den Wettbewerbsstand zu verstehen, und behandelt ihn nicht als neuen Beleg. | Der zuvor abstrakte Preis der Sorgfalt wird real. | Konkurrenzgeschwindigkeit verändert die eigene Evidenz nicht. | David muss den verlorenen First-Mover-Vorteil akzeptieren. | Nora↔David geraten erneut unter Druck, jetzt mit realen Kosten. | R-01 |
| BT037 | E028 | S9 | Nora Feld | David stellt die Frage, ob die eigene engere Fassung nun noch Wert hat. | Nora hält dagegen: gerade die Unterschiede in Belegreichweite und Stellungnahme sind der Wert. | Die Entscheidung wird zur publizistischen Positionsfrage. | „später“ ist nicht automatisch „überholt“. | Die Redaktion bleibt handlungsfähig statt in Konkurrenzreaktion zu geraten. | Nora verteidigt ihre Linie gegenüber David ohne dessen Verlust kleinzureden. | R-01 |
| BT038 | E028 | S9 | Nora Feld | Nora prüft ein letztes Mal, ob der Konkurrenztext irgendeinen neuen verifizierbaren Beleg für K enthält; es liegt keiner vor. | Sie ändert die eigene Behauptungsgrenze nicht. | Der externe Druck erreicht Maximum und verliert dennoch Entscheidungsgewalt. | Eigene Evidenz bleibt maßgeblich. | S10 kann freigeben, ohne K künstlich nachzuliefern. | Nora↔David endet nicht harmonisch, aber auf gemeinsamer Faktenbasis. | R-01 |
| BT039 | E029 | S10 | Nora Feld | Nora gibt die engere Fassung frei: T, Versionskontext, Unternehmensstellungnahme, keine ungesicherte persönliche K-Zuschreibung. | Sie entscheidet für Veröffentlichung jetzt statt weitere Vollständigkeitssuche. | Die zentrale Entscheidung wird irreversibel. | Der Leser der Story erhält eine kleinere, klar belegte Aussage. | SPERRFRIST endet nicht mit maximaler Enthüllung, sondern kontrollierter Behauptungsreichweite. | Nora trägt die publizistische Verantwortung sichtbar. | R-01, R-02 |
| BT040 | E029 | S10 | Nora Feld | Die Veröffentlichung geht online; die sperrfrist- und quellenbezogenen Schutzgrenzen bleiben gewahrt. | Nora kontrolliert nur noch, ob die veröffentlichte Fassung den freigegebenen Behauptungsrahmen hält. | Recherchezeitdruck fällt ab, Folgen beginnen. | T ist öffentlich; konkrete K-Zuschreibung fehlt bewusst. | Die Redaktion zahlt mit späterem Zeitpunkt für höhere Belegkontrolle. | Mira unterstützt die Fassung; Jonas bleibt im Team. | R-01, R-02 |
| BT041 | E030 | S10 | Nora Feld | Quelle A kritisiert die Fassung als zu vorsichtig, David kritisiert den Zeitverlust. | Nora verteidigt weder sich selbst noch die Story als perfekt; sie verweist auf die belegte Grenze. | Der Konflikt bleibt nach Veröffentlichung real. | Unterschiedliche Interessen werden nicht durch den richtigen Beschluss aufgelöst. | Keine harmonische Nachauflösung. | Nora↔Quelle A und Nora↔David bleiben belastet, aber funktionsfähig. | R-01 |
| BT042 | E030 | S10 | Nora Feld | Die technische Kernfrage ist öffentlich, während K als weitere offene Recherchefrage bestehen bleibt. | Nora akzeptiert, dass ein sauber begrenzter Text ein Ergebnis und kein Scheitern ist. | Äußerer Zeitdruck endet; methodischer Nachhall bleibt. | T publiziert; K außerhalb der Tatsachenbehauptung offen. | Abschluss ohne Tätertwist oder Totalaufklärung. | Noras Bogen endet bei kontrollierter Behauptungsreichweite statt maximaler Gewissheit. | R-01 |

## Horizontale Event-Abdeckung

- E001 → BT001
- E002 → BT002
- E003 → BT003–BT004
- E004 → BT005
- E005 → BT006
- E006 → BT007
- E007 → BT008
- E008 → BT009
- E009 → BT010
- E010 → BT011
- E011 → BT012
- E012 → BT013
- E013 → BT014
- E014 → BT015
- E015 → BT016–BT017
- E016 → BT018
- E017 → BT019
- E018 → BT020–BT021
- E019 → BT022
- E020 → BT023
- E021 → BT024–BT025
- E022 → BT026
- E023 → BT027–BT028
- E024 → BT029–BT030
- E025 → BT031–BT032
- E026 → BT033
- E027 → BT034–BT035
- E028 → BT036–BT038
- E029 → BT039–BT040
- E030 → BT041–BT042

**Umfang:** 42 Beats; M2-Minimum 36 erfüllt. Alle 30 G1-freigegebenen Events sind abgedeckt.

## Geplante Szenenabdeckung

- **S1 – Das Dossier:** BT001–BT004
- **S2 – Zwei Behauptungen:** BT005–BT008
- **S3 – Die falsche Version:** BT009–BT013
- **S4 – Zweite Quelle:** BT014–BT017
- **S5 – Der Preis der Anfrage:** BT018–BT021
- **S6 – Die engere Story:** BT022–BT026
- **S7 – Quelle ist nicht Wahrheit:** BT027–BT030
- **S8 – Ein Beleg, zwei Wirkungen:** BT031–BT035
- **S9 – Zu spät:** BT036–BT038
- **S10 – Veröffentlichen:** BT039–BT042

Damit entstehen genau zehn aktive Szenen. Die G2-Batch-Grenze liegt nach S5 an einem realen Zustandswechsel: Quellenschutz-/Teamgovernance ist verändert, T/K sind noch offen; Batch 2 beginnt mit der publizistischen Eingrenzung und führt bis zur Veröffentlichung.

## Cross-Scene-Kontrollen

- **T-Strang:** S1 potenzielle Relevanz → S2 erster Testbeleg → S3 Versionszweifel → S4 unabhängige Bestätigung → S6 Rollout-/Betriebsrelevanz → S8 endgültige Release-Kette → S10 Publikation.
- **K-Strang:** S1 gekoppelte Ausgangsannahme → S2 methodische Trennung → S3 ausdrückliche Gegenbehauptung → S4 Chronologie beschädigt K → S6 nur offene Verdachtsebene → S7 Quelle A kann K nicht aus eigener Kenntnis bestätigen → S8 konkrete Zuschreibung widerlegt → S10 K bleibt außerhalb der Tatsachenbehauptung.
- **Nora↔David:** S2 Timingkonflikt → S6 Annäherung über T-Priorisierung → S9 realer Wettbewerbsverlust → S10 Restkonflikt.
- **Nora↔Jonas:** S2 fachliches Vertrauen → S3 erste Korrektur → S5 Quellenschutzfehler und Kontaktbegrenzung → S8 fachliche Teilrehabilitation → S10 bleibt im Team.
- **Nora↔Quelle A:** S1 hohes Vertrauen → S3 Interpretationsskepsis → S5 Schutzkrise → S7 inhaltliche Abgrenzung bei fortbestehendem Schutz → S10 Restkonflikt.

## Recherchegrenzen

- `R-01` begrenzt Stellungnahme, Verdachts-/Tatsachenreichweite und Quellenschutzlogik. Beats dürfen daraus keine konkrete Rechtsberatung oder Prozessprognose ableiten.
- `R-02` begrenzt die fiktive Plattform auf vendorseitige Release-/Test-/Redundanzlogik. Beats dürfen keine realen amtlichen Warnprozesse als vom Unternehmen gesteuert darstellen.

## Offene Prose-Ready-Punkte

- none auf Beat-Ebene.
- Szenenkarten und Character States müssen nun Informationsstände, Entscheidungen, Konsequenzen und Beziehungen exakt konkretisieren.
- Der separate M2-Backtracking-Test ist **noch nicht** durchgeführt und darf nicht mit E027/BT034 verwechselt werden.

**Arbeitsregel:** Erst nach vollständiger horizontaler Beat-Ebene werden die zehn Szenenkarten und Character States systematisch abgeleitet. Zwischen Beats und Szenenkarten entsteht kein zusätzlicher Human Gate.
