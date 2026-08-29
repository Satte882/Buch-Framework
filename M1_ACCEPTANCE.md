# M1 – Acceptance Criteria

## Zweck

M1 ist der erste Nachweis, dass das Framework im **realen Chat-Betriebsmodell** nicht nur einzelne Prüfwerkzeuge besitzt, sondern einen vollständigen Erzeugungspfad von der Buchidee bis zu einem Produktionsartefakt tragen kann.

M1 ist **kein** Beweis für die Qualität oder Skalierbarkeit eines vollständigen Romans.

Verbindliche Grundlagen:

- `ZIEL.md`
- `BETRIEBSMODELL.md`
- `SOURCE_OF_TRUTH.md`
- `KISS_LEITPLANKEN.md`
- `FRAMEWORK_PIPELINE.md`

## Fester Umfang des M1-Testfalls

Der M1-Testfall umfasst mindestens:

- 1 dokumentierte Buchidee,
- 1 Story Package,
- 1–2 zentrale Figuren,
- mindestens 1 plotrelevanten Rechercheeintrag,
- mindestens 3 geplante Szenen,
- mindestens 3 echte Prosa-Drafts,
- ein kanonisches Mini-Manuskript,
- ein finales Test-Produktionsartefakt.

Der generative Teil wird bewusst in ChatGPT ausgeführt. CI erzeugt keine Inhalte.

# Erfolgskriterien

M1 gilt nur dann als bestanden, wenn **alle** folgenden Kriterien erfüllt sind.

## A. Vollständiger Artefaktpfad

1. Ein dokumentierter Start-Input wurde durch die vollständige Kette G0–G6 geführt.
2. Die für jede Stufe vorgesehenen Repository-Artefakte existieren.
3. Kein notwendiges Zwischenergebnis existiert ausschließlich im Chat.

## B. Human Gates

4. Kein Human Gate wurde umgangen.
5. Jeder erforderliche Gate-Record bezieht sich auf einen konkreten Artefaktstand.
6. `APPROVE`, `REWORK` oder `STOP` wird ausschließlich als bewusste menschliche Entscheidung gesetzt.
7. ChatGPT oder ein deterministischer Checker darf keinen menschlichen Gate automatisch freigeben.

## C. Szenen und Prosa

8. Mindestens 3 Szenen erreichen nach den vorgesehenen Upstream-Gates eine G3-Freigabe.
9. Zu jeder dieser Szenen wird in einer bewusst angestoßenen Chat-Runde ein echter Prosa-Draft erzeugt und im Repository gespeichert.
10. Jeder Draft besitzt einen nachvollziehbaren Provenienzrecord nach `BETRIEBSMODELL.md`.
11. Jeder Draft verweist auf die relevanten freigegebenen Upstream-Artefakte bzw. deren feste Git-Referenzen.
12. Mindestens ein G4-Prosa-Stichproben-Gate wird real durchlaufen.

## D. Source of Truth und Invalidierung

13. Das kanonische Mini-Manuskript enthält ausschließlich freigegebene, nicht `stale`/`invalidated` Prosa-Artefakte.
14. Ein absichtlich veränderter relevanter Upstream-Stand führt dazu, dass das abhängige Downstream-Artefakt nicht still weiter als gültig verwendet werden darf.
15. Eine reine sprachliche Draft-Änderung aktualisiert keinen Story-/Character-State automatisch.
16. Eine beabsichtigte Storyänderung aus der Prosa wird zuerst upstream eingearbeitet und durch die betroffenen Gates zurückgeführt.

## E. Qualität

17. Der bestehende Prosa-Audit läuft auf dem M1-Manuskript.
18. Vor G5 gilt `FAIL = 0`.
19. Verbleibende `REVIEW`-Treffer sind entweder bearbeitet oder mit einer bewussten menschlichen Disposition dokumentiert.
20. M1 behauptet keine literarische Gesamtqualität, für die noch kein validierter Gate/Prüfmechanismus existiert.

## F. Produktion

21. Aus dem kanonischen Mini-Manuskript wird mindestens ein reproduzierbares finales Test-Produktionsartefakt erzeugt.
22. G6 bezieht sich auf genau diesen finalen Artefaktstand.
23. Das Produktionsformat darf für M1 bewusst minimal sein; es muss aber ein echter abgeleiteter Output sein und darf nicht nur eine Kopie des Manuskripttexts unter anderem Namen sein.

## G. Fehler- und Abbruchfälle

24. Ein absichtlich fehlendes oder inkonsistentes Upstream-Artefakt blockiert den deterministischen Pipeline-Check.
25. Eine ungelöste plotrelevante Rechercheabhängigkeit blockiert die betroffene Szene entsprechend den bestehenden Regeln.
26. Ein fehlender Human Gate blockiert den Übergang in die nächste geschützte Stufe.
27. Wird ein Chat-Schritt abgebrochen oder kein gültiges Zielartefakt committed, gilt die Stufe nicht als abgeschlossen.
28. Ein `stale` oder `invalidated` Draft darf nicht in das kanonische Mini-Manuskript gelangen.

## H. CI-Grenze

29. CI prüft ausschließlich deterministische Bestandteile: Contracts, Referenzen, Gate-Status, Tests, Audits, Invalidierungslogik und Builds.
30. Kein M1-Erfolgskriterium setzt einen programmatischen LLM-Aufruf, Provider-Adapter, API-Key, Mock-Provider, Tokenzähler oder Kostenbudget voraus.

# Messbarer M1-Abschlussbericht

Der Abschlussbericht muss mindestens enthalten:

```text
Artefaktpfad G0–G6: PASS / FAIL
Human Gates vollständig: PASS / FAIL
G3-freigegebene Szenen: <n> (Minimum 3)
committete Prosa-Drafts: <n> (Minimum 3)
Drafts mit Provenienz: <n>/<n>
Invalidierungstest: PASS / FAIL
Prosa-Audit FAIL: <n> (erwartet 0)
Prosa-Audit REVIEW offen ohne Disposition: <n> (erwartet 0 vor G5)
Produktionsartefakt erzeugt: PASS / FAIL
Deterministische CI: PASS / FAIL
bekannte Einschränkungen dokumentiert: PASS / FAIL
M1 Gesamt: PASS / FAIL
```

# Bewusste Nicht-Kriterien

Für M1 werden **nicht** verlangt:

- 70.000+ Wörter,
- vollständige Romanqualität,
- autonome Storyentwicklung,
- autonome Rewrite-Loops,
- wortgleiche Reproduktion eines Chat-Outputs,
- LLM-Kostenmessung,
- API-/Provider-Infrastruktur,
- generative CI.

# M1-Abnahme

M1 ist nur abgeschlossen, wenn der reale Chat-/GitHub-Prozess einmal vollständig durchlaufen und die obige Acceptance-Liste gegen die tatsächlich entstandenen Artefakte geprüft wurde.

> **M1 beweist die Kette, nicht die Tiefe.**
