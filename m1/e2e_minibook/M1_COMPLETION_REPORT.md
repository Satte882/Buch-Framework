# M1 Abschlussbericht – FEHLALARM v0.2

status: PASS
fixture_status: frozen_regression_fixture
date: 2026-08-30
acceptance_basis: `M1_ACCEPTANCE.md` blob `c366c3f3f30b76e6f2358143d7ab72d254b5fe36`
issue: `#8 – M1 E2E-Lauf nach v0.2-Arbeitsweise durchführen`
issue_status: completed

## Ergebnis

**M1 Gesamt: PASS**

Der FEHLALARM-Testfall hat den vollständigen realen Chat-/GitHub-Pfad der v0.2-Arbeitsweise durchlaufen:

`Buchidee → Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten + Character States → Prosa-Stichprobe → vollständige Prosa → Manuskript → Produktion`

Die sechs fachlichen Human Gates G0–G5 wurden jeweils bewusst durch den Menschen erteilt. Generative Arbeit fand im Chat statt; GitHub hält die konkreten Artefaktstände; CI blieb deterministisch.

M1 beweist damit die kleine End-to-End-Arbeitskette und ihre notwendige Entwicklungstiefe. Es beweist ausdrücklich **nicht** die literarische Gesamtqualität oder Skalierbarkeit eines vollständigen Romans.

## Messbarer M1-Abschluss

```text
Makro→Mikro-Arbeitsfolge eingehalten: PASS
Bausteine vollständig: PASS
Ereignisse/Sequenzen vollständig: PASS
Beats vollständig: PASS
G2-freigegebene Szenenkarten: 3 (Minimum 3)
Human Gates G0–G5 vollständig: PASS
committete Prosa-Drafts: 3 (Minimum 3)
Drafts mit Provenienz: 3/3
G3 Prosa-Stil real durchlaufen: PASS
Invalidierungstest: PASS
Prosa-Audit FAIL: 0
Prosa-Audit REVIEW offen ohne Disposition: 0
Produktionsartefakt erzeugt: PASS
Deterministische CI: PASS
bekannte Skalierungsfragen dokumentiert: PASS
M1 Gesamt: PASS
```

## Kanonische Abschlussstände

### Human Gates

- G0 — `gates/G0.md` blob `b95c0af8e0d33044ae1e7522528c1076e655a085`
- G1 — `gates/G1.md` blob `41a9016f55a3a793b9e0e51a73471b9341c8be5e`
- G2 — `gates/G2.md` blob `8eec3e520fedffb68390cdc5194d5e9dbe7bfc05`
- G3 — `gates/G3.md` blob `fe3a69c49432ffa4a142b883eed0da960c31f916`
- G4 — `gates/G4.md` blob `8c4181e878c0f64d233c2bdaeaf73a218a1ab5ac`
- G5 — `gates/G5.md` blob `96e2033e60575794645485924fe6045147a5a458`

### Makro→Mikro

- `BOOK_IDEA.md` — dokumentierte Buchidee
- `STORY_PACKAGE.md` — Story Package
- `STORY_BLOCKS.md` — 6 vollständige dramaturgische Bausteine
- `EVENTS.md` — E001–E010, vollständige Block→Event-Abdeckung
- `CHARACTERS.md` — Figurenkern
- `RESEARCH_REGISTER.md` — R-001 plotrelevant, aufgelöst, nicht mehr blockierend
- `BEATS.md` — 15 Beats, vollständige E001–E010-Abdeckung
- `scenes/S1.md`, `S2.md`, `S3.md` — 3 G2-freigegebene Szenenkarten
- 7 szenenspezifische Character-State-Dateien

### Prosa und Manuskript

- `drafts/v02/S1.md` — blob `695c4122820f29aa26b1efa82bbbbe920b84b108`
- `drafts/v02/S2.md` — blob `322c13d3aa045f5b9915faa162a7b263fdabf3b3`
- `drafts/v02/S3.md` — blob `d70b18b3195a240bedcef0295dce1737fa388a73`
- Provenienz für S1/S2/S3 vorhanden
- G3 wurde mit S1+S2 als repräsentativem Stil-Batch vor der Skalierung auf S3 durchgeführt
- `MANUSCRIPT_v02.md` — G4-freigegebener blob `ee6117b52ea0cf80c2c8d312f46c0844bfc0498a`
- `PROSA_AUDIT_v02.json` — `FAIL = 0`, `REVIEW = 0`, `INFO = 4`; INFO-Signale bewusst dokumentiert

### Produktion

- `production/FEHLALARM_v02.html` — G5-freigegebener blob `1add4d45fea3e552521041ae5d6120fba717d214`
- `scripts/build_html.py` — reproduzierbarer dependency-freier Builder
- `tests/test_build_html.py` — byte-genauer Rebuild-Test
- `production/BUILD_MANIFEST.md` — finaler Build-Nachweis
- `provenance/v02/PRODUCTION.md` — Status `accepted`

### Deterministische QA

