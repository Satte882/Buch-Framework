# G3 Review Request – SPERRFRIST M2

status: AWAITING_HUMAN_G3_DECISION
gate_name: Prosa-Stil
prior_gate: `gates/G2.md`
prior_gate_ref: `dc4123e5e83302fed08fdac6142fcf541b2f98f1`
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`
sample_scope: S1; S5; S8

## Zweck

G3 prüft den **Stilpfad**, nicht das vollständige Manuskript. Der Mensch entscheidet, ob die drei bewusst unterschiedlichen Prosa-Szenen denselben tragfähigen Stil zeigen und dieser Stil auf die übrigen sieben bereits G2-freigegebenen Szenen skaliert werden darf.

Ein `G3-APPROVE` bestätigt keine neue Storywahrheit und ist noch keine G4-Manuskriptfreigabe.

## Feste Schreibbasis

- `PROSE_PROFILE.md` — blob `97795f16ca8684a5e80d50a22d54127c02da8919`
- `G3_SAMPLE_CONTEXT.md` — blob `26f00763ba1a35a1530cfbfdfb5a9c7a39a22497`
- `BEATS.md` — blob `0fc2896bd4a33bf6124a835770c9357961c631ab`
- `RESEARCH_REGISTER.md` — blob `0a4f457663e3c5244203c2a6324e51972744b645`

## Repräsentativer Prosa-Batch

| Szene | Testfunktion | Draft-Blob | Provenienz |
|---|---|---|---|
| S1 – Das Dossier | Einstieg, Quelle, Exposition, Zeitdruck | `07ca8139e15f6d8985fe8b97592685cd8de50599` | `provenance/g3_sample/S1.md` — `1424140984d5287c1d45fb899599c1eb20602a11` |
| S5 – Der Preis der Anfrage | Quellenschutz, Beziehungskrise, Führungsverantwortung | `2d9d74d2e1164899d4288e488ece21909392c836` | `provenance/g3_sample/S5.md` — `7f743af0e8a6c69f5575940092573a5cc01d5df7` |
| S8 – Ein Beleg, zwei Wirkungen | Evidenz-Reversal, Mehrpersonenszene, Behauptungsgrenze | `10274f1b66b2d13f1a8061f1be992edbbd256946` | `provenance/g3_sample/S8.md` — `ef6f51df7d7a1dbd9745945966630dd423414f94` |

Alle drei Provenienzmanifeste stehen weiterhin auf `status: draft`; G3 wird nicht vorweggenommen.

## Technischer Audit

Finaler Stand: CI Run #40, Commit `424fab21730ad417cba47c53a62f7d23b5859c7a` — **PASS**.

- `FAIL`: 0
- `REVIEW`: 0
- `INFO`: 14
- alle 14 INFO: `dialogue_pingpong`
- `staccato_sequence`: 0
- Draft-Provenienz: 3/3 `OK`
- Framework-Label-Leak-Test: PASS

Die 14 `dialogue_pingpong`-Treffer sind nach dem bestehenden Scanner-Contract rein beschreibende INFO-Befunde. Sie werden nicht automatisch als Stilproblem oder Rework-Grund behandelt.

## Same-context Self-Review

`SEMANTIC_G3_SELF_REVIEW.md` — blob `dc4876b8fb6702559281a399ba6129d0a020371b`

Gefunden und korrigiert wurden:

1. eine POV-Grenzverletzung in S1,
2. Framework-Labels in S5/S8,
3. mehrere überkonstruierte Rhythmusstellen.

Kein neuer G2-Storyentscheid wurde gefunden. Wichtig: Der Review war **nicht unabhängig** und belegt weiterhin keine implementierte semantische QA-Fähigkeit.

## G3-Prüffragen

1. Trägt die enge Nora-Perspektive über Einstieg, Beziehungskrise und Evidenz-Reversal konsistent?
2. Wirkt die Prosa zugänglich und spannungsorientiert, ohne journalistische Prozessprosa zu werden?
3. Klingen die Dialoge trotz hoher Dialogdichte natürlich genug und haben die Figuren unterscheidbare Funktionen?
4. Bleiben technische und rechtliche Informationen verständlich, ohne Erklär- oder Beweisprosa?
5. Sind S5s Beziehungskosten und S8s Reversal im Erleben sichtbar, ohne nachträgliche Methodenerklärung?
6. Gibt es sichtbare KI-Prosa-Muster, die vor Skalierung auf sieben weitere Szenen korrigiert werden müssen?
7. Trägt der Stil stark genug, um ihn jetzt auf S2–S4, S6–S7 und S9–S10 zu skalieren?

## Nächste menschliche Entscheidung

- `G3-APPROVE` — genau dieser Stilpfad und diese drei Draft-Blobs werden als G3-Stil-Stichprobe freigegeben; danach werden die übrigen sieben G2-Szenen in Prosa geschrieben.
- `G3-REWORK` — konkrete Stilbefunde am Sample bearbeiten; übrige Prosa bleibt gesperrt.
- `G3-STOP` — M2 an dieser Stelle beenden.

**Wichtig:** Nur der Mensch kann G3 freigeben.