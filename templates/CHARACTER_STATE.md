# CHARACTER_STATE

scene_id: <scene_id>
character: <Name>
status: ready

## Vor der Szene

knows_before: <was die Figur sicher weiß>
believes_before: <was sie glaubt / wie sie die Lage deutet>
wants_now: <unmittelbares Ziel>
fears_or_avoids: <relevante Gegenkraft, falls vorhanden>
relationship_state: <relevanter Beziehungsstand oder `n/a - Begründung`>
must_not_know_yet: <Informationen, die diese Figur noch nicht haben darf>

## Nach der Szene

knows_after: <neues sicheres Wissen>
believes_after: <veränderte Deutung oder `unchanged`>
relationship_change: <Veränderung oder `n/a - Begründung`>
decision_or_commitment: <Entscheidung / neue Bindung oder `none`>

## Konsistenzhinweis

<Welche frühere Szene/Entscheidung muss für diese Figur hier mitgedacht werden?>

**Zweck:** Dieser Stub ist kein vollständiges Figurenmodell. Er liefert nur den Zustand, den eine Szene für eine prose-ready Planung benötigt. Ein späteres Character-State-System darf ihn ersetzen, muss dieselben Informationen mindestens erhalten.
