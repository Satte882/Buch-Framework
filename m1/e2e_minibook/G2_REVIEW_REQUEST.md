# G2 Review Request – FEHLALARM v0.2

status: AWAITING_HUMAN_G2_DECISION
prior_gate: `m1/e2e_minibook/gates/G1.md`
prior_gate_ref: `41a9016f55a3a793b9e0e51a73471b9341c8be5e`
prior_g2_record: `m1/e2e_minibook/gates/G2.md` – superseded v0.1 test trace; not valid for this v0.2 package
prior_g3_artifacts: historical v0.1 traces; not active before a new valid G2 decision

## Zweck

Dies ist die gebündelte menschliche **G2 – Prose Ready**-Vorlage für den FEHLALARM-M1-Lauf nach der v0.2-Arbeitsweise.

G2 prüft gemeinsam:

1. die horizontal geschlossene Beat-Ebene,
2. alle daraus aktiven Szenenkarten,
3. die szenenspezifischen Character States,
4. die für diese Szenen relevanten Rechercheabhängigkeiten.

Es gibt keinen isolierten Human Gate für einzelne Beats oder Szenenkarten.

## Zu prüfende Artefaktstände

### Beats

- `m1/e2e_minibook/BEATS.md` — blob `ce33eb6a09458484b69691dc1425c50e318dce3e`

### Aktive Szenenkarten

- `m1/e2e_minibook/scenes/S1.md` — blob `f48d98a3ba5fd46df773a240e39462cc8746faf2`
- `m1/e2e_minibook/scenes/S2.md` — blob `3927e437150f0cd504f874f0cf3d081cfed8e8f1`
- `m1/e2e_minibook/scenes/S3.md` — blob `fbef326de65711c50c9baf4d0c0fc2c2f1158eb3`

### Character States

- `m1/e2e_minibook/character_states/S1_MARA.md` — blob `0c17101e0a7a97f12c0d8edace64abbe47eceb27`
- `m1/e2e_minibook/character_states/S1_NILS.md` — blob `91f8aa5dddd057e9f6c1766de5e98d91538465c6`
- `m1/e2e_minibook/character_states/S2_MARA.md` — blob `91828b11e00b41b199fd149d160d0a5b42d3812c`
- `m1/e2e_minibook/character_states/S2_NILS.md` — blob `156c8177175363119e7ac1a94bb8e7ce1400cc2a`
- `m1/e2e_minibook/character_states/S3_MARA.md` — blob `a2798e72fd9b229cf113e7e6bb3d44658862982c`
- `m1/e2e_minibook/character_states/S3_NILS.md` — blob `0d4e7e5c8c2b8d281a09c7856e80e0141c10e62f`
- `m1/e2e_minibook/character_states/S3_LEA.md` — blob `331de76f01df0d05346dc99928bbc70280928b9a`

### Recherche

- `m1/e2e_minibook/RESEARCH_REGISTER.md` — blob `a1026077fc15be857827f691f76bcb4ca0bfe4eb`

## Makro→Mikro-Abdeckung

### S1 – Die vernünftige Abkürzung

`BT001–BT004`

Die Szene etabliert Warnsignal, unvollständige Fernverifikation, offiziellen Leerstand, realen Versuchsschaden und Maras bewusste Entscheidung zur lokalen Prüfung. Ein alter v0.1-Zusatzhinweis („zweite Statusabweichung“) wurde entfernt, weil er nicht Teil der freigegebenen v0.2-Event-/Beat-Kette ist.

### S2 – Das Muster passt nicht mehr

`BT005–BT010`

Die Fehlalarm-Hypothese bleibt zunächst plausibel, verliert aber durch Anwesenheitsabweichung und physischen Gefahrenhinweis ihre Tragfähigkeit. Nils bleibt eine legitime Gegenoption. Mara beendet die lokale Prüfroutine aufgrund kumulierender Evidenz und aktiviert die volle interne Alarm-/Evakuierungskette.

### S3 – Der Preis der richtigen Entscheidung

`BT011–BT015`

