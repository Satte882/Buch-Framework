# Analyse: Was aus NORMALFALL als Buch-Framework wiederverwendbar ist

## 1. Gesamturteil

`Satte882/Buch` ist als **einzelnes Buchprojekt** inzwischen sehr stark organisiert. Die entscheidende Leistung ist nicht der konkrete Plot, sondern die Kombination aus:

- schrittweiser Storyzerlegung,
- bewusster Leserwissenssteuerung,
- klaren Qualitätsgates,
- Recherche erst nach stabiler Szenenarchitektur,
- getrennten Struktur-/Tempo-/Continuity-/Stil-Pässen,
- einem verbindlichen Kontext- und Source-of-Truth-System,
- reproduzierbarer Buchproduktion per Build/CI.

Für eine thematische Psychothriller-Reihe ist davon sehr viel wiederverwendbar.

**Bewertung als abgeschlossener Ein-Buch-Prozess: 8,5/10**  
**Bewertung als heute bereits direkt kopierbares Framework: 6,5/10**

Der Unterschied entsteht, weil die Methodik stark ist, die Implementierung aber noch an vielen Stellen hart auf `NORMALFALL` zugeschnitten ist.

---

## 2. Was besonders gut funktioniert hat

### A. Vom Groben ins Feine – über den gesamten Roman

Die stärkste wiederverwendbare Entscheidung ist die 5-Ebenen-Logik:

1. dramaturgische Bausteine
2. Ereignisse
3. Beats
4. Szenenkarten
5. Prosa

Wichtig ist dabei die horizontale Arbeitsweise: erst den **gesamten Roman** auf einer Ebene stabilisieren, dann tiefer gehen. Dadurch können Reversal, Finale oder spätere Erkenntnisse noch auf frühe Teile zurückwirken, bevor dort teure Prosa entstanden ist.

**Bewertung: 10/10 – Framework-Kern.**

### B. Das Prosa-Gate

Vor der Ausformulierung gilt sinngemäß:

> Kann die Szene geschrieben werden, ohne dass das Schreibmodell noch relevante Plotentscheidungen selbst treffen muss?

Das ist für KI-gestütztes Schreiben besonders wichtig. Es trennt kreatives Schreiben von unkontrolliertem Plot-Erfinden.

**Bewertung: 10/10 – Framework-Kern.**

### C. Leserwissen als eigene Architektur

`NORMALFALL` plant nicht nur, **was passiert**, sondern auch:

- was der Leser weiß,
- was die Hauptfigur glaubt,
- welche alternative Lesart plausibel bleibt,
- was noch nicht verraten werden darf,
- welche spätere Zweitlesart möglich sein soll.

Das war für den Psychothriller entscheidend. Der Reversal funktioniert dadurch als Reframing statt als nachträglicher Faktenaustausch.

**Bewertung: 10/10 – für die Thriller-Reihe zentral.**

### D. Grenzverschiebung als Entwicklungsachse

Sehr stark ist die Regel:

> Was ist jetzt möglich oder akzeptabel, was hundert Seiten zuvor noch undenkbar gewesen wäre?

Das macht aus einem moralischen Thema tatsächlich eine Dramaturgie. Für die geplante Reihe ist das wahrscheinlich sogar die wichtigste gemeinsame DNA.

`NORMALFALL` nutzt:

> Ausnahme → funktioniert → legitimiert weitere Ausnahme → Normalisierung.

`ABWEICHUNG` kann denselben Meta-Mechanismus mit einem anderen Sachkonflikt verwenden:

> KI berät → KI ist besser → menschlicher Override verursacht Schaden → Overrides werden begründungspflichtig → menschliche Entscheidungsmacht wird faktisch eingeschränkt.

**Bewertung: 10/10 – Serienkern, nicht universeller Romankern.**

### E. Psychothriller zuerst, Thema darunter

Eine wichtige Korrektur während des Projekts war die Positionierung:

> Psychothriller zuerst. Politisch-gesellschaftlicher Tiefgang darunter.

Das verhindert, dass aus einem interessanten Dilemma ein verkleidetes Sachbuch wird. Jede zentrale Szene muss auch für jemanden funktionieren, der sich nicht für das Sachthema interessiert.

