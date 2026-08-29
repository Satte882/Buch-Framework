# Analyse: Anti-KI-Prosa aus NORMALFALL

## Zweck

Diese Analyse extrahiert aus den späten Leser-, Perplexity- und Sprachpässen von `NORMALFALL` die wiederverwendbaren Regeln gegen **sichtbar modellhafte / KI-typische Prosa**.

Das ist kein kosmetischer Zusatz. Für die zukünftige Buchreihe ist die Prosaqualität ein eigenes Qualitätsgate. Ein strukturell guter Roman darf nicht daran scheitern, dass Satzbau, Kontrastmuster, Erklärlogik oder Rhythmus nach LLM-Ausgabe aussehen.

Die zentrale Lehre aus `NORMALFALL` lautet:

> **Anti-KI-Prosa muss bereits beim Schreiben verhindert, danach systematisch gesucht und vor dem Freeze regressionssicher gemacht werden.**

Ein einzelner Stilprompt reicht dafür nicht.

---

## 1. Was bei NORMALFALL tatsächlich passiert ist

Die erste Stilreferenz enthielt bereits Anti-KI-Regeln. Trotzdem entstanden im vollständigen Manuskript wiederkehrende Muster. Mehrere externe Leser-/Perplexity-Schleifen und gezielte Repo-Pässe waren nötig, um sie sichtbar zu machen und zu entfernen.

Die wichtigsten späten Eingriffe waren:

1. Einstiegspass: Methodikerklärungen, Nachunterricht und doppelte Deutungen entfernen.
2. Mittelteilpass: wiederholte Beweisführung, Kontrollschleifen und methodische Demonstrationen reduzieren.
3. Finaler Leserpass: Selbsterklärungen, Taxonomien und nachträgliche Absicherung von bereits verständlichen Beats entfernen.
4. Anti-Tick-/Anti-KI-Pass: Weichmacher-Cluster, Stakkato, Negations-/Dreischritt-Muster, Erklärsätze und wiederkehrende Choreografien kontextuell prüfen.
5. separater `Nicht-X-sondern-Y`-Pass: alle 38 Vorkommen von `sondern` gezielt umschreiben und anschließend per CI auf **0** einfrieren.

Wichtig: Die Änderungen waren überwiegend **kontextuell und chirurgisch**. Es wurde ausdrücklich kein globales Synonym-Suchen/Ersetzen als Stilstrategie verwendet.

---

## 2. Hochsignal-Muster: `Nicht X, sondern Y`

### Befund

Die Konstruktion trat in vielen Varianten auf:

- `nicht X, sondern Y`
- `nicht nur X, sondern Y`
- `Nicht X. Sondern Y.`
- `Nicht: X. Sondern: Y.`
- `Sondern?` als dialogische Anschlussfrage
- `weder / kein ... sondern ...`

Sie war über den Roman verteilt und dadurch als wiederkehrende Modellformel sichtbar.

Für `NORMALFALL` wurden **38 `sondern`-Vorkommen** einzeln umgeschrieben. Danach wurden sowohl der kanonische Build als auch die Metrik-Pipeline mit einem harten Guard versehen:

> Im finalen Manuskript darf das Wort `sondern` nicht vorkommen.

### Warum das Muster problematisch ist

Die Konstruktion ist grammatisch völlig korrekt. Das Problem ist ihre **Frequenz und rhetorische Funktion** in LLM-Prosa:

1. Das Modell stellt eine falsche/vereinfachte Lesart auf.
2. Es korrigiert sie sofort.
3. Der Satz erhält dadurch künstliche Prägnanz.
4. Dieses Muster wiederholt sich auf Satz-, Absatz- und Dialogebene.

Es erzeugt sehr schnell den Eindruck eines Textes, der seine eigene Interpretation gleich mitliefert.

### Wichtig für das Framework

Das Framework darf nicht nur das Token `sondern` kennen. Sonst verschiebt ein Modell die gleiche Formel lediglich zu:

