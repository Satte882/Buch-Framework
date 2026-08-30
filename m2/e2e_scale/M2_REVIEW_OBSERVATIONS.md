# M2 Review Observations – laufender Skalierungsnachweis

status: active
date_started: 2026-08-30
m2_issue: #10

## Zweck

Diese Datei protokolliert **beobachtete** Skalierungs- und Review-Effekte aus dem realen M2-Lauf. Sie ist kein neues Framework-Contract-Artefakt und führt keine neue Funktionalität ein.

## Aktueller Umfang

- dramaturgische Bausteine: 12
- Events: 30
- Beats: 42
- aktive Szenen: 10
- Character-State-Dateien: 31
- G2 Batch 1: S1–S5 = 5 Szenen, 21 Beats, 13 Character States
- G2 Batch 2 geplant: S6–S10 = 5 Szenen, 21 Beats, 18 Character States

## Beobachtung O-01 – semantischer Methodenfehler vor G1

type: semantic_self_review
independent_review: no
context: same_chat_same_model_context
status: corrected

Befund:

Der geplante inhaltliche Reversal E027 war zunächst fälschlich als Framework-Invalidierung interpretiert worden.

Korrektur:

- Story-Reveal und Framework-Backtracking wurden getrennt.
- Ein von Anfang an kanonisch geplanter späterer Reveal macht frühere Szenen nicht stale, wenn deren Figurenwissen korrekt ist.
- Der echte M2-Invalidierungstest bleibt eine separate kontrollierte Upstream-Änderung **nach** vorhandenen Downstream-Artefakten.

Erkenntnis:

Die KI-Selbstprüfung kann reale methodische Fehler finden, ist aber damit weiterhin **keine unabhängige semantische QA**.

## Beobachtung O-02 – deterministischer Gate-Metadatenfehler

type: deterministic_contract_check
status: corrected

Befund:

Die zunächst geschriebenen M2-Gate-Records waren fachlich richtig, aber nicht vollständig kompatibel mit dem vorhandenen Pipeline-Contract:

- G0 verwendete `artifact:` statt des verlangten Feldes `artifacts:`.
- G1 listete die freigegebenen Artefakte nur im Markdown-Text, aber nicht im maschinenlesbaren Feld `artifacts:`.

Korrektur:

- G0 enthält jetzt `artifacts: BOOK_IDEA.md`.
- G1 enthält jetzt `artifacts: STORY_PACKAGE.md; STORY_BLOCKS.md; EVENTS.md; CHARACTERS.md; RESEARCH_REGISTER.md`.

Storyinhalt wurde nicht verändert.

Erkenntnis:

Der bestehende deterministische Contract hat bereits unter M2-Last einen echten, nicht-literarischen Integrationsfehler sichtbar gemacht. Dafür war keine neue Framework-Funktion nötig.

## Beobachtung O-03 – Artefaktwachstum auf Szenenebene

type: scale_observation
status: active

M1 hatte 3 aktive Szenen und 7 Character States. M2 hat bei 10 Szenen bereits 31 Character States.

Erkenntnis bisher:

- Die Zustandslogik ist weiterhin explizit und kontrollierbar.
- Der Review aller Einzeldateien als Volltext wäre jedoch unnötig schwerfällig.
- Deshalb wird G2 wie geplant in zwei 5-Szenen-Batches geprüft.

Noch **keine** Schlussfolgerung:

Aus diesem Befund wird noch kein Character-Arc-Report-Generator gebaut. Erst M2 soll zeigen, ob eine wiederkehrende kompakte Sicht tatsächlich notwendig ist.

## Beobachtung O-04 – kompakte Batch-Sicht wird praktisch benötigt

type: review_context_observation
status: provisional

Für G2 Batch 1 wurde eine kompakte Review-Datei erstellt, die aus den bereits kanonischen Szenen/States nur die für die menschliche Entscheidung relevanten Informationen zusammenführt:

- Story-Funktion je Szene,
- zentrale Entscheidung,
- Leserwissen danach,
- Beziehungsverschiebung,
- T-/K-Kontinuität,
- Batch-Grenzzustand.

Einordnung:

Das ist aktuell **ad-hoc Review-Aufbereitung**, kein deterministischer `Scene Batch View`, kein neues Contract-Artefakt und kein neuer Gate.

Hypothese für den M2-Abschluss:

Wenn dieselbe Sicht auch in Batch 2 und im Gesamtcheck benötigt wird und der menschliche Review dadurch klar besser handhabbar ist, gibt es erstmals reale Evidenz für ein festes Review-Template oder späteres Tooling.

## Beobachtung O-05 – Batch-Grenze ist fachlich, nicht numerisch gewählt

type: batch_design
status: active_test

Die Grenze nach S5 wurde nicht nur gewählt, weil fünf Szenen erreicht sind. Nach S5 liegt ein echter Zustandswechsel vor:

- T ist unabhängig gestützt, aber noch ohne finale RC-Brücke.
- K ist deutlich geschwächt.
- Quelle A ist weiterhin geschützt, aber verunsichert.
- Jonas' externe Autonomie wurde nach dem Quellenschutzfehler begrenzt.
- Publikationsreichweite ist noch nicht final definiert.

S6 startet deshalb einen neuen funktionalen Abschnitt: Eingrenzung der publizierbaren Story bis zur Veröffentlichung.

## Noch offene Messpunkte

- menschlich wahrgenommener Aufwand Batch 1: ausstehend
- Cross-Batch-Probleme: ausstehend
- menschlich wahrgenommener Aufwand Batch 2: ausstehend
- Probleme, die erst im 10-Szenen-Gesamtcheck sichtbar werden: ausstehend
- kontrollierter Upstream-Änderungs-/Invalidierungstest: ausstehend
- Bedarf für feste Review-Sichten: ausstehend
- Bedarf für strukturierte semantische QA: ausstehend

## Regel

Beobachtungen dürfen Empfehlungen erzeugen. Sie dürfen nicht rückwirkend eine noch nicht getestete Framework-Fähigkeit als vorhanden darstellen.
