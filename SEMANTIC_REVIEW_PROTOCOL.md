# Unabhängiges semantisches Review-Protokoll

## Zweck

Dieses Protokoll definiert einen reproduzierbaren semantischen Review für Story-/Szenen-/Prosa-Artefakte.

Es ist keine automatische Qualitätssicherung, kein Score und kein Ersatz für Human Gates.

Ziel ist:

> Kann ein Reviewer auf Basis eines fixierten Zielstands und klar definierter kanonischer Quellen konkrete semantische Fehler, Drift oder belastbare Whole-Manuscript-Risiken finden, die anschließend menschlich dispositioniert werden können?

Der Real-Pilot `Satte882/ABWEICHUNG` hat drei Anforderungen bestätigt:

1. Whole-Manuscript-Reviews müssen Muster **über Szenengrenzen hinweg** beurteilen können.
2. Ein Raw-Review ist ein Befundlieferant, keine unanfechtbare Gate-Entscheidung. Findings brauchen Adjudikation.
3. Für produktive Buch-Gates ist ein vollständig kontextfreier Reviewer nicht nötig und erzeugt unnötige operative Hürden. Entscheidend ist **Evidenzdisziplin**, nicht Gedächtnislosigkeit.

## 1. Zwei Review-Modi

### A. `EVIDENCE_BOUND_REVIEW` – Standard für produktive Buch-Gates

Dieser Modus ist der Standard für G1–G5-nahe semantische Reviews und Re-Reviews.

Vorwissen über das Buch, frühere Diskussionen oder bekannte Schwachstellen **darf vorhanden sein**. Das Review bleibt gültig, solange folgende Regeln eingehalten werden:

- Bewertet wird ausschließlich der explizit fixierte Zielstand.
- Jedes Finding muss **neu aus dem Zielstand hergeleitet** werden.
- Jedes Finding muss mit kanonischer Evidenz aus den für den Auftrag zugelassenen Quellen belegbar sein.
- Frühere Findings, Reviews, Diffs, Chat-Erinnerungen oder Lessons Learned dürfen **nicht als Beweis** für ein aktuelles Finding verwendet werden.
- Ein früher bekanntes Problem darf erneut gefunden werden, aber nur dann zählen, wenn es im Zielstand tatsächlich noch vorhanden und dort konkret belegbar ist.
- Ein früher bekanntes Problem, das im Zielstand nicht mehr nachweisbar ist, ist kein Finding.

Damit gilt:

> Vorwissen ist zulässig. Fremde oder historische Evidenz ist es nicht.

Ein versehentlich eingesehener früherer Review macht einen produktiven Review **nicht** ungültig. Der Reviewer ignoriert diesen Input als Evidenz und prüft die Frage erneut am Zielstand.

### B. `CLEAN_FRESH_CONTEXT` – optionaler Blind-/Holdout-Modus

Dieser strengere Modus wird nur verwendet, wenn ausdrücklich ein **Methodentest, Benchmark oder Holdout** durchgeführt werden soll.

Dann erhält der Reviewer nicht:

- den Erzeugungsdialog,
- frühere semantische Review-Befunde,
- bekannte Korrekturlisten,
- Diffs zwischen fehlerhaftem und korrigiertem Stand,
- Abschlussberichte, die bekannte Fehler nennen,
- Issue-/PR-Kommentare mit Review-Ergebnissen.

Nur in diesem Modus gilt: Wenn verbotener Benchmark-Kontext vorab bekannt wird, kann der Test als `CONTAMINATED` markiert werden.

`CONTAMINATED` ist damit **kein regulärer Produktionsstatus**, sondern ausschließlich ein Integritätsstatus für echte Blind-/Holdout-Experimente.

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

## 3. Evidenzhygiene

### Im produktiven Modus

Frühere Review-Dateien, Completion Reports, Diffs, Issue-/Chat-Historie oder Lessons Learned sind **keine zulässige Finding-Evidenz**.

Falls solche Informationen bereits bekannt sind oder versehentlich gesehen wurden:

1. Review nicht abbrechen.
2. Die Information nicht als Beweis verwenden.
3. Das vermutete Problem ausschließlich am fixierten Zielstand neu prüfen.
4. Finding nur aufnehmen, wenn der Zielstand selbst ausreichende Evidenz liefert.

### Im Blind-/Holdout-Modus

Für einen ausdrücklich als Holdout definierten Test gelten die im jeweiligen Auftrag genannten verbotenen Quellen weiterhin strikt. Ein Verstoß kann dort `CONTAMINATED` auslösen, weil sonst die Benchmark-Aussage beschädigt wäre.

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
- bloße Zählwerte ohne nachvollziehbare literarische/strukturelle Wirkung,
- ein Problem nur deshalb, weil es aus einem früheren Review bekannt ist.

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

Erst nach Abschluss des Reviews wird jeder Befund im regulären Arbeitskontext dispositioniert.

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
4. **Review-Konflikt:** Widerspricht das Finding einem anderen Review, der dieselbe Frage spezifischer geprüft hat?
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

Wenn ein Raw-Major seine eigene Evidenz falsch klassifiziert, bereits strukturell veränderte Szenen als unverändert beschreibt oder einem spezifischeren bestandenen Review widerspricht:

`raw finding → adjudicate evidence → rework only if confirmed`

Kein automatischer Rework nur aufgrund eines neuen Reviewer-Labels.

## 9. Validierungsmetrik

Für einen **Holdout mit historisch bekannten Fehlern** wird erst nach Abgabe des Blind-Reviews verglichen:

- bekannte historische Fehlergruppen gefunden: n / N
- zusätzliche neue Findings: n
- davon nach Human-Disposition bestätigt: n
- False Positives / rejected: n
- Severity-Downgrades: n
- kontaminierter Holdout: yes/no

Diese Metrik betrifft Methodentests, nicht reguläre Produktionsreviews.

Kein Gesamt-Quality-Score.

## 10. Statuslogik

### Produktive Reviews

- `EVIDENCE_BOUND_REVIEW` – gültiger Review gegen fixierten Zielstand; Vorwissen erlaubt, Findings ausschließlich aus kanonischer Target-Evidenz hergeleitet.
- `REVIEW_INCOMPLETE` – Zielstand oder notwendige Quellen nicht vollständig geprüft.
- `REVIEW_INVALID_TARGET` – Zielcommit/-artefakt stimmt nicht mit dem Auftrag überein.

### Blind-/Holdout-Methodentests

- `CLEAN_FRESH_CONTEXT` – sauberer Blind-/Holdout-Test.
- `CONTAMINATED` – nur für einen ausdrücklich als blind definierten Test; Benchmark-Kontext war vor Review bekannt.
- `FAIL` – Holdout durchgeführt, Verfahren liefert keinen hinreichend belastbaren Nutzen.
- `PASS_FOR_PILOT` – Holdout findet reale, menschlich bestätigte Fehler mit vertretbarer False-Positive-Last.

Für konkrete Gate-Reviews können zusätzlich projektbezogene Readiness-Werte verwendet werden. Diese sind Review-Ausgaben, nicht Human-Gate-Tokens.

## 11. KISS-Regel

> Für Buchproduktion zählt ein fixierter Zielstand plus evidenzgebundene zweite Lesung. Blindheit ist optional und nur für Methodentests nötig. Findings werden anschließend menschlich adjudiziert; keine Scores, Judges oder automatischen Rewrite-Loops bauen, solange dieser einfache Ablauf den Zweck erfüllt.