- `Es war nicht X. Es war Y.`
- `Nicht X. Vielmehr Y.`
- `Nicht weil X. Weil Y.`
- `X war nicht das Problem. Y war es.`
- `Es ging nicht um X. Es ging um Y.`

Deshalb wird zwischen zwei Ebenen unterschieden:

**Hard Guard für diese Reihe:** `sondern` = 0 im finalen Prosatext.

**Semantischer Warn-Guard:** binäre Korrektur-/Kontrastformeln unabhängig vom verwendeten Bindewort markieren und kontextuell prüfen.

Das Hard-Ban ist Teil des **Prosa-/Serienprofils**, nicht des universellen Framework-Core. Der Core muss lediglich konfigurierbare Hard- und Warnregeln unterstützen.

---

## 3. Negationsketten und rhetorische Dreischritte

### Typischer Befund

LLM-Prosa erzeugt gern kontrollierte Reihen wie:

- `Nicht A.`
- `Nicht B.`
- `Nicht C.`
- danach eine erklärende Zielaussage.

Oder:

- drei ähnlich gebaute Kurzsätze,
- drei sauber abgestufte Beispiele,
- drei Negationen und anschließend die Pointe.

Bei `NORMALFALL` wurden solche Ketten mehrfach entfernt, obwohl jeder Einzelsatz für sich funktionieren konnte.

### Warum es auffällt

Das Problem ist die **sichtbare rhetorische Konstruktion**. Menschen schreiben ebenfalls Dreierfiguren. Ein Roman wirkt aber modellhaft, wenn diese Form regelmäßig erscheint und der Text ständig wie eine optimierte Präsentation argumentiert.

### Framework-Regel

- perfekte Dreierlisten nicht grundsätzlich verbieten;
- Häufungen auf Absatz-, Kapitel- und Gesamttextebene markieren;
- besonders kritisch: drei parallele Negationen, drei Ein-Satz-Absätze, drei syntaktisch gleich lange Aussagen;
- Dialog ausnehmen, wenn die Wiederholung klar aus Stimme, Stress oder Verhörsituation entsteht.

Leitfrage:

> **Entsteht der Rhythmus aus Figur und Situation – oder aus der Vorliebe des Modells für eine saubere rhetorische Form?**

---

## 4. Weichmacher- und Unsicherheitscluster

Beim Anti-Tick-Pass wurden unter anderem folgende Wörter kontextuell gescannt:

- `vielleicht`
- `schien`
- `wirkte`
- `könnte`
- `offenbar`
- `vermutlich`
- `möglicherweise`
- `soweit`
- `zumindest`

Der Pass reduzierte die gezählten Weichmacher von **108 auf 90**, ohne sie pauschal zu verbieten.

### Das eigentliche Problem

Nicht das einzelne `vielleicht` ist KI-Prosa. Problematisch sind:

- mehrere Weichmacher im selben Absatz,
- dieselbe Absicherung mehrfach hintereinander,
- Erzählerunsicherheit, obwohl die Szene die Information direkt zeigen könnte,
- doppelte Unsicherheit (`vielleicht ... wahrscheinlich`, `schien offenbar`, usw.),
- dauerndes Filtern der Wahrnehmung über `wirkte`, `schien`, `bemerkte`.

### Framework-Regel

**Dichte prüfen, nicht Wörter blind verbieten.**

Automatischer Scan soll ausgeben:

- Treffer je Kapitel,
- Cluster je Absatz,
- Kombination mehrerer Weichmacher in engem Abstand,
- starke Ausreißer gegenüber dem restlichen Manuskript.

Danach kontextuelle Entscheidung:

- epistemisch notwendige Unsicherheit behalten,
- rhetorische Absicherung entfernen,
- direkte Wahrnehmung bevorzugen, wenn keine echte Unsicherheit besteht.

---

