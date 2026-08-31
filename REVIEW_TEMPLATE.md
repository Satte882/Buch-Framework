# Review-Template – nicht-kanonische Entscheidungsansicht

## Zweck

Dieses Template standardisiert die Review-Aufbereitung für größere Bücher, ohne eine neue Story-Ebene oder einen neuen Human Gate einzuführen.

Es verdichtet ausschließlich bereits vorhandene kanonische Artefakte für eine menschliche Entscheidung.

**Nicht-kanonisch bedeutet:**

- keine neue Story-Wahrheit,
- keine automatische Änderung von Szenen, Beats, Character States oder Recherche,
- kein eigener Gate,
- kein Ersatz für die zugrunde liegenden Artefakte,
- bei Widerspruch gilt immer die kanonische Quelle.

## Wann verwenden

Primär bei G2 und vergleichbaren gebündelten Reviews, wenn die Rohmenge aus Szenenkarten, Character States und Informationsabhängigkeiten unergonomisch wird.

M2 hat gezeigt, dass fünf Szenen als Review-Batch in einem komplexeren 10-Szenen-Fall praktikabel waren. Das ist **kein fester Standard**. Batch-Grenzen sollen zusätzlich an funktionalen Zustandswechseln liegen.

## Kanonische Inputs

Nur soweit für den konkreten Review nötig:

- Szenenkarten des Batches,
- referenzierte Beats,
- zugehörige Character States,
- relevante Informations-/Reveal-Stränge,
- relevante Rechercheabhängigkeiten,
- Zustand am Ende des vorigen Batches,
- bereits freigegebene Gate-Basis.

Nicht standardmäßig in den Review kippen:

- Volltext aller Character-State-Dateien des Buchs,
- vollständige Rechercheakten ohne aktuelle Relevanz,
- Erzeugungsdialog oder interne Begründungsprosa,
- historische/stale Artefakte ohne Review-Zweck.

## Review-Sicht A – Scene Batch

Pro Szene nur entscheidungsrelevante Punkte:

| Feld | Inhalt |
|---|---|
| Szene | ID + Arbeitstitel |
| Story-Funktion | Warum die Szene im Gesamtverlauf existiert |
| **Primary Dramatic Carrier** | dominante dramaturgische Form, z. B. clinical_action, personal_confrontation, data_review, governance_design, implementation_test, aftermath |
| zentrale Entscheidung / Veränderung | Was sich irreversibel oder relevant verschiebt |
| Leserwissen danach | Was der Leser nach der Szene belastbar weiß / nicht weiß |
| relevante Evidenz / Reveal | Welche Informationsstränge verändert werden |
| Character-/Relationship-Shift | Nur relevante Zustandsänderungen |
| offene fachliche Frage | Nur falls sie den Gate-Entscheid beeinflusst |

Der `Primary Dramatic Carrier` ist eine **Review-Projektion**, keine neue kanonische Story-Wahrheit. Er dient dazu, die Verteilung der Szenenformen über das ganze Buch sichtbar zu machen.

## Review-Sicht B – Information / Reveal

Für jeden relevanten Informationsstrang:

| Feld | Inhalt |
|---|---|
| Thread | z. B. T, K, Täterwissen, Motiv, Herkunft eines Belegs |
| Zustand vor Batch | belastbar / offen / geschwächt / widerlegt / unbekannt |
| Veränderung im Batch | konkrete Evidenz- oder Wissensverschiebung |
| Zustand nach Batch | neuer belastbarer Stand |
| darf noch nicht behauptet werden | Schutz vor vorgezogenem Wissen / Story-Drift |

Nur tatsächlich plotrelevante Threads aufnehmen. Keine künstliche Vollständigkeitsmatrix.

## Review-Sicht C – Character / Relationship

Nur Beziehungen oder Figurenbögen mit realer Veränderung im Batch:

| Feld | Inhalt |
|---|---|
| Figur / Beziehung | betroffene Einheit |
| Zustand vor Batch | Wissen, Haltung, Vertrauen oder Grenze |
| Druck / Ereignis | was den Zustand verändert |
| Zustand nach Batch | neuer gültiger Zustand |
| persistierende Kosten / offene Spannung | was ausdrücklich nicht zurückgesetzt wird |

