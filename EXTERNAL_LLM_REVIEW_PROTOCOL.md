# Externes LLM-Review-Protokoll

## Zweck

Dieses Protokoll ergänzt den internen semantischen Review um eine bewusst **außerhalb des Erzeugungs-/Review-Kontexts liegende zweite Modellperspektive**.

Es soll insbesondere das Risiko reduzieren, dass dasselbe Modell oder derselbe Arbeitskontext über längere Zeit:

- eigene Prämissen zu selbstverständlich übernimmt,
- wiederkehrende Schwächen nicht mehr wahrnimmt,
- bekannte Erklärungen mit Qualität verwechselt,
- lokale Konsistenz stärker gewichtet als tatsächliche Leserwirkung.

Das externe Review ist **modell- und anbieteragnostisch**. Verwendet werden kann ein leistungsfähiges allgemeines oder research-fähiges LLM, das nicht am bisherigen Produktionsprozess des konkreten Manuskripts beteiligt war.

> Externes Modell = zweite Sicht, nicht zweite Wahrheit.

## 1. Position in der Pipeline

Für ein vollständiges Buch erfolgt der externe Review standardmäßig innerhalb von **G4**, wenn ein nahezu finaler Manuskript-Snapshot vorliegt:

1. internes Whole-Manuscript-/Evidence-Bound-Review,
2. bestätigtes Rework,
3. finaler horizontaler Prosa-/Rhythmuspass und Regression,
4. **externer unabhängiger LLM-Review auf fixiertem G4-Kandidaten**,
5. interne Human-/Evidence-Adjudikation der externen Findings,
6. bei bestätigtem Blocker/Major gezieltes Rework und betroffene Regression,
7. erst danach G4-Human-Entscheidung.

Der externe Review ist **kein zusätzliches Human Gate**.

## 2. Reviewer-Anforderung

Der externe Reviewer soll:

- nicht am bisherigen Schreiben oder internen Review des konkreten Manuskripts beteiligt gewesen sein,
- einen vollständigen Manuskript-Snapshot lesen können,
- seine Findings konkret am Text belegen,
- bei faktischen Plausibilitätsfragen optional aktuelle externe Quellen recherchieren können,
- keine Kenntnis früherer interner Findings benötigen.

Der konkrete Anbieter oder Modellname wird im Framework **nicht fest verdrahtet**.

## 3. Anti-Anchoring-Regel

Im ersten externen Durchlauf werden **keine internen Review-Ergebnisse, Finding-Listen oder Rework-Begründungen** mitgegeben.

Erlaubte Inputs:

- fixierter Manuskript-Snapshot,
- kanonische Story-/Figuren-/Recherche-Leitplanken, soweit für Konsistenzprüfung nötig,
- der externe Review-Auftrag,
- bei Bedarf konkrete reale Fachquellen für gesetzte Recherchegrenzen.

Nicht mitgeben:

- interne Raw-Findings,
- bereits diskutierte Schwachstellen,
- frühere Reviewer-Urteile,
- gewünschte Bestätigung einer bestimmten Hypothese.

Erst **nach** Abgabe des externen Reviews wird mit internen Findings verglichen.

## 4. Review-Scope

Der externe Reviewer prüft mindestens:

1. **Story-/Kausalitätskonsistenz**
   - Widersprüche, unmotivierte Folgen, fehlende Vorbereitung, unlogische Eskalationen.

2. **Figurenkonsistenz und Motivation**
   - glaubwürdige Entscheidungen, Beziehungsentwicklung, Wissensstände, Konsequenzen.

3. **Spannung / Pacing / Leserwirkung**
   - Längen, Wiederholungen, zu ähnliche Szenenträger, Expositionsballungen, Spannungsabfälle.

4. **Prosa-/Dialogmuster**
   - sichtbare Produktionsformeln, monotone Frage-Antwort-Choreografie, Erklär-Echos, künstliche Symmetrie, auffällige KI-Prosa-Muster.

5. **Plausibilität / Fachlichkeit**
   - konkrete Stellen, an denen institutionelle, technische, medizinische, rechtliche oder andere reale Mechaniken unglaubwürdig wirken.

