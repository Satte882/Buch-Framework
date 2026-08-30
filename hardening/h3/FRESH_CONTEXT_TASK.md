# H3 Fresh-Context Holdout – Ausführungsauftrag

## Ziel

Führe einen **blinden, unabhängigen semantischen Review** eines historischen SPERRFRIST-Manuskriptstands durch.

Dieser Auftrag ist ein Methodentest. Du sollst keine Prosa verbessern und keine neue Story entwickeln.

## Unabhängigkeitsregel

Arbeite ausschließlich mit den unten ausdrücklich erlaubten GitHub-Artefakten.

**Nicht verwenden:**

- frühere Chats oder Erinnerungen zum Projekt,
- persönliche Kontext-/Memory-Retrievals,
- Issue-Kommentare,
- frühere Review-Dateien,
- Completion Reports,
- Git-Diffs,
- die aktuelle korrigierte Manuskriptfassung.

Falls du versehentlich einen verbotenen Input öffnest oder sein Inhalt bereits im aktuellen Gespräch steht, markiere das Ergebnis als `CONTAMINATED` und stoppe die Validierung.

## Repository

`Satte882/Buch-Framework`

## Zielartefakt

Prüfe **exakt diesen historischen Git-Blob**:

`d4a4225d76b3f8699660683cda26252ed4a2809c`

Der Blob enthält einen früheren vollständigen 10-Szenen-Manuskriptstand von SPERRFRIST.

Lies ihn direkt per Blob-SHA. **Nicht** stattdessen `m2/e2e_scale/MANUSCRIPT_v01.md` auf `main` lesen; diese Datei enthält einen späteren Stand.

## Erlaubte Review-Quellen

Du darfst ausschließlich diese kanonischen Quellen auf `main` verwenden:

1. `SEMANTIC_REVIEW_PROTOCOL.md`
2. `m2/e2e_scale/gates/G2.md`
3. `m2/e2e_scale/BEATS.md`
4. `m2/e2e_scale/scenes/S1.md` bis `m2/e2e_scale/scenes/S10.md`
5. alle Character-State-Dateien unter `m2/e2e_scale/character_states/`, **nur soweit sie zu S1–S10 gehören**
6. `m2/e2e_scale/RESEARCH_REGISTER.md`
7. `m2/e2e_scale/PROSE_PROFILE.md`
8. falls für eine konkrete Kausalitätsprüfung zwingend nötig: `m2/e2e_scale/EVENTS.md` und `m2/e2e_scale/STORY_PACKAGE.md`

## Verbotene GitHub-Quellen

Insbesondere **nicht öffnen**:

- `m2/e2e_scale/MANUSCRIPT_v01.md`
- `m2/e2e_scale/SEMANTIC_G3_SELF_REVIEW.md`
- `m2/e2e_scale/SEMANTIC_G4_SELF_REVIEW.md`
- `m2/e2e_scale/SEMANTIC_REVIEW_LOG.md`
- `m2/e2e_scale/M2_COMPLETION_REPORT.md`
- `m2/e2e_scale/M2_OBSERVATIONS.md`
- `m2/e2e_scale/M2_REVIEW_OBSERVATIONS.md`
- `m2/e2e_scale/PROSA_AUDIT_G4.md`
- alle Issue-/PR-Kommentare zu M1/M2/Hardening
- alle Commits/Diffs, die den historischen Blob mit einem späteren Stand vergleichen

## Review-Auftrag

Prüfe den historischen Manuskript-Blob gegen die erlaubten kanonischen Quellen nach `SEMANTIC_REVIEW_PROTOCOL.md`.

Fokus:

1. Kausalität / Story-Wahrheit
2. Information / Reveal-Reihenfolge
3. Figuren-/Beziehungs-/Konsequenzkontinuität
4. Chronologie / Timing / Sperrfrist
5. Recherche-/Quellenschutz-/Wissensgrenzen
6. Prosa gegen G2-kanonische Planung
7. klarer Verstoß gegen das freigegebene `PROSE_PROFILE.md`, aber nur wenn konkret und textlich lokalisierbar

Suche **konkrete Widersprüche oder belastbare Risiken**, keine Alternativideen.

## Keine Rewrite-Aufgabe

- keine neue Szene schreiben,
- keine Stelle umformulieren,
- keine neuen Twists/Figuren/Belege erfinden,
- keine Qualitätsnote vergeben,
- keine Confidence-Scores.

## Ausgabeformat

Beginne mit:

```text
review_status: CLEAN_FRESH_CONTEXT | CONTAMINATED
review_target: d4a4225d76b3f8699660683cda26252ed4a2809c
```

Wenn `CONTAMINATED`: Grund nennen und keine Findings bewerten.

Wenn sauber: jeden Befund exakt so ausgeben:

```text
finding_id: SR-001
location: <Szene/Stelle>
finding_type: <causality | information | character | chronology | research_boundary | prose_drift | style_profile>
problem: <konkreter Befund>
canonical_evidence: <konkreter erlaubter Pfad + relevante ID/Angabe>
impact: <warum das für die Story-/Prosa-Konsistenz relevant ist>
recommended_rework_level: <prose | scene | beat | event | story_architecture | research | none>
```

Danach:

```text
finding_count: <n>
reviewer_note: <maximal 5 Sätze zu Grenzen des Reviews>
```

Wenn keine belastbaren Findings vorliegen, `finding_count: 0` ausgeben. Keine Probleme erfinden, um den Test zu bestehen.

## Wichtig

Du kennst den späteren Korrekturstand absichtlich nicht. **Versuche nicht, ihn zu rekonstruieren oder zu suchen.** Der Blind-Review wird erst nach deiner Abgabe gegen einen zurückgehaltenen historischen Benchmark dispositioniert.