## 5. Stakkato und bedeutungsschwere Ein-Satz-Absätze

### Befund

Insbesondere im Prolog lagen mehrere Ketten aus sehr kurzen Ein-Satz-Absätzen vor. Einzelne kurze Sätze waren wirksam; in Serie wurde der Mechanismus sichtbar.

Typisches LLM-Muster:

> Aussage.  
> Noch kürzer.  
> Bedeutungssteigerung.  
> Pointe.

### Framework-Regel

Nicht `kurze Sätze` verbieten. Stattdessen Runs markieren:

- mehrere sehr kurze Prosasätze direkt hintereinander,
- drei oder mehr Ein-Satz-Absätze in Folge,
- wiederholte Kapitelenden aus isolierten Bedeutungssätzen,
- identische Stakkatoform in mehreren Spannungsszenen.

Dialogzeilen, Verhör, echte Hochspannung oder bewusst gesetzte Finalmomente benötigen andere Schwellenwerte.

Leitregel:

> **Kurze Sätze sind ein Rhythmusinstrument, kein Standardmodus für Spannung.**

---

## 6. Erklär-Echo nach einem bereits verständlichen Beat

Das war einer der größten Qualitätsverluste nach dem Ausbau.

Typischer Aufbau:

1. Figur handelt.
2. Konsequenz ist sichtbar.
3. Dialog oder Körpersprache macht die Bedeutung bereits klar.
4. Erzähler erklärt anschließend noch einmal, **was das gerade bedeutet hat**.

Bei `NORMALFALL` wurden zahlreiche solcher Nachsätze oder ganzen Nachanalyseblöcke entfernt.

Beispiele als abstrakte Muster:

- Handlung zeigt den Vertrauensbruch → Erzähler erklärt anschließend den Vertrauensbruch.
- Figur setzt eine Grenze → danach wird erklärt, dass die Grenze nun wirklich gesetzt ist.
- Beziehungsszene endet in einer Handlung → danach deutet der Erzähler die Beziehung aus.
- eine Gegenhypothese wurde praktisch geprüft → anschließend folgt eine Methodiklektion darüber.

### Framework-Regel

Für jeden Absatz nach einem starken Beat prüfen:

> **Welche neue Information enthält dieser Satz?**

Wenn die Antwort nur lautet `Er erklärt die Bedeutung des unmittelbar Vorherigen`, ist er ein Löschkandidat.

Das gilt besonders für Formulierungen mit Funktionen wie:

- Schlussfolgerung erklären,
- Moral absichern,
- Leserinterpretation steuern,
- bereits gezeigten Gefühlszustand benennen,
- vorangegangene Handlung in Methodensprache übersetzen.

---

## 7. Methodik- und Beweisführungsprosa

Die präzise Planung von `NORMALFALL` hatte eine Nebenwirkung: Teile dieser Präzision wanderten beim Ausformulieren sichtbar in den Roman.

Befunde aus den Leser-Pässen:

- Figuren erklären wiederholt ihre Prüfmethode.
- gleiche Logik wird erst gezeigt und später nochmals verbal bewiesen.
- Listen/Taxonomien erscheinen als besonders saubere Denkblöcke.
- Frage-Antwort-Schleifen demonstrieren einen bereits etablierten Prüfprozess erneut.
- Figuren reden gelegentlich wie Reviewer ihrer eigenen Szene.

### Kernlektion

> **Saubere Konstruktion im Unterbau. Unsaubere, menschliche Oberfläche im Erleben.**

Die Szenenkarte darf hochsystematisch sein. Der fertige Roman darf diese Systematik nicht wie ein Ablaufdiagramm vorführen.

### Framework-Regel

Vor Prosa explizit festhalten:

- Planungskategorien sind **nicht automatisch prosefähige Begriffe**.
- Beats, Gates, Gegenhypothesen, Leserwissen und Prüflogik steuern das Schreiben intern.
- Im Roman erscheinen sie nur, wenn die Figur sie in dieser Situation tatsächlich so ausdrücken würde.

