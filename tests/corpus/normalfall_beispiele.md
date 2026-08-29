# NORMALFALL – reale Vorher/Nachher-Beispiele aus der Commit-Historie

Zweck dieser Datei: **Rohmaterial** aus `Satte882/Buch` sichern. Jeder Eintrag basiert auf einem tatsächlichen Git-Diff. Es werden hier **keine** Schwellenwerte, Detector-Regeln, CI-Entscheidungen oder Framework-Architektur abgeleitet.

Umfang: **50 reale Beispiele** aus Anti-KI-/Stil-/Leserpass-Commits.

Hinweise:
- `Nachher: [entfernt]` bedeutet, dass die Passage im Commit vollständig gelöscht wurde.
- `Muster-Kategorie` ist nur eine deskriptive Einordnung des konkreten Diffs, keine generalisierte Regel.
- `Warum` wird nur angegeben, wenn es aus Commit-Message, Skriptkommentar oder Diff-Kontext erkennbar ist.
- Temporäre Audit-/Workflow-Commits ohne direkte Prosaänderung wurden bei der Suche berücksichtigt, liefern aber naturgemäß keine Vorher/Nachher-Paare.

## Durchsuchte relevante Commit-Ketten

### Frühe Prosa-/External-Review-Pässe
- `0196047` – `Polish prose and remove overly constructed phrasing`
- `3534195` – `Polish opening prose after external review`
- `c6ed4ce` – `Tighten reversal prose and reduce rhetorical symmetry`
- `ca4d501` – `Tighten aftermath prose and remove meta explanation`

### Externe Leser-/Straffungspässe
- `2d1529f` – `Tighten opening reader flow through chapter 10`
- `d9d418d` – `Tighten middle reader flow through chapter 26`
- `492537b` – `Polish final reader rhythm before test readers`

### Anti-Tick / Rhythmus / Style-Depth
- `5ffa95b` – `Polish manuscript language patterns`
- `6904351` / `eaddb8d` – temporärer Rhythmus-Audit
- `f27a076` / `044f433` – konservativer Rhythmus-Pass / resultierende Prosaänderungen
- `5d383b9` / `b0b07b5` – Rhythmus-Korrektur / Redundanzentfernung
- `b350d11` / `de55a16` – Style-/Ambiguity-Audit
- `944e826` / `bd072c7` / `7836a2d` – Style-Depth-Pass / resultierende Prosaänderungen
- `155d36c` / `e5fc9a4` / `5d8761a` – finaler Style-Depth-/Kontrast-Pass

### Nicht-Antithese / `sondern`
- `4a4839a` / `03be0af` – temporärer `Nicht`-Antithesen-Audit
- `abd1772` / `acf536c` / `1e18458` / `6c0725d` / `dbfbf69` – Antithesen-Reduktion und Korrekturen
- `a777fb9` – Kontroll-Audit nach Reduktion
- `bae5937` / `4f5a6b7` – `Nicht-sondern`-Audit
- `b67777f` / `a4b456d` / `79c75bd` – `sondern`-Rewrite
- `d5808fd` / `48ab74d` / `babeeac` / `9eb964b` – temporäre Audit-/Rewrite-Artefakte wieder entfernt
- `cf685a6` / `50973bd` – anschließende Guards im Quell-Repo

---

# Korpus

## A. `sondern` / binäre Kontrastformulierung

### 01
**Vorher**
> Vielleicht hatte die Quelle nicht die Gefahr gebaut, sondern genau diesen Moment.

**Nachher**
> Vielleicht hatte die Quelle genau diesen Moment gebaut. Die Gefahr selbst konnte unabhängig davon real sein.

- Muster-Kategorie: `nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd` – `Remove Nicht-sondern constructions`

### 02
**Vorher**
> Eine Person verließ den Kleinbus und ging nicht zur Seiteneinfahrt, sondern zu einem Nebengebäude.

**Nachher**
> Eine Person verließ den Kleinbus, ließ die Seiteneinfahrt links liegen und ging zu einem Nebengebäude.