**Bewertung: 9/10 – Serienprofil.**

### F. Figuren erst nach stabiler Ereignis-/Beat-Struktur konkretisieren

Das hat Cast-Aufblähung reduziert. Figuren wurden aus dramaturgischem Bedarf abgeleitet und mussten ein eigenes Ziel, Konfliktpotenzial und Agency besitzen.

Besonders gut war die Schutzregel:

> Keine Figur nur für einen Twist, ein moralisches Experiment oder als spätere Geisel erfinden.

**Bewertung: 9/10 – Framework-Kern.**

### G. Recherche nach Szenenkarten statt vor der Story

Das ist effizient und schützt vor Recherche als Selbstzweck:

> Wie kann die bereits gesetzte dramaturgische Funktion realistisch funktionieren?

Recherche darf die Story nicht stillschweigend neu schreiben. Wenn Realität eine Szene widerlegt, wird bewusst auf die betroffene Planungsebene zurückgesprungen.

**Bewertung: 10/10 – Framework-Kern.**

### H. Rücksprung-/Discovery-Regel

Neue bessere Ideen dürfen entstehen, werden aber nicht spontan in die Prosa eingebaut.

Stattdessen:

1. betroffene Ebene bestimmen,
2. dort ändern,
3. Auswirkungen prüfen,
4. abhängige Ebenen synchronisieren,
5. erst dann weiter schreiben.

Das ist eine sehr gute Governance für probabilistische KI-Arbeit.

**Bewertung: 10/10 – Framework-Kern.**

### I. Getrennte Qualitäts-Pässe

Die Reihenfolge war sinnvoll:

- Structural Edit
- Page-Turner-Pass
- Continuity-/Fakten-Pass
- Stil-/Sprach-Pass
- externe Leser-/Red-Team-Pässe
- gezielter Anti-KI-/Anti-Tick-Pass
- Freeze vor menschlichen Testlesern

Ein Modell soll nicht gleichzeitig Plot, Tempo, Fakten und Sprache optimieren. Die Trennung reduziert Seiteneffekte.

**Bewertung: 9/10 – Framework-Kern.**

### J. Source of Truth und Kontextsystem

Sehr stark wurde am Ende festgelegt:

- genau eine aktive Volltextquelle,
- Architekturdateien für bewusste Änderungen,
- generierte DOCX nie als Inhaltsmaster,
- historische Dateien sind über Git vorhanden, aber keine aktuelle Wahrheit,
- nur so viel Kontext laden wie nötig, aber genug für Konsistenz.

**Bewertung: 10/10 – Framework-Kern.**

### K. Reproduzierbare Buchproduktion

Der Word-/KDP-Build prüft u. a.:

- Struktur,
- Typografie,
- Seitenformat,
- Ränder,
- Kapitelstarts,
- Silbentrennung,
- Dialogtypografie,
- Seitenzahlbereich,
- generierte kanonische DOCX.

Auch der KDP-Produktionsstandard mit Cover-PDF, eingebetteten Fonts und finaler KDP-Seitenzahl ist klar wiederverwendbar.

**Bewertung: 8/10 – technisch sehr wertvoll, aber noch nicht ausreichend parametriert.**

---

## 3. Was nicht optimal lief

### A. Die erste vollständige Prosa war viel zu stark verdichtet

Nach den ersten Prosa- und Qualitäts-Pässen lag der komplette Roman nur bei ungefähr **27.370 Wörtern**. Danach musste er massiv auf Romanlänge ausgebaut werden.

Das zeigt:

> Die Storyarchitektur war vollständig, aber die Szenenkarten steuerten noch nicht ausreichend, wie viel **Romanerleben** eine Szene braucht.

Für das Framework sollte die Szenenkarte deshalb nicht nur Plotfunktion definieren, sondern auch prüfen, ob ausreichend Raum vorhanden ist für:

- Konfliktdauer,
- Reaktion und psychologische Folge,
- räumliche Konkretion,
- Subtext,
- Konsequenz,
- Suspense,
- Beziehungshandlung.

Nicht als Wortzahlpflicht, sondern als **Erlebnisdichte-Gate**.

