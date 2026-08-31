# Unabhängiges semantisches Review-Protokoll

## Zweck

Dieses Protokoll definiert einen reproduzierbaren, bewusst **vom Erzeugungskontext getrennten** Review für Story-/Szenen-/Prosa-Artefakte.

Es ist keine automatische Qualitätssicherung, kein Score und kein Ersatz für Human Gates.

Ziel ist ausschließlich:

> Kann ein entkoppelter Reviewer auf Basis der kanonischen Quellen konkrete semantische Fehler oder Drift finden, die anschließend menschlich bzw. im regulären Arbeitskontext dispositioniert werden können?

Der Real-Pilot `Satte882/ABWEICHUNG` hat zwei zusätzliche Anforderungen bestätigt:

1. Whole-Manuscript-Reviews müssen Muster **über Szenengrenzen hinweg** beurteilen können.
2. Ein Raw-Review ist ein Befundlieferant, keine unanfechtbare Gate-Entscheidung. Findings brauchen Adjudikation.

## 1. Was „unabhängig“ hier bedeutet

Ein Review zählt nur dann als unabhängiger Test, wenn der Reviewer **nicht** erhält:

- den Erzeugungsdialog,
- Chain-of-Thought oder interne Erzeugungsbegründungen,
- frühere semantische Review-Befunde,
- bereits bekannte Korrekturlisten,
- Diffs zwischen fehlerhaftem und korrigiertem Stand,
- Abschlussberichte, die bekannte Fehler nennen,
- Issue-Kommentare mit Review-Ergebnissen.

Erlaubt sind ausschließlich die vorher festgelegten **kanonischen Quellen**, der zu prüfende Zielstand und dieses Review-Protokoll bzw. ein daraus abgeleiteter Review-Auftrag.

Ein neuer Chat allein genügt nicht, wenn ihm bekannte Findings oder Diffs wieder mitgegeben werden.

## 2. Zulässige Inputs

Je Review vorab explizit aufzählen. Typischer Minimalumfang:

- Zielartefakt bzw. fester Ziel-Commit,
- freigegebene Szenenkarten,
- zugehörige Beats,
- relevante Character States,
- freigegebene Gate-Basis,
- relevante Research-Entscheidungen,
- Prosa-Profil, falls Stil-/Prosa-Drift Teil des Auftrags ist.

Bei einem **Whole-Manuscript-Review** muss die vollständige Prosa in narrativer Reihenfolge gelesen werden. Stichproben reichen nicht für Aussagen über manuskriptweite Häufungen.

Der Reviewer darf fehlende Quellen melden, aber nicht still durch allgemeines Wissen oder Vermutungen ersetzen.

## 3. Verbotene Inputs

Für einen Blind-/Holdout-Test insbesondere nicht lesen:

- frühere `SEMANTIC_*_REVIEW.md`-Dateien,
- Completion Reports mit bekannten Befunden,
- spätere korrigierte Versionen des Zielartefakts,
- Git-Diffs zum korrigierten Stand,
- Issue-/Chat-Historie des Erzeugungslaufs,
- Lessons-Learned-Dateien, die bekannte Fehler des Zielstands verraten.

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

7. **Whole-Manuscript Pattern** – wenn der Auftrag das Gesamtmanuskript betrifft
   - wiederholt sich über viele Szenen dieselbe dramaturgische Trägerform?
   - dominiert Frage–Kurzantwort–Gegenfrage manuskriptweit, obwohl einzelne Dialoge lokal funktionieren?
   - häufen sich Erklärungsechos, Übergangsformeln, gleiche Eröffnungs-/Schlussmechaniken oder Policy-/Analyse-Szenen?
   - entsteht eine konkrete Ermüdungs-/Vorhersagbarkeitswirkung aus der Verteilung?

8. **Stilprofil / sichtbare Konstruiertheit** – optional
   - nur wenn ein freigegebenes Prosa-Profil vorliegt; keine Geschmacksscores.

Bei Whole-Manuscript-Mustern gilt:

> Nicht die bloße Existenz eines Stilmittels ist das Finding, sondern seine **Verteilung und konkrete Wirkung über den gesamten Text**.

## 5. Was nicht bewertet wird

Keine pauschalen Qualitätsnoten wie `8/10`, keine Confidence-Scores und kein allgemeines „gefällt mir / gefällt mir nicht“.

Nicht als Finding zählen:

- bloße Alternativideen,
- persönliche Stilpräferenz ohne Contract- oder belastbaren Whole-Manuscript-Bezug,
- neue Twists oder Figurenideen,
- Optimierungen ohne konkretes Problem,
- bereits bewusst akzeptierte Trade-offs, sofern die zugelassenen Quellen dies zeigen,
- bloße Zählwerte ohne nachvollziehbare literarische/strukturelle Wirkung.

## 6. Finding-Schema

Jeder konkrete Befund exakt in diesem Schema:

