# M2 Observations – SPERRFRIST

status: COMPLETE
m2_issue: `#10`
date: 2026-08-30
scope: vollständiger M2-Lauf G0–G5 inklusive G2-Batching, kontrolliertem Invalidierungstest, repräsentativem G3-Prosa-Batch, Vollmanuskript und Produktion

## Messbarer Gesamtumfang

- Story Blocks: 12
- Events: 30
- Beats: 42
- Szenen: 10
- Character States: 31
- plotrelevante Figuren/Rollen: 6
- G2 Batch 1: 5 Szenen / 21 Beats / 13 Character States
- G2 Batch 2: 5 Szenen / 21 Beats / 18 Character States
- Human Gates abgeschlossen: G0–G5 = 6/6
- interne G2-Batches menschlich akzeptiert: 2/2
- Cross-Batch-Probleme im Gesamtcheck: 0
- Human-Rework in den beiden G2-Batches: 0
- kontrollierter Invalidierungstest: PASS
- G3 repräsentativer Prosa-Batch: 3 Szenen
- vollständiges Manuskript: 10 Szenen
- finaler M2-Manuskript-Audit: FAIL 0 / REVIEW 0 / INFO 36
- dokumentierte semantische Befundgruppen: 8
- davon reale Korrekturen: 8
- unabhängige semantische Reviews: 0
- kanonischer Produktionsbuild: Run #48 PASS
- finaler Repo-/Rebuild-Check: Run #49 PASS

## O-01 – fünf Szenen sind für diesen Fall als G2-Review-Batch praktikabel

Beide 5-Szenen-Batches konnten ohne Rückfrage und ohne Human-Rework akzeptiert werden. Ein belastbarer Zeitwert in Minuten wurde nicht erhoben und wird nicht nachträglich geschätzt.

Schlussfolgerung: Fünf Szenen sind für einen Stoff dieser Dichte ein brauchbarer Startwert, aber kein Framework-Standard. Die Batch-Grenze sollte zusätzlich an einem funktionalen Zustandswechsel liegen.

## O-02 – Volltext aller Character States ist bereits Kontextmüll

31 Character-State-Dateien direkt vorzulegen wäre unergonomisch. Praktisch nützlich waren ad-hoc, aus kanonischen Daten abgeleitete Sichten:

- Scene-Batch-Sicht,
- Information/Reveal-Sicht,
- Character-/Relationship-Sicht,
- expliziter Batch-Grenzzustand.

Eine separate Research Dependency View war im M2-Fall nicht wiederholt erforderlich.

Schlussfolgerung: Ein festes, nicht-kanonisches Review-Template für diese verdichteten Sichten ist durch M2 gerechtfertigt. Ein eigener Generator, neue Artefakttypen oder neue Gates sind nicht belegt.

## O-03 – Gesamtlogik blieb über zwei G2-Batches erhalten

Der Gesamtcheck S1–S10 fand 0 neue Cross-Batch-Widersprüche. Geprüft wurden insbesondere Chronologie, technische Evidenzkette, Verantwortungszuschreibung, Nora↔Jonas, Nora↔David, Quellenschutz und Recherchegrenzen.

Der Review erfolgte im selben Arbeitskontext und ist daher kein Beleg unabhängiger semantischer QA.

## O-04 – deterministische Checks skalierten und fanden reale Integrationsprobleme

Im Lauf wurden reale nicht-literarische Fehler sichtbar und korrigiert:

- G0/G1-Gate-Metadaten zunächst nicht vollständig vertragskonform,
- BT009-Placeholder-False-Positive auf legitimer Unsicherheitsbeschreibung,
- 10/10 Szenen-Provenienzen nach G2 deterministisch geprüft,
- G4-Manuskript als exakte Verkettung der zehn Drafts geprüft,
- G5-Quellblob und Produktionsoutput bytegenau geprüft.

Keine neue fachliche Gate- oder Pipeline-Stufe war dafür nötig.

