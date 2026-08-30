# M2 Observations – SPERRFRIST

status: IN_PROGRESS
m2_issue: `#10`
date: 2026-08-30
scope: Beobachtungen bis einschließlich beider G2-Review-Batches und Gesamt-Self-Review vor Human Gate G2

## Messbarer Umfang bisher

- Story Blocks: 12
- Events: 30
- Beats: 42
- Szenen: 10
- Character States: 31
- G2 Batch 1: 5 Szenen / 21 Beats / 13 Character States
- G2 Batch 2: 5 Szenen / 21 Beats / 18 Character States
- Human Gates abgeschlossen: G0, G1
- interne G2-Batches menschlich akzeptiert: 2/2
- Human Gate G2: noch offen

## Beobachtung O-01 – fünf Szenen sind als Review-Batch grundsätzlich handhabbar

Beide 5-Szenen-Batches konnten als kompakte Review-Pakete vorgelegt und vom Menschen ohne REWORK akzeptiert werden.

Wichtig: Daraus wird noch **kein allgemeiner Standard `5 Szenen`** abgeleitet. Der Test zeigt nur, dass 5 Szenen bei diesem 10-Szenen-Fall praktisch reviewbar waren.

Ein Zeitwert in Minuten wurde nicht belastbar erhoben und wird daher nicht erfunden. Objektiv dokumentierbar sind Umfang, Zahl der benötigten Review-Schritte, Rückfragen und Rework.

Bisher:

- Batch 1 Rückfragen: 0
- Batch 1 Rework durch Human Review: 0
- Batch 2 Rückfragen: 0
- Batch 2 Rework durch Human Review: 0

## Beobachtung O-02 – Volltext aller Character States wäre Kontextmüll

Mit 31 Character-State-Dateien ist eine direkte Volltextvorlage an den Menschen bereits bei 10 Szenen unergonomisch.

Für die zwei Batch-Reviews wurden deshalb **ad hoc**, nicht als neues Tooling, verdichtete Sichten verwendet:

1. Scene-Batch-Sicht: Story-Funktion, zentrale Entscheidung, Leserwissen, Beziehungsverschiebung je Szene.
2. Information/Reveal-Sicht: getrennte T- und K-Entwicklung über den Batch.
3. Character-/Relationship-Sicht: Nora↔David, Nora↔Jonas, Nora↔Quelle A sowie relevante Nebenbeziehungen.

Diese Sichten wurden aus den kanonischen Artefakten zusammengefasst. Sie sind weder neue Source-of-Truth-Artefakte noch deterministische Reports.

**Tatsächlich benötigt:** Scene Batch + Information/Reveal + Character/Relationship.

**Bislang nicht separat benötigt:** eigene Research Dependency View; R-01/R-02 konnten innerhalb der Szenen-/Batch-Prüfung ausreichend kontrolliert werden.

## Beobachtung O-03 – Batch-Grenze S5→S6 benötigt expliziten Übergabezustand

Der wichtigste Cross-Batch-Mechanismus war nicht die Wiederholung aller fünf ersten Szenen, sondern ein expliziter Zustand vor S6:

- T unabhängig gestützt, letzte RC-Brücke fehlt,
- K deutlich geschwächt,
- Quelle A geschützt, aber verunsichert,
- Quelle B geschützt,
- Jonas fachlich im Fall, externe Autonomie eingeschränkt,
- Timingkonflikt Nora↔David offen,
- noch kein Publikationsbeschluss.

Dieser Übergabezustand war für Batch 2 deutlich nützlicher als das erneute Lesen aller 13 Character States aus Batch 1.

## Beobachtung O-04 – Gesamtlogik blieb über zwei Batches erhalten

Der Gesamt-Self-Review S1–S10 fand nach den beiden menschlich akzeptierten Einzelbatches **keinen neuen Cross-Batch-Widerspruch**.

Geprüft wurden insbesondere:

- Chronologie: ca. 09:15 Uhr bis nach 18:00 Uhr ohne Rücksprung/Widerspruch,
- T-Strang: Ausgangsbehauptung → erster Beleg → Versionsbruch → unabhängige Bestätigung → Rolloutbezug → finale RC-Brücke → Veröffentlichung,
- K-Strang: frühe Kopplung → Trennung → Gegenbehauptung → Chronologieschwächung → Quelle-A-Interpretation → konkrete Widerlegung → nicht publiziert,
- Nora↔Jonas: Fachvertrauen → Korrektur → Schutzpanne → Kontaktgrenze → interne Weiterarbeit → Teilrehabilitation ohne Vertrauensreset,
- Nora↔David: Timingkonflikt → Annäherung über enges T → realer First-Mover-Verlust → gemeinsame Veröffentlichung bei verbleibender Kostenabweichung,
- Nora↔Quelle A: Schutzvertrauen → Deutungsdistanz → Schutzkrise → Schutz trotz inhaltlichem Widerspruch → unversöhnter Nachhall,
- Quelle B: Schutzbedingung bleibt bestehen; identifizierende Details werden nicht nachträglich publiziert.

Cross-Batch-Probleme im Gesamtcheck: **0**.

## Beobachtung O-05 – zwei reale Fehler wurden vor G2 sichtbar, aber unterschiedlicher Art

### Semantischer Self-Review-Fund

Vor G1 war ein geplanter Story-Reversal fälschlich als Framework-Invalidierung interpretiert worden. Derselbe Chat-/Modellkontext fand und korrigierte den Fehler. Das ist in `SEMANTIC_REVIEW_LOG.md` dokumentiert und **kein** Nachweis einer unabhängigen semantischen QA-Fähigkeit.

### Mechanischer Metadatenfehler

Beim Abgleich mit dem bestehenden Pipeline-Contract fiel auf, dass die zunächst geschriebenen G0-/G1-Gate-Records das für den Checker erforderliche Feld `artifacts:` nicht vertragskonform enthielten (`artifact:` bzw. nur Markdown-Liste). Die Gate-Metadaten wurden korrigiert; Storyinhalt blieb unverändert.

Dafür wurde keine neue Framework-Funktion gebaut.

## Beobachtung O-06 – bisher kein ungeplanter Funktionsausbau nötig

Bis vor G2 wurden keine neuen Checker, Reportgeneratoren, semantischen Scores, Agenten, Gates oder Produktionspfade benötigt.

Neu entstanden sind ausschließlich M2-Testartefakte und ad-hoc Review-Zusammenfassungen.

Neue Framework-Funktionen ungeplant erforderlich: **keine**.

## Noch offen für M2

- Human Gate G2 und danach deterministischer Pipeline-Check bis `READY_FOR_PROSE`.
- kontrollierte relevante Upstream-Änderung nach vorhandenen Downstream-Artefakten + echte Invalidierung/Rework-Messung.
- G3 Prosa-Stil.
- G4 Gesamtmanuskript.
- G5 Produktion.
- finale Bewertung von Review-Aufwand und Review-Sichten.
- M2-Abschlussbericht mit den sieben Prüffragen.

## Zwischenfazit

Der bisherige Engpass ist **nicht** die Anzahl der Szenen allein, sondern die Zahl der Zustands- und Abhängigkeitsartefakte. Der Test spricht bisher dafür, bei größeren Stoffen den Human Review über verdichtete, nicht-kanonische Sichten zu führen und die Detailartefakte nur bei Befund oder Rückfrage aufzublenden.

Ob daraus festes Tooling werden sollte, wird ausdrücklich erst im M2-Abschluss entschieden.
