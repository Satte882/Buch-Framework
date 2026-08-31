# Arbeitsweise – vom Großen ins Kleine

## Zweck

Dieses Dokument definiert die verbindliche Arbeitsweise des Buch-Frameworks. Die konkrete Verzeichnisstruktur steht in `PROJECT_STRUCTURE.md`.

> **Viele Entwicklungsebenen, wenige menschliche Freigaben.**

Das Framework entwickelt Bücher bewusst **vom Großen ins Kleine**. Eine feinere Entwicklungsebene erzeugt nicht automatisch einen neuen Human Gate.

## 1. Verbindliche Entwicklungsebenen

Die normale Arbeitsrichtung lautet:

`Thema / Buchidee → dramaturgische Bausteine → Ereignisse / Sequenzen → Szenen → Beats → Prosa`

Danach folgen Gesamtqualitätsprüfung und Produktion.

### Horizontal vor vertikal

Jede Ebene wird zuerst **über das gesamte Buch** ausreichend geschlossen, bevor die nächste Ebene systematisch ausgebaut wird.

Beispiel:

1. alle dramaturgischen Bausteine des Buchs,
2. dann alle Ereignisse / Sequenzen innerhalb der Bausteine,
3. dann die vollständige Szenenlandschaft über das Buch,
4. dann die Beats und Character States innerhalb dieser Szenen,
5. erst danach Prosa.

Es ist ausdrücklich nicht der Standard, B01 oder Szene 1 bis zur fertigen Prosa auszubauen, während spätere Teile des Buchs noch nur grob geplant sind.

**Grund:** Je später eine Storyentscheidung geändert wird, desto teurer ist das Downstream-Rework. Die horizontale Entwicklung macht Widersprüche, Lücken und Fehlgewichtungen sichtbar, bevor sie in Prosa vervielfacht werden.

## 2. Verzeichnisstruktur folgt der Storystruktur

Neue echte Buchprojekte verwenden die in `PROJECT_STRUCTURE.md` definierte Hierarchie:

`Root/Meta → BAUSTEINE/Bxx → SZENEN/Sxxx → BEATS / CHARACTER_STATES → PROSA`

Events liegen beim jeweiligen Baustein; Beats und Character States bei der jeweiligen Szene. Prosa ist die unterste Ebene.

Globale Dateien wie `STORY_BLOCKS.md`, `EVENTS.md` oder `BEATS.md` dürfen als abgeleitete Index-/Checker-Sichten existieren, sind in hierarchischen Buchprojekten aber keine zweite fachliche Source of Truth.

## 3. Entwicklungsebenen sind keine Gate-Ebenen

Ein Human Gate schützt eine **irreversible oder teuer rückholbare Entscheidung**. Er existiert nicht, weil eine neue Markdown-Datei oder Planungsebene entstanden ist.

Für v0.x gelten sechs Freigabephasen:

| Gate | Mensch entscheidet über | Vor dem Gate intern entwickelte Ebenen |
|---|---|---|
| **G0 – Konzept** | Thema, Prämisse, Leitfrage, Leser-Versprechen, zentrale Nicht-Ziele | Buchidee / Konzept |
| **G1 – Story-Architektur** | ob die Gesamtgeschichte trägt | Story Package, alle Bausteine, alle Ereignisse/Sequenzen, Figurenkern, relevante Rechercheabhängigkeiten |
| **G2 – Prose Ready** | ob die Geschichte vollständig genug für Prosa geplant ist **und die Szenenfolge als Ganzes ausreichend variiert** | alle Szenen, alle Beats, Character States, für diese Planung blockierende Recherche, Whole-Book Scene-Shape Review |
| **G3 – Prosa-Stil** | ob der Prosaansatz sprachlich und erzählerisch trägt | repräsentative Einzelszenen **plus zusammenhängender Mittelteil-Run** aus G2-freigegebenen Szenen |
| **G4 – Manuskript** | ob das Gesamtmanuskript inhaltlich und qualitativ abgenommen wird | vollständige Prosa, Reviews, Rework, Qualitätsprüfungen, Finding-Adjudikation |
| **G5 – Produktion** | ob das konkrete Produktionsartefakt freigegeben wird | DOCX/PDF/KDP- bzw. andere Produktionsausgaben |

Zwischen **Bausteinen → Ereignissen/Sequenzen**, **Ereignissen → Szenen** und **Szenen → Beats** gibt es standardmäßig keinen separaten Human Gate.

## 4. Wenige Gates bedeutet nicht wenig Kontrolle

