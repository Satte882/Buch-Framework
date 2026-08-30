# M2 COMPLETION REPORT – SPERRFRIST

status: PASS
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`
date: 2026-08-30
framework_baseline: v0.2
final_human_gate: G5 APPROVE
g5_ref: `89f4cb5d84d0fb3b2935f3dc7dc33d5604f763be`

## Ergebnis in einem Satz

M2 hat die bestehende v0.2-Arbeitsweise ohne neue fachliche Pipeline oder zusätzliche Gates erfolgreich von 3 auf 10 Szenen skaliert und dabei zwei reale Skalierungsengpässe sichtbar gemacht: verdichteter Human-Review wird praktisch notwendig und file-level Provenienz erzeugt einen zu großen technischen Invalidierungsradius. Eine unabhängige semantische QA-Fähigkeit ist weiterhin nicht validiert.

## Messbarer M2-Abschluss

```text
10-Szenen-Testfall vollständig: PASS
Dramaturgische Komplexitätsanforderungen erfüllt: PASS
Makro→Mikro-Arbeitsfolge eingehalten: PASS
G0–G5 vollständig: PASS
G2 in mehreren Review-Batches real durchgeführt: PASS
G2-Batch-Größe getestet: 5 Szenen
Cross-Batch-Probleme gefunden: 0
Ad-hoc-Review-Sichten tatsächlich benötigt: Scene Batch; Information/Reveal; Character/Relationship; Batch-Grenzzustand
Relevante Upstream-Änderung + Invalidierung real durchlaufen: PASS
Manueller Review-Aufwand dokumentiert: PASS – qualitativ; keine belastbare Minutenmessung erhoben
Semantische Review-Befunde dokumentiert: 8
Davon reale Korrekturen ausgelöst: 8
Neue Framework-Funktionen während M2 ungeplant erforderlich: keine fachlichen Funktionen
Deterministische CI nach Abschluss: PASS – Run #49
Empfehlung für Review-Batching: 5 Szenen waren praktikabel; funktionale Zustandsgrenze zusätzlich berücksichtigen; kein harter Standard
Empfehlung für feste Review-Sichten: ein nicht-kanonisches Review-Template aus den vier tatsächlich genutzten Sichten; kein neuer Gate und zunächst kein Generator
Empfehlung für semantische QA als nächster Schritt: unabhängiges Review-Protokoll gezielt validieren; noch kein Score/LLM-as-a-Judge
M2 Gesamt: PASS
```

## Komplexitätsnachweis

Issue #10 verlangte mehr als eine bloße Verlängerung des M1-Falls. SPERRFRIST erreicht:

- 10 aktive Szenen,
- 12 dramaturgische Story Blocks,
- 30 Events in 12 Sequenzen,
- 42 Beats,
- 6 plotrelevante Rollen,
- 31 Character-State-Dateien,
- mehrere szenenübergreifende Figuren-/Beziehungsentwicklungen,
- getrennte technische und persönliche Verantwortungs-/Reveal-Stränge,
- zwei reale Recherchefelder R-01/R-02 mit expliziter Blockierentscheidung,
- eine kontrollierte relevante Upstream-Änderung nach vorhandenem G2-Downstream.

Damit ist der geforderte Testkorridor erfüllt, ohne zusätzliche Figuren, Twists oder Füllereignisse nur zur Zahlenerreichung einzuführen.

## Human Gates

- G0 – Konzept: APPROVE — `gates/G0.md` blob `7be39a775f81b1c59d5d35f7aa6a9571a182ab54`
- G1 – Story-Architektur: APPROVE — `gates/G1.md` blob `4cef4778ec307c00a485539bc21633dda248d73e`
- G2 – Prose Ready: APPROVE — `gates/G2.md` blob `dc4123e5e83302fed08fdac6142fcf541b2f98f1`
- G3 – Prosa-Stil: APPROVE — `gates/G3.md` blob `17330cb19c3b6b25d47f06868f690bc1828445c3`
- G4 – Manuskript: APPROVE — `gates/G4.md` blob `0d462e477fceb319ed7db9146e1c56f66b1fa6ef`
- G5 – Produktion: APPROVE — `gates/G5.md` blob `89f4cb5d84d0fb3b2935f3dc7dc33d5604f763be`

Alle sechs fachlichen Gates wurden real durch den Menschen entschieden. Die zwei G2-Review-Batches blieben interne Review-Pakete und wurden nicht zu G2a/G2b-Gates umgedeutet.

## Sieben M2-Prüffragen

### 1. Makro→Mikro

**Antwort: PASS.**

Der Testfall wurde horizontal als Buchidee → 12 Story Blocks → 30 Events → 42 Beats → 10 Szenenkarten + 31 Character States entwickelt. Prosa wurde erst nach Human G2 begonnen. Es war keine vorzeitige vertikale Ausarbeitung nötig, um die Story-Architektur zu schließen.

### 2. Batch-Ergonomie

**Antwort: Für diesen Fall sind fünf Szenen praktisch prüfbar.**

S1–S5 und S6–S10 wurden jeweils als 5-Szenen-Paket menschlich akzeptiert, ohne Human-Rework in den beiden Batch-Entscheidungen. Ein Zeitwert in Minuten wurde nicht erhoben und wird nicht rekonstruiert.

Wichtiger als die Zahl allein war die funktionale Grenze nach S5. Empfehlung: fünf Szenen als brauchbarer Startwert für vergleichbare Dichte, aber Batch-Grenzen zusätzlich an echten Zustandswechseln ausrichten. Kein Framework-Standard `5`.

### 3. Gesamtlogik

**Antwort: Im M2-Fall ging durch das Batching keine nachweisbare Gesamtlogik verloren.**

Der Gesamtcheck S1–S10 fand 0 neue Cross-Batch-Widersprüche. Geprüft wurden Chronologie, T/K-Informationslogik, Figuren-/Beziehungsentwicklung, Quellenschutz und Recherchegrenzen.

Einschränkung: Der Gesamtcheck erfolgte im selben Chat-/Modellkontext. Das Ergebnis belegt die Praktikabilität des Batching, nicht die Trefferquote unabhängiger semantischer QA.

### 4. Backtracking

**Antwort: PASS, mechanisch beherrschbar – mit realem Skalierungsproblem.**

Die kontrollierte Änderung an Jonas' Governance-Baseline nach G2 erzeugte:

- unveränderte `accepted`-Manifeste + Drift → 10/10 BLOCK,
- explizit `stale` + derselbe Drift → 10/10 STALE_OK.

Damit verhindert das Framework stille Weiterverwendung zuverlässig.

Gleichzeitig wurden technisch 10/10 Szenen invalidiert, obwohl der fachliche Rework-Radius voraussichtlich kleiner gewesen wäre. Ursache ist die Referenz auf den gesamten `CHARACTERS.md`-Blob. Dieser zu große technische Blast Radius ist ein real beobachteter Skalierungsengpass.

### 5. Review-Aufwand

**Antwort: qualitativ dokumentiert; quantitative Zeitmessung fehlt.**

Beobachtet:

- G2: zwei 5-Szenen-Batches, beide ohne Human-Rework akzeptiert; Volltext aller 31 States wäre unergonomisch gewesen.
- G3: repräsentative 3-Szenen-Stichprobe S1/S5/S8 vor Vollskalierung; drei reale semantische/Stil-Befundgruppen korrigiert.
- G4: vollständiges 10-Szenen-Manuskript; vier gezielte Befundgruppen korrigiert, danach Audit FAIL=0 / REVIEW=0 / INFO=36 und Human APPROVE.
- G5: reproduzierbarer minimaler HTML-Build; kein Manuskript-Rework nötig.

Damit ist der Review-Aufwand in Art und Rework-Last dokumentiert. Ein belastbarer Minuten-/Stundenbenchmark wurde in M2 nicht erhoben.

### 6. Review-Kontext

**Antwort: verdichteter Entscheidungs-Kontext ist nützlich; Rohartefakte allein erzeugen bereits bei 10 Szenen unnötige Last.**

Wiederholt nützlich waren:

- Story-Funktion und zentrale Entscheidung je Szene,
- Leserwissen/Informationsstand danach,
- T/K-Entwicklung,
- relevante Figuren-/Beziehungsverschiebungen,
- expliziter Zustand an der Batch-Grenze.

Nicht sinnvoll war, alle 31 Character-State-Dateien als Volltext in den Human Review zu kippen. Eine separate Research-Dependency-Sicht war im M2-Fall nicht wiederholt erforderlich.

### 7. Review-Sichten

**Antwort: Ja, aber als verdichtete Review-Projektion – nicht als neue kanonische Ebene.**

Tatsächlich wiederholt gebraucht wurden:

1. Scene Batch View,
2. Information/Reveal View,
3. Character/Relationship View,
4. Batch Boundary State.

Empfehlung: daraus ein festes, nicht-kanonisches Review-Template machen. Kein eigener Human Gate, keine neue Story-Wahrheit, zunächst kein Generator. Eine Research Dependency View bleibt ad hoc, solange kein wiederholter Bedarf belegt ist.

## Semantische Review-Evidenz

M2 dokumentiert insgesamt 8 konkrete Befundgruppen, die 8 reale Korrekturen ausgelöst haben:

- 1 methodischer Fehler vor G1: Story-Reveal vs. Framework-Invalidierung,
- 3 G3-Befundgruppen: POV-Grenze, interne Label-Leaks, überkonstruierte Rhythmusstellen,
- 4 G4-Befundgruppen: S4 Negationsfolge, S6 zu frühe Publizierbarkeit, S9 Rhythmus, S10 Sperrfrist/Rhythmus.

Alle Reviews erfolgten im selben Arbeitskontext. Daher gilt weiterhin:

- unabhängige semantische Reviews: 0,
- validierte Trefferquote: nicht vorhanden,
- reproduzierbare semantische QA-Methode: nicht nachgewiesen,
- LLM-as-a-Judge/Quality Score: durch M2 nicht gerechtfertigt.

M2 liefert aber erstmals reale Evidenz, dass strukturierte semantische Reviews genügend Nutzen haben, um einen bewusst unabhängigen Review-Ansatz gezielt zu testen.

## Deterministische und Produktions-Evidenz

- G2 Pipeline: READY_FOR_PROSE nach realer CI.
- 10/10 G2-Szenen-Provenienzen: OK auf unverändertem main.
- Invalidierungstest: PASS.
- G3 Sample: FAIL=0 / REVIEW=0 / INFO=14; 3/3 Draft-Provenienzen OK.
- G4 Manuskript: exakte Verkettung 10/10 aktueller Drafts; FAIL=0 / REVIEW=0 / INFO=36.
- G4-approved Manuskript-Blob: `55753bb0ce177a80886343a8ac4e23a71de05c4a`.
- G5 Run #48: 60/60 Tests PASS, G4-Blob bestätigt, bytegenauer HTML-Build PASS.
- HTML SHA-256: `233d4285f020a070ee6128dac8a15b2d4c87cdf0136524b14821daa228ea2acb`.
- finaler Dokumentations-/Rebuild-Run #49: PASS und erneut derselbe HTML-SHA-256.

## Beobachtete Probleme vs. nicht belegte Vermutungen

### Real beobachtet

- 31 State-Dateien machen Volltext-Review unergonomisch.
- kompakte Review-Sichten wurden praktisch in beiden G2-Batches und im Gesamtcheck benötigt.
- file-level Provenienz erzeugte bei einer fachlich engeren Character-Änderung technisch 10/10 stale.
- same-context Reviews fanden reale korrigierbare Fehler.
- deterministische Checks fanden reale Metadaten-/Placeholder-/Drift-Probleme.

### Noch nicht belegt

- welche Batch-Größe bei 40+ Szenen optimal ist,
- wie viele Stunden Human Review ein 70.000+-Wörter-Roman tatsächlich benötigt,
- ob unabhängiger LLM-Review zusätzliche Fehler zuverlässig findet,
- welche Trefferquote eine semantische Review-Methode hat,
- ob Review-Projektionen einen Generator benötigen,
- ob DOCX/PDF/KDP-Produktion zusätzliche Framework-Probleme erzeugt.

## Definition of Done – Issue #10

1. komplexerer 10-Szenen-Testfall durch reale Pipeline: **PASS**
2. sieben Prüffragen anhand des Laufs beantwortet: **PASS**
3. beobachtete Skalierungsprobleme von Vermutungen getrennt: **PASS**
4. keine unbelegte neue Framework-Funktion rückwirkend als notwendig erklärt: **PASS**
5. messbarer M2-Abschlussbericht vorhanden: **PASS**
6. Entscheidung für den nächsten Schritt klar: **PASS**

## Entscheidung nach M2

**Kein M3-Testbuch. Nicht direkt unverändert in einen 40+-Szenen-Roman starten.**

Vor dem echten Buch-3-/Romanlauf ist ein kleines, evidenzbasiertes Hardening-Paket sinnvoll:

1. **Provenienzgranularität / Impact-Disposition:** den real beobachteten 10/10-Blast-Radius reduzieren, ohne semantische Relevanz automatisch vorzutäuschen.
2. **Festes Review-Template:** Scene Batch + Information/Reveal + Character/Relationship + Batch Boundary als nicht-kanonische Sicht standardisieren; kein neuer Gate, zunächst kein Generator.
3. **Unabhängiges semantisches Review-Protokoll:** Erzeugungs- und Review-Kontext bewusst trennen, Befunde/Human-Disposition/Rework messen; noch kein Score und keine automatische Rewrite-Schleife.

Danach ist der sinnvollere nächste Skalierungstest **der echte Roman selbst in kontrollierten Batches**, nicht ein weiteres künstliches M3-Mini-/Mittelbuch.

## Schlussbewertung

M2 hat seinen Zweck erfüllt. Die Kernpipeline ist bei zehn Szenen nicht gebrochen und musste fachlich nicht erweitert werden. Die jetzt sichtbaren Risiken liegen an den Rändern der Skalierung – Review-Ergonomie, Abhängigkeitsgranularität und unabhängige semantische Qualitätssicherung – und können deshalb gezielt statt spekulativ bearbeitet werden.

**M2 Gesamt: PASS.**