---

## 8. Wiederholte Frage-Antwort-Schleifen

Ein weiteres Muster war die dialogische Wiederholung bereits etablierter Logik:

- Figur A fragt.
- Figur B erklärt.
- A präzisiert.
- B bestätigt.
- später wird derselbe Prüfschritt noch einmal in einer leicht anderen Schleife gespielt.

Solche Dialoge wirken zunächst klar und professionell, erzeugen über viele Kapitel jedoch synthetischen Gleichklang.

### Framework-Regel

Dialog-Review prüft:

- Wird hier tatsächlich ein Konflikt ausgetragen?
- Ändert eine Antwort die Beziehung, Entscheidung oder Informationslage?
- Oder führt der Dialog nur eine Logik vor, die der Leser schon kennt?

Wenn letzteres: verdichten oder über Handlung lösen.

---

## 9. Symmetrie und zu saubere Oberfläche

LLMs bevorzugen Ausgewogenheit:

- These und Gegenthese bekommen ähnlich viel Raum.
- Figurenargumente werden sauber gespiegelt.
- Szenen liefern klaren Setup → Erkenntnis → Konsequenz.
- Hinweise besitzen auffällig perfekte Gegenhinweise.
- Absätze sind syntaktisch ausbalanciert.

Für Planung ist das hilfreich. In Prosa wird es schnell künstlich.

### Framework-Regel

Die Qualitätsprüfung fragt ausdrücklich:

- Ist jede relevante Information zu sauber platziert?
- Haben mehrere Figuren symmetrisch passende Geheimnisse oder Argumente?
- endet jedes Gespräch mit einem klaren Ergebnis?
- erhält jede Szene eine perfekte kleine Pointe?
- ist die moralische Versuchsanordnung zu leicht erkennbar?

Gewollt sind dagegen:

- Nebenaspekte,
- abgebrochene Gespräche,
- unterschiedliche Gewichtung,
- echte Missverständnisse,
- teilweise folgenlose Details,
- asymmetrische Figurenreaktionen,
- natürliche Wiederholung,
- unvollständig formulierte Gefühle.

---

## 10. Wiederkehrende Mikro-Choreografie

Der Anti-Tick-Pass prüfte auch wiederkehrende Handlungsformulierungen. Einzelne Gesten sind natürlich, können in hoher Dichte aber zum LLM-Tick werden:

- `X sah ihn an.`
- `X nickte.`
- `X schwieg.`
- `X atmete aus.`
- `X legte ... auf den Tisch.`
- `X bemerkte ...`

### Framework-Regel

Nicht einzelne Gesten verbieten. Stattdessen wiederkehrende N-Gramme / Aktionsmuster und auffällige Kapitelhäufungen melden.

Die Frage lautet nicht `Ist diese Geste erlaubt?`, sondern:

> **Benutzt der Text dieselbe neutrale Regieanweisung immer wieder, weil dem Modell für Mikro-Staging nichts Spezifischeres einfällt?**

---

## 11. Weitere verbindliche Anti-KI-Regeln aus der Stilarchitektur

Folgende Regeln bleiben ausdrücklich Teil des zukünftigen Prosa-Profils:

### Vermeiden

- dauernde Synonymvariation nur gegen natürliche Wiederholung,
- abstrakte Gefühle ohne körperlichen oder handlungsbezogenen Träger,
- gleichmäßig kunstvolle Metaphern,
- Figuren, die ihre Gefühle jederzeit exakt benennen können,
- moralisierende Erzählerstimme,
- Wiederholung derselben Aussage in leicht anderen Worten,
- symmetrisch gebaute Absätze,
- permanente bedeutungsschwere Kurzabsätze.

### Zulassen

