# GATE_RECORD

gate_id: <G0-G6>
artifacts: <Pfad(e), mit Semikolon getrennt>
decision: <APPROVE | REWORK | STOP>
decided_by: human
date: <YYYY-MM-DD>
open_blockers: <yes | no>
next_step: <konkret erlaubter nächster Schritt>

## Entscheidungsgrund

<kurze Begründung>

## Offene Punkte

- <Punkt oder `none`>

**Regel:** Ein LLM darf diesen Record vorbereiten, aber `decision` wird ausschließlich durch eine bewusste menschliche Freigabe gesetzt. Der Pipeline-Checker akzeptiert für den Übergang nur `APPROVE`, `decided_by: human` und `open_blockers: no`.
