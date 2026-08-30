# M2 – Semantic Review Log

status: active
purpose: Semantische Reviews im M2-Lauf sichtbar dokumentieren, ohne sie als unabhängige oder bereits validierte QA-Fähigkeit auszugeben.

## SR-001 – Story-Reversal wurde fälschlich als Framework-Invalidierung interpretiert

date: 2026-08-30
review_purpose: G1-Gesamtcheck vor Vorlage an den Human Gate; prüfen, ob die geplante M2-Invalidierung tatsächlich ein Provenienz-/Backtracking-Ereignis und nicht nur Teil der Storyhandlung ist.
review_context: same_chat_same_model_context
independent_review: no
artifacts_reviewed:
- `STORY_PACKAGE.md`
- `STORY_BLOCKS.md`
- `EVENTS.md`
- Issue #10 M2-Anforderung zur realen Upstream-Änderung nach vorhandenen Downstream-Artefakten

### Befund

Die erste G1-Fassung behandelte B11/E027 sinngemäß als geplanten Invalidierungsanlass: Ein später Beleg innerhalb der Story widerlegt eine frühe Verantwortungsannahme.

Das ist methodisch falsch. Da B11/E027 bereits auf G1-Ebene kanonisch zur Geschichte gehören, können spätere Beats und Szenen den früheren Figuren-Glauben an K korrekt abbilden. Diese Downstream-Artefakte werden durch den späteren In-Story-Reveal nicht stale; sie sind gerade dann korrekt, wenn sie den jeweiligen Wissensstand der Figuren zeigen.

Damit hätte M2 eine Story-Wendung fälschlich als Framework-Backtracking gezählt.

severity: high
real_framework_risk: yes

### Korrektur

Vor G1 wurden drei noch nicht human-freigegebene Artefakte korrigiert:

- `STORY_PACKAGE.md`: klare Abgrenzung Story-Reversal vs. Framework-Backtracking.
- `STORY_BLOCKS.md`: B11 bleibt Story-Reversal; kein Anspruch auf Artefaktinvalidierung.
- `EVENTS.md`: E027 ändert den Figuren-/Story-Wissensstand, nicht den kanonischen Upstream-Stand des Frameworks.

Der echte M2-Invalidierungstest wird separat erst **nach Existenz realer Downstream-Artefakte** durchgeführt: Eine relevante kanonische Upstream-Annahme wird kontrolliert geändert, betroffene Git-Abhängigkeiten müssen sichtbar stale/invalidated werden und das Rework wird gemessen.

correction_triggered: yes
human_disposition: pending_G1
notes: Die Korrektur erfolgte vor dem G1-Human-Gate. Der Mensch entscheidet mit `G1-APPROVE/REWORK/STOP` über das korrigierte Gesamtpaket; der Self-Review selbst ersetzt diese Entscheidung nicht.

## Zählung aktuell

semantic_review_findings: 1
real_corrections_triggered: 1
independent_semantic_reviews: 0
validated_semantic_QA_capability: no

**Regel:** Weitere semantische Reviews im M2-Lauf werden analog dokumentiert: Zweck, Artefakte, Kontext-Unabhängigkeit, konkreter Befund, Human-Disposition und tatsächliche Korrekturwirkung.
