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
| Szenen-Architektur | vollständige Szenen, vollständige Beats, Character States, blockierende Rechercheentscheidungen | **G2 – Prose Ready** | ob beim Schreiben keine relevante Storyentscheidung mehr improvisiert werden muss **und ob die Szenenfolge als Ganzes ausreichend unterschiedliche dramaturgische Träger besitzt** |
| Prosa-Stichprobe | repräsentativer Prosa-Batch aus G2-freigegebenen Szenen | **G3 – Prosa-Stil** | Stil, Rhythmus, Erlebnisdichte, sichtbare KI-Prosa-Muster **auch über mehrere aufeinanderfolgende Szenen** |
| Gesamtmanuskript | vollständige Prosa, Qualitätsreviews, Rework, Adjudikation, **finaler horizontaler Prosa-/Rhythmuspass**, Regression/Fresh-Context-Check | **G4 – Manuskript** | inhaltliche und qualitative Gesamtfreigabe des tatsächlich finalisierten Manuskript-Snapshots |
| Produktion | DOCX/PDF/KDP-/andere Produktionsausgaben | **G5 – Produktion** | konkreter finaler Produktionsstand |

Jeder Human Gate erlaubt nur `APPROVE`, `REWORK` oder `STOP` und bezieht sich auf konkrete Artefaktstände.

## Keine Gates zwischen jeder Arbeitsebene

Standardmäßig gibt es **keinen** separaten Human Gate zwischen:

- Bausteinen und Ereignissen/Sequenzen,
- Ereignissen/Sequenzen und Szenen,
- Szenen und Beats,
- globaler Figurenarbeit und szenenspezifischen Character States,
- dem Erfassen und Bearbeiten einzelner Recherchefragen,
- Gesamtmanuskript-Review und finalem Prosa-/Rhythmuspass.

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

## Whole-Book Scene-Shape vor G2

Der ABWEICHUNG-Pilot hat gezeigt: Viele Szenen können einzeln korrekt und prose-ready sein, während ihre Summe monoton wirkt, weil zu viele Storyfunktionen über denselben dramaturgischen Träger erzählt werden.

Deshalb gehört vor G2 zusätzlich ein **Whole-Book Scene-Shape Review** zur Szenen-Architektur.

Für jede Szene wird im Review ein `Primary Dramatic Carrier` klassifiziert. Diese Klassifikation darf als nicht-kanonische Review-Projektion geführt werden; sie benötigt keine zusätzliche Pflichtdatei.

Beispielklassen:

- `clinical_action`
- `resource_conflict`
- `personal_confrontation`
- `solo_analysis`
- `data_review`
- `governance_design`
- `audit_investigation`
- `relationship_scene`
- `implementation_test`
- `aftermath`

Die konkrete Taxonomie ist zweitrangig. Entscheidend ist die Verteilung über das Buch.

### Review-Heuristiken

Folgende Werte sind **Warnsignale, keine automatischen Romanregeln**:

- mehr als 2 direkt aufeinanderfolgende Szenen mit praktisch demselben Primary Carrier,
- mehr als 4 Meeting-/Review-/Governance-/Data-Discussion-Szenen in einem Fenster von 8 Szenen,
- mehrere neue Regel-/Governance-Stufen hintereinander, ohne dass Anwendung, Folge, Konflikt oder Beziehung dazwischen erlebbar wird,
- wiederholt dieselbe Erkenntnismechanik über mehrere Szenen, obwohl die Storyinformation jeweils neu ist.

Eine Überschreitung blockiert G2 nicht mathematisch. Sie verlangt eine bewusste Prüfung der Ermüdungs-/Redundanzwirkung. Nur ein belastbarer semantischer Befund führt zu `REWORK`.

Zusätzliche G2-Frage:

> **Ist die Szenenfolge als Leseerlebnis ausreichend variiert, oder wiederholt die Architektur über längere Strecken denselben dramaturgischen Träger?**

## Figuren und Recherche als Querschnitt

Figuren und Recherche laufen über mehrere Entwicklungsebenen:

