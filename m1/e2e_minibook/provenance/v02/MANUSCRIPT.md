# Provenienz – FEHLALARM v0.2 Manuskript

artifact: `m1/e2e_minibook/MANUSCRIPT_v02.md`
artifact_ref: `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
generated_via: chatgpt_chat
action: generated
date: 2026-08-30
purpose: Die drei v0.2-Prosa-Drafts nach erfolgreichem G3-Stil-Gate zu einem vollständigen Mini-Manuskript für G4 zusammensetzen.
gate_basis: G2 APPROVE + G3 APPROVE + G4 APPROVE
status: accepted

## Upstream-Drafts

- `m1/e2e_minibook/drafts/v02/S1.md` — blob `695c4122820f29aa26b1efa82bbbbe920b84b108` — G3-Stil-Stichprobe `accepted`
- `m1/e2e_minibook/drafts/v02/S2.md` — blob `322c13d3aa045f5b9915faa162a7b263fdabf3b3` — G3-Stil-Stichprobe `accepted`
- `m1/e2e_minibook/drafts/v02/S3.md` — blob `d70b18b3195a240bedcef0295dce1737fa388a73` — nach G3 skaliert und mit G4 als Bestandteil des Manuskripts akzeptiert

## Gate- und Profilbasis

- `m1/e2e_minibook/gates/G2.md` — blob `8eec3e520fedffb68390cdc5194d5e9dbe7bfc05`
- `m1/e2e_minibook/gates/G3.md` — blob `fe3a69c49432ffa4a142b883eed0da960c31f916`
- `m1/e2e_minibook/gates/G4.md` — menschlicher G4-APPROVE-Record vom 2026-08-30
- `m1/e2e_minibook/PROSE_PROFILE.md` — blob `971e334ed6a3b6b6a421525eb9e1ef0a06fa7021`

## Qualitätsprüfung vor G4

- `m1/e2e_minibook/PROSA_AUDIT_v02.json` — blob `ff9d288a44408731b6ad8769c664ce9d7960f12e`
- Ergebnis: `FAIL = 0`, `REVIEW = 0`, `INFO = 4`
- Alle vier INFO-Signale sind mit bewusster Disposition dokumentiert; INFO ist nach der geltenden Regelmatrix kein Qualitätsgrenzwert.
- Die semantische Eigenprüfung der erzeugenden KI ist dokumentiert, aber ausdrücklich kein unabhängiger Human Review.

## G4-Entscheidung

Der Mensch hat im Chat am 2026-08-30 ausdrücklich `G4-APPROVE` für exakt `MANUSCRIPT_v02.md` blob `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a` erteilt.

Damit ist dieser Stand der kanonische M1-Manuskriptstand für die Produktion.

## Zusammenbau-Regel

Das Manuskript enthält ausschließlich die Prosa der drei aktuellen v0.2-Drafts in Reihenfolge S1 → S2 → S3. Es übernimmt keine alten v0.1-Drafts und keine historischen G3-/G4-Spuren.

## Gültigkeit

Das akzeptierte Manuskript darf im Produktionsschritt nur formatierend und technisch abgeleitet werden. Jede relevante inhaltliche Änderung erzeugt einen neuen Manuskriptstand und erfordert erneute G4-Prüfung. Relevante Änderungen an referenzierten Upstream-Artefakten machen diesen Stand mindestens `stale`.