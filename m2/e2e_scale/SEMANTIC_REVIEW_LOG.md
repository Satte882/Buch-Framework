# M2 – Semantic Review Log

status: complete
purpose: Semantische Reviews im M2-Lauf sichtbar dokumentieren, ohne sie als unabhängige oder bereits validierte QA-Fähigkeit auszugeben.

## SR-001 – Story-Reversal wurde fälschlich als Framework-Invalidierung interpretiert

date: 2026-08-30
review_context: same_chat_same_model_context
independent_review: no
severity: high
correction_triggered: yes
human_disposition: accepted_with_G1

Vor G1 wurde ein geplanter In-Story-Reveal fälschlich als Framework-Backtracking behandelt. `STORY_PACKAGE.md`, `STORY_BLOCKS.md` und `EVENTS.md` wurden vor Human Gate G1 korrigiert. Der reale Invalidierungstest wurde anschließend separat nach vorhandenen Downstream-Artefakten durchgeführt.

## G3 – repräsentativer Prosa-Self-Review

Vollständige Dokumentation: `SEMANTIC_G3_SELF_REVIEW.md`.

review_context: same_chat_same_model_context
independent_review: no
human_disposition: accepted_with_G3

Reale korrigierte Befundgruppen:

1. POV-Grenze in S1 überschritten — FIXED.
2. interne Framework-Labels in S5/S8 in Romanprosa geleakt — FIXED plus Regressionstest.
3. überkonstruierte Rhythmusstellen — SELECTIVELY FIXED; Staccato-Treffer im Sample von 2 auf 0 reduziert.

Der zusätzliche G2-Storydrift-Check fand keine neue Storyentscheidung und zählt nicht als Fehlerbefund.

## G4 – Vollmanuskript-Self-Review

Vollständige Dokumentation: `SEMANTIC_G4_SELF_REVIEW.md`.

review_context: same_chat_same_model_context
independent_review: no
human_disposition: accepted_with_G4

Reale korrigierte Befundgruppen:

1. S4 unnötige Negationsfolge — FIXED.
2. S6 zu frühe Publizierbarkeit gegenüber G2-Zustand — FIXED.
3. S9 künstliche Rhythmusverdichtung — FIXED.
4. S10 Sperrfrist sprachlich zu nah an 18:00 plus Rhythmus — FIXED; Veröffentlichung explizit 18:01.

## Finale M2-Zählung

semantic_review_findings: 8
real_corrections_triggered: 8
independent_semantic_reviews: 0
validated_semantic_QA_capability: no

Zählweise: 1 realer Methodenfehler vor G1 + 3 korrigierte G3-Befundgruppen + 4 korrigierte G4-Befundgruppen. Reine Checks ohne gefundenen Fehler werden nicht als Befund gezählt.

## Schlussfolgerung

M2 zeigt: strukturierte same-context Reviews können konkrete methodische, perspektivische, Stil- und Kontinuitätsfehler finden und echte Korrekturen auslösen. M2 zeigt ausdrücklich **nicht**, dass dieselbe Methode unabhängig, reproduzierbar oder mit bekannter Trefferquote funktioniert.

Daher ist eine bewusst unabhängige semantische Review-Methode ein evidenzbasierter nächster Prüfpunkt; ein automatischer Quality Score oder LLM-as-a-Judge ist durch M2 nicht gerechtfertigt.