- Muster-Kategorie: `nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 03
**Vorher**
> Sein Dienstausweis lag nicht wie sonst in der Jackentasche, sondern auf dem Tisch. Er hatte ihn herausgenommen, bevor Berg gekommen war.

**Nachher**
> Sein Dienstausweis lag auf dem Tisch. Sonst trug er ihn in der Jackentasche. Er hatte ihn herausgenommen, bevor Berg gekommen war.

- Muster-Kategorie: `nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 04
**Vorher**
> Berg zog Daniels Vermerk wieder zu sich und schrieb oben rechts eine kurze Notiz. Nicht für Daniel, sondern für die Akte.

**Nachher**
> Berg zog Daniels Vermerk wieder zu sich und schrieb oben rechts eine kurze Notiz für die Akte.

- Muster-Kategorie: `Nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 05
**Vorher**
> Die Frage war nicht mehr nur, woher die Quelle etwas wusste.
>
> Sondern was sie wollte, dass Daniel mit diesem Wissen tat.

**Nachher**
> Die Frage war nicht mehr nur, woher die Quelle etwas wusste. Ebenso wichtig war, was sie wollte, dass Daniel mit diesem Wissen tat.

- Muster-Kategorie: abgesetzte `Nicht ... Sondern ...`-Pointe
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 06
**Vorher**
> Das Problem lag weder im Kennzeichen noch im Altbestand, sondern in der Zahl der Treffer.

**Nachher**
> Das Problem lag in der Zahl der Treffer, nicht im Kennzeichen oder im Altbestand.

- Muster-Kategorie: `weder X noch Y, sondern Z`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 07
**Vorher**
> „Was machst du mit der Tatsache, dass du vielleicht nicht nur informiert, sondern ausgewählt wurdest?“

**Nachher**
> „Was machst du mit der Tatsache, dass du vielleicht ausgewählt wurdest und die Information nur das Mittel dazu war?“

- Muster-Kategorie: `nicht nur X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 08
**Vorher**
> Daniel ging zum Tisch zurück und öffnete nicht seinen privaten Block, sondern den formalen Projektvermerk.

**Nachher**
> Daniel ging zum Tisch zurück, ließ seinen privaten Block liegen und öffnete den formalen Projektvermerk.

- Muster-Kategorie: `nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 09
**Vorher**
> Das Foto zeigte nicht den Fahrer, sondern den Fahrzeugstandort.

**Nachher**
> Auf dem Foto war der Fahrzeugstandort zu sehen; der Fahrer fehlte.

- Muster-Kategorie: `nicht X, sondern Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

### 10
**Vorher**
> Damals hatte sich die Regel nicht wie Feigheit angefühlt, sondern wie Arbeit.

**Nachher**
> Damals war die Regel für ihn schlicht Arbeit gewesen. Feigheit hatte er darin nicht gesehen.

- Muster-Kategorie: `nicht wie X, sondern wie Y`
- Warum: gezielter `sondern`-Rewrite
- Quelle: `79c75bd`

---

## B. Rhetorische Symmetrie / Negations- und Dreischrittverdichtung

### 11
**Vorher**
> Die Quelle hatte einen wahren Punkt geliefert.
>
> Sie hatte nicht gelogen.
>
> Sie hatte nur den Satz weggelassen, der den Punkt weniger bedrohlich aussehen ließ.

**Nachher**
> Der Punkt war wahr. Nur der Satz darunter fehlte – der, der ihn weniger bedrohlich aussehen ließ.

- Muster-Kategorie: symmetrische Dreischritt-Erklärung
- Warum: Commit nennt ausdrücklich `reduce rhetorical symmetry`
- Quelle: `c6ed4ce` – `Tighten reversal prose and reduce rhetorical symmetry`

### 12
**Vorher**
> Kein Kennzeichen.
>
> Kein Ort.
>
> Kein Hinweis auf das Fahrzeug.

**Nachher**
> Das Kennzeichen fehlte. Der Ort auch. Vom Fahrzeug kein Wort.

- Muster-Kategorie: parallele Negationskette
- Warum: Reduktion rhetorischer Symmetrie
- Quelle: `c6ed4ce`

### 13
**Vorher**
> Das war der Satz.
>
> Nicht größer.
>
> Nicht sauberer.
>
> Nur der Satz.

**Nachher**
> Mehr brauchte Lena nicht zu sagen.

