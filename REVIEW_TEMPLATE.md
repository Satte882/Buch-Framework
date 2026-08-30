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
| zentrale Entscheidung / Veränderung | Was sich irreversibel oder relevant verschiebt |
| Leserwissen danach | Was der Leser nach der Szene belastbar weiß / nicht weiß |
| relevante Evidenz / Reveal | Welche Informationsstränge verändert werden |
| Character-/Relationship-Shift | Nur relevante Zustandsänderungen |
| offene fachliche Frage | Nur falls sie den Gate-Entscheid beeinflusst |

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

## Review-Abschluss

Am Ende eines Review-Pakets:

```text
Batch: <Szenenbereich>
Review-Zweck: <z. B. G2 fachliche Teilprüfung>
Cross-Scene-Widersprüche: <n>
Cross-Batch-Widersprüche: <n / n.a.>
offene Blocker: <Liste / keine>
Rework erforderlich: <ja/nein + konkret>
neue Storyentscheidung erforderlich: <ja/nein>
Human-Entscheidung: <noch offen / internes Batch-OK / Gate-Entscheidung>
```

## Grenzen

Dieses Template ist eine **Review-Projektion**, kein deterministischer Qualitätsnachweis.

Es darf nicht:

- fehlende kanonische Informationen erfinden,
- eine Storyentscheidung als geklärt markieren, die upstream offen ist,
- semantische Relevanz automatisch entscheiden,
- einen Human Gate ersetzen,
- aus einem internen Batch-OK einen neuen Gate `G2a/G2b/...` machen.

## KISS-Regel

> Zeige dem Menschen nur die Informationen, die er für die konkrete Entscheidung braucht – aber jede relevante Zustandsänderung genau einmal.
