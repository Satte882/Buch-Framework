# Provenienz – FEHLALARM G3-Paket

generated_via: chatgpt_chat
action: generated
date: 2026-08-29
purpose: Drei Szenenpläne und zugehörige Character States nach menschlichem G2-APPROVE als gebündeltes G3-Review-Paket vorbereiten.
status: draft
gate_basis: G0 APPROVE + G1 APPROVE + G2 APPROVE

## Kanonische Upstream-Quellen

- `BOOK_IDEA.md` – freigegebener G0-Stand
- `STORY_PACKAGE.md` – Blob `d2b1c8d5c46f5afb51f876a652735b431ed9ab22`
- `CHARACTERS.md` – Blob `8acecd8cc47d707bd3f614e29609602587b3ce14`
- `RESEARCH_REGISTER.md` – Blob `d0094d9a7a88b43eaf7481e7b357ae93e6d4830c`
- `gates/G2.md` – menschliche Freigabe der Figuren-/Recherchebasis

## Erzeugte Szenenartefakte

- `scenes/S1.md` – Die vernünftige Abkürzung
- `scenes/S2.md` – Das Muster passt nicht mehr
- `scenes/S3.md` – Der Preis der richtigen Entscheidung

## Erzeugte Character States

- `character_states/S1_MARA.md`
- `character_states/S1_NILS.md`
- `character_states/S2_MARA.md`
- `character_states/S2_NILS.md`
- `character_states/S3_MARA.md`
- `character_states/S3_NILS.md`
- `character_states/S3_LEA.md`

## Bewusste Grenze vor G3

Die drei Szenen stehen aktuell auf `experience_status: pending_human_review`. Damit wird keine menschliche Scene-Readiness-Freigabe vorweggenommen. Bei einem ausdrücklichen gebündelten `G3 = APPROVE` werden die drei konkreten Szenenstände auf `human_reviewed_ready` gesetzt und ein G3-Gate-Record für die dann gültigen Blobs angelegt.

## Schutz gegen Drift

Die Szenen dürfen keine neue Storywahrheit einführen, die dem freigegebenen Story Package widerspricht. Insbesondere bleiben Nils' fehlendes Mehrwissen, Leas banale Restanwesenheit, die interne Warnsystem-Abgrenzung aus R-001 sowie der reale Verlust des Nachtversuchs verbindlich.