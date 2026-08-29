# NORMALFALL – Provenienz der 50 Korpusbeispiele

Zweck dieser Datei: die 50 realen Vorher/Nachher-Beispiele aus `tests/corpus/normalfall_beispiele.md` auf ihre konkrete Herkunft und ihren späteren Bestand im kanonischen Manuskript zurückführen.

Diese Datei enthält **keine** Regeln, Schwellenwerte, Detektionslogik oder Framework-Architektur.

## Bedeutung der Spalten

- **Beispiel**: Nummer aus `normalfall_beispiele.md`
- **Kapitel**: Kapitel, in dem der konkrete Diff lag
- **Quelle-Commit**: vollständiger SHA des Commits mit der Prosaänderung
- **Datei**: im Quell-Commit geänderte Manuskriptdatei
- **Bis Final?**: ob die konkrete Nachher-Fassung bzw. Entfernung bis zum finalen kanonischen Manuskript Bestand hatte
- **Hinweis**: nur Provenienz-/Bestandsinformation

`Final` bezeichnet den aktuellen kanonischen Prosa-Stand in `Satte882/Buch/AUSNAHMEZUSTAND_FINAL.md` auf `main`.

| Beispiel | Kapitel | Quelle-Commit | Datei | Bis Final? | Hinweis |
|---:|:---:|---|---|:---:|---|
| 01 | 14 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 02 | 16 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 03 | 17 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 04 | 17 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 05 | 18 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 06 | 20 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 07 | 26 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 08 | 26 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 09 | 31 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 10 | 36 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 11 | 34 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung ist im finalen Kapitel 34 noch vorhanden. |
| 12 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Keine spätere Ersetzung der Nachher-Fassung gefunden. |
| 13 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Keine spätere Ersetzung der Nachher-Fassung gefunden. |
| 14 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung blieb im späteren Kapitel-35-Stand erhalten. |
| 15 | 36 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung ist im finalen Kapitel 36 noch vorhanden. |
| 16 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Nachher-Fassung blieb bestehen. |
| 17 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Entfernung blieb bestehen. |
| 18 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Nachher-Fassung blieb bestehen. |
| 19 | Prolog | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | `Der Knall war kurz und trocken.` ist im finalen Prolog vorhanden. |
| 20 | 1 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Entfernung blieb bestehen. |
| 21 | 1 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Nachher-Fassung blieb bestehen. |
| 22 | 2 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Nachher-Fassung blieb bestehen. |
| 23 | 2 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Später im Reader-Pass `2d1529f957075da72201978ce16d3c25b1b8004b` erneut gekürzt; die konkrete Nachher-Fassung ist nur ein Zwischenstand. |
| 24 | 3 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Nachher-Fassung blieb bestehen. |
| 25 | 4 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Entfernung blieb bestehen. |
| 26 | 6 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Die Kapitel-6-Szene wurde in späteren Reader-/Ausbau-Pässen erneut überarbeitet; die konkrete Nachher-Fassung ist nicht final. |
| 27 | 6 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Der Kapitelabschluss wurde später erweitert/neu gefasst; die konkrete Nachher-Fassung ist ein Zwischenstand. |
| 28 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 29 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 30 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 31 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 32 | 7 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 33 | 9 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 34 | 10 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 35 | 13 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 36 | 21 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Entfernung blieb bestehen. |
| 37 | 23 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Nachher-Fassung blieb bestehen. |
| 38 | 24 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Nachanalyse blieb bestehen. |
| 39 | 26 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | `Im Moment meinte er jedes Wort.` wurde in späteren Guards ausdrücklich als geschützter Anker geführt. |
| 40 | 27 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Entfernung der wiederholten Selbsterklärung blieb bestehen. |
| 41 | 29 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Kosten-/Nutzen-Passage blieb bestehen. |
| 42 | 40 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Verdichtete Hochspannungsfassung blieb bestehen. |
| 43 | 6 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 44 | 6 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 45 | 8 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung blieb bestehen. |
| 46 | 18 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung ist im finalen Kapitel 18 weiterhin vorhanden. |
| 47 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Eine Hand hielt die Waffe ruhig genug.` ist final vorhanden. |
| 48 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Ein paar Meter entfernt ...` ist final vorhanden. |
| 49 | 1 | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Reduzierte `Vielleicht`-Fassung ist final vorhanden. |
| 50 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Es fiel kein zweiter Schuss. / Erst jetzt trat er ...` ist final vorhanden. |

## Bestandsübersicht

- **47 von 50** Korpusbeispielen: konkrete Nachher-Fassung bzw. Entfernung blieb bis zum finalen Manuskript bestehen.
- **3 von 50**: später erneut überarbeitet (`23`, `26`, `27`).
- Diese drei bleiben bewusst im Rohkorpus, weil sie reale Korrekturschritte dokumentieren; sie sind lediglich als **Zwischenstand** gekennzeichnet.

Damit ist die Provenienz der positiven Korpusbeispiele dokumentiert. Weitere Interpretation erfolgt hier nicht.