# M2 Invalidation Test – SPERRFRIST

status: PASS
date: 2026-08-30
m2_issue: `#10`
canonical_branch: `main`
test_branch: `m2-invalidation-test`
test_pr: `#15` — closed, not merged

## Zweck

M2 musste nach vorhandenem, menschlich G2-freigegebenem Downstream eine **relevante Upstream-Änderung** durchlaufen und zeigen, dass stille Weiterverwendung verhindert wird.

Der Test verwendet ausschließlich die bestehende Provenienzmechanik aus `scripts/provenance_check.py`. Es wurde kein neuer Invalidierungsalgorithmus gebaut.

## Baseline auf main

Nach `G2-APPROVE` wurden zehn Szenen-Provenienzmanifeste angelegt:

- `provenance/v02/S1.md` bis `S10.md`
- Status jeweils `accepted`
- alle referenzieren den G2-kanonischen `CHARACTERS.md`-Blob `6eaeb1fdb2a9eef6eb13fe0cd98e686242abd343`
- zusätzlich referenzieren sie Szene, Beats, Events, Story Blocks, Research Register und ihre Character States.

`tests/test_m2_provenance.py` prüfte auf `main` alle zehn Manifeste gegen den unveränderten Stand.

**Baseline-Ergebnis:** 10/10 `OK`.

CI-Nachweis: Framework Validation Run **#35**, conclusion `success`.

## Kontrollierte relevante Upstream-Änderung

Die Test-Branch änderte ausschließlich zu Testzwecken Jonas Rehms Governance-Baseline in `CHARACTERS.md`:

- vorher: hohes operatives Vertrauen; unter Zeitdruck ist eine zu konkrete Verifikationsanfrage als unbeabsichtigter Fehler plausibel;
- Testannahme: externe Kontakte sind von Beginn an nur nach expliziter Freigabe durch Nora erlaubt.

Damit würde die kanonische S5-Mechanik nicht mehr denselben Figurenfehler darstellen: Eine eigenmächtige Anfrage wäre nun ein bewusster Governance-Verstoß. Die Änderung ist daher semantisch relevant und kein Tippfehler.

Blob-Änderung:

- kanonisch: `6eaeb1fdb2a9eef6eb13fe0cd98e686242abd343`
- Testinjektion: `40138918df1f040a178a3cb7dea7864c7bb4bd94`

Die Testinjektion wurde nie nach `main` gemergt.

## Phase 1 – accepted + Upstream-Drift

Die zehn Szenenmanifeste blieben zunächst unverändert auf `status: accepted` und referenzierten weiterhin den alten `CHARACTERS.md`-Blob.

Erwartung:

`accepted + blob mismatch → BLOCK`

Ergebnis:

- S1–S10: **10/10 BLOCK**
- der `CHARACTERS.md`-Mismatch blieb in jedem Ergebnis sichtbar.

CI-Nachweis: Draft-PR #15, Framework Validation Run **#36**, conclusion `success`, weil der Test exakt das Blockieren erwartete.

## Phase 2 – sichtbare Invalidierung

Anschließend wurden auf der Test-Branch alle zehn Manifeste explizit auf `status: stale` gesetzt. Die alten Blob-Referenzen wurden absichtlich **nicht** aktualisiert.

Erwartung:

`stale + derselbe blob mismatch → STALE_OK`

Ergebnis:

- S1–S10: **10/10 STALE_OK**
- der `CHARACTERS.md`-Mismatch blieb weiterhin sichtbar.

CI-Nachweis: Draft-PR #15, Framework Validation Run **#38**, conclusion `success`.

Der Test-PR wurde danach geschlossen und nicht gemergt.

## Nachgewiesene Zustandsfolge

```text
accepted + unverändert       → OK
accepted + relevanter Drift  → BLOCK
stale + derselbe Drift       → STALE_OK
```

Damit verhindert das Framework stille Weiterverwendung eines akzeptierten Downstreams und erlaubt zugleich einen expliziten, sichtbaren Rework-Zustand.

## Skalierungsbefund: technischer Blast Radius ist zu grob

Die Teständerung betrifft semantisch primär Jonas’ Governance- und Vertrauensbogen. Mindestens S2/S5 und die späteren Jonas-Folgen in S6/S8/S10 müssten fachlich überprüft werden; S3 kann wegen seiner frühen Korrektur ebenfalls relevant sein.

Der bestehende Checker entscheidet solche semantische Relevanz bewusst **nicht**. Weil jedes Szenenmanifest den gesamten `CHARACTERS.md`-Blob referenziert, erzeugte eine Änderung in Jonas’ Abschnitt technisch:

**10/10 Szenen stale.**

Das ist sicher, aber grobgranular. Bei größeren Büchern kann der technische Invalidierungsradius deshalb deutlich größer sein als der tatsächliche semantische Rework-Radius.

Dieser Befund rechtfertigt noch keine sofortige neue Funktion. Er ist aber ein konkreter Kandidat für spätere Verbesserung, z. B. feinere Provenienzreferenzen oder eine bewusst menschlich/semantisch disponierte Impact-Analyse.

## Bewertung

- relevante Upstream-Änderung nach vorhandenem Downstream: PASS
- akzeptierter Downstream blockiert bei Drift: PASS
- explizite Stale-Markierung wird erkannt: PASS
- Drift bleibt nach Stale-Markierung sichtbar: PASS
- kanonischer `main`-Stand unverändert durch Testinjektion: PASS
- neue Invalidierungsfunktion nötig: NEIN
- Skalierungsproblem sichtbar: JA — file-level Provenienz ist konservativ und grobgranular

**M2-Invalidierungstest: PASS.**
