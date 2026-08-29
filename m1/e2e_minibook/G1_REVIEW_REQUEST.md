# G1 Review Request – FEHLALARM

status: AWAITING_HUMAN_G1_DECISION
story_package: `m1/e2e_minibook/STORY_PACKAGE.md`
story_package_ref: `d2b1c8d5c46f5afb51f876a652735b431ed9ab22`
provenance: `m1/e2e_minibook/provenance/STORY_PACKAGE.md`
prior_gate: `m1/e2e_minibook/gates/G0.md`

## Zweck

Dies ist die menschliche G1-Vorlage für den vollständigen M1-End-to-End-Test. Sie enthält bewusst noch **keine** Freigabe.

G1 prüft hier, ob die Storyarchitektur für den kleinen Integrationsfall ausreichend feststeht, damit Figuren-/Recherche-Basis und anschließend drei konkrete Szenen entwickelt werden dürfen.

## Was jetzt festgelegt ist

- **Drei-Szenen-Struktur:**
  - S1: Alarm + nachvollziehbare Abkürzung,
  - S2: lokale Prüfung + Harmlosigkeitsannahme bricht,
  - S3: volle Eskalation + reale Konsequenz.
- **Protagonistin:** Mara Voss trägt Perspektive und finale Entscheidung.
- **Gegenkraft:** Nils Berger vertritt einen legitimen betrieblichen Gegenanreiz; kein versteckter Bösewicht.
- **Mechanismus:** frühere Fehlalarme + informelle Routine + wirtschaftlicher Druck senken die Eskalationsbereitschaft; neue konkrete Hinweise erzwingen eine Neubewertung.
- **Reversal/Umdeutung:** Frühere Fehlalarme bleiben wahr, liefern aber keine Entwarnung für den aktuellen Fall.
- **Konsequenz:** Eine unerwartet noch anwesende Laborperson macht das Risiko real; der Nachtversuch geht durch die richtige Eskalation tatsächlich verloren.
- **Storyentscheidungen offen:** `no`.

## Bewusst noch nicht abgeschlossen

`R-001` bleibt als Recherche-Risiko offen: Welche vereinfachte Alarm-/Verifikationskette ist für ein modernes Forschungs-/Laborgebäude plausibel?

Das ist **kein offener Storyentscheid**. Die Storyfunktion ist fest: Mara prüft zunächst lokal und löst später die volle Sicherheitsreaktion aus. G2 muss lediglich eine plausible, nicht sicherheitskritisch überdetaillierte Ausgestaltung dafür festlegen.

## G1-Reviewfragen

1. Trägt der Konflikt die drei Szenen ohne künstliche Zusatzhandlung?
2. Ist Maras Entscheidungskette nachvollziehbar und klar genug, um später nicht in der Prosa neu erfunden werden zu müssen?
3. Bleibt Nils ein legitimer Gegenanreiz statt ein nachträglich bequem gemachter Antagonist?
4. Funktioniert die Umdeutung ohne Twist-Trick oder verstecktes Wissen?
5. Ist die Informationsarchitektur klar genug: Leser und Mara lernen schrittweise dieselben relevanten Signale?
6. Ist der Umfang weiterhin angemessen für einen wegwerfbaren M1-Integrationsfall?
7. Gibt es eine noch offene irreversible Storyentscheidung, die vor G1 geklärt werden müsste?

## Nächste menschliche Entscheidung

- `APPROVE` – Story Package darf als G1-Basis für Figuren-/Recherche-Basis verwendet werden.
- `REWORK` – konkrete Storypunkte werden gezielt überarbeitet.
- `STOP` – M1-Testfall wird beendet.

Erst nach einer ausdrücklichen menschlichen G1-Entscheidung werden `CHARACTERS.md` und `RESEARCH_REGISTER.md` für diesen M1-Lauf erzeugt.