Zwischen zwei Human Gates darf ChatGPT Arbeitskontrollen durchführen. Dabei wird klar zwischen mechanischer und semantischer Kontrolle unterschieden.

### Mechanische / deterministische Kontrolle

Geeignet für automatische oder Chat-gestützte Checks:

- Pflichtfelder vorhanden,
- IDs und Referenzen stimmen,
- alle Bausteine sind durch Ereignisse abgedeckt,
- alle Ereignisse sind durch Szenen abgedeckt,
- alle aktiven Szenen besitzen Beats,
- Character-State-Referenzen sind vorhanden,
- keine bekannte blockierende Rechercheabhängigkeit ist offen,
- Upstream-Referenzen sind aktuell.

### Inhaltliche Selbstprüfung

ChatGPT darf eigene Entwürfe auf Kausalität, Konflikt, Informationslogik oder Figurenkonsistenz prüfen. Diese Prüfung ist jedoch **keine unabhängige Qualitätssicherung**.

> Dieselbe KI, die ein Artefakt erzeugt hat, ersetzt durch ihre Selbstprüfung weder den Human Gate noch einen bewusst entkoppelten Fresh-Context-/Red-Team-Review.

Format- und Konsistenzchecks dürfen deterministisch blockieren. Inhaltliche Fragen wie Strohmann-Konflikt, Deus-ex-machina, schwacher Reversal oder unglaubwürdige Motivation werden spätestens im gebündelten Human Gate bzw. in einem dafür vorgesehenen unabhängigen Review bewertet.

## 5. Figuren und Recherche sind Querschnittsarbeit

Figurenentwicklung und Recherche sind keine isolierten linearen Stufen mit automatisch eigenem Gate.

### Figuren

- Figurenkern und zentrale Beziehungen werden in der Story-Architektur entwickelt.
- Wissensgrenzen und Zustände werden mit zunehmender Tiefe konkretisiert.
- Szenenspezifische Zustände liegen bei der jeweiligen Szene in `CHARACTER_STATES.md` bzw. bei Bedarf einem lokalen `CHARACTER_STATES/`-Unterordner.

### Recherche

Recherche beginnt, sobald eine relevante Unsicherheit sichtbar wird. Sie darf offen bleiben, solange sie keine aktuelle irreversible Entscheidung blockiert.

**Blockierregel v0.x:**

> Eine offene Recherchefrage blockiert die aktuelle Entwicklungsebene nur dann, wenn ihre Antwort eine jetzt zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung verändern kann.

Austauschbare Oberflächendetails blockieren nicht.

## 6. Gate-Batching bei großen Büchern

Ein Gate ist eine **fachliche Freigabephase**, keine Verpflichtung zu einer einzigen riesigen Lesesitzung.

Bei einem Roman mit vielen Szenen darf G2 beispielsweise in mehrere Review-Batches aufgeteilt werden:

- Szenen 1–15,
- Szenen 16–30,
- Szenen 31–45,
- abschließender Gesamtcheck der Szenen-/Beat-Architektur,
- ein fachlicher G2-Abschluss.

Dadurch steigt die Review-Ergonomie, ohne künstlich `G2a`, `G2b`, `G2c` als neue Prozessgates einzuführen.

**Wichtig:** Der Abschlusscheck darf nicht nur die Batch-Ergebnisse addieren. Er muss die vollständige Szenenfolge über Batch-Grenzen hinweg betrachten und insbesondere die Verteilung der dramaturgischen Träger prüfen.

## 7. G2 prüft zusätzlich die Scene-Shape-Verteilung

Der Real-Pilot ABWEICHUNG hat gezeigt, dass lokale Korrektheit keine ausreichende Whole-Book-Variation garantiert.

Deshalb wird für G2 jede Szene in der Review-Sicht einem dominanten `Primary Dramatic Carrier` zugeordnet, z. B.:

- klinische Handlung,
- Ressourcenkonflikt,
- persönliche Konfrontation,
- Solo-Analyse,
- Datenreview,
- Governance-/Regeldesign,
- Audit/Investigation,
- Beziehungsszene,
- Implementationstest,
- Nachhall.

Die Klassifikation ist eine **Review-Projektion**, keine neue kanonische Storydatei.

Warnsignale, nicht automatische Blocker:

- mehr als 2 direkt aufeinanderfolgende Szenen mit praktisch demselben Carrier,
- mehr als 4 Meeting-/Review-/Governance-/Data-Szenen in 8 aufeinanderfolgenden Szenen,
- mehrere Regel-/Governance-Stufen ohne erlebte Anwendung/Folge/Konflikt dazwischen,
- wiederholt dieselbe Erkenntnismechanik über mehrere Szenen.

