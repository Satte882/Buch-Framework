# RESEARCH_REGISTER

register_status: ready

Dieses Register enthält nur Recherchefragen, die für Plot, Figurenhandlung, Plausibilität oder konkrete Szenenentscheidungen relevant sind. Recherche ist ein **Querschnittsartefakt** und besitzt standardmäßig keinen eigenen Human Gate.

| ID | Frage | Betroffene Ebene / Artefakte | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung | blocking_now |
|---|---|---|---|---|---|---|---|
| R-001 | <Frage> | <Baustein/Event/Beat/Szene> | low / medium / high | open / resolved / not_applicable | <Quelle> | <was gilt für das Buch> | yes / no |

## Blockierregel v0.x

Eine offene Recherchefrage blockiert die **aktuelle Entwicklungsebene** nur dann, wenn ihre Antwort eine jetzt zu treffende

- Plotentscheidung,
- Figurenentscheidung,
- Szenenentscheidung,
- Informationsentscheidung oder
- Konsequenzentscheidung

verändern kann.

Austauschbare Oberflächendetails blockieren nicht.

`blocking_now: yes` bedeutet deshalb: Die abhängige Entscheidung darf nicht als fertig bzw. freigabereif behandelt werden, solange der Recherchepunkt `open` ist.

`blocking_now: no` bei einem offenen Punkt muss bedeuten, dass die aktuelle Entscheidung unabhängig von der späteren Detailantwort stabil bleibt.

Für v0.x wird bewusst kein zusätzlicher Score und keine Bewertungsmatrix eingeführt.

## Gate-Bezug

- G1 darf keine offene Recherchefrage übergehen, die eine Story-Architekturentscheidung verändern kann.
- G2 darf keine offene Recherchefrage übergehen, die Beat-, Szenen-, Character-State-, Informations- oder Konsequenzentscheidungen verändern kann.
- Spätere sprachliche oder austauschbare Detailrecherche darf nach G2 offen bleiben, wenn sie keine Storywahrheit mehr verändert.

`register_status: ready` bedeutet nur: Die bekannten relevanten Recherchefragen sind erfasst und ihr aktueller Blockierstatus ist bewusst gesetzt. Es bedeutet nicht, dass sämtliche Recherche abgeschlossen ist.