```text
finding_id: SR-XXX
location: <Szene/Kapitel/Stelle/Bereich>
finding_type: <causality | information | character | chronology | research_boundary | prose_drift | scene_repetition | dialogue_pattern | pacing | exposition | style_profile | other>
severity: <blocker | major | minor>
problem: <konkreter Widerspruch / konkretes Risiko>
canonical_evidence: <Pfad/ID/Blob oder eindeutiger Artefaktbezug>
impact: <was dadurch falsch/inkonsistent/ermüdend wird>
recommended_rework_level: <prose | scene | beat | event | story_architecture | research | none>
```

Keine Rewrite-Lösung im Review selbst.

## 7. Human-Disposition / Adjudikation danach

Erst nach Abschluss des Blind-Reviews wird jeder Befund im regulären Arbeitskontext dispositioniert.

```text
disposition: confirmed | rejected | duplicate_known | accepted_tradeoff | needs_more_evidence
confirmed_severity: blocker | major | minor | none
correction_triggered: yes | no
notes: <kurze Begründung>
```

Die Adjudikation prüft mindestens:

1. **Target-Evidenz:** Beschreibt das Finding den tatsächlich geprüften Stand korrekt?
2. **Severity:** Trägt die angeführte Evidenz wirklich `major/blocker`, oder nur ein Minor-/Restrisiko?
3. **Rework-Ebene:** Ist die empfohlene Ebene die kleinste sinnvolle?
4. **Review-Konflikt:** Widerspricht das Finding einem anderen unabhängigen Review, der dieselbe Frage spezifischer geprüft hat?
5. **Trade-off:** Ist die Häufung/Entscheidung bewusst und für das konkrete Buch vertretbar?

Der Reviewer darf seine eigenen Befunde nicht selbst als „bestätigt“ deklarieren.

**Wichtig:** Ein Raw-Abschluss wie `REWORK_REQUIRED` ist **advisory**. Das nächste Human Gate wird nur durch **bestätigte** Blocker/Major-Findings blockiert.

Das Raw-Urteil bleibt trotzdem unverändert dokumentiert; Adjudikation überschreibt nicht die Review-Historie.

## 8. Stop-Regeln gegen Rework-Schleifen

### Wiederholter bestätigter Manuskript-Major

Wenn nach einem reinen Prosa-Rework derselbe Scene-Repetition-/Pacing-Major erneut auftaucht und bestätigt wird:

`repeated manuscript-level major → inspect scene architecture → controlled G2 backtrack`

Kein weiterer bloßer Satzprosa-Pass auf unveränderter Szenenarchitektur.

### Reviewer-Overfitting

Wenn ein Raw-Major seine eigene Evidenz falsch klassifiziert, bereits strukturell veränderte Szenen als unverändert beschreibt oder einem spezifischeren bestandenen unabhängigen Review widerspricht:

`raw finding → adjudicate evidence → rework only if confirmed`

Kein automatischer Rework nur aufgrund eines neuen Reviewer-Labels.

## 9. Validierungsmetrik

Für einen Holdout mit historisch bekannten Fehlern wird **erst nach Abgabe des Blind-Reviews** verglichen:

- bekannte historische Fehlergruppen gefunden: n / N
- zusätzliche neue Findings: n
- davon nach Human-Disposition bestätigt: n
- False Positives / rejected: n
- Severity-Downgrades: n
- kontaminierter Test: yes/no

Kein Gesamt-Quality-Score.

Ein einzelner Test kann zeigen, ob das Verfahren grundsätzlich nützlich ist. Er beweist noch keine allgemeine Trefferquote für ganze Romane.

## 10. Statuslogik

- `NOT_YET_VALIDATED` – Protokoll vorhanden, aber noch kein sauberer Fresh-Context-Test.
- `CONTAMINATED` – Reviewer kannte verbotene Findings/Diffs; Ergebnis zählt nicht.
- `FAIL` – sauberer Test durchgeführt, aber Verfahren liefert keinen hinreichend belastbaren Nutzen oder zu viele falsche Befunde für den vorgesehenen Zweck.
- `PASS_FOR_PILOT` – sauberer Test findet reale, menschlich bestätigte Fehler mit vertretbarer False-Positive-Last. Bedeutet: im echten Roman kontrolliert einsetzen, nicht „voll validiert“.

Für einen konkreten Gate-Review können zusätzlich projektbezogene Readiness-Werte verwendet werden. Diese sind **Review-Ausgaben**, nicht Human-Gate-Tokens.

## 11. KISS-Regel

> Erst unabhängigen Review als klar begrenzte zweite Lesung nutzen, dann Findings evidenzbasiert adjudizieren. Keine Scores, Judges, Agenten oder automatischen Rewrite-Loops bauen, solange der einfache Fresh-Context-Review plus Human-Disposition den Zweck erfüllt.
