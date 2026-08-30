# G2 Review Request – SPERRFRIST M2

status: AWAITING_HUMAN_G2_DECISION
gate_name: Prose Ready
prior_gate: `m2/e2e_scale/gates/G1.md`
prior_gate_ref: `4cef4778ec307c00a485539bc21633dda248d73e`
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`
review_model: 2 internal batches à 5 scenes + overall S1-S10 check
batch_1_result: `G2-BATCH1-OK`
batch_2_result: `G2-BATCH2-OK`

## Zweck

G2 prüft, ob **alle zehn Szenen gemeinsam Prose Ready** sind: Ein Autor soll jede Szene schreiben können, ohne dabei noch eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung erfinden zu müssen.

Die zwei Batch-OKs waren nur ergonomische Teilreviews. Diese Datei ist der erste eigentliche Human-Gate-Entscheidungspunkt G2.

Noch nicht Gegenstand von G2 sind Prosa-Stil, fertiges Manuskript oder Produktion.

## Kanonische Downstream-Basis

- `BEATS.md` — blob `ea40689e3a5e7439a0d460612e37be6f39d3b73a`
- `RESEARCH_REGISTER.md` — G1-freigegebener blob `0a4f457663e3c5244203c2a6324e51972744b645`

## Szenenbestand

| Szene | Blob | Beats | Character States | Batch |
|---|---|---:|---:|---|
| S1 – Das Dossier | `48d16bd81e144a290a4fb2f0c8435c69c6fba2c4` | 4 | 2 | 1 |
| S2 – Zwei Behauptungen | `d91ba1a11acf9b4e394d8a0dd27e7c11f4e620a7` | 4 | 3 | 1 |
| S3 – Die falsche Version | `1769ec3c6fcee99db9fd6b784dd8dc092155906a` | 5 | 3 | 1 |
| S4 – Zweite Quelle | `1f8b42c69833fe18bf983ea180a5800c93527077` | 4 | 2 | 1 |
| S5 – Der Preis der Anfrage | `d761bd6eaf254cb9ac46b66c78b9384d818b477f` | 4 | 3 | 1 |
| S6 – Die engere Story | `01b30b0daf68e1dca76297aca2ad7077c24ec1a7` | 5 | 5 | 2 |
| S7 – Quelle ist nicht Wahrheit | `3e0ae1b510efbc59790840b9cdcb7d9df36f6172` | 4 | 2 | 2 |
| S8 – Ein Beleg, zwei Wirkungen | `944e557b761fad15dfdc68b850a578d8d0e3aeb9` | 5 | 4 | 2 |
| S9 – Zu spät | `66599e6a50745eec2d65bd2656b3e45f497a9765` | 3 | 2 | 2 |
| S10 – Veröffentlichen | `7a581c12a245015737155521d85012e7988da222` | 4 | 5 | 2 |

**Gesamt:** 10 Szenen, 42 Beats, 31 Character States.

Alle Szenen stehen vor Human Gate G2 weiterhin auf `experience_status: pending_human_review`.

## Interne Batch-Reviews

- Batch 1 S1–S5: `G2-BATCH1-OK`, Result `G2_BATCH_1_RESULT.md`.
- Batch 2 S6–S10: `G2-BATCH2-OK`, Result `G2_BATCH_2_RESULT.md`.

Beide Entscheidungen stammen vom Menschen. Keines der Batch-OKs ist ein eigenständiger Human Gate.

## Gesamtcheck S1–S10

### 1. Chronologie

Die Szenen verlaufen ohne Rücksprung oder widersprüchliche Zeitlage:

09:15 → 10:00 → 11:00–11:45 → 12:10 → 12:45–13:15 → 14:00–14:45 → 15:05 → 16:10–16:45 → 17:35 → nach 18:00.

Die in S1 vereinbarte 18-Uhr-Sperrfrist bleibt bis S10 aktiv; veröffentlicht wird erst danach.

### 2. Informationsstrang T – technischer Befund

S1 potenzieller Befund → S2 erster technischer Beleg → S3 Versionsbruch → S4 unabhängige technische Bestätigung → S5 keine neue Sachbehauptung → S6 aktueller Rolloutbezug + technische Eingrenzung → S7 kein neuer T-Beleg → S8 finale Release-/Test-Brücke → S9 Konkurrenz verändert eigene Evidenz nicht → S10 enger T-Kern wird publiziert.

Keine Szene setzt T früher voraus, als es der Informationsstand erlaubt.

### 3. Informationsstrang K – Wissen/Verantwortung

S1 zunächst mit T gekoppelt → S2 eigene Belegkette → S3 konkrete Gegenbehauptung → S4 Chronologie schwächt K → S5 kein neuer K-Beleg → S6 nur offene Frage → S7 Quelle A besitzt kein direktes Eigenwissen für K → S8 konkrete Personenzuschreibung wird zeitlich widerlegt → S9 keine neue eigene K-Evidenz → S10 K bleibt außerhalb der Tatsachenbehauptung.

T und K werden nach S2 nicht unzulässig wieder zusammengeschoben.

### 4. Nora ↔ Jonas

Fachvertrauen → frühe technische Korrektur → reale Quellenschutzpanne → externe Kontaktgrenze → interne Weiterarbeit → finale Dokumentarbeit → fachliche Teilrehabilitation.

Der S8-Beleg entsteht aus bestehendem internem Dokumentpfad; S5 wird nicht heimlich rückgängig gemacht. Kompetenzvertrauen steigt wieder, Autonomievertrauen wird nicht vollständig resettiert.

### 5. Nora ↔ David

Legitimer Timingkonflikt → Annäherung über kleinere belastbare T-Story → gemeinsamer Evidenzrahmen → realer First-Mover-Verlust → Veröffentlichung wird mitgetragen, Kostenbewertung bleibt unterschiedlich.

David wird weder zum Sorgfaltsgegner noch am Ende künstlich harmonisiert.

### 6. Nora ↔ Quelle A

Schutzversprechen → wachsende Deutungsdistanz → Schutzkrise durch Recherchehandlung → direkte Trennung von Quellenschutz und redaktioneller Zustimmung → Restkonflikt nach Veröffentlichung.

Quelle A bleibt ehrliche, teilweise fehlinterpretierende Quelle und wird nicht nachträglich zum Täuscher umgeschrieben.

### 7. Quelle B / Mira / Recherchegrenzen

Quelle Bs Schutzbedingung bleibt aktiv; identifizierende Details werden nicht nachträglich veröffentlicht.

Mira begrenzt Aussageformen und trägt später die engere Fassung mit, löst aber nicht selbst den Evidenzfall.

R-01 und R-02 sind geklärt; es existiert keine offene `blocking_now: yes`-Rechercheabhängigkeit.

### 8. Story-Reversal vs. Framework-Backtracking

S8 ist ein von Anfang an kanonisch geplanter Story-Reversal: derselbe Beleg stärkt T und widerlegt konkrete K.

Das ist weiterhin **keine** Framework-Invalidierung. Der separate M2-Backtracking-Test folgt erst nach einem vorhandenen freigegebenen Downstream-Stand als kontrollierte Änderung einer kanonischen Upstream-Annahme.

## Ergebnis des Gesamt-Self-Reviews

review_context: same_chat_same_model_context
independent_review: no
cross_batch_conflicts_found: 0
new_story_decisions_required: 0
open_research_blockers: 0
human_batch_reworks: 0

Dieser Gesamtcheck wird nicht als validierte semantische QA-Fähigkeit des Frameworks ausgegeben. Er ist ein ad-hoc Self-Review zur Vorbereitung des Human Gate.

## Skalierungsbefund bis G2

Der 10-Szenen-Fall zeigt bereits einen Unterschied zu M1:

- 31 Character-State-Dateien sind als direkte Human-Review-Eingabe zu viel Detailkontext.
- Die beiden 5-Szenen-Pakete waren dagegen mit verdichteter Sicht praktisch handhabbar.
- Tatsächlich genutzt wurden ad hoc: Scene Batch View, Information/Reveal View und Character/Relationship View.
- Eine separate Research Dependency View war bisher nicht nötig.
- Der explizite Übergabezustand S5→S6 war wichtiger als das erneute Lesen aller Batch-1-State-Dateien.
- Neue Framework-Funktionalität war dafür nicht erforderlich.

Details stehen in `M2_OBSERVATIONS.md`.

## Was G2-APPROVE bedeuten würde

Mit `G2-APPROVE` werden genau die oben referenzierten 10 Szenenkarten zusammen mit ihren 31 referenzierten Character States, `BEATS.md` und dem geklärten Research-Stand als **Prose Ready** freigegeben.

Danach werden:

1. ein echter `gates/G2.md`-Record geschrieben,
2. die zehn Szenen auf `experience_status: human_reviewed_ready` gesetzt,
3. der bestehende deterministische Pipeline-Checker gegen den vollständigen M2-Stand ausgeführt/über CI abgesichert, sobald ein echter G2-Record existiert,
4. der separate kontrollierte M2-Upstream-Änderungs-/Invalidierungstest durchgeführt, bevor der Lauf als Skalierungsnachweis abgeschlossen wird,
5. erst anschließend der Prosa-/G3-Teil weitergeführt.

## G2-Reviewfragen

1. Ist die 10-Szenen-Kette als Ganzes klar genug, dass beim Schreiben keine relevante Storyentscheidung mehr erfunden werden muss?
2. Bleiben T und K über alle zehn Szenen sauber getrennt und zeitlich nachvollziehbar?
3. Tragen die drei zentralen Beziehungsentwicklungen ohne Widerspruch über die Batch-Grenze?
4. Ist S5→S6 als Übergang belastbar, insbesondere Jonass Kontaktgrenze und die noch fehlende RC-Brücke?
5. Funktioniert S8 als Reversal, ohne frühere Figurenkenntnis rückwirkend falsch zu machen?
6. Bleiben Quellenschutz und Recherchegrenzen bis S10 konsistent?
7. Ist die finale engere Veröffentlichung eine Konsequenz der Evidenzkette statt eine neue späte Plotentscheidung?
8. Ist der Gesamtbestand aus 42 Beats, 10 Szenen und 31 Character States fachlich ausreichend geschlossen für Prosa?
9. Ist die Review-Bündelung 5+5+Gesamtcheck für diesen M2-Fall praktikabel genug, um G2 jetzt als Ganzes zu entscheiden?

## Nächste menschliche Entscheidung

- `G2-APPROVE` — genau der referenzierte Gesamtstand wird Prose Ready; danach kein stilles Story-Rewrite in Prosa.
- `G2-REWORK` — konkrete Gesamt-/Cross-Batch-Befunde bearbeiten; Prosa bleibt gesperrt.
- `G2-STOP` — M2 an dieser Stelle beenden.

**Wichtig:** Nur der Mensch kann G2 freigeben.