**Framework-Lektion:** Plot vollständig zu planen reicht nicht; die Szene muss auch genügend erzählerisches Material besitzen.

### B. Der anschließende Ausbau erzeugte stellenweise Übererklärung

Nach dem großen Ausbau mussten mehrere externe Leser-Pässe wieder deutlich kürzen. Vor allem wurden entfernt:

- doppelte Methodikerklärungen,
- Nachanalysen bereits verständlicher Entscheidungen,
- wiederholte Frage-Antwort-Schleifen,
- explizite Regie-/Moralformulierungen,
- Produktionssprache.

Das ist die Gegenbewegung zur Unterlänge.

**Framework-Lektion:** Ausbau darf nur Romanerleben ergänzen, niemals die bereits saubere Planung im Text erklären.

Zusätzliche Regel für zukünftige Prosa:

> **Die Konstruktion darf im Unterbau präzise sein. Auf der Oberfläche muss sie menschlich, asymmetrisch und teilweise unordentlich wirken.**

### C. Wortzahl wurde zeitweise zu stark zum Abnahmekriterium

75.000–80.000 Wörter waren zunächst verbindlich. Spätere Leser-Pässe zeigten aber, dass gute Kürzungen wichtiger waren als das Halten eines Produktionsziels. Deshalb wurden die alten Umfangssteuerungen später bewusst archiviert.

**Framework-Lektion:**

- Wortzahl früh als Plausibilitäts- und Produktindikator verwenden.
- Korridore zur Diagnose nutzen.
- Nie eine Szene auffüllen oder behalten, nur um einen Zielwert zu erfüllen.
- Endregel: **Umfang folgt Funktion.**

### D. Issue-Struktur wurde zeitweise zu kleinteilig

Die Ausbau-Issues #31–#35 wurden später ausdrücklich als unnötige Zerteilung verworfen. Ein einziges Umsetzungs-Issue für den Gesamtausbau war effizienter.

**Framework-Lektion:**

> Planungs- und Qualitätsgates fein schneiden; reine Massenumsetzung nicht künstlich in viele Issues zerlegen.

### E. Generische und buchindividuelle Regeln sind vermischt

Beispiele aus dem aktuellen CI:

- Dateiname `AUSNAHMEZUSTAND_FINAL.md`
- exakt Prolog + Kapitel 1–47
- exakte letzte Romanzeile
- Verbot des Wortes `sondern`
- feste Garamond-Größe
- festes KDP-Trim
- feste Ränder
- fester 501–700-Seitenbereich
- Artefaktname `normalfall-kdp-5-06x7-81`

Diese Regeln sind für `NORMALFALL` korrekt, aber kein Framework.

**Framework-Lektion:** technische Regeln müssen in eine Projektkonfiguration ausgelagert werden.

### F. Alte Arbeitstitel bleiben technisch sichtbar

`NORMALFALL` verwendet weiterhin Dateinamen wie `AUSNAHMEZUSTAND_FINAL.md` und `AUSNAHMEZUSTAND.docx`.

Für ein einzelnes fertiges Projekt ist das tolerierbar. Für ein Framework würde es schnell zu Verwechslungen führen.

**Framework-Lektion:** neue Bücher müssen von Anfang an neutrale oder konfigurierte Dateinamen verwenden, z. B. `MANUSKRIPT_FINAL.md`, `BUCH.docx` oder aus `book.yml` generierte Namen.

### G. KDP-Cover ist dokumentiert, aber noch kein vollständig integrierter Build

Die Cover-PDF-Probleme haben gezeigt:

- Covergröße hängt von finalem KDP-Projektformat und Seitenzahl ab,
- ein statischer Wert darf nicht übernommen werden,
- Fonts müssen eingebettet sein,
- KDP Template/Calculator ist finale Source of Truth.

**Framework-Lektion:** Cover-Produktion gehört als eigene Phase in das Produktionsframework, aber die exakten Abmessungen dürfen erst nach finalem Innenraum/KDP-Preview gesetzt werden.

---

## 4. Wichtigste Architekturentscheidung für Buch-Framework

Das zukünftige System sollte **drei Ebenen strikt trennen**.

## Ebene A – Framework Core

