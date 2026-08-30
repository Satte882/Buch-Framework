# G4 Review Request – FEHLALARM v0.2

status: AWAITING_HUMAN_G4_DECISION
gate_name: Manuskript
prior_gate: `m1/e2e_minibook/gates/G3.md`
prior_gate_ref: `fe3a69c49432ffa4a142b883eed0da960c31f916`

## Zweck

G4 prüft den **vollständigen Mini-Manuskriptstand** nach erfolgreichem G3-Prosa-Stil-Gate.

G4 schützt nicht mehr Story- oder Szenenarchitektur und auch nicht nur einen Stil-Batch. Die Frage ist jetzt, ob genau dieser vollständige Text als kanonischer Manuskriptstand für die anschließende Produktion akzeptiert werden kann.

## Zu prüfender Manuskriptstand

- `m1/e2e_minibook/MANUSCRIPT_v02.md`
- blob: `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
- Provenienz: `m1/e2e_minibook/provenance/v02/MANUSCRIPT.md`
- Provenienz-blob: `ce978a074a76a961a62d0f630dda74a8670a0e9d`

Der Gesamttext besteht ausschließlich aus:

- S1 — blob `695c4122820f29aa26b1efa82bbbbe920b84b108`
- S2 — blob `322c13d3aa045f5b9915faa162a7b263fdabf3b3`
- S3 — blob `d70b18b3195a240bedcef0295dce1737fa388a73`

S1 und S2 wurden als repräsentativer Stil-Batch bereits in G3 freigegeben. S3 wurde danach aus dem G2-freigegebenen Szenenstand auf genau diesem Stilpfad erzeugt und vor G4 rein sprachlich geglättet.

## Deterministischer Prosa-Audit

- Report: `m1/e2e_minibook/PROSA_AUDIT_v02.json`
- blob: `ff9d288a44408731b6ad8769c664ce9d7960f12e`
- Scanner: `scripts/prosa_audit.py` — blob `b0ac99cad7d208e363a902b5a632de59661add3f`
- Regelkonfiguration: `config/prosa_rules.yml` — blob `001296c418c7827457cbd15249272840a691bfed`

Ergebnis:

- `FAIL = 0`
- `REVIEW = 0`
- `INFO = 4`

Die vier INFO-Signale sind bewusst disponiert:

1. zwei kurze berufliche Dialogketten in S1 (`dialogue_pingpong`),
2. zwei kurze narrative Spannungsfolgen in S2 (`staccato_sequence`).

Nach der geltenden Regelmatrix sind beide Detektorfamilien ausdrücklich nur deskriptive INFO-Signale und kein Qualitätsgrenzwert. Die Stellen waren außerdem bereits Bestandteil des menschlich freigegebenen G3-Stil-Batches.

## Semantischer Gesamtcheck vor G4

Eigenprüfung der erzeugenden KI, **kein unabhängiger Human Review**:

### Story-Fidelity

- keine neue Storyentscheidung in der Prosa,
- Mara trägt sowohl lokale Prüfung als auch spätere Eskalation selbst,
- Nils besitzt kein verborgenes Mehrwissen und bleibt legitime Gegenposition,
- Lea wird erst in S3 konkret bestätigt,
- ihre Restanwesenheit bleibt banal und kein Twist-Komplott,
- der aktuelle Gefahrenhinweis ist real,
- frühere Fehlalarme bleiben ebenfalls real,
- der Nachtversuch bleibt verloren,
- keine ungesicherte öffentliche BMA-/Feuerwehrprozedur wird behauptet.

### Prosa / Rhythmus

- S1 trägt ruhige Exposition und beruflichen Dialog,
- S2 beschleunigt über Anwesenheitsspur und physischen Gegenbeleg,
- S3 löst menschliche Konsequenz, technischen Payoff und Betriebskosten gemeinsam ein,
- keine `sondern`-Verletzung,
- keine deterministische REVIEW-Stelle,
- zwei zunächst zu weiche bzw. zu symmetrische S3-Formulierungen wurden vor G4 rein sprachlich entfernt.

### Bewusste menschliche Urteilspunkte

Es verbleiben keine mechanischen Blocker. Zwei Punkte sind echte redaktionelle Geschmacksentscheidungen und werden deshalb nicht automatisch verändert:

1. **Schluss-Explizitheit:** S3 formuliert die Grenze der Fehlalarm-Routine relativ klar (`aus drei alten Antworten eine vierte machen`). Das schließt die Leitidee sauber, könnte aber bewusst als etwas expliziter als der restliche Text empfunden werden.
2. **Konsequenz-Wiederholung:** Der verlorene Nachtversuch wird am Ende von S2 und mehrfach in S3 präsent gehalten. Das macht den Preis der Entscheidung sichtbar; menschlich ist zu entscheiden, ob die Wiederholung genau richtig oder minimal zu stark ist.

Diese Punkte sind keine festgestellten Fehler. Sie sind die verbleibenden qualitativen G4-Urteilsstellen.

## G4-Reviewfragen

1. Funktionieren S1 → S2 → S3 als geschlossener Mini-Thriller mit sauberer Eskalationskurve?
2. Ist die Prosa über alle drei Szenen stilistisch konsistent genug?
3. Bleibt Mara als Figur glaubwürdig und trägt sie die Entscheidungen selbst?
4. Bleibt Nils nachvollziehbar, ohne zum Strohmann zu werden?
5. Funktioniert Lea in S3 als reale Konsequenz, ohne künstliche Plotfalle zu wirken?
6. Ist der Verlust des Nachtversuchs ausreichend spürbar, ohne überbetont zu werden?
7. Ist der Schluss thematisch präzise oder bereits zu erklärend?
8. Gibt es störende sichtbare KI-Prosa-Muster, die der Audit nicht mechanisch erfassen kann?
9. Würdest du **genau diesen Manuskript-Blob** als kanonischen M1-Manuskriptstand für die Produktion freigeben?

## Nächste menschliche Entscheidung

- `G4-APPROVE` — genau `MANUSCRIPT_v02.md` blob `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a` wird als kanonischer Mini-Manuskriptstand akzeptiert; anschließend wird ein echtes Produktionsartefakt erzeugt und G5 vorbereitet.
- `G4-REWORK` — konkrete Manuskriptstellen/Befunde werden gezielt überarbeitet; Storyänderungen dürfen nicht still in der Prosa erfolgen.
- `G4-STOP` — der M1-Lauf wird beendet.

**Wichtig:** G4 wird nicht durch Audit oder KI-Selbstreview ersetzt. Erst eine bewusste menschliche Entscheidung darf den Manuskriptstatus von `draft` auf `accepted` setzen.