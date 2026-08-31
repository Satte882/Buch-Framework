# Finaler Prosa- und Rhythmuspass

## Zweck

Diese Datei operationalisiert die aus `NORMALFALL` gewonnenen Anti-KI-/Rhythmus-Lessons für zukünftige Bücher.

Die historische Evidenz und die abgeleiteten Muster stehen in `ANALYSE_ANTI_KI_PROSA_NORMALFALL.md`. Die mechanisch prüfbaren Regeln stehen in `PROSA_REGELMATRIX.md`.

Diese Datei beantwortet eine andere Frage:

> **Wie wird ein vollständiges Manuskript unmittelbar vor dem finalen G4-Freeze noch einmal horizontal auf Satzbau, Rhythmus, Dialogtakt und sichtbar modellhafte Prosa geprüft und chirurgisch überarbeitet?**

Der Pass ist **kein neues Human-Gate**. Er ist ein verbindlicher Arbeitsschritt innerhalb von G4.

---

## 1. Position in der Pipeline

Verbindliche Reihenfolge für ein vollständiges Manuskript:

`Vollprosa → Gesamtmanuskript-Review → Finding-Adjudikation/Rework → finaler Prosa- und Rhythmuspass → Regression/Fresh-Context-Check → G4-Freigabe → G5-Produktion`

Wird ein relevantes Prosa-/Rhythmusproblem erst **nach** G4 oder G5 erkannt, gilt:

- reine Prosaänderung → **G4 wieder öffnen**;
- bestehende G5-Artefakte → **stale**, bis G4 erneut freigegeben und G5 neu gebaut wurde;
- keine Rückkehr zu G2/G3, solange Plot, Szene, Beat, Figurenlogik und Informationsarchitektur unverändert bleiben.

---

## 2. Scope

Der Pass darf verändern:

- Satzbau und Satzlänge,
- Absatzrhythmus,
- Dialogtakt,
- Wiederholungen,
- Mikro-Choreografie,
- Filterformulierungen,
- erklärende Nachsätze,
- rhetorische Symmetrie,
- unnötige Methodik-/Beweisführungsprosa,
- Satzzeichen im Rahmen des aktivierten Prosa-/Sprachprofils.

Der Pass darf **nicht still verändern**:

- Plot,
- Szenenfunktion,
- Beat-Reihenfolge,
- Kausalität,
- Figurenentscheidung,
- Faktenlage,
- medizinische/juristische/technische Aussage,
- Informationsstand von Figur oder Leser,
- Ende oder zentrale Story-Anker.

Wenn eine notwendige Verbesserung eine dieser Ebenen berührt, wird gemäß Backtracking-Regel zur zuständigen Upstream-Ebene zurückgekehrt.

---

## 3. Grundregel

> **Nicht Sätze verschönern. Wiederkehrende Mechanik unsichtbar machen.**

Ein einzelner kurzer Satz, eine Negation, ein `wusste`, ein Blick oder ein knapper Dialogwechsel ist kein Fehler.

Problematisch wird ein Stilmittel, wenn es als **wiederkehrende Produktionsformel** über Absätze, Kapitel oder das Gesamtmanuskript sichtbar wird.

Deshalb wird immer in zwei Ebenen geprüft:

1. **lokal:** trägt die Formulierung in dieser konkreten Situation?
2. **horizontal:** wiederholt der Roman dieselbe Konstruktion so häufig, dass der Leser das Muster bemerkt?

---

## 4. Pass A – mechanischer Baseline-Audit

Vor jeder Änderung wird der aktuelle Manuskriptstand fixiert und gemessen.

Mindestens erfassen:

- Szenen-/Kapitelanzahl und Reihenfolge,
- Wortzahl,
- verbotene Hard-Guard-Zeichen/-Tokens des aktiven Profils,
- `dialogue_pingpong`,
- `staccato_sequence`,
- `negation_sequence`,
- Filterwörter wie `merkte`, `bemerkte`, `wusste`, `dachte`,
- Weichmacher-Cluster,
- wiederkehrende Mikro-Choreografie (`sah`, `nickte`, `schwieg`, `atmete aus` usw.),
- auffällige binäre Kontrastmuster (`Nicht X. Y.`, `X war nicht das Problem. Y war es.`),
- Häufungen bedeutungsschwerer Ein-Satz-Absätze.