- Figurenkern und große Beziehungen werden in der Story-Architektur festgelegt.
- Wissensstände und Beziehungszustände werden bis zur Szenen-/Beat-Architektur konkretisiert.
- Recherche beginnt bei sichtbarer Unsicherheit und wird nur dann blockierend, wenn ihre Antwort eine aktuell zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.

Austauschbare Oberflächendetails dürfen offen bleiben.

## Gate-Batching bei großen Romanen

Ein Human Gate ist eine **Freigabephase**, keine Pflicht zu einer einzigen riesigen Prüfsitzung.

Bei vielen Szenen darf G2 in mehrere Review-Batches aufgeteilt werden. Nach den Teilreviews folgt ein Gesamtcheck und ein fachlicher G2-Abschluss. Dieser Gesamtcheck umfasst ausdrücklich auch die Scene-Shape-Verteilung über Batch-Grenzen hinweg. Es werden dafür keine künstlichen zusätzlichen Gate-Typen eingeführt.

## Prosa beginnt nach G2

Systematische Prosaerzeugung startet erst, wenn die Szenen-/Beat-Architektur prose-ready ist.

Verbindliche Gate-Fragen:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

und auf Whole-Book-Ebene:

> **Sind die geplanten Szenenträger ausreichend variiert, damit nicht erst im Vollmanuskript eine strukturelle Monotonie sichtbar wird?**

## G3 prüft Einzelstil und Sequenzrhythmus

G3 darf nicht ausschließlich aus isolierten Vorzeigeszenen bestehen.

Standard für längere Romane:

- 2–3 repräsentative Einzelszenen für unterschiedliche Prosa-Anforderungen,
- **zusätzlich ein zusammenhängender Mittelteil-Run von mindestens 6 aufeinanderfolgenden Szenen**.

Der zusammenhängende Run prüft insbesondere:

- Dialogrhythmus über Szenengrenzen,
- Wiederholung von Meeting-/Review-Choreografien,
- Expositionsdichte,
- wiederkehrende Übergangs-/Schlussmechaniken,
- Wechsel zwischen Handlung, Analyse, Beziehung und Konsequenz.

Erst nach erfolgreicher G3-Freigabe wird auf das vollständige Manuskript skaliert.

## G4 endet mit einem finalen horizontalen Prosa-/Rhythmuspass

Ein erfolgreicher Gesamtmanuskript-Review allein garantiert noch nicht, dass die sprachliche Oberfläche frei von über das Buch verteilten Produktionsformeln ist. `NORMALFALL` hat gezeigt, dass genau am Ende noch wiederkehrende Satzbau-, Dialog- und Erklärmuster sichtbar werden können, obwohl jede Einzelstelle lokal funktioniert.

Deshalb ist vor dem finalen G4-Freeze der Ablauf aus [`FINAL_PROSE_RHYTHM_PASS.md`](FINAL_PROSE_RHYTHM_PASS.md) verbindlich:

1. Baseline-Audit des vollständigen Manuskripts;
2. horizontale semantische Prüfung von Dialog-Pingpong, Stakkato, Kontrast-/Negationsmustern, Erklär-Echos, Filterformulierungen, Mikro-Choreografie, Methodik-/Beweisführungsprosa und Symmetrie;
3. chirurgisches, kontextuelles Rework ohne stille Storyänderung;
4. Regression gegen Szenenfolge, Story-Anker und Hard Guards;
5. Fresh-Context-Lesecheck von Opening, zusammenhängendem Mittelteil und Finale/Nachhall;
6. erst dann G4-Freeze auf den neuen Manuskript-Snapshot.

Für `de_anti_ki_prosa_v1` sind insbesondere `sondern = 0` und `— = 0` deterministische Hard Guards.

Der Pass ist **kein neues Gate**. Er schließt die Qualitätsarbeit innerhalb von G4 ab.

## Review ist Befundlieferung, Gate ist Entscheidung

Ein Fresh-Context-/Red-Team-Review liefert unabhängige Findings, aber **keine unanfechtbare Gate-Entscheidung**.

Nach jedem relevanten Review werden Findings dispositioniert:

- Evidenz gegen den tatsächlich geprüften Target verifizieren,
- Severity prüfen,
- kleinste notwendige Rework-Ebene bestimmen,
- widersprüchliche Reviews ausdrücklich adjudizieren,
- bewusst akzeptierte Trade-offs dokumentieren.

