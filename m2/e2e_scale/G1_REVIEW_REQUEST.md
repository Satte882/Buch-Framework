# G1 Review Request – SPERRFRIST M2

status: AWAITING_HUMAN_G1_DECISION
gate_name: Story-Architektur
prior_gate: `m2/e2e_scale/gates/G0.md`
prior_gate_ref: `20b62ee1962ddf723f8faf71843a98ac704e293f`
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`

## Zweck

G1 prüft die vollständige **Story-Architektur vor Beats und Szenenkarten**. Das Paket wurde horizontal entwickelt und enthält die für M2 geforderte zusätzliche Abhängigkeitskomplexität.

Noch nicht Gegenstand von G1 sind:

- Beats,
- konkrete Zuordnung auf genau 10 Szenen,
- Szenenkarten,
- Character States,
- G2-Review-Batches,
- Prosa.

Diese Ebenen dürfen erst nach menschlichem G1-APPROVE systematisch erzeugt werden.

## Zu prüfende Artefaktstände

- `STORY_PACKAGE.md` — blob `60427fe9ebc289074415373b520dcfe3170b9444`
- `STORY_BLOCKS.md` — blob `b0a2e798646f075a41d4f259cafe84fc6e3d4205`
- `EVENTS.md` — blob `b490932618b8da3d95de8091c3345f54144cac5f`
- `CHARACTERS.md` — blob `6eaeb1fdb2a9eef6eb13fe0cd98e686242abd343`
- `RESEARCH_REGISTER.md` — blob `0a4f457663e3c5244203c2a6324e51972744b645`

Zusätzlicher M2-Beobachtungsnachweis:

- `SEMANTIC_REVIEW_LOG.md` — blob `ee3af0256bd98ad942cd1290e231c7a3c0786838`

## Quantitativer M2-Korridor auf G1-Ebene

| Kriterium | Ist | M2-Minimum | Status |
|---|---:|---:|---|
| dramaturgische Bausteine | 12 | 10 | PASS |
| Ereignisse/Sequenzen | 30 Events / 12 Sequenzen | 24 Events | PASS |
| plotrelevante Rollen | 6 | 4 | PASS |
| szenenübergreifende Beziehungsentwicklungen | 3 | 2 | PASS |
| Informations-/Reveal-Stränge | 2 zentrale + Quellenschutz-Querschnitt | 2 | PASS |
| plotrelevante Rechercheabhängigkeiten | 2 | 2 | PASS |
| davon Blockierregel real entschieden | 2 | 1 | PASS |
| offene `blocking_now: yes` vor G1 | 0 | 0 | PASS |

## Storykern

SPERRFRIST trennt zwei zunächst gekoppelte Behauptungen:

- **T – technischer Befund:** Ein kritischer Failover-/Auslieferungsbefund bestand in einem roll-out-relevanten Release Candidate.
- **K – Wissen/Verantwortung:** Eine konkrete Führungsperson wusste vor der maßgeblichen Freigabe von genau diesem relevanten Befund.

Die Geschichte wird komplexer, weil neue Informationen T und K unterschiedlich verändern. Der späte Beleg stärkt T, widerlegt aber die konkrete K-Zuschreibung. Die finale Publikationsentscheidung lautet daher nicht „alles wahr/alles falsch“, sondern: belastbaren T-Kern veröffentlichen, ungesicherte K-Personenzuschreibung entfernen.

## Cross-Block-Komplexität

### Informationsstränge

1. **T-Strang:** technischer Befund → Versionsunsicherheit → Zweitbestätigung → Rolloutrelevanz → finaler Release-/Testbeleg.
2. **K-Strang:** frühe Verantwortungsannahme → Unternehmenswiderspruch → Chronologieproblem → Quelleninterpretation → Verteilerbeleg widerlegt konkrete Vorwissenszuschreibung.

### Beziehungsstränge

1. **Nora ↔ David:** Vertrauen → Timingkonflikt → pragmatische Annäherung → Restkonflikt nach verspäteter Veröffentlichung.
2. **Nora ↔ Jonas:** operatives Vertrauen → Quellenschutzfehler → Kontaktbegrenzung → fachliche Teilrehabilitation durch finale Versionsklärung.
3. **Nora ↔ Quelle A:** Schutz-/Vertrauensbasis → Zweifel an Interpretation → Schutzkrise → inhaltliche Abgrenzung bei weiter bestehendem Quellenschutz.

## Recherche – reale Blockierregel

### R-01 – journalistische/presserechtliche Plausibilität

Vor Klärung war die Frage **blocking_now: yes**, weil die Architektur entscheiden musste, ob eine engere Veröffentlichung trotz verbleibender Unsicherheit plausibel ist und welche Rolle Stellungnahme und Quellenvertraulichkeit spielen.

Nach Prüfung von Pressekodex, BVerfG-Leitplanken und § 53 StPO wurde die Architekturentscheidung getroffen; jetzt `blocking_now: no`.

### R-02 – technischer Systemkontext

Vor Klärung war die Frage **blocking_now: yes**, weil ein privater Anbieter sonst versehentlich als Betreiber/Entscheider realer amtlicher Warninfrastruktur hätte konstruiert werden können.

Nach BBK-Abgleich ist die Story auf eine fiktive vendorseitige, redundante Kommunikations-/Verteilplattform mit eigenen Releases und Tests begrenzt; reale MoWaS-/Cell-Broadcast-Prozesse werden nicht fiktional behauptet. Jetzt `blocking_now: no`.

## Wichtiger M2-Befund vor G1

Ein semantischer Self-Review derselben KI fand einen methodischen Fehler in der ersten Architekturversion:

> Der geplante späte Story-Reveal B11/E027 war fälschlich als Framework-Invalidierung interpretiert worden.

Das wurde vor G1 korrigiert. Ein innerhalb der von Anfang an bekannten Story geplanter Informationswechsel macht frühere Szenen mit entsprechendem Figurenwissen **nicht** stale.

Der echte M2-Backtracking-Test bleibt daher separat: Erst nach vorhandenen Downstream-Artefakten wird eine relevante kanonische Upstream-Annahme kontrolliert geändert; dann werden tatsächliche Abhängigkeiten und Rework gemessen.

Dieser Befund ist in `SEMANTIC_REVIEW_LOG.md` ausdrücklich als `same_chat_same_model_context`, `independent_review: no` dokumentiert und wird **nicht** als validierte semantische QA-Fähigkeit ausgegeben.

## G1-Reviewfragen

1. Trägt die Gesamtgeschichte über zwölf Bausteine und 30 Events, ohne bloß künstlich komplex zu wirken?
2. Bleiben T und K wirklich getrennte Belegketten, oder werden sie an irgendeiner Stelle unzulässig wieder zusammengeschoben?
3. Ist der späte Reversal „T stärker / konkrete K-Zuschreibung fällt“ dramaturgisch verständlich und nicht nur methodisch konstruiert?
4. Bleibt David ein legitimer publizistischer Gegenpol statt eines Tempo-Strohmanns?
5. Ist Miras Funktion plausibel als Eingrenzung und Publizierbarmachung statt als pauschale juristische Bremse?
6. Ist Jonas' Quellenschutzfehler glaubwürdig genug, ohne ihn künstlich inkompetent zu machen?
7. Bleibt Quelle A als unvollständig informierte, aber nicht betrügerische Quelle konsistent?
8. Tragen die drei Beziehungsentwicklungen genug Eigenlogik, um bei späteren 10 Szenen echte Cross-Batch-Abhängigkeiten zu erzeugen?
9. Sind R-01 und R-02 ausreichend geklärt, ohne unnötige juristische oder technische Detailtiefe in die Story zu ziehen?
10. Ist die korrigierte Trennung von **Story-Reversal** und **Framework-Backtracking** methodisch sauber?
11. Ist die Architektur vollständig genug, um danach horizontal mindestens 36 Beats und genau 10 Szenen abzuleiten, ohne neue G1-Plotentscheidungen erfinden zu müssen?
12. Würdest du genau die oben referenzierten fünf G1-Artefaktstände als Story-Architektur freigeben?

## Nächste menschliche Entscheidung

- `G1-APPROVE` — genau die referenzierten STORY_PACKAGE/STORY_BLOCKS/EVENTS/CHARACTERS/RESEARCH_REGISTER-Blobs werden freigegeben; danach werden alle Events horizontal in Beats überführt und anschließend genau 10 Szenenkarten + Character States für das gebündelte G2-Batching vorbereitet.
- `G1-REWORK` — konkrete Architektur-/Figuren-/Recherchebefunde überarbeiten; noch keine Beats oder Szenenkarten erzeugen.
- `G1-STOP` — M2 an dieser Stelle beenden.

**Wichtig:** Weder ChatGPT noch Checker dürfen G1 selbst freigeben.
