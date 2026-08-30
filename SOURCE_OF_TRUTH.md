# Source of Truth, Ableitung und Invalidierung

## Zweck

Dieses Dokument verhindert, dass Story-, Figuren- oder Rechercheentscheidungen durch spätere Planung oder Prosa stillschweigend verändert werden. Es definiert für v0.x die kanonischen Artefakte, die Richtung von Änderungen und den Umgang mit veralteten Downstream-Artefakten.

Die verbindliche Entwicklungsrichtung steht in `ARBEITSWEISE.md`:

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Beats → Szenenkarten → Prosa`

## Kanonische Ebenen

### 1. Konzept

Kanonisch nach G0:

- `BOOK_IDEA.md`

Hier liegen Thema, Prämisse, Leitfrage, Leser-Versprechen und zentrale Nicht-Ziele.

### 2. Story-Architektur

Kanonisch nach G1:

- `STORY_PACKAGE.md`
- `STORY_BLOCKS.md`
- `EVENTS.md`
- relevante aktuelle Teile von `CHARACTERS.md`
- `RESEARCH_REGISTER.md` für bekannte Storyabhängigkeiten

`STORY_PACKAGE.md` hält Konflikt, Mechanismus, Reversal, Informationsarchitektur und Figurenfunktionen. `STORY_BLOCKS.md` zerlegt die Gesamtgeschichte horizontal in dramaturgische Bausteine. `EVENTS.md` konkretisiert anschließend die Ereignisse bzw. optionalen Sequenzgruppen innerhalb dieser Bausteine.

### 3. Szenen-Architektur / Prose Ready

Kanonisch nach G2:

- `BEATS.md`
- freigegebene `SCENE_PLAN`-Artefakte
- referenzierte `CHARACTER_STATE`-Artefakte
- für die Szenenentscheidung relevante aufgelöste Rechercheentscheidungen

Beats werden zuerst über das Buch ausreichend geschlossen. Erst danach werden daraus Szenenkarten abgeleitet.

### 4. Prosa-Stichprobe

Nach G2 erzeugte Prosa ist **abgeleitet**. Ein repräsentativer Batch wird vor breiter Skalierung in G3 geprüft.

Ein Draft darf die freigegebene Szenenwahrheit ausgestalten, rhythmisieren, konkretisieren und sprachlich verdichten. Er darf keine neue relevante Plot-, Figuren-, Wissens-, Recherche-, Informations- oder Konsequenzentscheidung heimlich zur kanonischen Wahrheit machen.

### 5. Kanonisches Manuskript

Nach erfolgreichem Prosa-Stil-Gate kann die vollständige Prosa erzeugt und überarbeitet werden. Das Gesamtmanuskript wird erst durch G4 zum freigegebenen Manuskriptstand.

### 6. Produktion

Produktionsartefakte sind vom G4-Manuskript abgeleitet. G5 gilt immer für den konkreten Produktionsstand.

## Querschnittsartefakte

### Figuren

`CHARACTERS.md` und `CHARACTER_STATE` sind keine isolierte lineare Stufe mit automatisch eigenem Human Gate.

- Figurenkern und zentrale Beziehungen werden mit der Story-Architektur entwickelt.
- Wissen, Glauben, Ziele und Beziehungsstände werden bis zur Szenen-Architektur konkretisiert.
- Eine Figurenänderung wird an der frühesten betroffenen kanonischen Ebene vorgenommen und invalidiert nur tatsächlich abhängige Artefakte.

### Recherche

`RESEARCH_REGISTER.md` läuft ebenfalls quer durch die Entwicklung.

Eine offene Recherchefrage blockiert nur dann, wenn ihre Antwort eine **jetzt zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung** verändern kann. Austauschbare Oberflächendetails dürfen offen bleiben.

## Einbahnstraßenregel

Die normale Ableitungsrichtung lautet:

`BOOK_IDEA → STORY_PACKAGE/STORY_BLOCKS → EVENTS → BEATS → SCENE_PLAN/CHARACTER_STATE → PROSA → MANUSKRIPT → PRODUKTION`

Prosa aktualisiert **niemals automatisch** einen Upstream-State.

Wenn beim Schreiben eine bessere Storyentscheidung entdeckt wird, gilt Backtracking statt Sync.

## Horizontalregel

Innerhalb der Storyentwicklung wird eine Ebene standardmäßig über das gesamte Buch ausreichend geschlossen, bevor die nächste Ebene systematisch abgeleitet wird.

Das bedeutet insbesondere:

- nicht einzelne frühe Szenen bis zur Prosa entwickeln, während spätere Bausteine noch offen sind,
- nicht Szenenkarten bauen, solange relevante Beats derselben Gesamtarchitektur fehlen,
- Prosa erst nach G2 systematisch skalieren.

## Backtracking-Regel

Soll eine Downstream-Änderung eine relevante Storywahrheit verändern:

1. Änderung nicht nur im Downstream-Artefakt vornehmen.
2. Betroffenes kanonisches Upstream-Artefakt identifizieren.
3. Änderung dort einarbeiten.
4. Erforderlichen Human Gate bzw. betroffene Review-Phase erneut durchlaufen.
5. Abhängige Downstream-Artefakte als `stale` oder `invalidated` markieren.
6. Betroffene Ableitungen neu prüfen bzw. neu erzeugen.

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

## Upstream-Referenzen

Ein abgeleitetes generatives Artefakt muss seine relevanten Inputs referenzieren. Für v0.x reichen Git-basierte Referenzen.

Beispiel:

```yaml
upstream:
  - path: BEATS.md
    ref: <blob-sha-oder-commit>
  - path: scenes/S-001.md
    ref: <blob-sha-oder-commit>
  - path: character_states/S-001_Alex.md
    ref: <blob-sha-oder-commit>
  - path: RESEARCH_REGISTER.md
    ref: <blob-sha-oder-commit>
