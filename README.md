# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

**Jede weitere Änderung in diesem Repository muss auf dieses Ziel einzahlen.** Methoden, Architektur, Tools und Implementierungsdetails dürfen sich ändern; das Projektziel selbst nicht.

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## End-to-End-Wirbelsäule

Die verbindliche Pipeline steht in [`FRAMEWORK_PIPELINE.md`](FRAMEWORK_PIPELINE.md):

`Buchidee → Story Package → Figuren-/Recherche-Basis → Szenenplanung → Scene Readiness → Prosa → Qualitätsprüfung → Produktion`

Jede Stufe besitzt ein konkretes Arbeitsartefakt und einen menschlichen Gate. Die Framework-Tiefe wird ab jetzt nur dort ausgebaut, wo sie nachweisbar Downstream-Rework spart oder eine irreversible Entscheidung schützt.

## Aktueller Status

### Scene Readiness v0.1 – erster Upstream-Baustein

[`SCENE_READINESS.md`](SCENE_READINESS.md) definiert das Gate zwischen Szenenplanung und Prosa.

Vorhanden sind:

- `templates/SCENE_PLAN.md` – machine-checkbarer Szenenvertrag,
- `templates/CHARACTER_STATE.md` – minimaler szenenbezogener Figurenstatus,
- `templates/RESEARCH_REGISTER.md` – plotrelevante Recherche-Blocker,
- `templates/GATE_RECORD.md` – einheitliches Format für menschliche Freigaben,
- `config/scene_readiness.yml` – Pflichtfelder und Blocker,
- `scripts/scene_readiness.py` – dependency-freier Completeness-Checker,
- `tests/test_scene_readiness.py` – Regressionstests,
- `tests/corpus/scene_readiness_normalfall.json` – acht echte retrospektive NORMALFALL-Fälle.

Die Priorität ist historisch belegt: Die NORMALFALL-Ausbau-Matrix dokumentierte nach bereits vollständiger Story 27.370 Wörter und einen Ausbauplan von 49.630 Wörtern, weil viele Szenen plot-komplett, aber auf Konflikt, Konsequenz, Figurenreaktion, Suspense und situatives Erleben zu stark verdichtet waren.

Die retrospektive Prüfung wurde bewusst nicht schönkalibriert: Kapitel 40 bleibt als bekannte False Negative im Korpus, weil seine Szenenkarte wahrscheinlich Scene Readiness bestanden hätte und trotzdem später deutlich mehr narratives Gewicht brauchte.

### Prosa-Audit v0.1 – Downstream-Qualitätsbaustein

Vorhanden sind:

- `PROSA_REGELMATRIX.md` – fachliche Source of Truth für Regel-Scope, Evidenz, Severity und Promotion,
- `config/prosa_rules.yml` – buchneutrale Prosa-Profil-Konfiguration,
- `scripts/prosa_audit.py` – Scanner ohne automatische Textänderungen,
- `tests/test_prosa_audit.py` – Unit-, Development- und Hold-out-Tests,
- `tests/corpus/normalfall_split.json` – festgeschriebener Dev/Hold-out-Split,
- `.github/workflows/prosa-audit.yml` – CI für Tests und Vollmanuskript-Rauschtest gegen NORMALFALL.

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