6. **Finale / Payoff**
   - ob zentrale Leitfrage, Reversal, Figurenbogen und Schlusswirkung tatsächlich eingelöst werden.

7. **Blind Spots**
   - relevante Probleme, die aus den vorgegebenen Kategorien herausfallen.

## 5. Recherche-Nutzung

Wenn das externe Modell Web-/Research-Funktionen besitzt, gilt:

- Web-Recherche nur für **prüfbare reale Sachfragen**, nicht um literarischen Geschmack zu objektivieren.
- Externe Sachbehauptungen müssen mit konkreten Quellen belegt werden.
- Factual Finding und literarisches Finding werden getrennt gehalten.
- Ein externer Artikel überschreibt nicht automatisch die kanonische Near-Future-Story-Policy; geprüft wird, ob der Roman eine reale Behauptung macht oder bewusst Fiktion setzt.

## 6. Finding-Schema

Jeder Befund wird einzeln geliefert:

```text
finding_id: XR-XXX
location: <Kapitel/Szene/Stelle oder Bereich>
finding_type: <causality | character | information | chronology | pacing | repetition | dialogue | exposition | plausibility | research | finale | other>
severity: <blocker | major | minor>
problem: <konkret beobachtetes Problem>
text_evidence: <kurzer eindeutiger Text-/Stellenbezug>
impact: <konkrete Wirkung auf Logik, Figur oder Leser>
external_source: <nur falls ein Sach-Finding externe Recherche benötigt; sonst none>
recommended_rework_level: <prose | scene | beat | event | story_architecture | research | none>
```

Keine Gesamtpunktzahl und kein pauschales `8/10`.

## 7. Adjudikation

Externe Findings sind **advisory**.

Nach Rückgabe wird jedes Finding intern geprüft:

```text
disposition: confirmed | rejected | duplicate_known | accepted_tradeoff | needs_more_evidence
confirmed_severity: blocker | major | minor | none
correction_triggered: yes | no
notes: <kurze Evidenzbegründung>
```

Nur bestätigte Blocker/Major-Findings blockieren G4.

Ein externes Modell darf weder direkt Prosa umschreiben noch selbst den Gate-Status setzen.

## 8. Stop-Regel

Standardmäßig gibt es **einen externen Vollreview pro G4-Kandidat**.

Ein zweiter externer Vollreview wird nur durchgeführt, wenn:

- ein bestätigter externer Blocker/Major relevantes Rework ausgelöst hat, oder
- das erste Review nachweislich unvollständig/ungeeignet war.

Keine Endlosschleife aus Reviewer → Rework → neuer Reviewer → neues kosmetisches Rework.

Minor-Findings werden gesammelt dispositioniert und rechtfertigen allein keinen vollständigen neuen externen Review.

## 9. Datenschutz / Manuskriptweitergabe

Ein vollständiges externes Review bedeutet, dass das Manuskript an einen weiteren Dienst übergeben wird.

Vor Nutzung eines externen Modells ist deshalb bewusst zu entscheiden, ob dessen aktuelle Datenschutz-, Trainings-, Speicher- und Nutzungsbedingungen für das konkrete Manuskript akzeptabel sind.

Diese Prüfung betrifft den gewählten Dienst, nicht das Review-Verfahren selbst.

## 10. Projektartefakte

Ein echtes Buchprojekt verwendet dafür typischerweise:

- `EXTERNAL_REVIEW_TASK.md` – fixer, anbieteragnostischer Auftrag für das externe Modell,
- `EXTERNAL_REVIEW_RESULT.md` – unveränderte externe Befunde,
- `EXTERNAL_REVIEW_ADJUDICATION.md` – interne Disposition der Befunde.

Der Task muss den konkret geprüften Commit/Snapshot nennen.

## KISS-Regel

> Erst intern sauber machen, dann einen nahezu finalen Snapshot einem unabhängigen externen Modell ohne interne Finding-Liste geben. Externe Befunde anschließend evidenzbasiert adjudizieren. Keine Scores, kein automatisches Umschreiben und kein Reviewer-Karussell.