Genre- und buchunabhängige Arbeitslogik:

- Source-of-Truth-System
- 5 Ebenen der Entwicklung
- horizontales Vorgehen über den ganzen Roman
- Prosa-Gate
- Discovery-/Rücksprung-Regel
- Figuren aus Funktion ableiten
- Recherche nach stabiler Szenenarchitektur
- Qualitäts-Pässe
- externe Feedbackauswertung
- Freeze-Regel
- Build-/Produktionsprinzipien

Diese Ebene darf weder `Daniel`, `NORMALFALL`, 47 Kapitel noch ein bestimmtes KDP-Format kennen.

## Ebene B – Serienprofil: thematischer Psychothriller

Gemeinsame DNA der geplanten Reihe:

- Psychothriller zuerst, gesellschaftliches Dilemma darunter
- reales Problem, keine einfache moralische Antwort
- zwei legitime Werte kollidieren
- zunächst vernünftige Lösung
- Lösung funktioniert tatsächlich
- Erfolg verschiebt die Grenze
- qualitative Eskalation
- Leser soll selbst ein Stück mitgehen
- Reframing statt billiger Fakten-Twist
- Gegenpositionen bleiben glaubwürdig
- kein einfacher Bösewicht als moralische Entlastung
- Ende zeigt eine neue Normalität / weitergeschobene Grenze

Hier kann die 9-Baustein-Struktur als **bewährtes Default-Profil** liegen, ohne sie zum universellen Gesetz für jeden Roman zu machen.

## Ebene C – Book Instance

Nur das konkrete Buch:

Beispiel `ABWEICHUNG`:

- Titel
- KI + Entscheidungsmacht
- konkrete Leitfrage
- Figuren
- Anwendungskontext
- Story
- Reversal
- Szenen
- Recherche
- Stilkalibrierung
- Kapitelzahl
- konkrete KDP-Daten

Damit kann Buch 3 später dasselbe Framework und Serienprofil nutzen, ohne Storymaterial aus Buch 2 mitzuschleppen.

---

## 5. Was konkret aus `Satte882/Buch` extrahiert werden sollte

| Quelle in NORMALFALL | Wiederverwendung | Ziel im Framework |
|---|---|---|
| `Bausteine_in_5_Ebenen_zerlegen.md` | sehr hoch | Core-Methodik abstrahieren |
| `KONTEXTSYSTEM.md` | sehr hoch | generisches Source-of-Truth-/Kontextmodell |
| `PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md` | hoch | Serienprofil statt Core |
| `STILREFERENZ.md` | mittel-hoch | generische Stil-/Anti-KI-Regeln + konfigurierbarer Benchmark |
| `ROTER_FADEN.md` | Struktur hoch, Inhalt niedrig | Template für Plot-, Leserwissens- und Reframing-Architektur |
| `FIGUREN.md` | Struktur hoch, Inhalt niedrig | Figuren-Template + Agency-/Funktionschecks |
| `RECHERCHE_PLAUSIBILITAET.md` | Prozess hoch, Inhalt niedrig | Recherchetemplate mit Szenenreferenz |
| `ROMAN_MAP.md` | hoch | generisches Szenen-/Kapitel-Mapping |
| `BAUSTEINE/` | hoch als Schema | leere Verzeichnis-/Dateitemplates |
| Issues #2–#26 | hoch als Workflowwissen | Phasen/Gates statt 1:1 kopierter Issues |
| Issues #29–#39 | hoch als Lessons Learned | Ausbau-, Reader-, Freeze- und Anti-Glättungs-Regeln |
| DOCX-Skripte | hoch | parametrieren |
| GitHub Actions | hoch | hart codierte Buchwerte entfernen |
| `MANUSKRIPT_FORMATIERUNG.md` | hoch | Produktionsprofil / konfigurierbarer Buchsatz |
| `KDP_PRODUKTIONSSTANDARD.md` | sehr hoch | generischer Publishing-Standard |
| `BUCHBESCHREIBUNG_KDP.md` | mittel | Publishing-Template, nicht Story-Core |

---

## 6. Vorgeschlagene Framework-Phasen

Noch keine Umsetzung, nur Zielbild der Analyse:

### Phase 0 – Konzept-Gate

- Genre / Serienprofil
- gesellschaftlicher Konflikt
- zwei legitime Werte
- paradoxe Leitfrage
- Mechanismus der Grenzverschiebung
- warum die problematische Lösung tatsächlich funktioniert

### Phase 1 – Architektur

- dramaturgische Bausteine
- Entwicklungsachsen
- Ereignisse
- globale Gesamtprüfung
- Beats
- globale Gesamtprüfung

### Phase 2 – Figuren und Informationsarchitektur

- nur notwendige Figuren
- Agency / eigenes Ziel / Reibung
- Leserwissen
- Gegenlesarten
- Misdirection / Reframing

### Phase 3 – Szenenarchitektur

- Szenenkarten
- konkrete Abläufe
- Prosa-Gate
- globale Szenenprüfung

### Phase 4 – Plausibilität

- konkrete Recherche nur für gesetzte Szenen
- bewusster Rücksprung bei Konflikten mit Realität

### Phase 5 – Prosa

- Szene für Szene ausformulieren
- keine neue Storylogik
- Erlebnisdichte prüfen
- Anti-Glättung / Anti-Erklärprosa

### Phase 6 – Manuskript-Qualität

- Structural
- Page-Turner
- Continuity/Fakten
- Stil/Sprache
- externe Leserdiagnose
- gezielter Anti-KI-/Anti-Tick-Pass
- menschliche Testleser
- Freeze

### Phase 7 – Produktion

- finaler Markdown-Master
- reproduzierbare DOCX/PDF-Ausgabe
- KDP-Innenformat
- finale Seitenzahl
- Cover-Template
- Cover-PDF mit eingebetteten Fonts
- Previewer / Qualitätsprüfung

---

## 7. Was NICHT 1:1 in das Framework kopiert werden sollte

Nicht generalisieren:

- Daniel Reuter oder andere Figuren
- Sicherheitsapparat / Terrorlage
- konkrete 9 Baustein-Inhalte
- konkreter Cold Open
- Heller-Reversal
- 47 Kapitel
- exakte Wortzahlen
- exakte Schlusszeile
- `sondern`-Verbot als globales Sprachgesetz
- `NORMALFALL`-Dateinamen
- 5,06 × 7,81 als zwingendes Format für jedes Buch
- 1,95-cm-Bundsteg für jedes Buch
- konkrete Covergröße eines KDP-Projekts

Das Framework soll **Entscheidungslogik und Prüfmechanismen** konservieren, nicht die Entscheidungen eines einzelnen Romans.

---

## 8. Hauptrisiko bei Wiederverwendung

Das größte Risiko ist nicht zu wenig Struktur, sondern **sichtbare Formelhaftigkeit**.

Wenn jedes Buch zwingend denselben Cold Open, denselben Midpoint, denselben großen Reversal und dasselbe Nachhallbild besitzt, erkennt der Leser irgendwann die Maschine.

Deshalb:

> **Prozess standardisieren, Erzähloberfläche und konkrete Dramaturgie nicht standardisieren.**

Die 9 Bausteine sind für die Reihe ein bewährter Ausgangspunkt. Sie müssen aber als funktionale Fragen verstanden werden, nicht als identischer Plotbauplan.

---

## 9. Empfohlene nächste Aktion

**Noch nichts nach `ABWEICHUNG` kopieren.**

Als nächster Schritt sollte `Buch-Framework` aus dieser Analyse ein minimales **Framework v0.1** erhalten, bestehend aus:

1. `FRAMEWORK.md` – Phasen, Gates und Rücksprunglogik
2. `SERIES_PROFILE_PSYCHOTHRILLER.md` – gemeinsame DNA der thematischen Reihe
3. `templates/` – Buchidee, Figuren, roter Faden, Szenenkarte, Recherche
4. `config/book.yml` – alle buchindividuellen technischen Werte
5. parametrierten Build-/Metrik-Skripten

Erst wenn dieses Grundgerüst sauber steht, wird `ABWEICHUNG` daraus initialisiert.

Damit wird `ABWEICHUNG` nicht Buch 2 nach alter Handarbeit, sondern der **erste echte Test des Frameworks**.