- Muster-Kategorie: bedeutungsschwere Ein-Satz-Absätze / Antithese
- Warum: Reduktion rhetorischer Symmetrie
- Quelle: `c6ed4ce`

### 14
**Vorher**
> Drei gewöhnliche Dinge.
>
> Keines davon sagte, warum.
>
> Zusammen sagten sie genug, um die Frage nicht mehr wegzulegen.

**Nachher**
> Keines der drei Dinge erklärte das Warum. Aber die Frage ließ sich nicht mehr weglegen.

- Muster-Kategorie: sauber gebauter Dreischritt
- Warum: Reduktion rhetorischer Symmetrie
- Quelle: `c6ed4ce`

### 15
**Vorher**
> Heller hatte Daniel nicht gezwungen, das Kennzeichen B-QV 4172 gegen den geschützten Bestand zu prüfen.
>
> Heller hatte ihn nicht gezwungen, die breitere Projektlogik anzunehmen.
>
> Heller hatte Lena nicht aus dem Informationsfluss genommen.
>
> Daniel hatte entschieden.
>
> Und die Entscheidungen hatten funktioniert.
>
> Genau deshalb waren sie brauchbar.

**Nachher**
> B-QV 4172 hatte Daniel selbst gegen den geschützten Bestand geprüft. Die breitere Projektlogik hatte er angenommen. Lena hatte er aus dem Informationsfluss genommen.
>
> Niemand hatte ihn dazu gezwungen.
>
> Und es hatte funktioniert.
>
> Genau deshalb waren die Entscheidungen brauchbar.

- Muster-Kategorie: dreifache Parallel-Negation / rhetorische Symmetrie
- Warum: Reduktion rhetorischer Symmetrie
- Quelle: `c6ed4ce`

---

## C. Meta-Erklärung / Erklär-Echo

### 16
**Vorher**
> Kein letzter Satz von Heller.
>
> Keine Nachricht.
>
> Keine Erklärung, die Daniel später hätte zitieren können.

**Nachher**
> Von Heller kam nichts mehr. Keine Nachricht, keine Erklärung.

- Muster-Kategorie: Negationskette / erklärende Nachführung
- Warum: Commit nennt `remove meta explanation`
- Quelle: `ca4d501` – `Tighten aftermath prose and remove meta explanation`

### 17
**Vorher**
> Nicht: Ob so etwas überhaupt noch einmal passieren darf.
>
> Welche Schwellen.
>
> Welcher Umfang.
>
> Welche Kontrolle.

**Nachher**
> [entfernt]

- Muster-Kategorie: explizite Meta-Ausdeutung / Listen-Pointe
- Warum: `remove meta explanation`
- Quelle: `ca4d501`

### 18
**Vorher**
> Kein Alarm.
>
> Keine moralische Pointe.
>
> Nur eine neue Frage, die schon so formuliert war, als wäre die alte erledigt.

**Nachher**
> Die neue Frage stand schon im Raum, als wäre die alte erledigt.

- Muster-Kategorie: Meta-Kommentar / Negationsdreischritt
- Warum: `remove meta explanation`
- Quelle: `ca4d501`

---

## D. Überkonstruiert / zu sichtbare Autorenformulierung

### 19
**Vorher**
> Der Schuss war härter als der Regen.

**Nachher**
> Der Knall war kurz und trocken.

- Muster-Kategorie: bedeutungsschwere / konstruierte Bildformulierung
- Warum: Commit nennt `remove overly constructed phrasing`
- Quelle: `0196047` – `Polish prose and remove overly constructed phrasing`

### 20
**Vorher**
> Normaler Dienstag.
>
> Normaler Verdacht.

**Nachher**
> [entfernt]

- Muster-Kategorie: künstliche Parallel-Pointe
- Warum: `remove overly constructed phrasing`
- Quelle: `0196047`

### 21
**Vorher**
> Das konnte etwas bedeuten.
>
> Es konnte auch genau das bedeuten, was es zeigte.

**Nachher**
> Daniel hatte schon schlechtere Gründe gesehen, nervös zu werden.
>
> Trotzdem reichte es nicht.

- Muster-Kategorie: abstrakte symmetrische Doppel-Lesart
- Warum: `remove overly constructed phrasing`
- Quelle: `0196047`

