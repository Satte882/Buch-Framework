# Framework-Pipeline v0.2

Diese Datei definiert die End-to-End-Wirbelsäule des Buch-Frameworks. Die konkrete Arbeitsweise steht in `ARBEITSWEISE.md`; die verbindliche Buch-Repository-Struktur in `PROJECT_STRUCTURE.md`.

> Aus einer Buchidee reproduzierbar ein veröffentlichungsreifes Manuskript entwickeln, indem KI die wiederholbaren Analyse-, Entwicklungs- und Prüfaufgaben übernimmt und der Mensch an den inhaltlich irreversiblen Entscheidungen bewusst freigibt.

## Kernprinzip

Das Framework trennt strikt:

- **Entwicklungstiefe:** Thema → Bausteine → Ereignisse/Sequenzen → Szenen → Beats → Prosa.
- **Freigabetiefe:** nur sechs gebündelte Human-Gates G0–G5.

> **Viele Entwicklungsebenen, wenige menschliche Freigaben.**

## Verbindliche Entwicklungsrichtung

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Szenen → Beats → Prosa → Gesamtqualität → Produktion`

Dabei gilt die Horizontalregel:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann systematisch tiefer gehen.

Die Ordnerstruktur bildet dieselbe Logik ab:

`Root/Meta → BAUSTEINE/Bxx → SZENEN/Sxxx → BEATS / CHARACTER_STATES → PROSA`

Events liegen beim jeweiligen Baustein. Prosa liegt bei der konkreten Szene und ist die unterste Ebene.

## Pipeline und Human Gates

| Phase | Interne Arbeitsartefakte | Human Gate | Gate schützt |
|---|---|---|---|
| Konzept | `BOOK_IDEA.md` / Konzeptartefakt | **G0 – Konzept** | Prämisse, Leitfrage, Leser-Versprechen, zentrale Nicht-Ziele |
| Story-Architektur | `STORY_PACKAGE.md`, vollständige Bausteine, vollständige Ereignisse/Sequenzen, Figurenkern, Rechercheabhängigkeiten | **G1 – Story-Architektur** | Gesamtkausalität, Konflikt, große Wendungen, Informationsarchitektur, Figurenkern |
| Szenen-Architektur | vollständige Szenen, vollständige Beats, Character States, blockierende Rechercheentscheidungen | **G2 – Prose Ready** | ob beim Schreiben keine relevante Storyentscheidung mehr improvisiert werden muss |
| Prosa-Stichprobe | repräsentativer Prosa-Batch aus G2-freigegebenen Szenen | **G3 – Prosa-Stil** | Stil, Rhythmus, Erlebnisdichte, sichtbare KI-Prosa-Muster |
| Gesamtmanuskript | vollständige Prosa, Qualitätsreviews, Rework, Audit | **G4 – Manuskript** | inhaltliche und qualitative Gesamtfreigabe |
| Produktion | DOCX/PDF/KDP-/andere Produktionsausgaben | **G5 – Produktion** | konkreter finaler Produktionsstand |

Jeder Human Gate erlaubt nur `APPROVE`, `REWORK` oder `STOP` und bezieht sich auf konkrete Artefaktstände.

## Keine Gates zwischen jeder Arbeitsebene

Standardmäßig gibt es **keinen** separaten Human Gate zwischen:

- Bausteinen und Ereignissen/Sequenzen,
- Ereignissen/Sequenzen und Szenen,
- Szenen und Beats,
- globaler Figurenarbeit und szenenspezifischen Character States,
- dem Erfassen und Bearbeiten einzelner Recherchefragen.

Diese Zwischenstufen werden durch Arbeitskontrollen begleitet und gemeinsam im nächsten fachlich sinnvollen Gate bewertet.

## Arbeitskontrollen zwischen Gates

Deterministische bzw. mechanische Checks dürfen prüfen:

- Pflichtfelder,
- IDs und Referenzen,
- vollständige Zuordnung von Bausteinen → Ereignissen → Szenen → Beats,
- Character-State-Referenzen,
- Status blockierender Recherchefragen,
- Git-/Upstream-Referenzen,
- Invalidierungsstatus.

ChatGPT darf zusätzlich semantische Selbstprüfungen durchführen. Diese gelten **nicht als unabhängiger Review**. Inhaltliche Storyqualität wird im Human Gate und bei Bedarf durch einen bewusst entkoppelten Fresh-Context-/Red-Team-Review bewertet.

## Figuren und Recherche als Querschnitt

Figuren und Recherche laufen über mehrere Entwicklungsebenen:

- Figurenkern und große Beziehungen werden in der Story-Architektur festgelegt.
- Wissensstände und Beziehungszustände werden bis zur Szenen-/Beat-Architektur konkretisiert.
- Recherche beginnt bei sichtbarer Unsicherheit und wird nur dann blockierend, wenn ihre Antwort eine aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.

Austauschbare Oberflächendetails dürfen offen bleiben.

## Gate-Batching bei großen Romanen

Ein Human Gate ist eine **Freigabephase**, keine Pflicht zu einer einzigen riesigen Prüfsitzung.

Bei vielen Szenen darf G2 in mehrere Review-Batches aufgeteilt werden. Nach den Teilreviews folgt ein Gesamtcheck und ein fachlicher G2-Abschluss. Es werden dafür keine künstlichen zusätzlichen Gate-Typen eingeführt.

## Prosa beginnt nach G2

Systematische Prosaerzeugung startet erst, wenn die Szenen-/Beat-Architektur prose-ready ist.

Verbindliche Gate-Frage:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

G3 prüft danach zunächst einen repräsentativen Prosa-Batch. Erst nach erfolgreicher Stil-/Prosa-Freigabe wird auf das vollständige Manuskript skaliert.

## Source of Truth und Projektlayout

Für neue echte Buchprojekte gilt `PROJECT_STRUCTURE.md`:

- Meta-Artefakte im Root,
- Bausteine und Events unter `BAUSTEINE/Bxx/`,
- Szenen unter dem zugehörigen Baustein,
- Beats/Character States/Prosa unter der zugehörigen Szene.

Globale Dateien wie `STORY_BLOCKS.md`, `EVENTS.md` und `BEATS.md` dürfen als **abgeleitete Index-/Checker-Sichten** existieren. Sie sind in hierarchischen Projekten keine zweite fachliche Source of Truth.

Historische M1/M2-Fixtures dürfen ihr flaches Layout behalten.

## Backtracking

Wenn eine tiefere Ebene eine bessere oder notwendige Storyänderung sichtbar macht, wird nicht downstream improvisiert. Die Änderung wandert zuerst zur kanonischen Upstream-Ebene, betroffene Ableitungen werden `stale`/`invalidated`, anschließend werden nur die betroffenen Freigabephasen erneut durchlaufen.

## Deterministischer v0.2-Checker

`scripts/pipeline_check.py` und `config/pipeline_contract.yml` bilden weiterhin den mechanischen Pfad bis G2 ab. Historische Fixtures nutzen dafür die flachen Aggregatdateien. Neue hierarchische Buchprojekte dürfen kompatible globale Indexsichten bereitstellen, solange die fachliche Source of Truth in der Hierarchie bleibt.

Der Checker bewertet keine Storyqualität und erzeugt keine Human-Entscheidung.

Ein vollständiger mechanisch konsistenter G0→G2-Lauf endet mit `READY_FOR_PROSE`. Das bedeutet ausschließlich, dass die deterministischen Verträge erfüllt sind und ein menschliches G2-`APPROVE` als Record vorhanden ist.

## Leitregel

> **Meta → Bausteine → Events → Szenen → Beats → Prosa. Mehr interne Entwicklungstiefe, wenige Gates, Prosa zuletzt.**
