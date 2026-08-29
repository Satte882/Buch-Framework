# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

**Jede weitere Änderung in diesem Repository muss auf dieses Ziel einzahlen.** Methoden, Architektur, Tools und Implementierungsdetails dürfen sich ändern; das Projektziel selbst nicht.

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## Betriebsmodell

Das reale Betriebsmodell steht in [`BETRIEBSMODELL.md`](BETRIEBSMODELL.md):

> **ChatGPT erzeugt und analysiert. GitHub hält den gültigen Stand. Der Mensch entscheidet. CI prüft nur das Deterministische.**

Kanonische Ebenen, Backtracking und Invalidierung sind in [`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) festgelegt. Neue Technik muss die Leitplanken aus [`KISS_LEITPLANKEN.md`](KISS_LEITPLANKEN.md) erfüllen.

## End-to-End-Wirbelsäule

Die verbindliche Pipeline steht in [`FRAMEWORK_PIPELINE.md`](FRAMEWORK_PIPELINE.md):

`Buchidee → Story Package → Figuren-/Recherche-Basis → Szenenplanung → Scene Readiness → Prosa → Qualitätsprüfung → Produktion`

Jede Stufe besitzt ein konkretes Arbeitsartefakt und einen menschlichen Gate. Die Framework-Tiefe wird nur dort ausgebaut, wo sie nachweisbar Downstream-Rework spart oder eine irreversible Entscheidung schützt.

Der erste vollständige Meilenstein wird gegen [`M1_ACCEPTANCE.md`](M1_ACCEPTANCE.md) abgenommen. **M1 beweist die Kette, nicht die Tiefe.**

## Aktueller Status

### G0–G3 v0.1 – erste ausführbare Upstream-Kette

Die Pipeline von der Buchidee bis zu einer **für den menschlichen Scene-Readiness-Gate vorbereiteten ersten Szene** ist jetzt mechanisch ausführbar.

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

### G3→G4 Chat-Prosa-Probe – realer REWORK-Pfad

Unter `m1/prose_probe_normalfall/` wird der erste reale Chat-/GitHub-Übergang von einer bereits realisierten NORMALFALL-Szenenarchitektur zu neu erzeugter Prosa getestet.

Revision 1 wurde menschlich mit **G4 = REWORK** bewertet. Die Entscheidung ist als Gate-Record gespeichert. Gründe:

- auffällig gleichförmiger Stakkato-Rhythmus,
- redundantes Nicht-Angriffs-Signal.

Die Nacharbeit wurde gezielt und ohne Storyänderung durchgeführt:

- vorher: 42 Prosaabsätze, davon 27 mit höchstens 7 Wörtern,
- Revision 2: 18 Prosaabsätze, davon 1 mit höchstens 7 Wörtern,
- redundantes Signal entfernt,
- `sondern`: 0.

Revision 2 ist erneut für G4 vorgelegt. Sie bleibt `draft`, bis eine neue menschliche Entscheidung `APPROVE | REWORK | STOP` vorliegt.

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

Semantische Muster wie Erklär-Echo, sichtbare Methodikprosa und übermäßige rhetorische Symmetrie bleiben bewusst außerhalb mechanischer Entscheidungen. Ein späterer LLM-Kontextreview ist als manueller Freigabe-Gate vorgesehen, nicht als CI- oder Auto-Rewrite-Schleife.

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
