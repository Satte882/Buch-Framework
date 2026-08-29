# G2 Review Request – FEHLALARM

status: AWAITING_HUMAN_G2_DECISION
artifacts:
- `m1/e2e_minibook/CHARACTERS.md`
- `m1/e2e_minibook/RESEARCH_REGISTER.md`
provenance: `m1/e2e_minibook/provenance/G2_PACKAGE.md`
upstream_gate: `m1/e2e_minibook/gates/G1.md`

## Was G2 entscheidet

G2 prüft, ob Figuren-Baseline und Recherchebasis stabil genug sind, um die drei konkreten Szenen zu planen, ohne dabei zentrale Figuren- oder Plausibilitätsentscheidungen zu improvisieren.

## Figuren-Baseline – Kurzcheck

- Mara Voss trägt Perspektive und Entscheidung.
- Nils Berger bleibt legitimer Gegenanreiz und erhält kein verborgenes Täterwissen.
- Lea Hartmann liefert die reale menschliche Konsequenz, ohne persönliche Abkürzung oder Nebenplot.
- Maras finale Entscheidung darf nicht aus persönlicher Nähe zu Lea motiviert werden.
- `open_character_decisions: no`.

## Recherche R-001 – gelöst

Die Recherche hat eine potenzielle Plausibilitätsfalle sichtbar gemacht: Eine reale, formal aufgeschaltete Brandmeldeanlage sollte nicht so erzählt werden, als könne eine Mitarbeiterin einen Hauptalarm nach Belieben wegen eines Nachtversuchs zurückhalten.

Deshalb gilt für FEHLALARM verbindlich:

- Das erste Signal ist eine **interne technische Rauch-/Prozesswarnung** des Forschungsbereichs.
- Diese darf im fiktiven Betriebsmodell eine lokale Verifikation auslösen.
- Die spätere volle interne Alarm-/Evakuierungskette ist Maras irreversible Entscheidung.
- Die Geschichte spezifiziert keine detaillierte automatische Feuerwehr-Aufschaltung oder reale BMA-Bedienlogik.

Damit bleibt der Storymechanismus erhalten und die Geschichte vermeidet eine unnötig konkrete technische Falschbehauptung.

## Gate-Fragen

1. Sind Mara, Nils und Lea in Funktion, Eigenziel und Wissensgrenzen ausreichend festgelegt?
2. Bleibt Nils ein legitimer Gegenpol statt versteckter Antagonist?
3. Ist Leas Anwesenheit als banaler betrieblicher Nachlauf plausibel genug, ohne neuen Nebenplot zu verlangen?
4. Ist die Entscheidung zu R-001 für diesen Mini-Testfall ausreichend plausibel und bewusst KISS?
5. Gibt es noch eine Figuren- oder Rechercheentscheidung, die beim Schreiben der Szenen sonst improvisiert werden müsste?

## Nächste menschliche Entscheidung

- `APPROVE` – G2 ist stabil; danach werden **alle drei Szenen plus Character States in einem Zug** vorbereitet und gemeinsam als G3-Paket vorgelegt.
- `REWORK` – konkrete Punkte werden zuerst korrigiert.
- `STOP` – M1-Testfall wird beendet.

Es wurde bewusst noch keine Szene angelegt, weil G2 noch nicht menschlich freigegeben ist.