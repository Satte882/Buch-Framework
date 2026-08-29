# G3 Review Request – FEHLALARM

status: AWAITING_HUMAN_G3_DECISION
scope: S1; S2; S3
prior_gate: G2 APPROVE

## Zweck

Alle drei Szenen und ihre Character States werden bewusst **gebündelt** für einen einzigen menschlichen G3-Review vorgelegt. Dadurch bleibt der Human Gate real, ohne drei separate Chat-Unterbrechungen zu erzeugen.

## Szenenpaket

### S1 – Die vernünftige Abkürzung

Funktion: Fehlalarm-Vorgeschichte, Versuchskosten und die zunächst plausible lokale Prüfroutine etablieren.

Entscheidung: Mara löst noch keinen Vollalarm aus und geht selbst zur lokalen Verifikation.

Prüffrage: Ist diese Entscheidung aus der bis dahin bekannten Lage nachvollziehbar, ohne dass beim Schreiben noch eine relevante Storyentscheidung erfunden werden muss?

### S2 – Das Muster passt nicht mehr

Funktion: Die Harmlosigkeitsannahme durch die Kombination aus falschem Leerstand und konkretem Gefahrindikator kippen lassen.

Entscheidung: Mara beendet die lokale Prüfroutine und aktiviert die volle interne Alarm-/Evakuierungskette.

Prüffrage: Ist der Kipppunkt konkret genug und wird er von mehreren Indizien getragen statt von einem künstlichen Wunderhinweis?

### S3 – Der Preis der richtigen Entscheidung

Funktion: Leas Anwesenheit und die reale Gefahrenlage bestätigen, den Verlust des Nachtversuchs erhalten und den Konflikt ohne Bösewicht auflösen.

Entscheidung: Mara hält die Eskalation bis zur bestätigten Räumung aufrecht.

Prüffrage: Trägt die Szene als echter Konsequenz-/Payoff-Moment und bleibt Mara Koordinatorin statt heroische Einzelretterin?

## Gemeinsame Konsistenzchecks

- Nils besitzt in keiner Szene verborgenes Mehrwissen.
- Lea wird vor S3 nicht als konkrete anwesende Person enthüllt.
- Leas Restanwesenheit bleibt banal und nicht absichtlich verborgen.
- Der Nachtversuch geht real verloren und wird nicht nachträglich gerettet.
- Das interne Rauch-/Prozesswarnsignal und die volle interne Alarm-/Evakuierungskette respektieren R-001; keine frei verzögerbare Haupt-BMA wird behauptet.
- Maras Risikogewichtung verändert sich aufgrund neuer Evidenz, nicht aufgrund persönlicher Nähe zu Lea.
- Keine Szene benötigt noch eine offene Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung.

## Character-State-Abdeckung

Vorhanden und auf `status: ready`:

- S1: Mara, Nils
- S2: Mara, Nils
- S3: Mara, Nils, Lea

Die Wissensgrenzen sind über die Szenen fortgeschrieben: Mara und Nils wissen vor S2 nichts von Leas Anwesenheit; S2 liefert nur die Spur; S3 löst die Identität auf.

## Warum `experience_status` noch nicht freigegeben ist

In `S1.md`, `S2.md` und `S3.md` steht bewusst `experience_status: pending_human_review`. Dieser Wert wird erst nach einer ausdrücklichen menschlichen G3-Freigabe auf `human_reviewed_ready` geändert. Damit simuliert ChatGPT keine Scene-Readiness-Entscheidung.

## Menschliche G3-Entscheidung

Eine Entscheidung gilt für **alle drei Szenen gemeinsam**:

- `APPROVE` – alle drei Szenen sind prose-ready; `experience_status` wird auf `human_reviewed_ready` gesetzt und ein gemeinsamer G3-Gate-Record angelegt.
- `REWORK` – konkrete Szene(n) und Gründe benennen; nur diese Punkte werden überarbeitet.
- `STOP` – der M1-Lauf wird beendet.

Die Freigabe bedeutet nicht, dass die spätere Prosa automatisch gut ist. Sie bedeutet nur, dass beim Schreiben keine relevante Storyentscheidung mehr improvisiert werden soll.