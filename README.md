# Buch-Framework

Dieses Repository enthält die **wiederverwendbare Entwicklungs- und Produktionslogik** für eigenständige Buchprojekte.

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md):

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

## Verbindliche Arbeitsweise

Die fachliche Arbeitsweise steht in [`ARBEITSWEISE.md`](ARBEITSWEISE.md), die verbindliche Buch-Repository-Struktur in [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md).

Die normale Entwicklungsrichtung lautet:

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Szenen → Beats → Prosa → Gesamtqualität → Produktion`

Dabei gilt:

> **Vom Groben ins Feine, horizontal über das ganze Buch, Prosa zuletzt.**

## Verbindliche Projektstruktur

Neue echte Buchprojekte werden nicht mit parallelen Top-Level-Ordnern für jede Planungsebene aufgebaut. Die Ordnerhierarchie folgt der fachlichen Ableitung:

```text
BUCH-REPO/
├── BOOK_IDEA.md
├── STORY_PACKAGE.md
├── CHARACTERS.md
├── RESEARCH_REGISTER.md
├── gates/
└── BAUSTEINE/
    └── Bxx/
        ├── BAUSTEIN.md
        ├── EVENTS.md
        └── SZENEN/
            └── Sxxx/
                ├── SZENE.md
                ├── BEATS.md
                ├── CHARACTER_STATES.md
                └── PROSA.md
```

**Meta-Ebene:** Buchidee, Gesamtarchitektur, Figuren, Research und Gates.  
**Story-Ebene:** Baustein → Events → Szene → Beats/States → Prosa.

Prosa ist die unterste Ebene und kein paralleler Arbeitsstrang.

Die vollständigen Regeln, einschließlich globaler Index-/Checker-Sichten, stehen in [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md).

## Sechs Human-Gate-Phasen

1. **G0 – Konzept**
2. **G1 – Story-Architektur**: Story Package + alle Bausteine + alle Ereignisse/Sequenzen + Figurenkern + relevante Rechercheabhängigkeiten
3. **G2 – Prose Ready**: vollständige Szenenlandschaft + Beats + Character States + blockierende Recherche
4. **G3 – Prosa-Stil**: repräsentativer Prosa-Batch
5. **G4 – Manuskript**: vollständiger Text + Qualitätsarbeit
6. **G5 – Produktion**: konkretes Produktionsartefakt

Bei langen Büchern darf ein Gate aus mehreren Review-Batches bestehen. Dadurch wird Review-Last portioniert, ohne künstlich neue Gate-Typen zu erzeugen.

## Betriebsmodell

Das reale Betriebsmodell steht in [`BETRIEBSMODELL.md`](BETRIEBSMODELL.md):

> **ChatGPT erzeugt und analysiert. GitHub hält den gültigen Stand. Der Mensch entscheidet. CI prüft nur das Deterministische.**

Kanonische Ebenen, Backtracking und Invalidierung sind in [`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) festgelegt. Neue Technik muss die Leitplanken aus [`KISS_LEITPLANKEN.md`](KISS_LEITPLANKEN.md) erfüllen.

Die verbindliche Pipeline steht in [`FRAMEWORK_PIPELINE.md`](FRAMEWORK_PIPELINE.md).

## Arbeitsartefakte

Meta-/Querschnittsartefakte:

- `templates/BOOK_IDEA.md`
- `templates/STORY_PACKAGE.md`
- `templates/CHARACTERS.md`
- `templates/RESEARCH_REGISTER.md`
- `templates/GATE_RECORD.md`

Story-/Szenenartefakte werden in neuen echten Buchprojekten gemäß `PROJECT_STRUCTURE.md` verschachtelt:

- `BAUSTEIN.md`
- `EVENTS.md`
- `SZENE.md`
- `BEATS.md`
- `CHARACTER_STATES.md`
- `PROSA.md`

Historische M1/M2-Fixtures dürfen ihr flaches Testlayout behalten.

## Globale Index-/Checker-Sichten

Für CI, Reviews oder Kompatibilität dürfen zusätzlich globale Dateien wie `STORY_BLOCKS.md`, `EVENTS.md` oder `BEATS.md` existieren.

In einem hierarchischen echten Buchprojekt sind sie **abgeleitete Gesamtansichten**, nicht die fachliche Source of Truth. Änderungen erfolgen zuerst in der verschachtelten Storystruktur; globale Sichten werden danach aktualisiert.

Der bestehende Pipeline-Checker v0.2 nutzt für die historischen Fixtures weiterhin diese Aggregatverträge. Das ändert nicht die verbindliche Projektstruktur neuer Buchprojekte.

## Wichtige Qualitätsgrenzen

### Selbstprüfung

ChatGPT darf mechanische und semantische Selbstprüfungen durchführen. Die semantische Selbstprüfung derselben KI ist jedoch **kein unabhängiger Review**. Bei hohem semantischem Risiko wird ein bewusst entkoppelter Fresh-Context-/Red-Team-Review verwendet.

### Recherche

Eine offene Recherchefrage blockiert nur dann, wenn ihre Antwort eine **aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung** verändern kann.

### Prosa

Systematische Prosa beginnt erst nach G2. Die zentrale Prose-Readiness-Frage lautet:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

## Bestehende technische Bausteine

Vorhanden sind unter anderem:

- Pipeline-/Scene-Readiness-Checker,
- Provenienz-/Invalidierungsprüfung,
- Prosa-Audit,
- Review-Templates,
- Fresh-Context-Semantic-Review-Protokoll.

Diese Technik dient dem Prozess. Sie darf die fachliche Ableitungshierarchie nicht umkehren.

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren. Meta → Bausteine → Events → Szenen → Beats → Prosa.**