- `scripts/provenance_check.py` — Git-Blob-basierter Drift-/Invalidierungs-Guard
- `tests/test_provenance_check.py` — isolierter Upstream-Änderungstest
- `INVALIDATION_TEST.md` — **PASS**
- finale relevante CI: `Framework Validation` Run #32 / ID `33306864034` — **success**

Der Produktions-Rebuild-Test hat im realen Lauf einen tatsächlichen Driftfehler gefunden: Die erste HTML-Ausgabe enthielt einen älteren S3-Zwischenstand. Der Fehler wurde nicht übergangen. Nur das Produktionsartefakt wurde aus dem bereits G4-freigegebenen Manuskript neu gebaut; der G4-Manuskriptstand blieb unverändert. Der anschließende byte-genaue Rebuild war grün.

# Prüfung der 48 Acceptance Criteria

## A. Arbeitsweise vom Großen ins Kleine — PASS

1. **PASS** — Der v0.2-Lauf folgt `Buchidee → Bausteine → Ereignisse → Beats → Szenenkarten → Prosa`.
2. **PASS** — Bausteine, Events und Beats wurden jeweils horizontal für den gesamten Mini-Fall geschlossen, bevor tiefer gegangen wurde.
3. **PASS** — Die v0.2-Prosa begann erst nach vollständiger G2-Planung aller drei Szenen; der alte verkürzte v0.1-Pfad wurde als historische Testspur verworfen.
4. **PASS** — Alle notwendigen Zwischenergebnisse wurden im Repository gespeichert; kein für die Freigabe notwendiger Stand existiert nur im Chat.

## B. Human Gates — PASS

5. **PASS** — G0 Konzept, G1 Story-Architektur, G2 Prose Ready, G3 Prosa-Stil, G4 Manuskript und G5 Produktion wurden real verwendet.
6. **PASS** — Keine zusätzliche Human-Gate-Stufe zwischen Bausteinen/Events oder Beats/Szenenkarten.
7. **PASS** — Alle Gate-Records referenzieren konkrete Artefaktstände/Blobs.
8. **PASS** — Alle APPROVE-Entscheidungen wurden ausdrücklich vom Menschen im Chat erteilt.
9. **PASS** — Checker, Audit, CI und ChatGPT haben keinen Human Gate automatisch freigegeben.

## C. Story- und Szenenarchitektur — PASS

10. **PASS** — G1 bündelte Story Package, 6 Story Blocks, E001–E010, Figurenkern und Research Register.
11. **PASS** — Kein separater Gate zwischen Story Blocks und Events.
12. **PASS** — G2 bündelte alle 15 Beats, alle 3 Szenenkarten, 7 Character States und relevante Recherche.
13. **PASS** — Kein separater Gate zwischen Beats und Szenenkarten.
14. **PASS** — 3 Szenenkarten erreichten menschlich G2 = APPROVE.
15. **PASS** — Für S1–S3 war die Scene-Readiness-Frage positiv beantwortbar; die Prosa musste keine relevante Storyentscheidung neu erfinden.

## D. Figuren und Recherche als Querschnitt — PASS

16. **PASS** — Figurenkern/Zentralbeziehungen wurden vor G1 festgelegt; szenenspezifische Wissens-, Ziel- und Beziehungszustände lagen vor G2 vor.
17. **PASS** — R-001 war eine reale plotrelevante Recherchefrage.
18. **PASS** — Die Blockierlogik wurde explizit über `status` + `blocking_now` gehandhabt; R-001 wurde vor downstream-abhängiger Freigabe aufgelöst.
19. **PASS** — Kein zusätzlicher Research-Score und kein Research-Human-Gate eingeführt.

## E. Arbeitskontrollen und Review-Grenze — PASS

20. **PASS** — Pipeline-/Readiness-Checker prüfen mechanische Felder, IDs, Referenzen, Abdeckung und Status.
21. **PASS** — Semantische Eigenprüfungen wurden in G3/G4 ausdrücklich als Eigenprüfung und nicht als unabhängiger Review gekennzeichnet.
22. **PASS** — Inhaltliche Risiken wurden in den Human-Gates offengelegt; kein KI-Selbstreview wurde als unabhängige Freigabe ausgegeben.

## F. Prosa — PASS

23. **PASS** — Zu allen 3 G2-freigegebenen Szenen wurde echte Prosa erzeugt und committed.
24. **PASS** — 3/3 Drafts besitzen Provenienzrecords.
25. **PASS** — Die Provenienz verweist auf feste relevante Upstream-Blobs.
26. **PASS** — G3 wurde real mit S1+S2 durchlaufen, bevor S3 auf den Stilpfad skaliert wurde.
27. **PASS (bedingt nicht ausgelöst)** — Es gab kein G3-REWORK. Sprachliche Eigenkorrekturen im Batch und S3 änderten keine Storyentscheidung; eine stille Storyänderung fand nicht statt.

## G. Source of Truth und Invalidierung — PASS

