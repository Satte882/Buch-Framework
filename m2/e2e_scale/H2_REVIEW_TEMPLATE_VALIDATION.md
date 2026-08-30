# H2 Validation – Review-Template gegen SPERRFRIST M2

status: PASS
issue: #16
basis: `REVIEW_TEMPLATE.md`
validation_case: G2 SPERRFRIST S1-S10

## Zweck

Prüfen, ob das nach M2 standardisierte, **nicht-kanonische** Review-Template den tatsächlich benötigten Entscheidungsinhalt aus den ad-hoc G2-Paketen reproduziert, ohne alle 31 Character-State-Dateien als Volltext in den Human Review zu laden.

## Batch 1 – S1 bis S5

### A – Scene Batch

| Szene | Story-Funktion | zentrale Veränderung | Leserwissen danach | Character/Relationship-Shift |
|---|---|---|---|---|
| S1 | Dossier, Schutz, Deadline etablieren | Nora bindet sich an Schutz/Sperrfrist, nicht an Gesamtdeutung | T/K ungeprüft; Schutz und Zeitdruck stehen | Nora↔Quelle A: Schutzverantwortung verbindlich |
| S2 | T und K trennen | zwei Evidenzketten werden getrennt geführt | T erster Testbeleg; K daraus nicht bewiesen | Timingkonflikt Nora↔David; technisches Mandat für Jonas |
| S3 | frühe Sicherheit brechen | T-Zuspitzung stoppt bis Versionsklärung | Versionsbruch real; K bleibt offen | Nora↔Mira enger; Dossierdeutung wird skeptischer |
| S4 | T unabhängig stützen, K schwächen | engere Belegkette wird priorisiert | T unabhängig bestätigt; K chronologisch schwächer | Schutzvertrauen zu Quelle B entsteht |
| S5 | Quellenschutz wird operative Abhängigkeit | Jonas' Außenkontakte werden begrenzt | kein neuer Sachbeleg; Recherchehandlung selbst birgt Risiko | Nora↔Jonas Autonomie sinkt; Nora↔Quelle A Vertrauen beschädigt |

### B – Information / Reveal

| Thread | vor Batch | Veränderung | nach Batch | darf noch nicht behauptet werden |
|---|---|---|---|---|
| T – technischer Befund | unbewiesen | Testbeleg → Versionsbruch → unabhängige Bestätigung | substanziell gestützt, RC-Brücke fehlt | relevanter Rollout ist bereits endgültig bewiesen |
| K – persönliche Kenntnis/Verantwortung | im Dossier mit T gekoppelt | methodisch getrennt, bestritten, Chronologie geschwächt | deutlich schwächer als T | konkrete persönliche Zuschreibung als Tatsache |

### C – Character / Relationship

| Beziehung | vor Batch | Druck / Veränderung | nach Batch | persistierende Kosten |
|---|---|---|---|---|
| Nora↔David | professionelles Vertrauen | Zeit-/Wettbewerbsdruck | Konflikt offen | David bleibt legitimer Gegenpol, kein Sorgfaltsgegner |
| Nora↔Jonas | hohes Fach-/Autonomievertrauen | technische Korrektur + zu konkrete Anfrage | Kompetenzvertrauen bleibt, externe Autonomie begrenzt | S5-Fehler darf später nicht gelöscht werden |
| Nora↔Quelle A | hohes Vertrauen + Schutzversprechen | Deutung wird schwächer; Anfrage erzeugt Schutzkrise | Schutz bleibt, Vertrauen sinkt | Quelle bleibt ehrlich trotz zu breiter Interpretation |

### D – Batch Boundary State vor S6

- T unabhängig gestützt; finale RC-Brücke fehlt.
- K deutlich geschwächt.
- Quelle A und Quelle B bleiben geschützt.
- Jonas bleibt technisch im Fall, externe Kontakte sind begrenzt.
- Nora↔David Timingkonflikt bleibt offen.
- noch kein Publikationsbeschluss.
- keine offene `blocking_now: yes`-Recherche.

## Batch 2 / Gesamtcheck – Rückprüfung

Dasselbe Schema trägt auch S6-S10:

- Scene Batch: Eingrenzung der publizierbaren Story → Quellenkonflikt → finaler Beleg/Reversal → First-Mover-Verlust → Veröffentlichung.
- Information/Reveal: T wird durch die finale Release-Brücke belastbar; K wird widerlegt/aus der Publikationsfassung entfernt.
- Character/Relationship: Jonas wird fachlich teilweise rehabilitiert, ohne S5 zu löschen; David akzeptiert die Evidenzgrenze, behält aber den Zeitkostenkonflikt; Quelle A bleibt geschützt, obwohl Nora ihrer Deutung nicht folgt.
- Boundary/Final State: Veröffentlichung nach Sperrfrist; technische Story publiziert; konkrete Verantwortungszuschreibung nicht als Tatsache übernommen.

Der M2-Gesamtcheck fand 0 neue Cross-Batch-Widersprüche.

## Vergleich zur ad-hoc M2-Aufbereitung

Das Template deckt die vier Sichten ab, die M2 tatsächlich wiederholt benötigt hat:

1. Scene Batch,
2. Information/Reveal,
3. Character/Relationship,
4. Batch Boundary State.

Nicht notwendig als feste Sicht war eine eigene Research-Dependency-Matrix; die zwei Rechercheabhängigkeiten konnten innerhalb des Entscheidungs-Kontexts kontrolliert werden.

## Ergebnis

- entscheidungsrelevanter G2-Inhalt erhalten: PASS
- alle 31 Character States als Volltext nötig: NEIN
- neue kanonische Story-Ebene erzeugt: NEIN
- neuer Human Gate erzeugt: NEIN
- Generator erforderlich: NEIN
- H2 Akzeptanz aus Issue #16 erfüllt: PASS

**H2 Gesamt: PASS.**
