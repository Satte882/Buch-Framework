# Localization

Dieser Baustein beschreibt, wie aus einem freigegebenen Ausgangsmanuskript eine hochwertige fremdsprachige Edition entsteht. Er ist bewusst **keine technische Übersetzungsplattform** und benötigt keinen LLM-Provider, keine Agenten-Orchestrierung und keine zusätzliche Infrastruktur.

Betriebsmodell:

> **ChatGPT bearbeitet. GitHub hält den gültigen Stand. Der Mensch entscheidet.**

Localization bedeutet hier nicht wortgetreue Übersetzung, sondern eine kontrollierte literarische Übertragung: Inhalt, Figuren, Fakten, Spannung und Erzählfunktion bleiben erhalten; Syntax, Idiomatik, Dialoge und Rhythmus dürfen so angepasst werden, dass der Zieltext wie originär in der Zielsprache geschriebene Genreliteratur funktioniert.

## Scope

Der Baustein beginnt erst, wenn eine belastbare Ausgangsfassung existiert. Er verändert die bestehende Buch-Pipeline nicht, sondern ist ein optionaler Downstream-Pfad für zusätzliche Sprach-/Markteditionen.

Nicht Bestandteil des generischen Localization-Kerns:

- Plotentwicklung oder neue Szenen,
- Änderungen am kanonischen Ausgangsmanuskript,
- automatische Veröffentlichung,
- Multi-Agenten- oder Provider-Infrastruktur.

Publishing bleibt fachlich ein eigener Verantwortungsbereich. Für englische Editionen liegt jedoch unter [`english/README.md`](english/README.md) ein **konkreter, wiederverwendbarer Downstream-Produktionspfad**, der die realen Learnings aus `NORMALFALL` → `REASONABLE MEASURES` konserviert: Print-DOCX/TOC, `en-US`-Hyphenation, Runner-PDF-QA, EPUB 3, EPUBCheck, Titel-/Metadaten-Gates und KDP-Submission-Grenzen.

## Drei verbindliche Projektartefakte

Für eine konkrete Zielausgabe werden zunächst nur drei buchbezogene Dateien benötigt:

1. `LOCALIZATION_PROFILE.md` – Source-Version, Zielvariante und verbindliche Lokalisierungsentscheidungen.
2. `STYLE_GUIDE.md` – aus dem Ausgangsmanuskript abgeleitete Regeln für Stimme, Rhythmus, Dialog und Genre-Wirkung.
3. `GLOSSARY.md` – verbindliche Übersetzungen und Entscheidungen für wiederkehrende Begriffe; wächst iterativ.

Templates:

- [`LOCALIZATION_PROFILE_TEMPLATE.md`](LOCALIZATION_PROFILE_TEMPLATE.md)
- [`STYLE_GUIDE_TEMPLATE.md`](STYLE_GUIDE_TEMPLATE.md)
- [`GLOSSARY_TEMPLATE.md`](GLOSSARY_TEMPLATE.md)

Für eine englische Edition kommt vor Publishing Production eine zentrale Config hinzu:

- [`english/PUBLISHING_CONFIG_TEMPLATE.json`](english/PUBLISHING_CONFIG_TEMPLATE.json)

## Empfohlene Struktur im konkreten Buch

Die bestehende Struktur eines Buch-Repositories muss dafür nicht umgebaut werden. Eine zusätzliche Edition kann beispielsweise so ergänzt werden:

```text
ENGLISH/
├── LOCALIZATION_PROFILE.md
├── STYLE_GUIDE.md
├── GLOSSARY.md
├── PUBLISHING_CONFIG.json
├── manuscript/
└── review/
```

Leere Output-Verzeichnisse werden nicht vorsorglich erzeugt, sondern erst wenn sie gebraucht werden.

## Arbeitsfolge

1. **Source festlegen** – konkrete Quelldatei und Git-Commit im Localization Profile verankern.
2. **Zielsprache/-markt festlegen** – z. B. `English (US)`; keine unnötigen Profile für Märkte anlegen, die aktuell nicht benötigt werden.
3. **Style Guide ableiten** – Stimme und Erzählmechanik des konkreten Buches vor der Vollübersetzung festhalten.
4. **Pilot übersetzen** – Prolog plus 2–3 repräsentative Kapitel bearbeiten.
5. **Voice prüfen** – Mensch entscheidet, ob die englische Stimme trägt; bei Bedarf Profile/Style Guide korrigieren, bevor der Rest folgt.
6. **Rest übertragen** – nach [`workflows/translate-chapter.md`](workflows/translate-chapter.md).
7. **Editorial Review** – nach [`workflows/editorial-review.md`](workflows/editorial-review.md), getrennt von der Erstübertragung.
8. **Gesamtkonsistenz prüfen** – nach [`workflows/final-consistency-review.md`](workflows/final-consistency-review.md).
9. **Bei englischer Edition:** den wiederverwendbaren Downstream-Pfad aus [`english/README.md`](english/README.md) ausführen.

Es gibt dafür bewusst keine zusätzliche Gate-Kaskade. Der einzige zwingende frühe menschliche Prüfpunkt ist die Freigabe der Zielstimme nach dem Pilot, weil ein falscher Ton sonst über das gesamte Buch skaliert. Für den englischen Downstream bleiben nur Markt-/Cover-/Publish-Entscheidungen menschliche Gates.

## Source-of-Truth-Regel

- Das Ausgangsmanuskript bleibt Source of Truth für Inhalt und Fakten.
- Die Zielsprache ist eine **abgeleitete, eigenständig redigierte Edition**.
- Jede Edition verweist auf die konkrete Source-Version/Commit.
- Änderungen im Ausgangsmanuskript invalidieren nicht automatisch die komplette Edition; sie müssen gezielt auf Relevanz für die Zielausgabe geprüft werden.
- Keine Lokalisierungsentscheidung darf rückwirkend den Plot oder die kanonische Figurenlogik verändern.

## Leitprinzip

> **Wirkung übertragen, nicht deutsche Syntax konservieren. Inhaltliche Treue und natürliches Zielsprachen-Englisch sind gleichzeitig Pflicht.**
