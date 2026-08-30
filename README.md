# Buch-Framework

Dieses Repository extrahiert die **wiederverwendbare Entwicklungs- und Produktionslogik** aus `Satte882/Buch` (`NORMALFALL`).

## Verbindliches Projektziel

Das unveränderliche Projektziel steht in [`ZIEL.md`](ZIEL.md) und ist die oberste Randbedingung für alle weiteren Arbeiten:

> **Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.**

Ziel ist nicht, `NORMALFALL` zu kopieren. Ziel ist ein Framework, mit dem weitere eigenständige Bücher reproduzierbar von der Buchidee bis zum produktionsreifen Manuskript entwickelt werden können.

## Verbindliche Arbeitsweise

Die fachliche Arbeitsweise steht in [`ARBEITSWEISE.md`](ARBEITSWEISE.md):

> **Mehr interne Entwicklungstiefe, weniger externe Prozessschritte. Vom Großen ins Kleine, horizontal über das ganze Buch, Prosa zuletzt.**

Die normale Entwicklungsrichtung lautet:

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten → Prosa → Gesamtqualität → Produktion`

Dabei werden Entwicklungsebenen und Human Gates bewusst getrennt. Eine neue Datei oder Planungsebene erzeugt nicht automatisch einen neuen Freigabepunkt.

### Sechs Human-Gate-Phasen

1. **G0 – Konzept**
2. **G1 – Story-Architektur**: Story Package + Bausteine + Ereignisse/Sequenzen + Figurenkern + relevante Rechercheabhängigkeiten
3. **G2 – Prose Ready**: Beats + Szenenkarten + Character States + blockierende Recherche
4. **G3 – Prosa-Stil**: repräsentativer Prosa-Batch
5. **G4 – Manuskript**: vollständiger Text + Qualitätsarbeit
6. **G5 – Produktion**: konkretes Produktionsartefakt

Bei langen Büchern darf ein Gate aus mehreren Review-Batches bestehen. Dadurch wird Review-Last portioniert, ohne künstlich neue Gate-Typen zu erzeugen.

## Betriebsmodell

Das reale Betriebsmodell steht in [`BETRIEBSMODELL.md`](BETRIEBSMODELL.md):

> **ChatGPT erzeugt und analysiert. GitHub hält den gültigen Stand. Der Mensch entscheidet. CI prüft nur das Deterministische.**

Kanonische Ebenen, Backtracking und Invalidierung sind in [`SOURCE_OF_TRUTH.md`](SOURCE_OF_TRUTH.md) festgelegt. Neue Technik muss die Leitplanken aus [`KISS_LEITPLANKEN.md`](KISS_LEITPLANKEN.md) erfüllen.

Die verbindliche Pipeline steht in [`FRAMEWORK_PIPELINE.md`](FRAMEWORK_PIPELINE.md). Der erste vollständige Meilenstein wird gegen [`M1_ACCEPTANCE.md`](M1_ACCEPTANCE.md) abgenommen.

## Arbeitsartefakte v0.2

Vorhanden bzw. vorgesehen sind:

- `templates/BOOK_IDEA.md` – Konzept,
- `templates/STORY_PACKAGE.md` – Storykern und Makroarchitektur,
- `templates/STORY_BLOCKS.md` – dramaturgische Bausteine über das ganze Buch,
- `templates/EVENTS.md` – Ereignisse und optionale Sequenzgruppen,
- `templates/CHARACTERS.md` – globale Figuren-Baseline als Querschnitt,
- `templates/RESEARCH_REGISTER.md` – Recherche-Register als Querschnitt,
- `templates/BEATS.md` – Beat-Ebene vor Szenenkarten,
- `templates/CHARACTER_STATE.md` – szenenspezifischer Figurenstatus,
- `templates/SCENE_PLAN.md` – Szenenkarte / Prose-Readiness-Artefakt,
- `templates/GATE_RECORD.md` – explizite menschliche Freigabe.

## Wichtige Qualitätsgrenzen

### Selbstprüfung

ChatGPT darf mechanische und semantische Selbstprüfungen durchführen. Die semantische Selbstprüfung derselben KI ist jedoch **kein unabhängiger Review**. Inhaltliche Qualitätsrisiken gehören in den Human Gate und bei Bedarf in einen bewusst entkoppelten Red-Team-Review.

### Recherche

Eine offene Recherchefrage blockiert nur dann, wenn ihre Antwort eine **aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung** verändern kann. Für v0.x gibt es dafür bewusst keinen zusätzlichen Score und keinen eigenen Recherche-Gate.

### Prosa

Systematische Prosa beginnt erst nach G2. Die zentrale Prose-Readiness-Frage lautet:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

## Bestehende technische Bausteine

### Scene Readiness / Pipeline-Checker v0.1

`scripts/pipeline_check.py`, `config/pipeline_contract.yml` und die zugehörigen Tests bilden noch das ältere Gate-Mapping mit separatem Figuren-/Recherche-Gate ab. Sie bleiben bis zur Migration als **Legacy-v0.1-Checker** erhalten und sind für die neue fachliche Gate-Semantik nicht autoritativ.

Die Migration soll die v0.2-Arbeitsweise abbilden, ohne zusätzliche Runtime-, Provider- oder Agenten-Infrastruktur einzuführen.

### Prosa-Audit v0.1

Vorhanden sind:

- `PROSA_REGELMATRIX.md`,
- `config/prosa_rules.yml`,
- `scripts/prosa_audit.py`,
- `tests/test_prosa_audit.py`,
- NORMALFALL-Korpus und Vollmanuskript-Rauschtest.

Der Scanner entscheidet nicht selbst über literarische Qualität. Breite Strukturmuster wie Stakkato und Dialog-Pingpong sind nach dem Vollmanuskript-Test nur INFO; semantische Muster bleiben kontextuelle Review-Aufgabe.

## Empirische Basis

Verbindliche Analysen und Korpora:

- `ANALYSE_NORMALFALL.md`
- `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md`
- `tests/corpus/normalfall_beispiele.md`
- `tests/corpus/normalfall_kontrollbeispiele.md`
- `tests/corpus/normalfall_provenienz.md`
- `tests/corpus/scene_readiness_normalfall.json`

## Leitprinzip

> **Den Prozess wiederverwenden, nicht den Plot kopieren.**

Das Framework soll klare Story- und Qualitätsgates liefern, ohne zukünftige Bücher in dieselbe sichtbare Formel zu pressen.