Ziel ist Konsistenz, nicht vollständige Figurenbiografie.

## Review-Sicht D – Batch Boundary State

Am Ende jedes Batches ein kompakter Übergabezustand:

- **Story-/Evidenzstand:** Was ist jetzt belastbar, offen, geschwächt oder widerlegt?
- **Figuren-/Beziehungsstand:** Welche Änderungen müssen im nächsten Batch weitergelten?
- **Schutzgrenzen:** Welche Wissens-, Quellen-, Rechts- oder Recherchegrenzen bleiben aktiv?
- **offene Blocker:** Nur aktuell wirklich blockierende Punkte.
- **Startbedingung nächster Batch:** Welcher Zustand darf nicht versehentlich übersprungen oder zurückgesetzt werden?

## Review-Sicht E – Whole-Book Scene-Shape

Nach allen G2-Batches folgt eine **Gesamtsicht über S001–Sxxx**, nicht nur eine Addition der Batch-OKs.

Minimaler Output:

| Szene | Primary Carrier | direkt vorher gleicher Carrier? | Meeting/Review/Governance/Data? | bewusste Begründung bei Häufung |
|---|---|---|---|---|

Zusätzlich prüfen:

- mehr als 2 direkt aufeinanderfolgende Szenen mit praktisch gleichem Carrier,
- mehr als 4 Meeting-/Review-/Governance-/Data-Szenen in einem Fenster von 8 Szenen,
- neue Regel-/Governance-Stufen ohne Anwendung/Folge/Konflikt dazwischen,
- wiederholt dieselbe Erkenntnismechanik über mehrere Szenen.

**Wichtig:** Diese Werte sind Warnsignale. Sie erzeugen nicht automatisch `REWORK`. Ein Finding braucht eine konkrete Ermüdungs-/Redundanzwirkung.

## Review-Abschluss

Am Ende eines Review-Pakets:

```text
Batch: <Szenenbereich>
Review-Zweck: <z. B. G2 fachliche Teilprüfung>
Cross-Scene-Widersprüche: <n>
Cross-Batch-Widersprüche: <n / n.a.>
Scene-Shape-Risiken: <n / keine / Gesamtcheck ausstehend>
offene Blocker: <Liste / keine>
Rework erforderlich: <ja/nein + konkret>
neue Storyentscheidung erforderlich: <ja/nein>
Human-Entscheidung: <noch offen / internes Batch-OK / Gate-Entscheidung>
```

Beim **finalen G2-Abschluss** zusätzlich:

```text
Whole-Book Scene-Shape Review: <PASS | REWORK_REQUIRED>
begründete Überschreitungen der Heuristiken: <Liste / keine>
bestätigte strukturelle Majors: <n>
```

## G3-Sequenzcheck

Für längere Romane darf der G3-Review nicht nur isolierte Vorzeigeszenen betrachten.

Zusätzlich zu 2–3 repräsentativen Einzelszenen wird ein **zusammenhängender Mittelteil-Run von mindestens 6 Szenen** gelesen.

Der Review dokumentiert mindestens:

- wiederkehrende Dialogrhythmen,
- wiederkehrende Szenenchoreografien,
- Expositionshäufung,
- gleiche Übergangs-/Schlussmechaniken,
- Verhältnis Handlung / Analyse / Beziehung / Konsequenz.

## Grenzen

Dieses Template ist eine **Review-Projektion**, kein deterministischer Qualitätsnachweis.

Es darf nicht:

- fehlende kanonische Informationen erfinden,
- eine Storyentscheidung als geklärt markieren, die upstream offen ist,
- semantische Relevanz automatisch entscheiden,
- einen Human Gate ersetzen,
- aus einem internen Batch-OK einen neuen Gate `G2a/G2b/...` machen,
- aus einem bloßen Zählwert automatisch einen literarischen Fehler ableiten.

## KISS-Regel

> Zeige dem Menschen nur die Informationen, die er für die konkrete Entscheidung braucht – aber jede relevante Zustandsänderung und jedes manuskriptweite Verteilungsmuster genau einmal.
