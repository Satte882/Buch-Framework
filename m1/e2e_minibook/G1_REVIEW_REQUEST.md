# G1 Review Request – FEHLALARM v0.2

status: AWAITING_HUMAN_G1_DECISION
story_package: `m1/e2e_minibook/STORY_PACKAGE.md`
story_package_ref: `d2b1c8d5c46f5afb51f876a652735b431ed9ab22`
story_blocks: `m1/e2e_minibook/STORY_BLOCKS.md`
story_blocks_ref: `95fc2b1e0583a5435e8eca519edaa78b5861b6f2`
events: `m1/e2e_minibook/EVENTS.md`
events_ref: `88972626c070762d856d9388c1a3a977538b04ed`
characters: `m1/e2e_minibook/CHARACTERS.md`
characters_ref: `1febb99bbb854658cf27d4be17edd3197fb12eb0`
research_register: `m1/e2e_minibook/RESEARCH_REGISTER.md`
research_register_ref: `a1026077fc15be857827f691f76bcb4ca0bfe4eb`
prior_gate: `m1/e2e_minibook/gates/G0.md`
prior_g1_record: `m1/e2e_minibook/gates/G1.md` – superseded v0.1 test trace; not valid for this v0.2 package

## Zweck

Dies ist die gebündelte menschliche **G1 – Story-Architektur**-Vorlage für den FEHLALARM-M1-Lauf nach der v0.2-Arbeitsweise.

G1 prüft jetzt nicht nur das Story Package, sondern gemeinsam:

1. Story Package,
2. alle dramaturgischen Bausteine,
3. alle Ereignisse/Sequenzen,
4. Figurenkern und zentrale Beziehungen,
5. bekannte relevante Rechercheabhängigkeiten.

Es gibt keinen zusätzlichen Human Gate zwischen Bausteinen und Events.

## Aktueller Makro→Mikro-Stand

### Storykern

Der bereits festgelegte Kern bleibt unverändert: Wiederholte Fehlalarme machen eine lokale Prüfroutine nachvollziehbar; im aktuellen Fall entziehen neue konkrete Hinweise dieser Routine schrittweise die Grundlage. Mara muss die Gewichtung ändern und trotz realer betrieblicher Kosten voll eskalieren.

### Sechs dramaturgische Bausteine

- **B01 – Gewöhnung und erneutes Warnsignal:** Fehlalarm-Erfahrung + neues mehrdeutiges Signal.
- **B02 – Vernünftige Abkürzung:** Nils macht den realen Versuchsschaden sichtbar; Mara entscheidet sich bewusst für lokale Verifikation.
- **B03 – Widerspruch:** Eine Anwesenheitsspur beschädigt die Annahme des leeren Bereichs.
- **B04 – Kipppunkt:** Physischer Gefahrenhinweis + Anwesenheitsabweichung machen weitere Verzögerung unvertretbar.
- **B05 – Entscheidung:** Mara aktiviert die volle interne Alarm-/Evakuierungskette und nimmt den Verlust des Versuchs in Kauf.
- **B06 – Konsequenz/Umdeutung:** Lea ist tatsächlich noch vor Ort; der aktuelle Alarm war real; die früheren Fehlalarme bleiben trotzdem wahr.

### Zehn Ereignisse

`E001–E010` decken alle sechs Bausteine vollständig ab. Die Kette verläuft horizontal von Signal → Informationslücke → betrieblichem Gegenanreiz → bewusster Abkürzung → Gegenbeleg → Gefahrenhinweis → verbleibender Gegenoption → Eskalation → menschlicher Konsequenz → Umdeutung.

Noch nicht festgelegt sind Beats, Szenenkarten, Mikrohandlungen, Dialoge oder Prosa. Diese gehören bewusst erst hinter G1.

## Figurenkern

- **Mara Voss:** trägt POV und Sicherheitsentscheidung; sie trägt die informelle Routine selbst mit und kämpft nicht nur gegen einen äußeren Fehler.
- **Nils Berger:** legitimer betrieblicher Gegenanreiz; kein versteckter Bösewicht und kein Wissensvorsprung gegenüber Mara.
- **Lea Hartmann:** reale menschliche Konsequenz; ihre Restanwesenheit entsteht banal betrieblich und nicht als Plotfalle.
- `open_character_decisions: no` für den G1-Figurenkern.

Szenenspezifische Wissens-, Glaubens-, Ziel- und Beziehungszustände werden erst bis G2 als Character States konkretisiert.

## Recherche

`R-001` ist `resolved` und technisch auf die v0.2-Blockierlogik migriert. Für G1 besteht keine offene `blocking_now: yes`-Abhängigkeit.

Festgelegt ist: FEHLALARM verwendet ein internes technisches Rauch-/Prozesswarnsignal mit lokaler Verifikation und späterer separater voller interner Alarm-/Evakuierungskette. Der spätere Text darf daraus keine frei erfundene, manuell verzögerbare öffentliche Brandmelde-/Feuerwehrlogik machen.

## G1-Reviewfragen

1. Tragen die sechs Bausteine den gesamten Mini-Fall, ohne Lücke oder unnötigen Doppelbaustein?
2. Ist die Event-Kette kausal genug, dass Beats später nur konkretisieren und keine neue Storylogik erfinden müssen?
3. Bleibt Maras erste Abkürzung nachvollziehbar, ohne als offensichtlich falsche Thriller-Entscheidung zu wirken?
4. Entsteht der Kipppunkt aus kumulierender Evidenz statt aus einem künstlichen Twist?
5. Bleibt Nils eine legitime Gegenposition statt Strohmann-Antagonist?
6. Bleibt Lea konkrete Konsequenz statt nachträglich eingesetztes Opfer?
7. Ist die Informationsarchitektur sauber: Leser und Mara erhalten die relevanten Gegenbelege im selben Entscheidungsprozess?
8. Ist R-001 ausreichend geklärt, um die Story-Architektur freizugeben, ohne Sicherheitsprozeduren als Plotmagie zu verwenden?
9. Gibt es eine noch offene irreversible Story- oder Figurenkernentscheidung, die vor Beats geklärt werden müsste?

## Nächste menschliche Entscheidung

- `G1-APPROVE` – genau die oben referenzierten fünf Artefaktstände werden als Story-Architektur freigegeben; danach dürfen `BEATS.md` horizontal über den gesamten Mini-Fall entwickelt werden.
- `G1-REWORK` – konkrete Makro-/Event-/Figuren-/Research-Punkte werden gezielt überarbeitet.
- `G1-STOP` – der M1-Testfall wird beendet.

**Wichtig:** Ein früheres G1-APPROVE des alten v0.1-Pfads gilt nicht automatisch für dieses neue Paket. Der neue Gate-Record darf erst nach einer bewussten menschlichen Entscheidung über genau diese Artefaktstände geschrieben werden.
