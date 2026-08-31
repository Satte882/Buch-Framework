# G4 Review Flow

status: binding_g4_supplement

## Zweck

Dieser Ablauf ist die verbindliche Review-Reihenfolge für vollständige Manuskripte in G4. Er ergänzt `FRAMEWORK_PIPELINE.md` und `ARBEITSWEISE.md`, ohne einen neuen Human Gate einzuführen.

## Ablauf

1. **Interner Whole-Manuscript-Review**
   - Modus: `EVIDENCE_BOUND_REVIEW`
   - Vertrag: `SEMANTIC_REVIEW_PROTOCOL.md`
   - vollständigen fixierten Manuskript-Snapshot lesen;
   - Findings nur aus Target-Evidenz herleiten.

2. **Adjudikation und bestätigtes Rework**
   - nur bestätigte Blocker/Major-Findings blockieren;
   - kleinste sinnvolle Rework-Ebene verwenden.

3. **Finaler horizontaler Prosa-/Rhythmuspass**
   - Vertrag: `FINAL_PROSE_RHYTHM_PASS.md`
   - danach Regression gegen Story-/Szenen-/Beat-Anker.

4. **Externer unabhängiger LLM-Review**
   - Vertrag: `EXTERNAL_LLM_REVIEW_PROTOCOL.md`
   - fixierter nahezu finaler G4-Kandidat;
   - leistungsfähiges externes allgemeines oder research-fähiges LLM;
   - Anbieter/Modell nicht im Framework fest verdrahten;
   - interne Finding-Liste im ersten externen Durchlauf nicht mitgeben.

5. **Externe Findings adjudizieren**
   - externe Findings sind advisory;
   - Evidenz, Severity und Rework-Ebene intern prüfen;
   - nur bestätigte Blocker/Major-Findings blockieren G4.

6. **Gezieltes Rework nur bei bestätigtem Bedarf**
   - bei bestätigtem externem Blocker/Major betroffene Ebene korrigieren;
   - erforderliche Regression wiederholen;
   - externen Vollreview nur erneut durchführen, wenn der bestätigte Major/Blocker relevantes Rework ausgelöst hat.

7. **G4 Human Gate**
   - erst auf dem konkret geprüften und dispositionierten Snapshot `APPROVE`, `REWORK` oder `STOP`.

## Warum zwei Modellperspektiven?

Ein langfristig im Projekt arbeitendes Modell kann trotz guter Evidenzdisziplin an eigene Prämissen, Formulierungslogiken oder bekannte Erklärmuster gewöhnt sein. Der externe Review soll genau diesen Kontextdrift angreifen.

Er ersetzt weder internen Review noch menschliche Entscheidung.

## KISS-Regel

> Intern sauber machen → extern unabhängige zweite Sicht einholen → Findings adjudizieren → G4 entscheiden.