Die Scanner-Ausgabe ist **Kandidatenmaterial**, keine automatische Änderungsanweisung.

### Deutsches Satzzeichenprofil

Für deutschsprachige Romanprosa gilt im Profil `de_anti_ki_prosa_v1`:

- Geviertstrich `—` = **FAIL / 0 zulässige Vorkommen**;
- notwendiger Gedankenstrich = Halbgeviertstrich `–`;
- der Halbgeviertstrich ist kein Ersatz-Tick und soll nur eingesetzt werden, wenn die Satzfunktion ihn tatsächlich braucht;
- abgebrochene Rede verwendet ebenfalls keinen Geviertstrich.

Ziel ist ein unauffälliges deutsches Schriftbild, nicht eine neue Gedankenstrich-Manier.

---

## 5. Pass B – Whole-Manuscript-Semantik

Der vollständige Roman wird horizontal nach den folgenden Musterfamilien gelesen.

### B1 – Dialog-Pingpong

Prüfen:

- mehrere kurze Frage-/Antwort-/Bestätigungszeilen hintereinander,
- wiederholt identischer Interview-/Review-Takt,
- `Ja. / Nein. / Gut. / Noch nicht.` als strukturelles Füllmaterial,
- Dialog, der nur eine bereits verstandene Prüflogik vorführt.

Rework-Optionen:

- Antworten bündeln,
- einen Teil als Handlung oder indirekte Wiedergabe führen,
- eine Reaktion durch konkrete Aktion ersetzen,
- nur die konflikttragenden Repliken stehen lassen.

### B2 – Stakkato und Fragmentketten

Prüfen:

- mehrere sehr kurze narrative Sätze/Absätze in Folge,
- wiederkehrendes Muster `Aussage. Verkürzung. Bedeutung. Pointe.`,
- Fragmente ohne situative Motivation.

Kurze Sätze bleiben erhalten, wenn Tempo, Wahrnehmung, Aktenlesen, Schock, medizinische Lage oder finale Zuspitzung sie tragen.

### B3 – Erklär-Echo

Nach einem verständlichen Beat prüfen:

> **Welche neue Information liefert der nächste Satz?**

Wenn er nur die Bedeutung der gerade sichtbaren Handlung, Körpersprache oder Dialogzeile auslegt, ist er Kürzungs-/Löschkandidat.

### B4 – Binäre Kontrastformeln und rhetorische Symmetrie

Markieren:

- `Nicht X. Y.`,
- `Es war nicht X. Es war Y.`,
- perfekt ausbalancierte Gegensätze,
- Dreierketten aus Negationen oder gleich gebauten Aussagen,
- Absatzfolgen, die wie eine argumentativ optimierte Präsentation klingen.

Nicht blind löschen. Die Häufung wird gebrochen, indem Satzform, Perspektive oder Informationsreihenfolge aus der konkreten Szene abgeleitet wird.

### B5 – Filter- und Wahrnehmungsformeln

Prüfen:

- `X merkte ...`,
- `X bemerkte ...`,
- `X wusste ...`,
- `X sah ...`,
- `X fühlte ...`,

wenn derselbe Effekt direkter über Körper, Objekt, Handlung oder Gedankeninhalt erzählt werden kann.

Filterverben bleiben erlaubt, wenn der **Akt des Wahrnehmens/Erkennens** selbst relevant ist.

### B6 – Mikro-Choreografie

Neutralregie wie `sah ihn an`, `nickte`, `schwieg`, `atmete aus`, `legte ... auf den Tisch` wird nicht einzeln verboten.

Geprüft wird, ob dieselbe neutrale Regie über viele Szenen die Funktion einer Standardanimation übernimmt.

### B7 – Methodik-/Beweisführungsprosa

Besonders in analytischen, medizinischen, juristischen, technischen oder Governance-Szenen prüfen:

- wird die interne Konstruktionslogik des Autors sichtbar?
- erklären Figuren wiederholt einen bereits etablierten Prozess?
- wird eine bereits gezeigte Gegenprüfung anschließend noch einmal methodisch zusammengefasst?
- klingt die Szene wie Review-Protokoll statt wie Erleben?

Leitregel:

> **Saubere Konstruktion im Unterbau. Menschliche, konkrete Oberfläche im Roman.**

---

## 6. Pass C – chirurgisches Rework

Änderungen erfolgen **kontextuell**, nicht als globales Synonym- oder Regex-Rewrite.

