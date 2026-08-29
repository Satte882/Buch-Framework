# Provenienz – FEHLALARM G2 Package

generated_via: chatgpt_chat
action: generated
date: 2026-08-29
purpose: Figuren-Baseline und Rechercheauflösung für den M1-End-to-End-Lauf
status: accepted
gate_basis: G1 APPROVE + human_G2_APPROVE

## Upstream

- `m1/e2e_minibook/STORY_PACKAGE.md`
  - Blob-SHA: `d2b1c8d5c46f5afb51f876a652735b431ed9ab22`
- `m1/e2e_minibook/gates/G1.md`
  - menschliche Entscheidung: `APPROVE`

## Freigegebene G2-Artefakte

- `m1/e2e_minibook/CHARACTERS.md`
  - Blob-SHA: `8acecd8cc47d707bd3f614e29609602587b3ce14`
- `m1/e2e_minibook/RESEARCH_REGISTER.md`
  - Blob-SHA: `d0094d9a7a88b43eaf7481e7b357ae93e6d4830c`
- `m1/e2e_minibook/gates/G2.md`
  - menschliche Entscheidung: `APPROVE`

## Recherche R-001

Externe fachliche Grundlage:

- DIN 14675-1 – Brandmeldeanlagen, Aufbau und Betrieb.
- DIN VDE 0833-2 – Festlegungen für Brandmeldeanlagen.
- DIN-Fachinformation 2023 zu Anschlussbedingungen für Brandmeldeanlagen.
- DIN-Fachinformation 2025 zu Übertragung und Fernzugriff auf Brandmeldeanlagen.

Entscheidung für den Testfall: Das erste Warnsignal wird als internes technisches Rauch-/Prozesssignal definiert. FEHLALARM beschreibt keine frei verzögerbare, feuerwehraufgeschaltete Haupt-BMA. Die volle interne Alarm-/Evakuierungskette wird erst Maras spätere Entscheidung.

## Schutzgrenzen

- Nils erhält kein verborgenes Täterwissen.
- Lea wird nicht zur absichtlich verschwiegenen Plotfigur.
- Keine detaillierte reale Feuerwehr-/BMA-Prozedur wird erfunden.
- Relevante Änderungen an Figuren- oder Recherchewahrheit erfordern Backtracking nach `SOURCE_OF_TRUTH.md`.

## Aktueller Gate-Status

`G2: APPROVE`