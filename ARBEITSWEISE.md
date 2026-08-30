# Arbeitsweise – vom Großen ins Kleine

## Zweck

Dieses Dokument definiert die verbindliche Arbeitsweise des Buch-Frameworks. Es konkretisiert `ZIEL.md`, ohne das dort festgelegte Projektziel zu verändern.

> **Viele Entwicklungsebenen, wenige menschliche Freigaben.**

Das Framework entwickelt Bücher bewusst **vom Großen ins Kleine**. Eine feinere Entwicklungsebene erzeugt nicht automatisch einen neuen Human Gate.

## 1. Verbindliche Entwicklungsebenen

Die normale Arbeitsrichtung lautet:

`Thema / Buchidee → dramaturgische Bausteine → Ereignisse / Sequenzen → Beats → Szenenkarten → Prosa`

Danach folgen Gesamtqualitätsprüfung und Produktion.

### Horizontal vor vertikal

Jede Ebene wird zuerst **über das gesamte Buch** ausreichend geschlossen, bevor die nächste Ebene systematisch ausgebaut wird.

Beispiel:

1. alle dramaturgischen Bausteine des Buchs,
2. dann alle Ereignisse / Sequenzen,
3. dann alle Beats,
4. dann alle Szenenkarten,
5. erst danach Prosa.

Es ist ausdrücklich nicht der Standard, Szene 1 bis zur fertigen Prosa auszubauen, während spätere Teile des Buchs noch nur grob geplant sind.

**Grund:** Je später eine Storyentscheidung geändert wird, desto teurer ist das Downstream-Rework. Die horizontale Entwicklung macht Widersprüche, Lücken und Fehlgewichtungen sichtbar, bevor sie in Prosa vervielfacht werden.

## 2. Entwicklungsebenen sind keine Gate-Ebenen

Ein Human Gate schützt eine **irreversible oder teuer rückholbare Entscheidung**. Er existiert nicht, weil eine neue Markdown-Datei oder Planungsebene entstanden ist.

Für v0.x gelten sechs Freigabephasen:

| Gate | Mensch entscheidet über | Vor dem Gate intern entwickelte Ebenen |
|---|---|---|
| **G0 – Konzept** | Thema, Prämisse, Leitfrage, Leser-Versprechen, zentrale Nicht-Ziele | Buchidee / Konzept |
| **G1 – Story-Architektur** | ob die Gesamtgeschichte trägt | Story Package, alle Bausteine, alle Ereignisse/Sequenzen, Figurenkern, relevante Rechercheabhängigkeiten |
| **G2 – Prose Ready** | ob die Geschichte vollständig genug für Prosa geplant ist | alle Beats, alle Szenenkarten, Character States, für diese Planung blockierende Recherche |
| **G3 – Prosa-Stil** | ob ein repräsentativer Prosa-Batch sprachlich und erzählerisch trägt | Prosa-Stichprobe aus freigegebenen Szenenkarten |
| **G4 – Manuskript** | ob das Gesamtmanuskript inhaltlich und qualitativ abgenommen wird | vollständige Prosa, Reviews, Rework, Qualitätsprüfungen |
| **G5 – Produktion** | ob das konkrete Produktionsartefakt freigegeben wird | DOCX/PDF/KDP- bzw. andere Produktionsausgaben |

Zwischen **Bausteinen → Ereignissen/Sequenzen** und **Beats → Szenenkarten** gibt es standardmäßig keinen separaten Human Gate.

## 3. Wenige Gates bedeutet nicht wenig Kontrolle

Zwischen zwei Human Gates darf ChatGPT Arbeitskontrollen durchführen. Dabei wird klar zwischen mechanischer und semantischer Kontrolle unterschieden.

### Mechanische / deterministische Kontrolle

Geeignet für automatische oder Chat-gestützte Checks:

- Pflichtfelder vorhanden,
- IDs und Referenzen stimmen,
- alle Bausteine sind durch Ereignisse abgedeckt,
- alle Ereignisse besitzen nachgelagerte Beats,
- Character-State-Referenzen sind vorhanden,
- keine bekannte blockierende Rechercheabhängigkeit ist offen,
- Upstream-Referenzen sind aktuell.

### Inhaltliche Selbstprüfung

ChatGPT darf eigene Entwürfe auf Kausalität, Konflikt, Informationslogik oder Figurenkonsistenz prüfen. Diese Prüfung ist jedoch **keine unabhängige Qualitätssicherung**.

