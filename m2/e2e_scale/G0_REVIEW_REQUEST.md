# G0 Review Request – SPERRFRIST M2

status: AWAITING_HUMAN_G0_DECISION
gate_name: Konzept
m2_issue: `#10 – M2 – Skalierungsnachweis mit komplexem 10-Szenen-Testfall`

## Zweck

G0 prüft ausschließlich, ob die **Konzeptbasis** von SPERRFRIST tragfähig genug ist, um danach horizontal in die Story-Architektur einzusteigen.

Noch nicht Gegenstand von G0 sind:

- konkrete dramaturgische Bausteine,
- Ereignisse/Sequenzen,
- Beats,
- Szenenkarten,
- Character States,
- Prosa,
- konkrete Review-Batch-Pakete.

Diese Ebenen dürfen erst nach G0 systematisch erzeugt werden.

## Zu prüfender Konzeptstand

- `m2/e2e_scale/BOOK_IDEA.md`
- blob: `1699fd17f8feda996fb542380c20d3045b235587`

## Konzept in Kurzform

**Arbeitstitel:** SPERRFRIST  
**Genre:** Investigativ-Thriller / M2-Skalierungstest

Nora Feld, Leiterin eines Investigativ-Teams, erhält ein internes Dossier über möglicherweise geschönte sicherheitsrelevante Prüfberichte eines fiktiven Notfall-Kommunikationssystems. Unter Veröffentlichungs- und Konkurrenzdruck muss sie klären, welche Teile belastbar sind, welche Dokumentstände veraltet sein könnten, wer was wann wusste und wie Quelle, Redaktion und Öffentlichkeit durch eine falsche oder verspätete Veröffentlichung betroffen wären.

Der Fall arbeitet bewusst mit mindestens zwei getrennten Informationssträngen:

1. tatsächliche technische Gefährdung,
2. Verantwortungs-/Wissensfrage im Unternehmen.

Ein später Beleg soll die technische Kernkritik stärken, aber eine bis dahin zentrale Verantwortungsannahme widerlegen. Die Auflösung besteht deshalb nicht aus einem großen Täter-Twist, sondern aus einer engeren, besser belegten Veröffentlichung mit realem Preis.

## Warum dieses Konzept M2 tatsächlich belastet

Der Stoff erzwingt voraussichtlich:

- mindestens vier plotrelevante Figuren mit legitimen, teilweise gegensätzlichen Zielen,
- mehrere über Szenen laufende Vertrauens-/Beziehungsentwicklungen,
- zwei getrennte Reveal-/Informationsstränge,
- mehrere widersprüchliche Quellen und Dokumentstände,
- mindestens zwei Rechercheabhängigkeiten,
- eine spätere relevante Upstream-Korrektur mit Downstream-Rework,
- Koordination unter einer durchgehenden Deadline.

Damit testet M2 nicht nur `3 → 10 Szenen`, sondern zusätzliche Abhängigkeitskomplexität.

## Bewusste Grenzen

- Kein realer Konzern und kein politischer Schlüsselroman.
- Kein Hacker-/Geheimdienst-/KI-Twist.
- Keine künstliche Komplexität nur zur Erfüllung von Kennzahlen.
- Noch keine neue semantische QA-Funktion.
- Noch keine deterministischen Review-Projektionen.
- Keine zusätzlichen Human Gates.
- Der Testfall wird nicht zu Buch 3 weiterentwickelt.

## Vorgesehene Recherchefelder – noch ungelöst

1. `R-01` – plausibler deutscher Veröffentlichungs-/Presserechtsrahmen für Tatsachenbehauptung, Verdachtsberichterstattung, Stellungnahme und Quellenschutz.
2. `R-02` – plausibler technischer Prüf-/Versions-/Freigabekontext für ein sicherheitsrelevantes Notfall-Kommunikationssystem.

Diese Punkte werden bewusst **nicht vor G0 gelöst**. Ihre konkrete Blockierwirkung wird erst dort entschieden, wo die jeweilige Story-/Ereignisentscheidung tatsächlich davon abhängt.

## G0-Reviewfragen

1. Trägt der zentrale Konflikt `Tempo vs. Belegbarkeit/Quellenschutz` einen 10-Szenen-Testfall, ohne künstlich gestreckt zu wirken?
2. Ist die Leitfrage klar genug und gleichzeitig offen genug, dass keine moralisch vorentschiedene Geschichte entsteht?
3. Bietet der Stoff echte Multi-Strang-Komplexität statt bloß mehr Szenen?
4. Sind David, Mira, Jonas sowie die beiden Quellen als legitime Gegenkräfte/Funktionsrollen plausibel genug, ohne bereits zu tief in Figurenplanung einzusteigen?
5. Ist die Trennung zwischen technischer Kernkritik und Verantwortungs-/Wissensfrage als Informationsarchitektur sinnvoll?
6. Ist der geplante spätere Gegenbeleg als Rework-/Invalidierungsanlass geeignet, ohne einen künstlichen Testfehler zu erzwingen?
7. Sind die beiden vorgesehenen Recherchefelder relevant genug, um die Blockierregel unter realer Last zu testen?
8. Ist der Stoff ausreichend eigenständig gegenüber FEHLALARM und NORMALFALL?
9. Würdest du genau `BOOK_IDEA.md` blob `1699fd17f8feda996fb542380c20d3045b235587` als Konzeptbasis für M2 freigeben?

## Nächste menschliche Entscheidung

- `G0-APPROVE` — genau der referenzierte BOOK_IDEA-Blob wird als M2-Konzept akzeptiert; danach folgen horizontal STORY_BLOCKS → EVENTS → Figurenkern/Recherche und das gebündelte G1-Paket.
- `G0-REWORK` — konkrete Konzeptbefunde werden überarbeitet; noch keine tieferen Ebenen erzeugen.
- `G0-STOP` — M2 an dieser Stelle beenden.

**Wichtig:** Weder ChatGPT noch Checker dürfen G0 selbst freigeben.