```

Wo ein externes Repository als kanonische Quelle dient, müssen Repository, Pfad und feste Git-Referenz eindeutig genannt werden.

## Statusmodell für abgeleitete Artefakte

Erlaubte Zustände:

- `draft` – erzeugt, noch nicht menschlich freigegeben,
- `accepted` – erforderlicher Gate wurde bestanden,
- `stale` – ein relevanter Upstream-Stand hat sich geändert; erneute Prüfung/Erzeugung erforderlich,
- `invalidated` – Artefakt darf nicht weiterverwendet werden.

`stale` und `invalidated` dürfen nicht in ein kanonisches Manuskript übernommen werden.

## Invalidierungsregel

Ein Downstream-Artefakt ist mindestens dann `stale`, wenn sich nach seiner Erzeugung ein referenzierter relevanter Upstream-Stand ändert.

Für v0.x muss nicht jede semantische Abhängigkeit automatisch erkannt werden. Entscheidend ist:

1. Referenzen sind explizit,
2. eine bekannte Änderung wird nicht ignoriert,
3. der betroffene Downstream-Status wird sichtbar aktualisiert,
4. vor weiterer Verwendung findet erneute Prüfung statt.

Deterministische Hash-/Referenzprüfungen dürfen ergänzt werden, wenn sie real Rework sparen. Eine Datenbank ist dafür nicht erforderlich.

## Prosaänderungen ohne Upstream-Änderung

Reine sprachliche Überarbeitungen – Rhythmus, Wortwahl, Satzbau, Kürzung von Erklär-Echos – verändern Story-/Character-State nicht automatisch.

Ein semantischer Review darf einen Widerspruch melden. Er darf keinen State selbst aktualisieren.

## Human Gates

Ein Human Gate bezieht sich immer auf konkrete Artefaktstände, darf aber mehrere Entwicklungsebenen bündeln. Ein Gate pro Datei oder pro Planungsebene ist ausdrücklich nicht erforderlich.

Bei großen Büchern darf eine Freigabephase aus mehreren Review-Batches bestehen; der fachliche Gate bleibt derselbe.

Wird ein freigegebener Stand inhaltlich relevant geändert, gilt eine frühere Freigabe nicht automatisch für die neue Version.

## Leitregel

> **Upstream definiert die Storywahrheit. Downstream wird daraus abgeleitet. Entwicklung geht horizontal vom Großen ins Kleine; relevante Änderungen wandern zuerst zurück zur Quelle und dann wieder vorwärts durch die betroffenen Gates.**
