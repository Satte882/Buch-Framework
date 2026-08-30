# G1 Review Request – FEHLALARM v0.2

status: APPROVED
human_decision: G1-APPROVE
decision_date: 2026-08-30
gate_record: `m1/e2e_minibook/gates/G1.md`
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

## Entscheidung

Der Mensch hat am 2026-08-30 im Chat ausdrücklich **G1-APPROVE** für genau die oben referenzierten fünf Artefaktstände erteilt. Der kanonische Human-Gate-Record steht in `m1/e2e_minibook/gates/G1.md`.

Damit ist **G1 – Story-Architektur** abgeschlossen. Beats dürfen nun horizontal über den gesamten Mini-Fall entwickelt werden. Szenenkarten, Character States und Prosa sind durch diese Entscheidung nicht freigegeben.

## Freigegebener Makro→Mikro-Stand

### Storykern

Der festgelegte Kern bleibt unverändert: Wiederholte Fehlalarme machen eine lokale Prüfroutine nachvollziehbar; im aktuellen Fall entziehen neue konkrete Hinweise dieser Routine schrittweise die Grundlage. Mara muss die Gewichtung ändern und trotz realer betrieblicher Kosten voll eskalieren.

### Sechs dramaturgische Bausteine

- **B01 – Gewöhnung und erneutes Warnsignal:** Fehlalarm-Erfahrung + neues mehrdeutiges Signal.
- **B02 – Vernünftige Abkürzung:** Nils macht den realen Versuchsschaden sichtbar; Mara entscheidet sich bewusst für lokale Verifikation.
- **B03 – Widerspruch:** Eine Anwesenheitsspur beschädigt die Annahme des leeren Bereichs.
- **B04 – Kipppunkt:** Physischer Gefahrenhinweis + Anwesenheitsabweichung machen weitere Verzögerung unvertretbar.
- **B05 – Entscheidung:** Mara aktiviert die volle interne Alarm-/Evakuierungskette und nimmt den Verlust des Versuchs in Kauf.
- **B06 – Konsequenz/Umdeutung:** Lea ist tatsächlich noch vor Ort; der aktuelle Alarm war real; die früheren Fehlalarme bleiben trotzdem wahr.

### Zehn Ereignisse

`E001–E010` decken alle sechs Bausteine vollständig ab. Die Kette verläuft horizontal von Signal → Informationslücke → betrieblichem Gegenanreiz → bewusster Abkürzung → Gegenbeleg → Gefahrenhinweis → verbleibender Gegenoption → Eskalation → menschlicher Konsequenz → Umdeutung.

## Figurenkern

- **Mara Voss:** trägt POV und Sicherheitsentscheidung; sie trägt die informelle Routine selbst mit und kämpft nicht nur gegen einen äußeren Fehler.
- **Nils Berger:** legitimer betrieblicher Gegenanreiz; kein versteckter Bösewicht und kein Wissensvorsprung gegenüber Mara.
- **Lea Hartmann:** reale menschliche Konsequenz; ihre Restanwesenheit entsteht banal betrieblich und nicht als Plotfalle.
- `open_character_decisions: no` für den G1-Figurenkern.

Szenenspezifische Wissens-, Glaubens-, Ziel- und Beziehungszustände werden erst bis G2 als Character States konkretisiert.

## Recherche

`R-001` ist `resolved`. Für G1 besteht keine offene `blocking_now: yes`-Abhängigkeit.

Festgelegt ist: FEHLALARM verwendet ein internes technisches Rauch-/Prozesswarnsignal mit lokaler Verifikation und späterer separater voller interner Alarm-/Evakuierungskette. Der spätere Text darf daraus keine frei erfundene, manuell verzögerbare öffentliche Brandmelde-/Feuerwehrlogik machen.

## Ergebnis der G1-Reviewfragen

Mit dem menschlichen `G1-APPROVE` gelten Konflikt, Makrostruktur, Event-Kausalität, Figurenkern, Informationsarchitektur und die relevante Recherchebasis als ausreichend freigegeben, um auf die Beat-Ebene herunterzubrechen.

Die Freigabe behauptet keine Prose-Readiness und keine literarische Qualität. Diese werden erst in den nachgelagerten Ebenen und Gates geprüft.