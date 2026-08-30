# Source of Truth, Ableitung und Invalidierung

## Zweck

Dieses Dokument verhindert, dass Story-, Figuren- oder Rechercheentscheidungen durch spätere Planung oder Prosa stillschweigend verändert werden. Die verbindliche Verzeichnisstruktur steht in `PROJECT_STRUCTURE.md`.

Die normale Entwicklungsrichtung lautet:

`Thema/Buchidee → Bausteine → Ereignisse/Sequenzen → Szenen → Beats → Prosa`

## Kanonische Ebenen

### 1. Konzept / Meta

Kanonisch nach G0:

- `BOOK_IDEA.md`

Weitere Meta-/Querschnittsartefakte im Root:

- `STORY_PACKAGE.md`,
- `CHARACTERS.md`,
- `RESEARCH_REGISTER.md`,
- `gates/`.

### 2. Story-Architektur – Bausteine und Events

Kanonisch nach G1:

- `STORY_PACKAGE.md`,
- alle `BAUSTEINE/Bxx/BAUSTEIN.md`,
- alle `BAUSTEINE/Bxx/EVENTS.md`,
- relevante aktuelle Teile von `CHARACTERS.md`,
- `RESEARCH_REGISTER.md` für bekannte Storyabhängigkeiten.

`BAUSTEIN.md` definiert die dramaturgische Makrofunktion eines Abschnitts. `EVENTS.md` konkretisiert, welche Ereignisse/Sequenzen innerhalb genau dieses Bausteins kausal stattfinden müssen.

Globale `STORY_BLOCKS.md` und `EVENTS.md` dürfen in hierarchischen Projekten als abgeleitete Gesamt-/Checker-Sichten existieren. Sie sind keine zweite fachliche Source of Truth.

### 3. Szenen-Architektur / Prose Ready

Kanonisch nach G2:

- alle `BAUSTEINE/Bxx/SZENEN/Sxxx/SZENE.md`,
- die zugehörigen `BEATS.md`,
- die zugehörigen `CHARACTER_STATES.md` bzw. lokalen State-Unterordner,
- relevante aufgelöste Rechercheentscheidungen.

Die Ableitung erfolgt in dieser Reihenfolge:

1. Events definieren, **was passieren muss**,
2. Szenen definieren, **was davon in welcher erzählten Einheit gezeigt wird**,
3. Beats definieren, **wie die einzelne Szene Schritt für Schritt abläuft**.

Erst wenn die Szenenlandschaft über das gesamte Buch steht, werden die Szenen systematisch in Beats präzisiert.

### 4. Prosa

Nach G2 ist Prosa **abgeleitet** und liegt bei der jeweiligen Szene:

- `BAUSTEINE/Bxx/SZENEN/Sxxx/PROSA.md`.

Ein Draft darf die freigegebene Szenen-/Beat-Wahrheit ausgestalten, rhythmisieren, konkretisieren und sprachlich verdichten. Er darf keine neue relevante Plot-, Figuren-, Wissens-, Recherche-, Informations- oder Konsequenzentscheidung heimlich zur kanonischen Wahrheit machen.

### 5. Kanonisches Manuskript

Nach erfolgreichem G3 wird die vollständige Prosa erzeugt und überarbeitet. Das Gesamtmanuskript wird erst durch G4 zum freigegebenen Manuskriptstand.

### 6. Produktion

Produktionsartefakte sind vom G4-Manuskript abgeleitet. G5 gilt immer für den konkreten Produktionsstand.

## Querschnittsartefakte

### Figuren

`CHARACTERS.md` ist die globale Figurenbaseline. Szenenspezifische Zustände liegen bei der jeweiligen Szene in `CHARACTER_STATES.md` bzw. einem lokalen Unterordner.

Eine Figurenänderung wird an der frühesten betroffenen kanonischen Ebene vorgenommen und invalidiert nur tatsächlich abhängige Artefakte.

### Recherche

`RESEARCH_REGISTER.md` läuft quer durch die Entwicklung.

Eine offene Recherchefrage blockiert nur dann, wenn ihre Antwort eine **jetzt zu treffende Plot-, Figuren-, Szenen-, Informations- oder Konsequenzentscheidung** verändern kann.

## Einbahnstraßenregel

Die normale Ableitungsrichtung lautet:

`BOOK_IDEA/STORY_PACKAGE → BAUSTEIN → EVENTS → SZENE → BEATS/CHARACTER_STATES → PROSA → MANUSKRIPT → PRODUKTION`