Leas reale Restanwesenheit und der reale Warnanlass werden bestätigt; der Nachtversuch bleibt verloren. Die früheren Fehlalarme werden nicht rückwirkend umgeschrieben. Der Schluss setzt die Grenze der Routine über Evidenzgewichtung statt über einen zusätzlichen Twist oder Schuldigen.

## Figuren- und Wissenskonsistenz

- Mara trägt die erste Abkürzung und deren spätere Korrektur selbst.
- Nils besitzt zu keinem Zeitpunkt verborgenes Mehrwissen; sein Gegenanreiz bleibt der reale Versuchsschaden.
- Lea ist bis S3 für Mara und Nils nicht als tatsächlich anwesende Person bestätigt.
- Leas Restanwesenheit bleibt eine banale betriebliche Abweichung und kein Komplott.
- Keine Szene benötigt für ihre zentrale Entscheidung neues Figurenwissen außerhalb der Character States.

## Recherche

`R-001` ist `resolved`, `blocking_now: no` und wird in allen sicherheits-/verifikationsrelevanten Beats und Szenen referenziert.

Die Szenen bleiben bei einem internen technischen Rauch-/Prozesswarnsignal mit lokaler Verifikation und einer späteren separaten vollen internen Alarm-/Evakuierungskette. Keine Szene behauptet eine frei verzögerbare öffentliche Brandmelde-/Feuerwehrlogik.

## Deterministischer G2-Vorcheck

Nach dem v0.2-Checker-Vertrag sind aktiv:

- `S1` mit exakt `BT001–BT004`,
- `S2` mit exakt `BT005–BT010`,
- `S3` mit exakt `BT011–BT015`,
- sieben referenzierte Character-State-Dateien,
- keine offene blockierende Recherche.

Der vorhandene alte `gates/G2.md` kann diesen Stand absichtlich **nicht** freigeben: Er enthält weder `BEATS.md` noch die drei aktiven Szenenkarten und deren Character States. Damit bleibt die Pipeline vor G2 korrekt blockiert, bis eine neue menschliche Entscheidung über dieses Paket vorliegt.

## G2-Reviewfragen

1. Sind alle 15 Beats in den drei Szenen vollständig und ohne zusätzliche Storylogik umgesetzt?
2. Könnte jede Szene auf Basis ihrer Karte geschrieben werden, ohne eine relevante Plot-, Figuren-, Recherche-, Informations- oder Konsequenzentscheidung neu erfinden zu müssen?
3. Ist Maras lokale Prüfung in S1 weiterhin nachvollziehbar, ohne als offensichtlich fahrlässig zu wirken?
4. Entsteht der Kipppunkt in S2 aus kumulierender Evidenz statt einem künstlichen Einzelindiz?
5. Bleibt Nils auch im Konflikt eine legitime Gegenposition statt eines Strohmann-Antagonisten?
6. Ist Leas Informations- und Anwesenheitslogik über S1–S3 konsistent?
7. Sind die Character States zwischen den Szenen widerspruchsfrei und ausreichend für kontrollierte Prosa?
8. Bleibt R-001 ausreichend geschlossen, sodass beim Schreiben keine plotrelevante Sicherheitsprozedur erfunden werden muss?
9. Gibt es noch irgendeine relevante Entscheidung, die derzeit erst beim Prosaschreiben getroffen werden müsste?

## Nächste menschliche Entscheidung

- `G2-APPROVE` – genau die oben referenzierten Beat-, Szenen-, Character-State- und Research-Stände werden als **Prose Ready** freigegeben.
- `G2-REWORK` – konkrete Beat-/Szenen-/State-/Research-Punkte werden gezielt überarbeitet.
- `G2-STOP` – der M1-Testfall wird an dieser Stelle beendet.

**Wichtig:** Ein früheres G2-/G3-APPROVE des alten v0.1-Pfads gilt nicht automatisch für dieses neue Paket. Erst nach einem neuen menschlichen `G2-APPROVE` darf `gates/G2.md` auf diese konkreten Artefaktstände aktualisiert und `experience_status` der drei aktiven Szenen auf `human_reviewed_ready` gesetzt werden.