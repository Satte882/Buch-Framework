# G0 Review Request – FEHLALARM

status: AWAITING_HUMAN_DECISION
gate_id: G0
artifact: `m1/e2e_minibook/BOOK_IDEA.md`
artifact_ref: `924fdeacaebec83020b5abedb6643feabbaf74fc`
provenance: `m1/e2e_minibook/provenance/BOOK_IDEA.md`

## Zweck

Dies ist die erste echte Human-Gate-Vorlage des vollständigen M1-End-to-End-Laufs. Es ist **kein Gate-Record** und enthält bewusst keine Freigabe.

## Kurzfassung der Idee

`FEHLALARM` ist ein dreiszeniger psychologischer Kurzthriller-Testfall: Eine Nachtschicht in einem Forschungsgebäude hat sich wegen wiederholter Fehlalarme daran gewöhnt, Warnungen zunächst lokal zu prüfen. Als derselbe Bereich erneut Rauch meldet, sprechen Erfahrung und wirtschaftlicher Druck für einen weiteren Fehlalarm. Mara Voss entscheidet sich gegen sofortige Volleskalation, prüft selbst und gerät dadurch in eine Lage, in der die eingeübte Abkürzung plötzlich reale Folgen haben kann.

## G0-Prüfpunkte

Bitte nur die für die Idee irreversiblen Punkte beurteilen:

1. Trägt der Kernkonflikt `Sicherheitspflicht vs. erlernte Routine/wirtschaftlicher Druck` den kleinen M1-Testfall?
2. Ist die Leitfrage klar genug, um die späteren drei Szenen zu führen?
3. Ist der Mechanismus der wiederholten Fehlalarme plausibel genug als Storymotor, vorbehaltlich späterer Recherche?
4. Ist der Testfall ausreichend eigenständig und klar von `NORMALFALL`, `ABWEICHUNG` und Buch 3 getrennt?
5. Ist die Idee klein genug für M1, ohne den E2E-Test künstlich zu vereinfachen?

## Nächste menschliche Entscheidung

- `APPROVE` – die Idee ist für M1 freigegeben; danach darf das Story Package entwickelt werden.
- `REWORK` – konkrete Änderungen an der Idee vor Storyentwicklung.
- `STOP` – dieser M1-Testfall wird verworfen.

Erst nach einer ausdrücklichen menschlichen Entscheidung wird ein echter `gates/G0.md`-Record für genau diesen Artefakt-Blob angelegt.