28. **PASS** — Das G4-Manuskript besteht ausschließlich aus den aktuellen v0.2-Drafts; keine alte/stale v0.1-Prosa wurde übernommen.
29. **PASS** — Der isolierte Provenienztest belegt `accepted + geänderter Upstream → BLOCK`; erst sichtbares `stale` erlaubt `STALE_OK`.
30. **PASS** — Reine sprachliche Änderungen an S3 änderten keinen Story-/Character-State automatisch.
31. **PASS (kein Backtracking-Fall erforderlich)** — Es wurde keine neue Storyidee aus der Prosa übernommen. Die verbindliche Regel für echte Storyänderungen bleibt upstream-first mit erneuten betroffenen Gates.

## H. Qualität — PASS

32. **PASS** — Der bestehende Prosa-Audit lief auf dem vollständigen M1-Manuskript.
33. **PASS** — Vor G4: `FAIL = 0`.
34. **PASS** — Vor G4: `REVIEW = 0`; die 4 verbleibenden INFO-Signale wurden bewusst dokumentiert.
35. **PASS** — Der Abschluss behauptet keine literarische Gesamtqualität; M1 bleibt Arbeitsketten-/Integrationsnachweis.

## I. Produktion — PASS

36. **PASS** — Aus dem G4-Manuskript wurde reproduzierbar `FEHLALARM_v02.html` erzeugt.
37. **PASS** — G5 bezieht sich exakt auf Output-Blob `1add4d45fea3e552521041ae5d6120fba717d214`.
38. **PASS** — HTML ist echter abgeleiteter Output mit Dokumentstruktur, Titel-/Szenenstruktur, Typografie, Responsive- und A5-Print-CSS; keine umbenannte Markdown-Kopie.

## J. Fehler- und Abbruchfälle — PASS

39. **PASS** — Pipeline-/Provenienztests decken fehlende bzw. inkonsistente Upstream-Artefakte ab und blockieren deterministisch.
40. **PASS** — `test_open_blocking_research_blocks` belegt die blockierende Rechercheabhängigkeit; nicht blockierende Recherche bleibt zulässig.
41. **PASS** — Pipeline-Tests belegen, dass fehlende Human-Gates den Übergang blockieren (`test_missing_human_g1_blocks_even_if_g2_exists`, weitere Gate-Coverage-Tests).
42. **PASS** — Der alte verkürzte/unterbrochene M1-Anlauf wurde nicht als v0.2-Abschluss gewertet; nur committed gültige Zielartefakte zählen.
43. **PASS** — Der Provenienz-Guard blockiert stillen Drift; das kanonische Manuskript verwendet keine als stale/invalidated markierten Drafts.

## K. Gate-Batching / Skalierungsgrenze — PASS

44. **PASS** — M1 nutzte gebündelte G1-, G2-, G3-, G4- und G5-Review-Pakete.
45. **PASS** — `ARBEITSWEISE.md` dokumentiert ausdrücklich mehrere Review-Batches innerhalb derselben fachlichen Gate-Phase für große Romane.
46. **PASS** — `ARBEITSWEISE.md` hält ausdrücklich fest, dass die optimale Batch-Größe für v0.x noch nicht allgemein festgelegt ist.

## L. CI-Grenze — PASS

47. **PASS** — CI prüft nur deterministische Bestandteile: Tests, Referenzen, Readiness, Audit, Invalidierung und Build-Reproduzierbarkeit.
48. **PASS** — Kein M1-Nachweis benötigt LLM-API-Aufruf, Provider-Adapter, API-Key, Mock-Provider, Tokenzähler oder Kostenbudget.

# Offene Skalierungsfragen nach M1

Diese Punkte sind bewusst **kein M1-FAIL**, sondern Grenzen des Nachweises:

- optimale Review-Batch-Größe bei 40+ Szenen,
- Review-Ergonomie und Änderungskosten bei einem vollständigen Roman,
- Validität der Stil-/Qualitätsmechanismen über 70.000+ Wörter,
- Produktionspfade DOCX/PDF/KDP statt des minimalen HTML-Nachweises,
- Umfang und Nutzen zusätzlicher entkoppelter Red-Team-Reviews bei langen Manuskripten,
- welche Provenienzabhängigkeiten bei sehr großen Projekten automatisiert statt explizit gepflegt werden sollten.

`ARBEITSWEISE.md` dokumentiert bereits die zentrale Skalierungsregel: mehrere Review-Batches dürfen innerhalb derselben fachlichen Gate-Phase liegen; daraus entstehen keine künstlichen G2a/G2b/G2c-Prozessgates.

# Freeze

Mit diesem Bericht wird FEHLALARM zu:

`status: frozen_regression_fixture`

Der Testfall wird nicht als Geschichte weiterentwickelt. Änderungen sind nur noch zulässig, wenn ein Framework-Contract bewusst geändert wird, ein Framework-Bug einen Regressionstest benötigt oder ein sachlicher/Referenzfehler im Fixture korrigiert werden muss.

## Schluss

> **M1 beweist die Arbeitskette im Kleinen: vom Makro zur Mikroplanung, mit wenigen echten Human Gates, nachvollziehbarer Provenienz, sichtbarer Invalidierung und reproduzierbarer Produktion. M1 beweist noch nicht die Skalierbarkeit oder Gesamtqualität eines vollständigen Romans.**
