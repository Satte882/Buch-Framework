# Framework-Pipeline v0.2

Diese Datei definiert die End-to-End-Wirbelsäule des Buch-Frameworks. Die konkrete Arbeitsweise steht in `ARBEITSWEISE.md`; `ZIEL.md` bleibt die unveränderliche oberste Randbedingung.

> Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.

## Kernänderung gegenüber v0.1

v0.1 koppelte Entwicklungsebenen zu stark an Human Gates und sprang im M1-Testfall nach der Storyarchitektur zu schnell auf fertige Szenenkarten.

v0.2 trennt deshalb strikt:

- **Entwicklungstiefe:** Thema → Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten → Prosa.
- **Freigabetiefe:** nur sechs gebündelte Human-Gates G0–G5.

> **Viele Entwicklungsebenen, wenige menschliche Freigaben.**

## Verbindliche Entwicklungsrichtung

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten → Prosa → Gesamtqualität → Produktion`

Dabei gilt die Horizontalregel:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann systematisch tiefer gehen.

Das Framework soll nicht standardmäßig einzelne frühe Szenen bis zur Prosa fertigstellen, während spätere Teile noch auf Plotebene offen sind.

## Pipeline und Human Gates

| Phase | Interne Arbeitsartefakte | Human Gate | Gate schützt |
|---|---|---|---|
| Konzept | `BOOK_IDEA.md` / Konzeptartefakt | **G0 – Konzept** | Prämisse, Leitfrage, Leser-Versprechen, zentrale Nicht-Ziele |
| Story-Architektur | `STORY_PACKAGE.md`, vollständige Bausteine, vollständige Ereignisse/Sequenzen, Figurenkern, Rechercheabhängigkeiten | **G1 – Story-Architektur** | Gesamtkausalität, Konflikt, große Wendungen, Informationsarchitektur, Figurenkern |
| Szenen-Architektur | vollständige Beats, vollständige Szenenkarten, Character States, blockierende Rechercheentscheidungen | **G2 – Prose Ready** | ob beim Schreiben keine relevante Storyentscheidung mehr improvisiert werden muss |
| Prosa-Stichprobe | repräsentativer Prosa-Batch aus G2-freigegebenen Szenen | **G3 – Prosa-Stil** | Stil, Rhythmus, Erlebnisdichte, sichtbare KI-Prosa-Muster |
| Gesamtmanuskript | vollständige Prosa, Qualitätsreviews, Rework, Audit | **G4 – Manuskript** | inhaltliche und qualitative Gesamtfreigabe |
| Produktion | DOCX/PDF/KDP-/andere Produktionsausgaben | **G5 – Produktion** | konkreter finaler Produktionsstand |

Jeder Human Gate erlaubt nur `APPROVE`, `REWORK` oder `STOP` und bezieht sich auf konkrete Artefaktstände.

## Keine Gates zwischen jeder Arbeitsebene

Standardmäßig gibt es **keinen** separaten Human Gate zwischen:

- Bausteinen und Ereignissen/Sequenzen,
- Beats und Szenenkarten,
- globaler Figurenarbeit und szenenspezifischen Character States,
- dem Erfassen und Bearbeiten einzelner Recherchefragen.

Diese Zwischenstufen werden durch Arbeitskontrollen begleitet und gemeinsam im nächsten fachlich sinnvollen Gate bewertet.

Ein zusätzlicher Gate ist nur gerechtfertigt, wenn er eine konkrete irreversible Entscheidung schützt, die im nächsten gebündelten Gate zu spät käme.

## Arbeitskontrollen zwischen Gates

Deterministische bzw. mechanische Checks dürfen prüfen:

- Pflichtfelder,
- IDs und Referenzen,
- vollständige Zuordnung von Bausteinen → Ereignissen → Beats → Szenen,
- Character-State-Referenzen,
- Status blockierender Recherchefragen,
- Git-/Upstream-Referenzen,
- Invalidierungsstatus.

ChatGPT darf zusätzlich semantische Selbstprüfungen durchführen. Diese gelten **nicht als unabhängiger Review**. Inhaltliche Storyqualität wird im Human Gate und bei Bedarf durch einen bewusst entkoppelten Red-Team-Review bewertet.

## Figuren und Recherche als Querschnitt

Figuren und Recherche laufen über mehrere Entwicklungsebenen:

- Figurenkern und große Beziehungen werden in der Story-Architektur festgelegt.
- Wissensstände und Beziehungszustände werden bis zur Szenenarchitektur konkretisiert.
- Recherche beginnt bei sichtbarer Unsicherheit und wird nur dann blockierend, wenn ihre Antwort eine aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.

Austauschbare Oberflächendetails dürfen offen bleiben.

## Gate-Batching bei großen Romanen

Ein Human Gate ist eine **Freigabephase**, keine Pflicht zu einer einzigen riesigen Prüfsitzung.

Bei vielen Szenen darf G2 beispielsweise in mehrere Review-Batches aufgeteilt werden. Nach den Teilreviews folgt ein Gesamtcheck und ein fachlicher G2-Abschluss. Es werden dafür keine künstlichen zusätzlichen Gate-Typen eingeführt.

Die optimale Batch-Größe ist noch eine bekannte Skalierungsfrage und wird erst mit einem realen längeren Buch kalibriert.

## Prosa beginnt nach G2

Systematische Prosaerzeugung startet erst, wenn die Szenenarchitektur prose-ready ist.

Verbindliche Gate-Frage:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

G3 prüft danach zunächst einen repräsentativen Prosa-Batch. Erst nach erfolgreicher Stil-/Prosa-Freigabe wird auf das vollständige Manuskript skaliert.

## Backtracking

Wenn eine tiefere Ebene eine bessere oder notwendige Storyänderung sichtbar macht, wird nicht downstream improvisiert. Die Änderung wandert zuerst zur kanonischen Upstream-Ebene, betroffene Ableitungen werden `stale`/`invalidated`, anschließend werden nur die betroffenen Freigabephasen erneut durchlaufen.

## Deterministischer v0.2-Checker

`scripts/pipeline_check.py` und `config/pipeline_contract.yml` bilden den v0.2-Upstream-Pfad bis G2 mechanisch ab:

`BOOK_IDEA → STORY_PACKAGE/STORY_BLOCKS → EVENTS → BEATS → SCENE_PLAN/CHARACTER_STATE`

Der Checker arbeitet phasenweise: Erst nach einem mechanisch gültigen vorhandenen Human-Record der früheren Phase werden die Artefakte der nächsten Phase verpflichtend. Dadurch erzeugt ein G1-Check noch keine künstlichen G2-Fehler.

Der Checker prüft:

- Pflichtfelder und Versionsbezüge,
- Baustein→Event- und Event→Beat-Abdeckung,
- Beat→Szenen-Zuordnung und `beat_refs`,
- referenzierte Character States,
- Research-Referenzen,
- offene Recherche nur dann als Blocker, wenn `blocking_now: yes`,
- vorhandene menschliche Gate-Records G0, G1 und G2 sowie deren Artefaktumfang.

Er erzeugt keine Human-Entscheidung und bewertet keine Storyqualität. Historische Szenendateien außerhalb der aus `BEATS.md` abgeleiteten aktiven Szenenmenge werden nicht als v0.2-Abdeckung gewertet.

Ein vollständiger mechanisch konsistenter G0→G2-Lauf endet mit `READY_FOR_PROSE`. Das bedeutet ausschließlich, dass die deterministischen Verträge erfüllt sind und ein menschliches G2-`APPROVE` als Record vorhanden ist.

## Leitregel

> **Mehr interne Entwicklungstiefe, weniger externe Prozessschritte. Vom Großen ins Kleine, horizontal über das ganze Buch, Prosa zuletzt.**
