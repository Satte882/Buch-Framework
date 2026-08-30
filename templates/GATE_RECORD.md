# GATE_RECORD

gate_id: <G0-G5>
gate_name: <Konzept | Story-Architektur | Prose Ready | Prosa-Stil | Manuskript | Produktion>
artifacts: <Pfad(e), mit Semikolon getrennt>
review_scope: <gesamter Gate-Umfang oder konkrete Review-Batches>
decision: <APPROVE | REWORK | STOP>
decided_by: human
date: <YYYY-MM-DD>
open_blockers: <yes | no>
next_step: <konkret erlaubter nächster Schritt>

## Entscheidungsgrund

<kurze Begründung>

## Offene Punkte

- <Punkt oder `none`>

## Regel

Ein LLM darf diesen Record vorbereiten, aber `decision` wird ausschließlich durch eine bewusste menschliche Freigabe gesetzt.

Ein Gate darf mehrere Arbeitsartefakte und bei großen Projekten mehrere Review-Batches bündeln. Eine neue Entwicklungsebene oder Datei erzeugt nicht automatisch einen zusätzlichen Human Gate.