### 22
**Vorher**
> Der Verdacht löste sich nicht spektakulär auf. Kein Moment, in dem aus schwarz plötzlich weiß wurde. Die einzelnen Punkte verloren nur nacheinander ihre Richtung.
>
> Das Foto war ein Foto.
>
> Die Frage war eine Arbeitsfrage.
>
> Der Transporter war dort, weil er dort sein sollte.

**Nachher**
> Mit jedem Dokument wurde die Sache langweiliger.
>
> Daniel mochte langweilige Erklärungen.

- Muster-Kategorie: Übererklärung / rhetorisch ausgestellte Auflösung
- Warum: `remove overly constructed phrasing`
- Quelle: `0196047`

### 23
**Vorher**
> Als er später an Ahrens' Akte vorbeikam, war sie bereits aus seiner offenen Liste verschwunden.
>
> Das war der Sinn der Sache.

**Nachher**
> Als er später noch einmal in seine offene Liste sah, war Ahrens' Name verschwunden.

- Muster-Kategorie: Erklär-Echo nach bereits verständlicher Handlung
- Warum: `remove overly constructed phrasing`
- Quelle: `0196047`

### 24
**Vorher**
> Dann fiel es ihm auf.
>
> Nicht der Zusammenhang. Das Gegenteil.

**Nachher**
> Dann blieb er an den Zeitstempeln hängen.

- Muster-Kategorie: bedeutungsschwere Antithese / isolierte Pointe
- Warum: `remove overly constructed phrasing`
- Quelle: `0196047`

---

## E. External Review – Handlung statt Erzählerausdeutung

### 25
**Vorher**
> Das Thema war für sie beendet.

**Nachher**
> [entfernt]

- Muster-Kategorie: Erzähler erklärt sichtbare Szenenbedeutung
- Warum: Opening-Prosa nach externem Review poliert
- Quelle: `3534195` – `Polish opening prose after external review`

### 26
**Vorher**
> Es war der erste Satz des Abends, bei dem sie sich sichtbar ärgerte.
>
> „Nein“, sagte sie. „Ich kann denen nicht sagen, ich melde mich, wenn dein Kalender irgendwann freundlicher aussieht.“
>
> „Das verlange ich nicht.“
>
> „Noch nicht.“

**Nachher**
> Mara nahm ihr Glas und trank.
>
> „Ich kann denen nicht sagen, ich melde mich, wenn dein Kalender irgendwann freundlicher aussieht.“
>
> „Das verlange ich nicht.“
>
> Mara stellte das Glas ab. „Gut.“

- Muster-Kategorie: Gefühlsausdeutung durch konkrete Handlung ersetzt
- Warum: Opening-Prosa nach externem Review poliert
- Quelle: `3534195`

### 27
**Vorher**
> Sie redeten danach über andere Dinge. Einen kaputten Wasserhahn. Einen Kollegen von Mara, der bei jeder Videokonferenz zu früh in die Kamera kam. Darüber, dass Jana am Freitag allein zum Makler wollte.
>
> Der Abend wurde wieder normal.
>
> Der Termin blieb im Kalender.
>
> Sonntag, achtzehn Uhr.

**Nachher**
> Später räumten sie zusammen ab. Mara erzählte von einem Kollegen, der bei jeder Videokonferenz zehn Minuten zu früh im Bild saß und dann so tat, als wäre es Absicht.
>
> Daniel kannte den Mann nicht.
>
> Er lachte trotzdem.

- Muster-Kategorie: zusammenfassende Autorenaussage durch erlebte Alltagshandlung ersetzt
- Warum: Opening-Prosa nach externem Review poliert
- Quelle: `3534195`

---

## F. Frage-Antwort-Schleifen / Dialogrhythmus

### 28
**Vorher**
> „Donnerstag, halb vier.“
>
> „Jeweils wie lange?“
>
> „Wissen wir nicht.“
>
> „Video?“
>
> „Nur vom Donnerstag. Eingangskamera. Vier Minuten sichtbar.“

**Nachher**
> „Donnerstag, halb vier. Wie lange er jeweils dort war, wissen wir nicht. Video gibt es nur vom Donnerstag – Eingangskamera, vier Minuten sichtbar.“

