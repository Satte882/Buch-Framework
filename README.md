# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

**Jede weitere Änderung in diesem Repository muss auf dieses Ziel einzahlen.** Methoden, Architektur, Tools und Implementierungsdetails dürfen sich ändern; das Projektziel selbst nicht.

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## Betriebsmodell und Architekturleitplanken

Das Framework ist bewusst **chat-getrieben** und keine klassische LLM-Anwendung mit eigener API-Runtime.

Verbindlich sind:

- [`BETRIEBSMODELL.md`](BETRIEBSMODELL.md) – ChatGPT-Chat als generative Arbeits-/Orchestrierungsebene, GitHub als Source of Truth, Human Gates und minimaler Chat-Provenienzstandard,
- [`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) – kanonische Artefakte, Ableitungsrichtung, Backtracking und Invalidierung,
- [`KISS_LEITPLANKEN.md`](KISS_LEITPLANKEN.md) – `Artefakt + ChatGPT + Gate` vor zusätzlicher Infrastruktur; CI bleibt deterministisch,
- [`M1_ACCEPTANCE.md`](M1_ACCEPTANCE.md) – messbare Kriterien für den ersten vollständigen G0–G6-Testlauf.

Leitbild:

> **ChatGPT erzeugt und analysiert. GitHub hält den gültigen Stand. Der Mensch entscheidet. CI prüft nur das Deterministische.**

## End-to-End-Wirbelsäule

Die verbindliche Pipeline steht in [`FRAMEWORK_PIPELINE.md`](FRAMEWORK_PIPELINE.md):

`Buchidee → Story Package → Figuren-/Recherche-Basis → Szenenplanung → Scene Readiness → Prosa → Qualitätsprüfung → Produktion`

Jede Stufe besitzt ein konkretes Arbeitsartefakt und einen menschlichen Gate. Die Framework-Tiefe wird nur dort ausgebaut, wo sie nachweisbar Downstream-Rework spart oder eine irreversible Entscheidung schützt.

## Aktueller Status

### Realer G3→G4-Chat-Probe-Lauf

Der erste reale generative Übergang wurde unter `m1/prose_probe_normalfall/` durchgeführt:

- `SCENE_CONTEXT_PACKAGE.md` – feste, historisch freigegebene NORMALFALL-Szenenarchitektur als Input,
- `drafts/NF-01.01.01.md` – in ChatGPT neu erzeugter und direkt committeter Prosa-Draft,
- `provenance/NF-01.01.01.md` – Herkunft und feste Upstream-Referenzen,
- `G4_REVIEW_REQUEST.md` – vorbereitete menschliche Review-Anfrage.

Der Probe-Lauf simuliert **keinen** menschlichen Gate. Der Draft bleibt aktuell `draft`; `G4` wartet auf eine ausdrückliche menschliche Entscheidung.

### G0–G3 v0.1 – erste ausführbare Upstream-Kette

Die Pipeline von der Buchidee bis zu einer **für den menschlichen Scene-Readiness-Gate vorbereiteten ersten Szene** ist mechanisch ausführbar.

Vorhanden sind:

- `templates/BOOK_IDEA.md` – G0-Vertrag,
- `templates/STORY_PACKAGE.md` – G1-Vertrag,
- `templates/CHARACTERS.md` – minimale globale Figuren-Baseline,
- `templates/RESEARCH_REGISTER.md` – Recherche-Register; offene Recherche darf bestehen, solange sie die konkrete Szene nicht blockiert,
- `templates/CHARACTER_STATE.md` – szenenbezogener Figurenstatus,
- `templates/SCENE_PLAN.md` – Scene-Readiness-Vertrag,
- `templates/GATE_RECORD.md` – explizite menschliche Freigabe,
- `config/pipeline_contract.yml` – maschinenlesbarer G0–G2-Vertrag,
- `scripts/pipeline_check.py` – prüft Artefakte, Gate-Reihenfolge, Titel-/Versionskonsistenz, Character-State-Referenzen und Recherche-Referenzen,
- `tests/test_pipeline_check.py` – synthetischer End-to-End-Test von G0 bis `READY_FOR_G3`.

Der Checker erzeugt **keine** menschliche Freigabe. Ohne vorhandene `G0`, `G1` und `G2`-Records mit `decision: APPROVE`, `decided_by: human` und `open_blockers: no` wird die Kette blockiert. Eine mechanisch vollständige Szene endet nur bei `READY_FOR_G3`.

Aufruf für G0–G2:

```bash
python scripts/pipeline_check.py project
```

Aufruf bis zur ersten G3-fähigen Szene:

```bash
python scripts/pipeline_check.py project --scene scenes/S-001.md
```

Mögliche Ergebnisse:

- `BLOCK` – Upstream-Entscheidung, Gate oder Referenz fehlt beziehungsweise widerspricht sich.
- `READY_FOR_SCENE_PLANNING` – G0–G2 sind konsistent und menschlich freigegeben.
- `READY_FOR_G3` – zusätzlich ist die konkrete Szene mechanisch vollständig; G3 selbst bleibt eine menschliche Entscheidung.

### Scene Readiness v0.1

[`SCENE_READINESS.md`](SCENE_READINESS.md) definiert das Gate zwischen Szenenplanung und Prosa.

Die Priorität ist historisch belegt: Die NORMALFALL-Ausbau-Matrix dokumentierte nach bereits vollständiger Story 27.370 Wörter und einen Ausbauplan von 49.630 Wörtern, weil viele Szenen plot-komplett, aber auf Konflikt, Konsequenz, Figurenreaktion, Suspense und situatives Erleben zu stark verdichtet waren.

Die retrospektive Prüfung wurde bewusst nicht schönkalibriert: Kapitel 40 bleibt als bekannte False Negative im Korpus, weil seine Szenenkarte wahrscheinlich Scene Readiness bestanden hätte und trotzdem später deutlich mehr narratives Gewicht brauchte.

### Prosa-Audit v0.1 – Downstream-Qualitätsbaustein

Vorhanden sind:

- `PROSA_REGELMATRIX.md` – fachliche Source of Truth für Regel-Scope, Evidenz, Severity und Promotion,
- `config/prosa_rules.yml` – buchneutrale Prosa-Profil-Konfiguration,
- `scripts/prosa_audit.py` – Scanner ohne automatische Textänderungen,
- `tests/test_prosa_audit.py` – Unit-, Development- und Hold-out-Tests,
- `tests/corpus/normalfall_split.json` – festgeschriebener Dev/Hold-out-Split,
- `.github/workflows/prosa-audit.yml` – gemeinsame Framework-CI inklusive Vollmanuskript-Rauschtest gegen NORMALFALL.

Der Vollmanuskript-Rauschtest verhinderte, dass technisch korrekte, aber praktisch zu laute Strukturdetektoren als REVIEW-Regeln bestehen blieben: Stakkato und Dialog-Pingpong wurden nach 403 bzw. 268 Treffern auf INFO zurückgestuft.

Semantische Muster wie Erklär-Echo, sichtbare Methodikprosa und übermäßige rhetorische Symmetrie bleiben bewusst außerhalb mechanischer Entscheidungen. Ein späterer Chat-Kontextreview ist als manueller Freigabe-Schritt vorgesehen, nicht als CI- oder Auto-Rewrite-Schleife.

## Empirische Basis

Verbindliche Analysen und Korpora:

- `ANALYSE_NORMALFALL.md` – Entwicklungs-, Story-, Qualitäts- und Produktionsprozess
- `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md` – tiefe Analyse der KI-typischen Formulierungs-, Satzbau-, Rhythmus- und Erklärmuster
- `tests/corpus/normalfall_beispiele.md` – reale Vorher/Nachher-Korrekturen aus der Historie
- `tests/corpus/normalfall_kontrollbeispiele.md` – reale auffällige Stellen, die nach kontextueller Prüfung bestehen blieben
- `tests/corpus/normalfall_provenienz.md` – Herkunft und Bestandsprüfung der positiven Korpusbeispiele
- `tests/corpus/scene_readiness_normalfall.json` – retrospektive Scene-Readiness-Prüfung an acht Ausbau-Fällen

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren.**

Das Framework soll klare Story- und Qualitätsgates liefern, ohne zukünftige Bücher in dieselbe sichtbare Formel zu pressen.