## O-05 – kontrolliertes Backtracking funktioniert, aber die Provenienz ist zu grob

Die separate, nicht gemergte Teständerung an Jonas' Governance-Baseline erzeugte erwartungsgemäß:

- accepted + Drift → 10/10 BLOCK,
- explizit stale + derselbe Drift → 10/10 STALE_OK.

Damit ist stille Weiterverwendung verhindert.

Gleichzeitig wurden technisch 10/10 Szenen stale, obwohl die Änderung fachlich primär einen Teil des Jonas-Bogens betraf. Ursache: alle Szenen referenzieren den gesamten `CHARACTERS.md`-Blob.

Schlussfolgerung: Die file-level Provenienz ist sicher, aber für größere Bücher zu grobgranular. Vor einem 40+-Szenen-Lauf sollte dieses reale Skalierungsrisiko gezielt gehärtet werden.

## O-06 – same-context semantische Reviews erzeugten realen Wert, aber keine validierte QA

Dokumentiert wurden 8 konkrete Befundgruppen mit 8 realen Korrekturen:

- 1 Methodenfehler vor G1,
- 3 Befundgruppen im G3-Sample,
- 4 Befundgruppen im G4-Vollmanuskript.

Dazu gehörten unter anderem POV-Überschreitung, interne Label-Leaks, Rhythmusprobleme, eine zu frühe Publizierbarkeit in S6 und die explizite Sperrfristkorrektur auf 18:01 in S10.

Schlussfolgerung: Eine strukturierte semantische Review-Schicht ist sinnvoll zu prüfen. Nicht belegt sind unabhängige Trefferquote, Reproduzierbarkeit oder ein Quality Score.

## O-07 – G3 als repräsentativer Stil-Gate funktioniert

Vor Vollskalierung wurden S1, S5 und S8 als repräsentative Stil-Stichprobe geschrieben und geprüft. Nach Human `G3-APPROVE` wurde der Stil auf die restlichen Szenen skaliert.

Der Vollmanuskript-Review fand anschließend vier gezielte Rework-Punkte, aber keinen Bedarf, G2 neu zu öffnen oder den G3-Stil grundsätzlich zurückzunehmen.

## O-08 – Vollmanuskript und Produktion bleiben kontrollierbar

Der finale Manuskriptstand hat `FAIL=0 / REVIEW=0 / INFO=36`; alle zehn Draft-Provenienzen und die Manuskript-Provenienz waren vor G4 aktuell. Human G4 akzeptierte exakt den Manuskript-Blob `55753bb0ce177a80886343a8ac4e23a71de05c4a`.

G5 baute aus genau diesem Blob ein minimales HTML-Produktionsartefakt. Run #48 und Run #49 erzeugten denselben HTML-SHA-256 `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`.

## O-09 – kein ungeplanter fachlicher Framework-Ausbau war nötig

M2 benötigte keine zusätzlichen Human Gates, keine neue Story-Pipeline, keinen semantischen Score, keinen Agentenstack und keine DOCX/PDF/KDP-Pipeline.

Hinzu kamen ausschließlich Test-/Review-Artefakte und Integration/CI-Prüfungen auf Basis bestehender Mechaniken. Die ad-hoc Review-Sichten blieben bewusst nicht-kanonisch.

## Finale Skalierungsaussage

M2 zeigt belastbar, dass die v0.2-Pipeline von 3 auf 10 Szenen und von 7 auf 31 Character States skaliert, ohne fachliche Pipeline-Erweiterung zu erzwingen.

Nicht bewiesen ist weiterhin ein 40+-Szenen-/70.000+-Wörter-Romanlauf. Die real sichtbaren Risiken dafür liegen nicht primär in der Makro→Mikro-Pipeline, sondern in:

1. zu grober Provenienzgranularität,
2. Review-Kontextverdichtung,
3. fehlendem Nachweis unabhängiger semantischer QA.

Diese drei Punkte sind jetzt beobachtete Risiken und keine bloßen Vermutungen.