- Muster-Kategorie: kleinteilige Frage-Antwort-Kaskade
- Warum: Commit `Refine manuscript dialogue rhythm`
- Quelle: `044f433`

### 29
**Vorher**
> „Hat Ahrens versucht reinzukommen?“
>
> „Nein.“
>
> „Hat er die Kamera verdeckt?“
>
> „Nein.“
>
> „Hat er irgendwen nach Sicherheitsmaßnahmen gefragt?“
>
> Jonas sah wieder auf den Vermerk. „Nicht laut dem Text.“

**Nachher**
> Daniel ging die nächsten Punkte selbst durch. Ahrens hatte weder versucht reinzukommen noch die Kamera verdeckt. Im Vermerk stand auch keine Frage nach Sicherheitsmaßnahmen.

- Muster-Kategorie: wiederholte Ja/Nein-Prüfschleife
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 30
**Vorher**
> „Fürs Prüfen schon.“
>
> „Für die Kontrolle nicht.“
>
> „Noch nicht.“

**Nachher**
> „Fürs Prüfen schon. Für die Kontrolle noch nicht.“

- Muster-Kategorie: künstlich fragmentierter Dialog
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 31
**Vorher**
> „Die hat dir die Firma geschickt?“
>
> „Ja.“
>
> „Mit vollständigen Headern?“
>
> „Weiterleitung aus ihrem System. Originalzeitstempel sichtbar.“
>
> „Gut.“

**Nachher**
> „Ja. Weiterleitung aus ihrem System, vollständige Header, Originalzeitstempel sichtbar.“

- Muster-Kategorie: Prüffrage-Bestätigung-Prüffrage-Bestätigung
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 32
**Vorher**
> „Hat jemand heute einen offenen Zugang gemeldet?“
>
> „Nein.“
>
> „Gestern?“
>
> „Nein.“
>
> „Fehlermeldung vom Schloss?“
>
> „Nicht dass ich wüsste.“

**Nachher**
> „Hat jemand heute oder gestern einen offenen Zugang gemeldet?“
>
> „Nein. Auch keine Fehlermeldung vom Schloss, nicht dass ich wüsste.“

- Muster-Kategorie: repetitive Abfrage-Schleife
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 33
**Vorher**
> „Die Abholung.“
>
> „Gut.“
>
> „Den Zusammenhang der Lieferadresse mit dem grauen Wagen, falls wir ihn identifizieren.“
>
> „Gut.“
>
> „Und ob Einheit 17 mit einem Dienstleister für die Veranstaltung verbunden ist.“

**Nachher**
> Jonas zählte auf: die Abholung; den Zusammenhang der Lieferadresse mit dem grauen Wagen, falls sie ihn identifizierten; und ob Einheit 17 mit einem Dienstleister für die Veranstaltung verbunden war.

- Muster-Kategorie: mechanische Listenabfrage im Dialog
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 34
**Vorher**
> „Kann Werkzeug sein.“
>
> „Ja.“
>
> „Messtechnik.“
>
> „Ja.“
>
> „Ersatzteile.“
>
> „Ja.“
>
> „Oder etwas Gefährliches.“
>
> „Ja.“

**Nachher**
> Werkzeug, Messtechnik, Ersatzteile – alles war möglich. Etwas Gefährliches auch.

- Muster-Kategorie: künstlich taktende Frage-/Bestätigungsstruktur
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

### 35
**Vorher**
> „Kennzeichen existiert. Mietfahrzeug. Seit gestern an eine kleine Kurierfirma ausgegeben.“
>
> „Verbindungen?“
>
> „Offen nichts. Firma ist real. Drei Fahrer, acht Fahrzeuge, macht alles von Medikamente bis Ersatzteile.“
>
> „Seit wann?“
>
> „Sieben Jahre im Register. Website passt. Keine auffällige Änderung.“
>
> „Wer hat den Wagen übernommen?“
>
> „Vertrag auf Firmenkonto. Fahrer nicht eindeutig zugeordnet.“
>
> „Zahlung?“
>
> „Normal über das Geschäftskonto.“

**Nachher**
> Jonas ging die Stammdaten gleich mit durch. Reale Firma, sieben Jahre im Register, drei Fahrer, acht Fahrzeuge, unauffällige Website. Vertrag und Zahlung liefen über das Geschäftskonto; der Fahrer war nicht eindeutig zugeordnet.