- harte oder banale Sätze,
- natürliche Wortwiederholungen,
- widersprüchliche Figuren,
- unklare Gefühle,
- unvollständige Gedanken,
- unterschiedliche rhythmische Dichte,
- Stellen ohne Metapher oder Pointe,
- sprachliche Kanten, wenn sie aus Figur und Situation entstehen.

---

## 12. Warum ein Stilprompt allein nicht reicht

`NORMALFALL` zeigt, dass Anti-KI-Regeln bereits früh dokumentiert waren und trotzdem später konkrete Muster entstanden.

Ursachen:

1. Längere LLM-Ausgaben driften trotz Regeln in statistisch bevorzugte Formen.
2. Ausbau-Pässe verstärken Erklärneigung, weil das Modell zusätzliche Wörter sinnvoll füllen will.
3. Ein Modell erkennt seine eigenen Lieblingsmuster nur unzuverlässig im selben Schreibdurchgang.
4. Lokale Sätze können gut wirken, während erst die globale Häufung künstlich aussieht.
5. Die gleiche rhetorische Formel kann mit anderen Wörtern wiederkehren.

Folge:

> **Prävention, Messung und Review müssen getrennte Stufen sein.**

---

## 13. Vorgeschlagene Anti-KI-Pipeline für Buch-Framework v0.1

### Stufe A – Prosa-Profil vor dem Schreiben

Ein verbindliches `PROSA_PROFIL.md` definiert:

- gewünschte Lesbarkeit,
- Rhythmus,
- Dialogprinzipien,
- erlaubte Rauheit,
- Anti-KI-Muster,
- Hard-Bans,
- Warnmuster,
- projektspezifische Kalibrierung.

### Stufe B – Szenenprompt

Jede Ausformulierung erhält nur die relevanten Regeln, darunter:

- Konstruktion nicht erklären,
- keine neuen Plotentscheidungen,
- keine rhetorische Glättung,
- keine Standard-Kontrastformeln,
- Subtext statt vollständiger Selbsterklärung,
- Rhythmus aus Szene und Figur ableiten.

### Stufe C – automatischer Prosa-Lint

Der Linter ändert **nichts automatisch**. Er meldet Kandidaten.

#### Hard Fail – konfigurierbar

Für das aktuelle Serienprofil mindestens:

- `\bsondern\b` → 0
- weitere bewusst definierte verbotene Zeichen-/Typografiemuster

#### Warnungen

- semantische `Nicht X → Y`-Korrekturformeln,
- Negationsketten,
- rhetorische Dreierstrukturen,
- Weichmacher-Cluster,
- Stakkato-Runs,
- mehrere Ein-Satz-Absätze,
- Wiederholungs-/Erklär-Echos,
- wiederkehrende Mikro-Choreografie,
- auffällige Wiederholung von Wahrnehmungsfiltern (`wirkte`, `schien`, `bemerkte`, ...).

### Stufe D – kontextueller Anti-Tick-Pass

Jeder Treffer wird im Absatz und im Szenenkontext bewertet.

Regel:

> **Scanner entscheidet, wo gelesen wird. Reviewer entscheidet, ob geändert wird.**

Keine pauschale automatische Umschreibung.

### Stufe E – Leserpass

Nicht nach Tokens suchen, sondern nach Wirkung:

- Wo erklärt der Text sich selbst?
- Wo erkennt man den Bauplan?
- Wo wird derselbe Gedanke zweimal bewiesen?
- Wo klingt eine Figur wie ein Analysemodell?
- Wo wird eine starke Szene nachträglich erklärt?
- Wo ist die Prosa zu sauber, symmetrisch oder rhetorisch vollständig?

### Stufe F – Regression / Freeze

Nach Abnahme:

- Hard Guards laufen in CI.
- Warnstatistiken werden dokumentiert, aber nicht blind als Fehler behandelt.
- erneute KI-Politur nur bei konkretem Befund.
- danach menschliche Testleser statt endloser Modelloptimierung.

---