G2 fragt deshalb zusätzlich:

> **Ist die Szenenfolge als Leseerlebnis ausreichend variiert, oder wiederholt die Architektur über längere Strecken denselben dramaturgischen Träger?**

Ein Zählwert allein erzeugt kein `REWORK`. Entscheidend ist die konkrete Ermüdungs-/Redundanzwirkung.

## 8. Prosa beginnt zuletzt

Prosa wird systematisch erst erzeugt, wenn G2 bestätigt hat, dass die relevanten Szenen inklusive Beats, Character States und blockierender Recherche prose-ready sind und kein bestätigter Whole-Book-Scene-Shape-Major offen ist.

Gate-Frage auf Szenenebene:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen?**

Ein repräsentativer Prosa-Batch testet anschließend früh Stil, Rhythmus, Erlebnisdichte und sichtbare KI-Muster.

### G3-Sample

Für längere Romane umfasst G3 standardmäßig:

1. 2–3 repräsentative Einzelszenen mit unterschiedlichen Anforderungen,
2. zusätzlich einen **zusammenhängenden Mittelteil-Run von mindestens 6 aufeinanderfolgenden Szenen**.

Der Mittelteil-Run soll Muster erkennen, die in isolierten Szenen unsichtbar bleiben:

- Dialogrhythmus über Szenengrenzen,
- wiederkehrende Meeting-/Review-Choreografie,
- Expositionsdichte,
- Übergangs- und Schlussmechaniken,
- Verhältnis von Handlung, Analyse, Beziehung und Konsequenz.

Erst nach G3 wird auf den vollständigen Prosaumfang skaliert.

## 9. Review-Befund und Gate-Entscheidung trennen

Ein Fresh-Context-/Red-Team-Review ist ein **Befundlieferant**, kein automatischer Entscheider.

Nach dem Blind-Review wird jeder relevante Befund im regulären Arbeitskontext dispositioniert:

- passt die Evidenz tatsächlich zum geprüften Target?
- ist die Severity belastbar?
- ist der Befund neu, bereits behoben, akzeptierter Trade-off oder False Positive?
- welche kleinste Rework-Ebene wäre nötig?
- widerspricht ein anderer unabhängiger Review mit spezifischerer Prüfung?

Nur bestätigte Blocker/Major-Findings blockieren das nächste Human Gate.

Das Raw-Urteil eines Reviewers bleibt dokumentiert, darf aber nach evidenzbasierter Adjudikation zurückgewiesen oder herabgestuft werden.

> **Review liefert Befunde. Der Prozess entscheidet über ihre Konsequenz.**

## 10. Backtracking bleibt erlaubt

Die Reihenfolge ist kein Wasserfall-Verbot für Lernen.

Wenn eine tiefere Ebene einen echten Storyfehler sichtbar macht:

1. nicht im Downstream-Artefakt kaschieren,
2. zur betroffenen kanonischen Upstream-Ebene zurückgehen,
3. dort ändern,
4. abhängige Artefakte `stale` oder `invalidated` markieren,
5. nur die betroffenen Freigabephasen erneut durchlaufen.

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

### Stop-Regel gegen Prosa-Endlosschleifen

Wenn ein unabhängiger Vollmanuskript-Review nach einem reinen Prosa-Rework **denselben Scene-Repetition-/Pacing-Major erneut meldet und dieser bestätigt wird**:

`repeated manuscript-level major → inspect scene architecture → controlled G2 backtrack`

Kein weiterer bloßer Satzprosa-Pass auf unveränderter Szenenarchitektur.

### Stop-Regel gegen Reviewer-Overfitting

Wenn ein neuer Raw-Major bekannte oder strukturell bereits veränderte Szenen falsch klassifiziert oder einem spezifischeren bestandenen Review widerspricht:

`raw finding → adjudicate evidence → rework only if confirmed`

Kein automatischer Rework nur deshalb, weil ein Reviewer `REWORK_REQUIRED` ausgibt.

## 11. KISS-Regel für Freigaben

Vor einem zusätzlichen Human Gate muss die Frage beantwortet werden:

> **Welche konkrete irreversible Entscheidung schützt dieser zusätzliche Stopp, die nicht sinnvoll im nächsten gebündelten Gate geprüft werden kann?**

Gibt es darauf keine klare Antwort, wird kein neuer Gate eingeführt.

## Leitformel

> **Meta → Bausteine → Events → Szenen → Beats → Prosa. Vom Großen ins Kleine, horizontal über das ganze Buch, Prosa zuletzt – und Whole-Book-Muster vor Skalierung prüfen.**