- Muster-Kategorie: lange interrogative Prüfschleife
- Warum: Dialogrhythmus verdichtet
- Quelle: `044f433`

---

## G. Leserpass – redundante Beweisführung und Nachanalyse

### 36
**Vorher**
> Heller sagte nicht mehr.
>
> Keine Geschichte. Keine Namen. Kein moralischer Schluss.
>
> Nur dieser Satz.

**Nachher**
> [entfernt]

- Muster-Kategorie: Erklär-Echo / autorenhafte Ausdeutung nach Dialog
- Warum: Skriptkommentar: `let Heller's sentence land without authorial interpretation`
- Quelle: `d9d418d` – `Tighten middle reader flow through chapter 26`

### 37
**Vorher**
> Auf dem zweiten Bildschirm liefen die übrigen Treffer aus der neuen Projektstruktur ein.
>
> [längere Parade einzelner banaler Fehlertreffer]
>
> Die Liste wurde länger, bevor sie kürzer wurde.

**Nachher**
> Auf dem zweiten Bildschirm liefen die übrigen Treffer aus der neuen Projektstruktur ein.
>
> Die meisten zerfielen schnell: Schreibvarianten, gemeinsam genutzte Bereitschaftsgeräte, verspätete Synchronisierung, legitime Schichten und reguläre Fahrzeuge. Jonas strich sie weg. Die Liste wurde länger, bevor sie kürzer wurde.

- Muster-Kategorie: wiederholte Demonstration / unnötig ausgespielte Beweisführung
- Warum: Skriptkommentar: `compress the first parade of banal false hits`
- Quelle: `d9d418d`

### 38
**Vorher**
> Daniel hörte Ahrens in dem Satz wieder.
>
> [längere methodische Nachanalyse des Weber-Fehlers]
>
> Er suchte nach der Form seiner eigenen Fehlentscheidung.

**Nachher**
> Nach dem Gespräch zog Daniel die Zeitlinie zurück. Diensthandy. Nachtzugang. Schichtübersicht. Bei jedem Punkt hatte es eine harmlose Gegenlesart gegeben. Er hatte sie gesehen. Nur weniger schwer gewichtet, je realer die Gefahr des Nicht-Handelns geworden war.
>
> Der breite Prüfkreis hatte real funktioniert. Weber war trotzdem falsch belastet worden. Beides blieb wahr.
>
> Der Fehler lag nicht in einer fehlenden Gegenhypothese. Er lag darin, was sie in Daniels Rechnung noch wert gewesen war.

- Muster-Kategorie: Methodiklektion / wiederholte Nachanalyse
- Warum: Skriptkommentar: `shorten Daniel's post-hoc methodology lecture`
- Quelle: `d9d418d`

### 39
**Vorher**
> Daniel blieb allein mit dem Projektvermerk.
>
> [erneutes Lesen / erneute Selbstvergewisserung der gesetzten Grenze]

**Nachher**
> Daniel blieb allein mit dem Projektvermerk.
>
> Im Moment meinte er jedes Wort.

- Muster-Kategorie: wiederholte Selbstbindungs-Erklärung
- Warum: Skriptkommentar: `remove repeated proof that he means it`
- Quelle: `d9d418d`

---

## H. Finaler Leserpass – Wiederholung und Übererklärung

### 40
**Vorher**
> Damit war der Druck nicht weg.
>
> Er hatte nur einen Zeugen dafür, dass Daniel ihn nicht heimlich in Evidenz verwandeln durfte.
>
> Nicht, dass die behauptete größere Gefahr stimmte.
>
> Nicht, dass Jana Ziel war.
>
> Nicht, dass beides zusammenhing.
>
> Daniel sagte sich das einmal.
>
> Dann noch einmal, weil sein Körper die Information offenbar nicht gelesen hatte.
>
> Sein Nacken war hart. Er stand noch immer.
>
> „Freigabe existiert“, sagte Jonas.

**Nachher**
> Damit war der Druck nicht weg.
>
> Er hatte nur einen Zeugen dafür, dass Daniel ihn nicht heimlich in Evidenz verwandeln durfte.
>
> „Freigabe existiert“, sagte Jonas.