Nur **bestätigte** Blocker/Major-Findings blockieren den nächsten Human Gate. Ein Raw-Review-Urteil wie `REWORK_REQUIRED` darf nicht automatisch eine Rework-Schleife auslösen, wenn die zugrunde liegende Evidenz nicht trägt.

## Backtracking und Stop-Regel

Wenn eine tiefere Ebene eine bessere oder notwendige Storyänderung sichtbar macht, wird nicht downstream improvisiert. Die Änderung wandert zuerst zur kanonischen Upstream-Ebene, betroffene Ableitungen werden `stale`/`invalidated`, anschließend werden nur die betroffenen Freigabephasen erneut durchlaufen.

Zusätzlich gilt aus dem ABWEICHUNG-Pilot:

> `repeated manuscript-level major → inspect scene architecture → controlled G2 backtrack`

Wenn nach einem reinen Prosa-Rework derselbe Scene-Repetition-/Pacing-Major erneut **bestätigt** wird, folgt kein weiterer bloßer Satzprosa-Pass auf unveränderter Szenenarchitektur.

Umgekehrt gilt gegen Reviewer-Overfitting:

> `raw finding → adjudicate evidence → rework only if confirmed`

### Reines Prosa-Rework nach G4/G5

Wird nach einer G4- oder G5-Freigabe ein relevantes Problem ausschließlich in Satzbau, Rhythmus, Dialogtakt oder anderer Prosaoberfläche bestätigt, gilt:

- G2/G3 bleiben gültig, solange Story-, Szenen- und Beat-Architektur unangetastet bleiben;
- G4 wird für den neuen Manuskript-Snapshot wieder geöffnet;
- vorhandene G5-Artefakte werden `stale`;
- nach bestandenem finalem Prosa-/Rhythmuspass und Regression wird G4 erneut menschlich freigegeben;
- G5 wird anschließend deterministisch aus genau diesem neuen G4-Snapshot neu gebaut.

Damit wird weder unnötig bis zur Storyarchitektur zurückgesprungen noch ein veraltetes Produktionsartefakt fälschlich als final geführt.

## Source of Truth und Projektlayout

Für neue echte Buchprojekte gilt `PROJECT_STRUCTURE.md`:

- Meta-Artefakte im Root,
- Bausteine und Events unter `BAUSTEINE/Bxx/`,
- Szenen unter dem zugehörigen Baustein,
- Beats/Character States/Prosa unter der zugehörigen Szene.

Globale Dateien wie `STORY_BLOCKS.md`, `EVENTS.md` und `BEATS.md` dürfen als **abgeleitete Index-/Checker-Sichten** existieren. Sie sind in hierarchischen Projekten keine zweite fachliche Source of Truth.

Für den finalen Prosa-/Rhythmuspass gilt entsprechend: Änderungen erfolgen zuerst in den szenenspezifischen `PROSA.md`-Quellen; ein konsolidiertes Manuskript wird danach neu erzeugt.

Historische M1/M2-Fixtures dürfen ihr flaches Layout behalten.

## Deterministischer v0.2-Checker

`scripts/pipeline_check.py` und `config/pipeline_contract.yml` bilden weiterhin den mechanischen Pfad bis G2 ab. Historische Fixtures nutzen dafür die flachen Aggregatdateien. Neue hierarchische Buchprojekte dürfen kompatible globale Indexsichten bereitstellen, solange die fachliche Source of Truth in der Hierarchie bleibt.

Der Checker bewertet keine Storyqualität, keine Scene-Shape-Ermüdung und erzeugt keine Human-Entscheidung.

Ein vollständiger mechanisch konsistenter G0→G2-Lauf endet mit `READY_FOR_PROSE`. Das bedeutet ausschließlich, dass die deterministischen Verträge erfüllt sind und ein menschliches G2-`APPROVE` als Record vorhanden ist.

## Leitregel

> **Meta → Bausteine → Events → Szenen → Beats → Prosa. Mehr interne Entwicklungstiefe, wenige Gates, Prosa zuletzt – aber Whole-Book-Verteilung und finale Prosaoberfläche horizontal prüfen.**