> Dieselbe KI, die ein Artefakt erzeugt hat, ersetzt durch ihre Selbstprüfung weder den Human Gate noch einen bewusst entkoppelten Red-Team-Review.

Format- und Konsistenzchecks dürfen deshalb deterministisch blockieren. Inhaltliche Fragen wie Strohmann-Konflikt, Deus-ex-machina, schwacher Reversal oder unglaubwürdige Motivation werden spätestens im gebündelten Human Gate bzw. in einem dafür vorgesehenen Red-Team-Review bewertet.

## 4. Figuren und Recherche sind Querschnittsarbeit

Figurenentwicklung und Recherche sind keine isolierten linearen Stufen mit automatisch eigenem Gate.

### Figuren

- Figurenkern und zentrale Beziehungen werden in der Story-Architektur entwickelt.
- Wissensgrenzen und Zustände werden mit zunehmender Tiefe konkretisiert.
- Szenenspezifische Zustände gehören spätestens vor G2 in `CHARACTER_STATE`.

### Recherche

Recherche beginnt, sobald eine relevante Unsicherheit sichtbar wird. Sie darf offen bleiben, solange sie keine aktuelle irreversible Entscheidung blockiert.

**Blockierregel v0.x:**

> Eine offene Recherchefrage blockiert die aktuelle Entwicklungsebene nur dann, wenn ihre Antwort eine jetzt zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.

Austauschbare Oberflächendetails blockieren nicht.

Für v0.x gibt es dafür bewusst keinen Score und keine zusätzliche Bewertungsmatrix. Die Grenze ist als bekannte Ermessensentscheidung dokumentiert und wird erst vertieft, wenn reale Fehlentscheidungen oder wiederkehrendes Rework dies rechtfertigen.

## 5. Gate-Batching bei großen Büchern

Ein Gate ist eine **fachliche Freigabephase**, keine Verpflichtung zu einer einzigen riesigen Lesesitzung.

Bei kleinen Testfällen kann beispielsweise G2 alle Szenenkarten gemeinsam prüfen. Bei einem Roman mit vielen Szenen darf dieselbe Freigabephase in mehrere Review-Batches aufgeteilt werden.

Beispiel:

- G2 Review-Batch 1: Szenen 1–15,
- G2 Review-Batch 2: Szenen 16–30,
- G2 Review-Batch 3: Szenen 31–45,
- abschließender Gesamtcheck der Szenenarchitektur,
- ein fachlicher G2-Abschluss.

Dadurch steigt die Review-Ergonomie, ohne künstlich `G2a`, `G2b`, `G2c` als neue Prozessgates einzuführen.

Die optimale Batch-Größe ist für v0.x **noch nicht allgemein festgelegt**. M1 muss nur beweisen, dass das Modell grundsätzlich funktioniert.

## 6. Prosa beginnt zuletzt

Prosa wird systematisch erst erzeugt, wenn G2 bestätigt hat, dass die relevanten Szenenkarten prose-ready sind.

Gate-Frage:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

Ein repräsentativer Prosa-Batch testet anschließend früh Stil, Rhythmus, Erlebnisdichte und sichtbare KI-Muster. Erst nach G3 wird auf den vollständigen Prosaumfang skaliert.

## 7. Backtracking bleibt erlaubt

Die Reihenfolge ist kein Wasserfall-Verbot für Lernen.

Wenn eine tiefere Ebene einen echten Storyfehler sichtbar macht:

1. nicht im Downstream-Artefakt kaschieren,
2. zur betroffenen kanonischen Upstream-Ebene zurückgehen,
3. dort ändern,
4. abhängige Artefakte `stale` oder `invalidated` markieren,
5. nur die betroffenen Freigabephasen erneut durchlaufen.

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

## 8. KISS-Regel für Freigaben

Vor einem zusätzlichen Human Gate muss die Frage beantwortet werden:

> **Welche konkrete irreversible Entscheidung schützt dieser zusätzliche Stopp, die nicht sinnvoll im nächsten gebündelten Gate geprüft werden kann?**

Gibt es darauf keine klare Antwort, wird kein neuer Gate eingeführt.

## Leitformel

> **Mehr interne Entwicklungstiefe, weniger externe Prozessschritte. Vom Großen ins Kleine, horizontal über das ganze Buch, Prosa zuletzt.**