- Muster-Kategorie: wiederholte Selbstkontroll-Erklärung / Negationskette
- Warum: Skriptkommentar: `one visible separation is enough; remove repeated self-explanation`
- Quelle: `492537b` – `Polish final reader rhythm before test readers`

### 41
**Vorher**
> Daniel zog ein Blatt quer vor sich und schrieb zwei Überschriften.
>
> **Was die breite Prüfung bereits gekostet hat.**
>
> **Was die breite Prüfung bereits gebracht hat.**
>
> [ausführliche Kosten-/Nutzen-Beweisführung mit mehreren Ergänzungen]

**Nachher**
> Daniel schrieb Weber und den Lagerraum nebeneinander. Beim einen: Fehlzuordnung, Arbeitgeberreaktion, Nachlauf. Beim anderen: realer Gefahrenstrang, wahrscheinlich früher sichtbar durch den breiten Kreis.
>
> Kein Erfolgs- oder Fehlschlagslabel.

- Muster-Kategorie: sichtbare Methodik-/Worksheet-Prosa
- Warum: Skriptkommentar: `keep the moral balance, remove the second checklist demonstration`
- Quelle: `492537b`

### 42
**Vorher**
> Heller sah kurz auf das Display.
>
> Daniel hörte seinen eigenen Atem lauter als den Funk.
>
> Keine der Alternativen verschwand.
>
> Sie liefen nur gleichzeitig aus derselben Sekunde heraus.
>
> Dann bewegte Heller den Daumen.
>
> Vielleicht hätte es gereicht.
>
> Vielleicht hätte Heller nur den Daumen bewegen müssen.
>
> Daniel wusste nicht, welche Möglichkeit wahrscheinlicher war.
>
> Er wusste nur, dass beide real waren.
>
> Heller bewegte den Daumen.
>
> Daniel zog die Waffe. Sein Unterarm war hart bis in die Finger. Er merkte es erst, als Heller schon fiel.
>
> Jetzt lag Heller vor ihm.

**Nachher**
> Heller sah kurz auf das Display.
>
> Daniel hörte seinen eigenen Atem lauter als den Funk.
>
> Hellers Daumen bewegte sich.
>
> Daniel zog die Waffe.
>
> Der Knall.
>
> Jetzt lag Heller vor ihm.

- Muster-Kategorie: Übererklärung unmittelbar vor Hochspannungsbeat
- Warum: Skriptkommentar: `alternatives are already established; final seconds stop explaining and accelerate`
- Quelle: `492537b`

---

## I. Style-Depth – Filterwörter, abstrakte Selbstbeobachtung und sichtbare Formel

### 43
**Vorher**
> Daniel merkte den Fehler, bevor sie etwas sagte.

**Nachher**
> Er hörte seinen eigenen Satz noch einmal, diesmal mit Maras Ohren.

- Muster-Kategorie: abstraktes Wahrnehmungs-/Filterverb
- Warum: Commit `Refine prose contrast and style formulas`
- Quelle: `7836a2d`

### 44
**Vorher**
> Er ging im Kopf die nächsten Tage durch. Zwei Termine am Samstag. Sonntagvormittag frei. Montag wieder voll. Er bemerkte, was er tat, und hörte damit auf.

**Nachher**
> Schon lief in seinem Kopf die nächste Woche an: zwei Termine am Samstag, Sonntagvormittag frei, Montag wieder voll. Als er bei Montag ankam, brach er die Rechnung ab.

- Muster-Kategorie: abstrakte Selbstbeobachtung (`bemerkte`) durch konkreten Denkablauf ersetzt
- Warum: `style formulas`
- Quelle: `7836a2d`

### 45
**Vorher**
> Daniel merkte, dass er den Atem angehalten hatte.
>
> Er ließ die Luft langsam aus.

**Nachher**
> Erst als die Brust spannte, fiel ihm auf, dass er den Atem anhielt. Langsam ließ er die Luft wieder aus.

- Muster-Kategorie: Filterformulierung durch körperlichen Träger konkretisiert
- Warum: `style formulas`
- Quelle: `7836a2d`

