# G4 Review Request – SPERRFRIST M2

status: AWAITING_HUMAN_G4_DECISION
gate_name: Manuskript
prior_gate: `gates/G3.md`
prior_gate_ref: `17330cb19c3b6b25d47f06868f690bc1828445c3`
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`

## Zweck

G4 prüft das **vollständige 10-Szenen-Manuskript** als zusammenhängenden Text. G3 hatte nur den Stilpfad an S1/S5/S8 freigegeben; G4 entscheidet erstmals über den kompletten Prosa-Stand S1–S10.

Ein `G4-APPROVE` bestätigt keine neue Storywahrheit. Es friert genau den unten referenzierten Manuskript-Blob als freigegebenen Manuskriptstand für die anschließende Produktion/G5 ein.

## G4-Kandidat

- `MANUSCRIPT_v01.md` — blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`
- Manuskript-Provenienz `provenance/MANUSCRIPT_v01.md` — blob `25182aaf660093122bdba64d91e17d44f0a04d7d`
- Umfang: 10 Szenen, ca. 6.6k Wörter

Der Manuskriptstand ist deterministisch die Verkettung der zehn aktuell referenzierten Drafts S1–S10.

## Technischer Gesamtcheck

Finale Prüfgrundlage: CI Run #42 — **PASS**.

- Tests: **60/60 PASS**
- M2 Manuskript `FAIL`: **0**
- M2 Manuskript `REVIEW`: **0**
- M2 Manuskript `INFO`: **36**
- exakte Verkettung der 10 Drafts: **PASS**
- Prosa-Provenienz: **10/10 aktuell**
- Manuskript-Provenienz: **aktuell**
- Framework-Label-Leaks: **0**

`PROSA_AUDIT_G4.md` — blob `e22a4a035143b3b890451e06e6e8f6973bd471fd`

Die 36 verbleibenden INFO-Befunde sind nach dem bestehenden Scanner-Contract rein deskriptiv (`dialogue_pingpong` 33, `staccato_sequence` 1, `softener_density` 2) und wurden nicht pauschal automatisch umgeschrieben.

## Gesamt-Self-Review

`SEMANTIC_G4_SELF_REVIEW.md` — blob `aaa4719e08fa841214432f6b36f24fa83e0a00ad`

Vor dem finalen G4-Kandidaten wurden vier konkrete Befunde korrigiert:

1. S4: einziger Scanner-REVIEW beseitigt,
2. S6: zu frühe Publizierbarkeit korrigiert; letzte Release-Brücke bleibt bis S8 offen,
3. S9: auffällige Rhythmusverdichtung reduziert,
4. S10: Veröffentlichung eindeutig auf 18:01 nach Ablauf der Sperrfrist gesetzt und Rhythmus geglättet.

Kein Befund erforderte eine neue G2-Storyentscheidung.

Wichtig: Dieser Review war **same-context Self-Review**. Er ist kein Nachweis unabhängiger semantischer QA. Diese M2-Frage bleibt separat offen.

## G4-Prüffragen

1. Funktioniert SPERRFRIST über alle zehn Szenen als zusammenhängende Geschichte statt als Folge sauberer Einzeltests?
2. Bleibt die Nora-Perspektive über den vollständigen Text konsistent und ausreichend nah?
3. Entwickeln sich technische Evidenz und persönliche Verantwortungsfrage verständlich, ohne methodische Erklärprosa?
4. Tragen Jonas' Fehler/Rehabilitation, Quelle As Konflikt und Davids Timing-Gegenposition über die Szenengrenzen hinweg?
5. Wirkt der Mittelteil S3–S7 wie zunehmender Druck oder wie repetitive Dokumentprüfung?
6. Funktioniert S8 als echter Reversal und S9/S10 als Konsequenz statt als bloßer Nachlauf?
7. Gibt es sichtbare Stil-/KI-Prosa-Muster, die vor Produktion noch zwingend revidiert werden müssen?
8. Ist der vollständige Manuskriptstand stark genug, um ihn für G5 einzufrieren?

## Nächste menschliche Entscheidung

- `G4-APPROVE` — genau Manuskript-Blob `55753bb0ce177a80886343a8ac4e23a71de05c4a` wird als vollständiger Manuskriptstand freigegeben; danach Produktion/G5.
- `G4-REWORK` — konkrete Manuskriptbefunde bearbeiten; G4 bleibt offen.
- `G4-STOP` — M2 an dieser Stelle beenden.

**Wichtig:** Nur der Mensch kann G4 freigeben.
