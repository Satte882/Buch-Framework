# G3 Review Request – FEHLALARM v0.2

status: AWAITING_HUMAN_G3_DECISION
gate_name: Prosa-Stil
prior_gate: `m1/e2e_minibook/gates/G2.md`
prior_gate_ref: `8eec3e520fedffb68390cdc5194d5e9dbe7bfc05`
prior_g3_record: `m1/e2e_minibook/gates/G3.md` – superseded v0.1 test trace; not valid for this v0.2 Prosa-Stil-Paket

## Zweck

G3 prüft nach v0.2 **nicht mehr die Szenenarchitektur**. Diese ist bereits mit G2 freigegeben.

G3 schützt jetzt die Skalierungsentscheidung für die Prosa: Ein repräsentativer Batch aus G2-freigegebenen Szenen wird als echte Prosa geprüft, bevor der Stil auf den restlichen Mini-Fall übertragen wird.

## Freigegebene Schreibbasis

- `m1/e2e_minibook/G3_SAMPLE_CONTEXT.md` — blob `4003455bf8b24385b59930404df855614a0ad859`
- `m1/e2e_minibook/PROSE_PROFILE.md` — blob `971e334ed6a3b6b6a421525eb9e1ef0a06fa7021`
- `m1/e2e_minibook/gates/G2.md` — blob `8eec3e520fedffb68390cdc5194d5e9dbe7bfc05`

## Repräsentativer Prosa-Batch

### S1 – Exposition / Entscheidung unter Unsicherheit

- Draft: `m1/e2e_minibook/drafts/v02/S1.md`
- blob: `695c4122820f29aa26b1efa82bbbbe920b84b108`
- Provenienz: `m1/e2e_minibook/provenance/v02/S1.md`

Prüft insbesondere:

- Einstieg und Lesefluss,
- Informationsdosierung ohne Infodump,
- enge dritte Person bei Mara,
- Natürlichkeit des Dialogs mit Nils,
- ob Maras lokale Prüfung nachvollziehbar aus der Szene entsteht,
- ob die Prosa zu sichtbar erklärt oder beweist.

### S2 – Drucksteigerung / Evidenzwechsel / Eskalation

- Draft: `m1/e2e_minibook/drafts/v02/S2.md`
- blob: `322c13d3aa045f5b9915faa162a7b263fdabf3b3`
- Provenienz: `m1/e2e_minibook/provenance/v02/S2.md`

Prüft insbesondere:

- Erlebnisdichte im ruhigen Flur,
- saubere Steigerung von Anwesenheitsspur zu Gefahrenhinweis,
- Nils als plausible Gegenposition,
- Rhythmus am Kipppunkt,
- ob Maras Eskalation aus Handlung und Evidenz entsteht statt aus Erklärtext,
- ob die Spannung ohne künstliche Überdramatisierung trägt.

## Warum S1 + S2 repräsentativ sind

Der Batch testet zwei unterschiedliche Schreibmodi, bevor skaliert wird:

1. **S1:** ruhige Exposition + Dialog + Abwägung,
2. **S2:** räumliche Spannung + Evidenzwechsel + irreversible Entscheidung.

S3 bleibt bewusst noch ungeschrieben. Nach erfolgreichem G3 muss gezeigt werden, dass der freigegebene Stil auf eine weitere Szene skaliert werden kann, statt G3 faktisch erst nach dem vollständigen Mini-Manuskript abzuhalten.

## Story-Fidelity-Check

Die Drafts verändern den G2-Stand nicht:

- Nils besitzt kein verborgenes Mehrwissen.
- Lea wird in S1/S2 nicht als konkrete anwesende Person bestätigt.
- Maras erste lokale Prüfung bleibt ihre eigene Entscheidung.
- S2 kippt über kumulierende Evidenz.
- Die volle interne Alarm-/Evakuierungskette wird erst in S2 ausgelöst.
- Der Nachtversuch geht dadurch real verloren.
- Keine detaillierte öffentliche BMA-/Feuerwehrprozedur wurde hinzugefügt.

## Prosa-Profil-Check vor Human Review

Interne Selbstprüfung der erzeugenden KI, **kein unabhängiger Review**:

- `sondern = 0` in beiden G3-Drafts,
- keine neue Storyentscheidung erkannt,
- zwei zunächst zu methodisch erklärte Entscheidungsstellen wurden vor dem Review rein sprachlich gestrafft,
- kurze Absätze und Dialogwechsel sind vorhanden und müssen im G3 bewusst auf Rhythmus statt mechanisch als Fehler bewertet werden.

## G3-Reviewfragen

1. Liest sich der Batch wie zugängliche Thriller-Prosa statt wie eine ausgearbeitete Szenenkarte?
2. Trägt die enge Mara-Perspektive, ohne ständig Wahrnehmung oder Schlussfolgerungen zu erklären?
3. Ist der Absatz- und Satzrhythmus funktional oder zu stakkato-/KI-typisch?
4. Wirkt der Dialog mit Nils wie echte berufliche Kommunikation statt Informationsabfrage für den Leser?
5. Bleibt Nils auch sprachlich eine legitime Gegenposition?
6. Entsteht der Kipppunkt in S2 im Erleben oder wird er noch zu stark erklärt?
7. Sind Erklär-Echos, Beweisprosa, rhetorische Symmetrie oder andere sichtbare KI-Prosa-Muster störend?
8. Ist die Prosa konkret genug, ohne unnötige technische Details zu erfinden?
9. Würdest du diesen Stil als Basis für S3 und danach den vollständigen Mini-Fall freigeben?

## Nächste menschliche Entscheidung

- `G3-APPROVE` – genau die beiden oben referenzierten Draft-Blobs plus das referenzierte Prosa-Profil werden als Stil-Stichprobe freigegeben; anschließend wird S3 auf diesem Stilpfad erzeugt und der vollständige Mini-Fall für G4 aufgebaut.
- `G3-REWORK` – konkrete Prosa-Befunde werden im repräsentativen Batch überarbeitet; keine Storyänderung wird still eingebaut.
- `G3-STOP` – der M1-Lauf wird beendet.

**Wichtig:** Das alte `gates/G3.md` dokumentiert die supersedierte v0.1-Szenenfreigabe und gilt nicht für diesen Prosa-Batch. Ein neuer G3-Record darf erst nach einer bewussten menschlichen Entscheidung über genau diese Draft-Stände geschrieben werden.