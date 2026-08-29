# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher – insbesondere eine thematische Psychothriller-Reihe – reproduzierbar vom gesellschaftlichen Konflikt bis zur KDP-Datei entwickelt werden können.

## Aktueller Status

**Phase 0 – Analyse. Noch kein Framework-Build.**

Zuerst wird bewertet:

- was bei `NORMALFALL` tatsächlich funktioniert hat,
- was nur für dieses konkrete Buch gilt,
- was unnötige Komplexität erzeugt hat,
- welche Teile generalisiert werden müssen,
- welche Teile als Serienprofil sinnvoll sind,
- welche technischen Bausteine parametriert werden müssen,
- welche sprachlichen Muster aus den späten Leser-/Perplexity-/Anti-KI-Pässen verbindlich verhindert und geprüft werden müssen.

Verbindliche Analysen:

- `ANALYSE_NORMALFALL.md` – Entwicklungs-, Story-, Qualitäts- und Produktionsprozess
- `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md` – tiefe Analyse der KI-typischen Formulierungs-, Satzbau-, Rhythmus- und Erklärmuster inklusive `Nicht-X-sondern-Y`, Weichmacher, Stakkato, Erklär-Echos und Prosa-Regression

Die Anti-KI-Analyse ist **kein optionaler Stilanhang**, sondern Pflichtinput für Buch-Framework v0.1. Das spätere Framework benötigt dafür ein eigenes Prosa-Profil, konfigurierbare Hard-/Warnregeln, einen Pattern-Audit, einen kontextuellen Anti-Tick-Pass und ein eigenes Qualitätsgate vor Testlesern.

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren.**

Das Framework soll klare Story- und Qualitätsgates liefern, ohne zukünftige Bücher in dieselbe sichtbare Formel zu pressen.