Prosa aktualisiert **niemals automatisch** einen Upstream-State.

## Horizontalregel

Innerhalb der Storyentwicklung wird eine Ebene standardmäßig über das gesamte Buch ausreichend geschlossen, bevor die nächste Ebene systematisch abgeleitet wird.

Das bedeutet insbesondere:

- nicht einzelne frühe Bausteine bis zur Prosa entwickeln, während spätere Bausteine noch offen sind,
- erst alle Baustein-/Eventketten schließen,
- dann die Szenenlandschaft über das gesamte Buch schließen,
- dann die Szenen in Beats/States präzisieren,
- Prosa erst nach G2 systematisch skalieren.

## Globale Index-/Checker-Sichten

Hierarchische Buchprojekte dürfen für CI, Review oder Kompatibilität zusätzlich globale Sichten führen, z. B. `STORY_BLOCKS.md`, `EVENTS.md`, `BEATS.md` oder einen Szenenindex.

Regeln:

1. Änderung immer zuerst in der kanonischen hierarchischen Datei.
2. Index danach aktualisieren/regenerieren.
3. Bei Widerspruch ist der Index `stale`.
4. Ein Index darf nicht unabhängig zur Story-Quelle werden.

Historische M1/M2-Fixtures dürfen ihr flaches Layout behalten.

## Backtracking-Regel

Soll eine Downstream-Änderung relevante Storywahrheit verändern:

1. Änderung nicht nur im Downstream-Artefakt vornehmen.
2. Früheste betroffene kanonische Upstream-Datei identifizieren.
3. Änderung dort einarbeiten.
4. Erforderlichen Human Gate bzw. betroffene Review-Phase erneut durchlaufen.
5. Abhängige Downstream-Artefakte als `stale` oder `invalidated` markieren.
6. Betroffene Ableitungen neu prüfen bzw. neu erzeugen.

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

## Upstream-Referenzen

Ein abgeleitetes generatives Artefakt muss seine relevanten Inputs referenzieren. Für hierarchische Projekte beispielsweise:

```yaml
upstream:
  - path: BAUSTEINE/B07/BAUSTEIN.md
    ref: <blob-sha>
  - path: BAUSTEINE/B07/EVENTS.md
    ref: <blob-sha>
  - path: BAUSTEINE/B07/SZENEN/S019/SZENE.md
    ref: <blob-sha>
  - path: BAUSTEINE/B07/SZENEN/S019/BEATS.md
    ref: <blob-sha>
  - path: BAUSTEINE/B07/SZENEN/S019/CHARACTER_STATES.md
    ref: <blob-sha>
  - path: RESEARCH_REGISTER.md
    ref: <blob-sha>
```

## Statusmodell für abgeleitete Artefakte

Erlaubte Zustände:

- `draft` – erzeugt, noch nicht menschlich freigegeben,
- `accepted` – erforderlicher Gate wurde bestanden,
- `stale` – relevanter Upstream-Stand hat sich geändert,
- `invalidated` – Artefakt darf nicht weiterverwendet werden.

`stale` und `invalidated` dürfen nicht in ein kanonisches Manuskript übernommen werden.

## Invalidierungsregel

Ein Downstream-Artefakt ist mindestens dann `stale`, wenn sich nach seiner Erzeugung ein referenzierter relevanter Upstream-Stand ändert.

Für v0.x muss nicht jede semantische Abhängigkeit automatisch erkannt werden. Entscheidend ist:

1. Referenzen sind explizit,
2. eine bekannte Änderung wird nicht ignoriert,
3. der betroffene Downstream-Status wird sichtbar aktualisiert,
4. vor weiterer Verwendung findet erneute Prüfung statt.

## Prosaänderungen ohne Upstream-Änderung

Reine sprachliche Überarbeitungen – Rhythmus, Wortwahl, Satzbau, Kürzung von Erklär-Echos – verändern Story-/Character-State nicht automatisch.

Ein semantischer Review darf einen Widerspruch melden. Er darf keinen State selbst aktualisieren.

## Human Gates

Ein Human Gate bezieht sich immer auf konkrete Artefaktstände, darf aber mehrere Entwicklungsebenen bündeln. Ein Gate pro Datei oder pro Planungsebene ist ausdrücklich nicht erforderlich.

## Leitregel

> **Meta definiert das Buch. Bausteine definieren den Romanbogen. Events definieren, was passieren muss. Szenen definieren, was erzählt wird. Beats definieren den Ablauf. Prosa schreibt erst das bereits Entschiedene aus.**