### 46
**Vorher**
> Das war sein Doppelspiel ab jetzt:
>
> Was die Quelle über den Fall wusste, wurde geprüft wie jeder andere Hinweis.
>
> Was sie über Daniel und den internen Ablauf wusste, wurde separat gegen mögliche Informationswege geprüft.

**Nachher**
> Von jetzt an liefen zwei Prüfungen nebeneinander: Was die Quelle über den Fall wusste, wurde geprüft wie jeder andere Hinweis. Was sie über Daniel und den internen Ablauf wusste, lief separat gegen mögliche Informationswege.

- Muster-Kategorie: autorenhafte Label-/Metaformel
- Warum: `style formulas`
- Quelle: `7836a2d`

---

## J. Anti-Tick-Pass – Weichmacher und Stakkato

### 47
**Vorher**
> Eine Hand hielt die Waffe ruhig.
>
> Nicht vollkommen ruhig. Aber ruhig genug.

**Nachher**
> Eine Hand hielt die Waffe ruhig genug.

- Muster-Kategorie: Antithesen-/Stakkato-Formel
- Warum: `Polish manuscript language patterns`; Passage war im Anti-Tick-Detailreport auffällig
- Quelle: `5ffa95b`

### 48
**Vorher**
> Drei, vielleicht vier Meter entfernt stand ein Mann im Regen. Mehr war von ihm kaum zu erkennen. Dunkle Kleidung. Die Schultern leicht nach vorn gezogen. Hinter ihm ein heller Streifen aus Glas und Beton, verschwommen im Wasser, das über die Scheiben lief.

**Nachher**
> Ein paar Meter entfernt stand ein Mann im Regen. Dunkle Kleidung, die Schultern leicht nach vorn gezogen. Hinter ihm verschwamm ein heller Streifen aus Glas und Beton im Wasser auf den Scheiben.

- Muster-Kategorie: Weichmacher + abgehackte Beschreibung
- Warum: Anti-Tick-/Sprachmuster-Pass
- Quelle: `5ffa95b`

### 49
**Vorher**
> „Vielleicht. Vielleicht fragt jemand nach dem Grund. Vielleicht wird aus einer Kontrolle eine zweite, weil ein Kollege den Vermerk sieht. Vielleicht passiert gar nichts.“

**Nachher**
> „Vielleicht fragt jemand nach dem Grund. Vielleicht wird aus einer Kontrolle eine zweite, weil ein Kollege den Vermerk sieht. Oder es passiert gar nichts.“

- Muster-Kategorie: Weichmacher-Cluster
- Warum: Anti-Tick-Report markierte den Absatz mit vier `vielleicht`; nach dem Pass blieben zwei
- Quelle: `5ffa95b`

### 50
**Vorher**
> Er blieb wieder stehen.
>
> Keine zweite Kugel.
>
> Keine Aufforderung.
>
> Keine Erklärung.

**Nachher**
> Es fiel kein zweiter Schuss.
>
> Erst jetzt trat er aus dem Schatten des Vordachs.

- Muster-Kategorie: Stakkato-/Negationskette
- Warum: Anti-Tick-Report führte die Passage ausdrücklich unter `Reine Prosa-Stakkato-Ketten` und `Negationsketten`
- Quelle: `5ffa95b`

---

## Quellen-Commits mit direkten Korpusbeispielen

- https://github.com/Satte882/Buch/commit/79c75bd0d234de9c62135024e717df9beb891998
- https://github.com/Satte882/Buch/commit/c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f
- https://github.com/Satte882/Buch/commit/ca4d50191b95f58ba1b99d61da9bf846141111ec
- https://github.com/Satte882/Buch/commit/01960472682349a7dd59fcebe2f528932dd20a46
- https://github.com/Satte882/Buch/commit/353419537bd78a8908b4307ba3255d2d461e6674
- https://github.com/Satte882/Buch/commit/044f433ca29b8446c7e72f3e9e7c01b7c614785b
- https://github.com/Satte882/Buch/commit/d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c
- https://github.com/Satte882/Buch/commit/492537b3e9175e4519a674dd1024badcd6a4dd93
- https://github.com/Satte882/Buch/commit/7836a2df945d45a95c9d5d0c7eeeb67885e7972b
- https://github.com/Satte882/Buch/commit/5ffa95b403eaeddc5ab6d34155462d344b3de133