Bevorzugte Eingriffe:

1. redundanten Satz löschen;
2. zwei kurze Sätze zu einem natürlichen Satz verbinden;
3. Frage-/Antwort-Kette verdichten;
4. abstrakte Deutung durch konkrete Handlung/Wahrnehmung ersetzen;
5. Filterformulierung direkt machen;
6. perfekte rhetorische Symmetrie brechen;
7. Wiederholung stehen lassen, wenn sie aus Figur oder Situation stammt;
8. bewusst starke Stakkato-/Cliffhanger-Stellen schützen.

### Konservativitätsregel

> **Wenn zwei Versionen gleich gut funktionieren, bleibt die bestehende.**

Der Pass soll den Roman nicht neu schreiben und keine neue Autorenstimme erfinden.

---

## 7. Pass D – Regression

Nach dem Rework zwingend erneut prüfen:

- Kapitel-/Szenenanzahl unverändert,
- Reihenfolge unverändert,
- geschützte Story-Anker vorhanden,
- Ende unverändert, sofern nicht ausdrücklich beauftragt,
- keine versehentlich verlorenen Fakten/Entscheidungen,
- Hard Guards = PASS,
- Audit erneut ausführen,
- starke Musterfamilien gegenüber Baseline reduziert oder bewusst begründet,
- keine neue Ersatzformel erzeugt.

### Wortzahl

Der Pass ist kein Kürzungsprojekt. Eine deutliche Wortzahlverschiebung ist ein Warnsignal.

Als Review-Schwelle gilt standardmäßig:

- Veränderung des Gesamtmanuskripts über **±5 %** → bewusst prüfen und begründen.

Das ist kein automatischer Qualitätsgrenzwert.

---

## 8. Pass E – Fresh-Context-Lesecheck

Nach dem technischen Re-Audit folgt mindestens ein entkoppelter Lesecheck auf:

- Opening/erste Kapitel,
- einen zusammenhängenden Mittelteil-Run,
- Finale/Nachhall.

Prüffragen:

- klingt der Text noch sichtbar nach einer wiederkehrenden LLM-Formel?
- variiert der Satzrhythmus aus Situation und Figur heraus?
- bleibt Dialog knapp, ohne dauerhaft in Pingpong zu kippen?
- erklärt der Erzähler weniger, als die Szene bereits zeigt?
- sind starke kurze Sätze weiterhin stark, weil sie nicht mehr überall stehen?

Erst danach ist der Prosa-Freeze für G4 fachlich sinnvoll.

---

## 9. Artefakte / Source of Truth

Bei hierarchischen Buchprojekten werden Änderungen zuerst in den kanonischen `PROSA.md`-Dateien der Szenen vorgenommen.

Ein konsolidiertes Gesamtmanuskript ist danach neu zu erzeugen. Es darf nicht zur zweiten, auseinanderlaufenden Prosa-Source-of-Truth werden.

Empfohlene temporäre Review-Artefakte:

- `FINAL_PROSE_RHYTHM_AUDIT.md`
- optional ein kuratiertes Rework-Protokoll mit Fundstelle, Musterfamilie und Entscheidung.

Diese Reports dürfen nach Abschluss archiviert oder entfernt werden; die fachliche Wahrheit bleibt in den Szenen-Prosaquellen und den Gate-Records.

---

## 10. Definition of Done

Der finale Prosa- und Rhythmuspass ist abgeschlossen, wenn:

- Baseline-Audit dokumentiert ist;
- das Gesamtmanuskript horizontal auf alle B1–B7-Musterfamilien geprüft wurde;
- bestätigte Muster chirurgisch überarbeitet wurden;
- keine Story-/Szenenänderung unbemerkt im Prosa-Pass erfolgt ist;
- `— = 0` im deutschen Prosa-Profil gilt;
- aktive Hard Guards PASS sind;
- Regression und Whole-Manuscript-Audit erneut gelaufen sind;
- Fresh-Context-Lesecheck keinen bestätigten manuskriptweiten Prosa-Major mehr enthält;
- G4 auf den **neuen** Manuskript-Snapshot freigegeben wird;
- ältere G5-Ausgaben bis zum Neubuild als stale gelten.

## Leitregel

> **Der Leser soll die Szene sehen, nicht das Muster, mit dem sie erzeugt wurde.**
