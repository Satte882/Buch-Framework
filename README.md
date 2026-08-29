# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

**Jede weitere Änderung in diesem Repository muss auf dieses Ziel einzahlen.** Methoden, Architektur, Tools und Implementierungsdetails dürfen sich ändern; das Projektziel selbst nicht.

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher – insbesondere eine thematische Psychothriller-Reihe – reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## Aktueller Status

**Phase 1 – Analysebasis vorhanden; Prosa-Audit v0.1 implementiert.**

Die bisherigen NORMALFALL-Analysen und realen Vorher/Nachher-/Kontrollbeispiele bilden die empirische Basis. Darauf aufbauend ist der erste lauffähige Framework-Baustein umgesetzt:

- `PROSA_REGELMATRIX.md` – fachliche Source of Truth für Regeln, Scope, Evidenz und Severity
- `config/prosa_rules.yml` – buchneutrales Prosa-Profil `de_anti_ki_prosa_v1`
- `scripts/prosa_audit.py` – deterministischer/heuristischer Scanner ohne automatische Textänderung
- `tests/test_prosa_audit.py` – Unit-, Development- und Hold-out-Tests
- `tests/corpus/normalfall_split.json` – feste Dev/Hold-out-Zuordnung mit Small-Sample-Regeln

### Prosa-Audit v0.1

Der Scanner unterscheidet:

- **FAIL** – nur deterministische, explizit konfigurierte Regelverletzungen; aktuell `sondern` im aktiven Prosa-Profil
- **REVIEW** – strukturelle Kandidaten wie Negationsketten, Stakkato oder Dialog-Pingpong; keine automatische Änderung
- **INFO** – deskriptive Signale wie Weichmacher- oder Filterwortdichte, solange die Korpuslage keinen belastbaren REVIEW-Schwellenwert trägt

Die kleinen Musterfamilien werden ausdrücklich nicht als statistisch „stark“ bezeichnet. Der Dev/Hold-out-Split wird nur dort sinnvoll genutzt, wo genügend Fälle vorhanden sind; bei sehr kleinen Gruppen bleiben Ergebnisse deskriptiv.

Der semantische LLM-Kontextreview ist **noch nicht implementiert**. Sein Trigger ist bereits festgelegt: manuell an Prosa-Freigabegates, niemals pro Commit und niemals als automatische Rewrite-Pipeline.

### Ausführen

```bash
python scripts/prosa_audit.py MANUSKRIPT.md
```

JSON-Report:

```bash
python scripts/prosa_audit.py MANUSKRIPT.md --format json --output prosa-audit.json
```

Tests:

```bash
python -m unittest discover -s tests -v
```

Der Scanner ist absichtlich dependency-frei. `config/prosa_rules.yml` verwendet JSON-Syntax, die zugleich gültiges YAML 1.2 ist.

## Verbindliche Analysen und Korpus

- `ANALYSE_NORMALFALL.md` – Entwicklungs-, Story-, Qualitäts- und Produktionsprozess
- `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md` – tiefe Analyse der KI-typischen Formulierungs-, Satzbau-, Rhythmus- und Erklärmuster inklusive `Nicht-X-sondern-Y`, Weichmacher, Stakkato, Erklär-Echos und Prosa-Regression
- `tests/corpus/normalfall_beispiele.md` – reale Vorher/Nachher-Korrekturen aus der Historie
- `tests/corpus/normalfall_kontrollbeispiele.md` – reale auffällige Stellen, die nach kontextueller Prüfung bestehen blieben
- `tests/corpus/normalfall_provenienz.md` – Herkunft und Bestandsprüfung der positiven Korpusbeispiele

Die Anti-KI-Prosa ist **kein optionaler Stilanhang**, sondern ein eigener Qualitätsbaustein des Frameworks. Regeln dürfen aus dem Korpus nur so weit automatisiert werden, wie die Evidenz das trägt.

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren.**

Das Framework soll klare Story- und Qualitätsgates liefern, ohne zukünftige Bücher in dieselbe sichtbare Formel zu pressen.
