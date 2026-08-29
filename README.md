# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

**Jede weitere Änderung in diesem Repository muss auf dieses Ziel einzahlen.** Methoden, Architektur, Tools und Implementierungsdetails dürfen sich ändern; das Projektziel selbst nicht.

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher – insbesondere eine thematische Psychothriller-Reihe – reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## Aktueller Status

**Prosa-Audit v0.1 ist implementiert und automatisiert geprüft.**

Vorhanden sind:

- `PROSA_REGELMATRIX.md` – fachliche Source of Truth für Regel-Scope, Evidenz, Severity und Promotion,
- `config/prosa_rules.yml` – buchneutrale Prosa-Profil-Konfiguration,
- `scripts/prosa_audit.py` – dependency-freier Scanner ohne automatische Textänderungen,
- `tests/test_prosa_audit.py` – Unit-, Development- und Hold-out-Tests,
- `tests/corpus/normalfall_split.json` – festgeschriebener Dev/Hold-out-Split,
- `.github/workflows/prosa-audit.yml` – CI für Tests und Vollmanuskript-Rauschtest gegen NORMALFALL.

Der erste Vollmanuskript-Rauschtest war bewusst Teil der Validierung. Er zeigte, dass die ursprünglich als REVIEW geführten breiten Detektoren für Stakkato und Dialog-Pingpong auf dem finalen NORMALFALL-Manuskript zu viele Kandidaten erzeugten. Sie wurden deshalb **nicht künstlich auf NORMALFALL hochoptimiert**, sondern auf INFO zurückgestuft. Die Entscheidung und Messwerte stehen in `PROSA_REGELMATRIX.md`.

Semantische Muster wie Erklär-Echo, sichtbare Methodikprosa und übermäßige rhetorische Symmetrie sind weiterhin bewusst nicht mechanisch entschieden. Ein späterer LLM-Kontextreview ist als manueller Freigabe-Gate vorgesehen, nicht als CI- oder Auto-Rewrite-Schleife.

## Empirische Basis

Verbindliche Analysen und Korpora:

- `ANALYSE_NORMALFALL.md` – Entwicklungs-, Story-, Qualitäts- und Produktionsprozess
- `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md` – tiefe Analyse der KI-typischen Formulierungs-, Satzbau-, Rhythmus- und Erklärmuster
- `tests/corpus/normalfall_beispiele.md` – reale Vorher/Nachher-Korrekturen aus der Historie
- `tests/corpus/normalfall_kontrollbeispiele.md` – reale auffällige Stellen, die nach kontextueller Prüfung bestehen blieben
- `tests/corpus/normalfall_provenienz.md` – Herkunft und Bestandsprüfung der positiven Korpusbeispiele

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren.**

Das Framework soll klare Story- und Qualitätsgates liefern, ohne zukünftige Bücher in dieselbe sichtbare Formel zu pressen.
