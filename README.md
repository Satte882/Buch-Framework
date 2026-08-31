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

Aus dem Real-Pilot `ABWEICHUNG` gilt zusätzlich:

> **Whole-Book-Muster vor Vollprosa prüfen; Raw-Reviews vor Rework adjudizieren.**

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
3. **G2 – Prose Ready**: vollständige Szenenlandschaft + Beats + Character States + blockierende Recherche **+ Whole-Book Scene-Shape Review**
4. **G3 – Prosa-Stil**: 2–3 repräsentative Einzelszenen **+ zusammenhängender Mittelteil-Run von mindestens 6 Szenen**
5. **G4 – Manuskript**: vollständiger Text + Qualitätsarbeit + unabhängige Reviews **+ Finding-Adjudikation**
6. **G5 – Produktion**: konkretes Produktionsartefakt

Bei langen Büchern darf ein Gate aus mehreren Review-Batches bestehen. Dadurch wird Review-Last portioniert, ohne künstlich neue Gate-Typen zu erzeugen.

### Titel- und Kapitelbenennung vor G5

Nach der inhaltlichen G4-Freigabe und vor dem finalen G5-Build wird das fertige Buch als Produkt benannt. Der verbindliche Ablauf steht in [`TITLE_AND_CHAPTER_NAMING.md`](TITLE_AND_CHAPTER_NAMING.md).

Kernlogik:

- Buchtitel, formaler Untertitel und Leitsatz/Tagline werden ausdrücklich getrennt.
- interne Szenennamen sind nur Kandidaten für leserseitige Kapitelüberschriften.
- Kapitel werden zuerst **lokal** treffend benannt und danach in einem **Whole-Book-Titelpass** als vollständige Folge auf Rhythmus, Wiederholung, Spoiler und dramaturgischen Verlauf optimiert.
- dafür wird kein zusätzliches Human-Gate eingeführt; das freigegebene Titelpaket gehört zu G5.

## Whole-Book Scene-Shape vor G2

Eine Szene kann einzeln prose-ready sein und trotzdem in einer monotonen Gesamtfolge liegen. Deshalb wird vor G2 die vollständige Szenenfolge zusätzlich nach ihrem dominanten **Primary Dramatic Carrier** betrachtet.

Beispiele:

- clinical_action
- personal_confrontation
- solo_analysis
- data_review
- governance_design
- audit_investigation
- relationship_scene
- implementation_test
- aftermath
- resource_conflict

Die Klassifikation ist eine **Review-Projektion**, keine neue kanonische Pflichtdatei.

Warnsignale wie mehr als zwei gleiche Carrier hintereinander oder eine starke Häufung von Meeting-/Review-/Governance-Szenen lösen **keinen automatischen Blocker** aus. Sie verlangen eine semantische Prüfung der konkreten Ermüdungs-/Redundanzwirkung.

Details: [`SCENE_READINESS.md`](SCENE_READINESS.md) und [`REVIEW_TEMPLATE.md`](REVIEW_TEMPLATE.md).

## G3 prüft auch Sequenzrhythmus

Drei isolierte Vorzeigeszenen können manuskriptweite Wiederholungsmuster übersehen.

Deshalb liest G3 bei längeren Romanen zusätzlich einen **zusammenhängenden Mittelteil-Run von mindestens 6 Szenen** und prüft dort unter anderem:

- Dialogrhythmus über Szenengrenzen,
- wiederkehrende Szenenchoreografie,
- Expositionsdichte,
- Übergangs-/Schlussmechaniken,
- Verhältnis von Handlung, Analyse, Beziehung und Konsequenz.

## Review-Adjudikation

Ein Fresh-Context-/Red-Team-Review ist ein **Befundlieferant**, kein automatischer Gate-Entscheider.

Nach dem Review werden Findings gegen den tatsächlich geprüften Target adjudiziert:

- Evidenz stimmt?
- Severity trägt?
- kleinste Rework-Ebene korrekt?
- Widerspruch zu spezifischerem Review?
- bewusster Trade-off oder echter Fehler?

Nur **bestätigte** Blocker/Major-Findings blockieren den nächsten Human Gate.

Stop-Regeln:

`repeated manuscript-level major → inspect scene architecture → controlled G2 backtrack`

`raw finding → adjudicate evidence → rework only if confirmed`

Details: [`SEMANTIC_REVIEW_PROTOCOL.md`](SEMANTIC_REVIEW_PROTOCOL.md).

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

Zusätzlich muss die Szenenfolge auf Whole-Book-Ebene ausreichend variiert sein.

## Bestehende technische Bausteine

Vorhanden sind unter anderem:

- Pipeline-/Scene-Readiness-Checker,
- Provenienz-/Invalidierungsprüfung,
- Prosa-Audit,
- Review-Templates,
- Fresh-Context-Semantic-Review-Protokoll,
- Titel-/Untertitel-/Kapitelbenennungs-Workflow.

Diese Technik dient dem Prozess. Sie darf die fachliche Ableitungshierarchie nicht umkehren.

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren. Meta → Bausteine → Events → Szenen → Beats → Prosa.**