## 14. Hard Rules vs. Warn Rules

Das Framework muss diese Unterscheidung technisch abbilden.

| Regeltyp | Beispiel | Reaktion |
|---|---|---|
| **Hard** | `sondern` im finalen Serienmanuskript | Build/Prosa-Gate schlägt fehl |
| **Hard** | verbotene Typografie oder Masterstruktur verletzt | Build schlägt fehl |
| **Warn** | 4× `vielleicht` in engem Kontext | Absatz prüfen |
| **Warn** | 3 kurze Ein-Satz-Absätze in Folge | Rhythmus prüfen |
| **Warn** | `Nicht X. Es war Y.` | Kontrastformel prüfen |
| **Warn** | drei parallele Negationen | Rhetorik prüfen |
| **Warn** | wiederholtes `sah ihn an / nickte / schwieg` | Mikro-Staging prüfen |
| **Warn** | Erklärsatz direkt nach sichtbar abgeschlossenem Beat | ggf. streichen |

Warum diese Trennung wichtig ist:

Ein Linter, der jedes Stilmerkmal automatisch verbietet, erzeugt selbst künstliche Prosa. Die meisten Stilprobleme sind **Dichte- und Kontextprobleme**, keine verbotenen Wörter.

---

## 15. Änderung gegenüber der ersten NORMALFALL-Framework-Analyse

In `ANALYSE_NORMALFALL.md` wurde das aktuelle `sondern`-Verbot zunächst als Beispiel für eine zu stark buchindividuelle CI-Regel genannt.

Diese Bewertung muss präzisiert werden:

- Die **hart codierte Implementierung direkt im NORMALFALL-Workflow** ist nicht frameworkfähig.
- Die **inhaltliche Anti-KI-Regel selbst** ist jedoch ausdrücklich wiederverwendbar für die geplante Reihe.
- Im Framework muss sie deshalb in ein **konfigurierbares Prosa-/Serienprofil** wandern.

Damit gilt:

> Nicht die Regel entfernen – die Regel parametrieren.

---

## 16. Qualitätsgate für zukünftige Bücher

Ein Buch ist nicht prosafertig, nur weil Grammatik, Plot und Stil allgemein stimmen.

Vor Testlesern muss ein eigener Anti-KI-Gate bestanden werden:

### Gate: `PROSA_AUTHENTIZITAET`

- [ ] keine Hard-Ban-Verstöße
- [ ] Kontrastformel-Scan geprüft
- [ ] Weichmacher-Cluster geprüft
- [ ] Stakkato-/Ein-Satz-Absatz-Scan geprüft
- [ ] Dreier-/Negationsmuster geprüft
- [ ] Erklär-Echos geprüft
- [ ] Methodik-/Beweisführungsprosa geprüft
- [ ] wiederkehrende Frage-Antwort-Schleifen geprüft
- [ ] Mikro-Choreografie geprüft
- [ ] globale Symmetrie / sichtbarer Bauplan geprüft
- [ ] keine automatischen Massenersetzungen als Stilkorrektur
- [ ] finaler Leserpass ohne neue KI-Politur-Schleife

Definition of Done:

> **Der Leser soll die Konstruktion spüren können, weil die Geschichte trägt – aber er darf die sprachliche Konstruktion des Modells nicht sehen.**

---

## 17. Konsequenz für Buch-Framework v0.1

Anti-KI-Prosa wird nicht als Unterpunkt von `STILREFERENZ` behandelt, sondern als **eigener Framework-Baustein** mit:

1. Prosa-Profil,
2. Pattern-Katalog,
3. Lint-/Audit-Schnittstelle,
4. konfigurierbaren Hard-/Warnregeln,
5. kontextuellem Anti-Tick-Pass,
6. eigenem Qualitätsgate,
7. Regression im finalen Build.

Das ist eine der zentralen Lehren aus `NORMALFALL` und für alle weiteren Bücher verbindlich.