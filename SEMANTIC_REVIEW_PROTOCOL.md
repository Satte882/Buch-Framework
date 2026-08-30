# Unabhängiges semantisches Review-Protokoll

## Zweck

Dieses Protokoll definiert einen reproduzierbaren, bewusst **vom Erzeugungskontext getrennten** Review für Story-/Szenen-/Prosa-Artefakte.

Es ist keine automatische Qualitätssicherung, kein Score und kein Ersatz für Human Gates.

Ziel ist ausschließlich:

> Kann ein entkoppelter Reviewer auf Basis der kanonischen Quellen konkrete semantische Fehler oder Drift finden, die anschließend menschlich dispositioniert werden können?

## 1. Was „unabhängig“ hier bedeutet

Ein Review zählt nur dann als unabhängiger Test, wenn der Reviewer **nicht** erhält:

- den Erzeugungsdialog,
- Chain-of-Thought oder interne Erzeugungsbegründungen,
- frühere semantische Review-Befunde,
- bereits bekannte Korrekturlisten,
- Diffs zwischen fehlerhaftem und korrigiertem Stand,
- Abschlussberichte, die bekannte Fehler nennen,
- Issue-Kommentare mit Review-Ergebnissen.

Erlaubt sind ausschließlich die vorher festgelegten **kanonischen Quellen**, der zu prüfende Zielstand und dieses Review-Protokoll.

Ein neuer Chat allein genügt nicht, wenn ihm bekannte Findings oder Diffs wieder mitgegeben werden.

## 2. Zulässige Inputs

Je Review vorab explizit aufzählen. Typischer Minimalumfang:

- Zielartefakt, z. B. Manuskript-Blob oder Szenenbatch,
- freigegebene Szenenkarten,
- zugehörige Beats,
- relevante Character States,
- freigegebene Gate-Basis,
- relevante Research-Entscheidungen,
- Prosa-Profil, falls Stil-/Prosa-Drift Teil des Auftrags ist.

Der Reviewer darf fehlende Quellen melden, aber nicht still durch allgemeines Wissen oder Vermutungen ersetzen.

## 3. Verbotene Inputs

Für einen Blind-/Holdout-Test insbesondere nicht lesen:

- frühere `SEMANTIC_*_REVIEW.md`-Dateien,
- Completion Reports mit bekannten Befunden,
- spätere korrigierte Versionen des Zielartefakts,
- Git-Diffs zum korrigierten Stand,
- Issue-/Chat-Historie des Erzeugungslaufs.

Wenn ein verbotener Input versehentlich eingesehen wurde, ist der Test als `CONTAMINATED` zu markieren und darf nicht als unabhängige Validierung zählen.

## 4. Review-Fragen

Der Reviewer prüft nur konkrete Widersprüche oder belastbare Risiken in folgenden Klassen:

1. **Kausalität / Story-Wahrheit**
   - widerspricht Downstream einer freigegebenen Upstream-Entscheidung?
   - entsteht ein Ereignis ohne ausreichende Ursache oder Vorbereitung?

2. **Information / Reveal**
   - weiß oder behauptet eine Figur/ein Text etwas zu früh?
   - wird Unsicherheit später rückwirkend als frühere Gewissheit behandelt?

3. **Figur / Beziehung / Konsequenz**
   - werden gesetzte Grenzen, Vertrauenskosten oder Fehlentscheidungen unmotiviert zurückgesetzt?
   - verhält sich eine Figur entgegen ihrem kanonischen Zustand, ohne neue Ursache?

4. **Chronologie / Timing**
   - passen Zeiten, Sperrfristen, Reihenfolgen und Abhängigkeiten zusammen?

5. **Recherche-/Schutzgrenzen**
   - verletzt der Text eine freigegebene Quellen-, Rechts-, Recherche- oder Wissensgrenze?
   - behauptet er technische/juristische Details, die upstream nicht gedeckt sind?

6. **Prosa gegen kanonische Planung**
   - führt die Prosa eine neue relevante Plot-, Figuren-, Informations- oder Konsequenzentscheidung ein?

Optional bei entsprechendem Auftrag:

7. **Stilprofil / sichtbare Konstruiertheit**
   - nur wenn ein freigegebenes Prosa-Profil vorliegt; keine Geschmacksscores.

## 5. Was nicht bewertet wird

Keine pauschalen Qualitätsnoten wie `8/10`, keine Confidence-Scores und kein allgemeines „gefällt mir / gefällt mir nicht“.

Nicht als Finding zählen:

- bloße Alternativideen,
- persönliche Stilpräferenz ohne Contract-Bezug,
- neue Twists oder Figurenideen,
- Optimierungen ohne konkretes Problem,
- bereits bewusst akzeptierte Trade-offs, sofern die zugelassenen Quellen dies zeigen.

## 6. Finding-Schema

Jeder konkrete Befund exakt in diesem Schema:

```text
finding_id: SR-XXX
location: <Szene/Kapitel/Stelle>
finding_type: <causality | information | character | chronology | research_boundary | prose_drift | style_profile>
problem: <konkreter Widerspruch / konkretes Risiko>
canonical_evidence: <Pfad/ID/Blob oder eindeutiger Artefaktbezug>
impact: <was dadurch falsch/inkonsistent wird>
recommended_rework_level: <prose | scene | beat | event | story_architecture | research | none>
```

Keine Rewrite-Lösung im Review selbst.

## 7. Human-Disposition danach

Erst nach Abschluss des Blind-Reviews wird jeder Befund menschlich bzw. im regulären Arbeitskontext dispositioniert:

```text
disposition: confirmed | rejected | duplicate_known | accepted_tradeoff | needs_more_evidence
correction_triggered: yes | no
notes: <kurze Begründung>
```

Der Reviewer darf seine eigenen Befunde nicht selbst als „bestätigt“ deklarieren.

## 8. Validierungsmetrik

Für einen Holdout mit historisch bekannten Fehlern wird **erst nach Abgabe des Blind-Reviews** verglichen:

- bekannte historische Fehlergruppen gefunden: n / N
- zusätzliche neue Findings: n
- davon nach Human-Disposition bestätigt: n
- False Positives / rejected: n
- kontaminierter Test: yes/no

Kein Gesamt-Quality-Score.

Ein einzelner Test kann zeigen, ob das Verfahren grundsätzlich nützlich ist. Er beweist noch keine allgemeine Trefferquote für ganze Romane.

## 9. Statuslogik

- `NOT_YET_VALIDATED` – Protokoll vorhanden, aber noch kein sauberer Fresh-Context-Test.
- `CONTAMINATED` – Reviewer kannte verbotene Findings/Diffs; Ergebnis zählt nicht.
- `FAIL` – sauberer Test durchgeführt, aber Verfahren liefert keinen hinreichend belastbaren Nutzen oder zu viele falsche Befunde für den vorgesehenen Zweck.
- `PASS_FOR_PILOT` – sauberer Test findet reale, menschlich bestätigte Fehler mit vertretbarer False-Positive-Last. Bedeutet: im echten Roman kontrolliert einsetzen, nicht „voll validiert“.

## 10. KISS-Regel

> Erst unabhängigen Review als klar begrenzte zweite Lesung validieren. Keine Scores, Judges, Agenten oder Rewrite-Loops bauen, bevor ein einfacher Fresh-Context-Review nachweisbar zusätzlichen Nutzen liefert.
