# G3 SAMPLE CONTEXT – FEHLALARM v0.2

status: ready
gate_basis: G2 APPROVE
g2_gate_ref: `8eec3e520fedffb68390cdc5194d5e9dbe7bfc05`
prose_profile: `PROSE_PROFILE.md`
prose_profile_ref: `971e334ed6a3b6b6a421525eb9e1ef0a06fa7021`
beats_ref: `ce33eb6a09458484b69691dc1425c50e318dce3e`
research_ref: `a1026077fc15be857827f691f76bcb4ca0bfe4eb`
sample_scenes: S1; S2

## Zweck

Dieser Kontext ist die feste Schreibbasis für den repräsentativen G3-Prosa-Batch. Er erlaubt sprachliche Konkretisierung, aber keine neue Storywahrheit.

## S1 – Upstream

- `scenes/S1.md` — `55d7d616044f42e789ecdb51ca0152e46fc19962`
- `character_states/S1_MARA.md` — `0c17101e0a7a97f12c0d8edace64abbe47eceb27`
- `character_states/S1_NILS.md` — `91f8aa5dddd057e9f6c1766de5e98d91538465c6`
- Beats: `BT001–BT004`

Muss erhalten bleiben: neues internes Warnsignal; Fehlalarm-Vorgeschichte; Kamera nicht verwertbar; Bereich offiziell leer; realer Versuchsschaden; Nils als legitime Gegenposition; Mara entscheidet selbst für lokale Verifikation; Lea und reale Ursache bleiben unbekannt.

## S2 – Upstream

- `scenes/S2.md` — `75e38f02ec385e99f6d54b594f67502622460f9c`
- `character_states/S2_MARA.md` — `91828b11e00b41b199fd149d160d0a5b42d3812c`
- `character_states/S2_NILS.md` — `156c8177175363119e7ac1a94bb8e7ce1400cc2a`
- Beats: `BT005–BT010`

Muss erhalten bleiben: zunächst ruhiger Bereich; frische Anwesenheitsspur widerspricht Leerstand; unabhängiger Rauch-/Hitzehinweis; Nils bittet plausibel um wenige weitere Sekunden; Mara entscheidet aufgrund kumulierender Evidenz gegen weiteres Warten; volle interne Alarm-/Evakuierungskette wird aktiviert; Nachtversuch geht verloren; Lea bleibt noch unbestätigt.

## Gemeinsame Schreibgrenzen

- enge dritte Person bei Mara,
- keine neue relevante Information oder Entscheidung,
- kein verborgenes Mehrwissen bei Nils,
- keine heroische Rettungsaktion,
- keine detaillierte öffentliche BMA-/Feuerwehrprozedur,
- keine Methodenerklärung im Romantext,
- `sondern = 0`,
- bei Konflikt gilt immer der G2-freigegebene Upstream vor sprachlicher Eleganz.

## Batch-Logik

S1 und S2 werden als echte Drafts erzeugt und gemeinsam in G3 geprüft. Erst nach menschlichem `G3-APPROVE` wird die Prosa auf S3 und damit auf den vollständigen Mini-Fall skaliert.