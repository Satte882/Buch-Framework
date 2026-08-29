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

## Direkter Final-Check

Am 29.08.2026 wurde der Bestandsstatus zusätzlich direkt gegen die aktuelle kanonische Datei `Satte882/Buch/AUSNAHMEZUSTAND_FINAL.md` auf `main` geprüft.

Prüflogik für diesen rein empirischen Check:

- Bei einer **Nachher-Formulierung** wurde die konkrete Nachher-Fassung bzw. eine ausreichend eindeutige exakte Passage im aktuellen Manuskript gesucht.
- Bei einer **vollständigen Entfernung** wurde geprüft, dass die charakteristische entfernte Formulierung im aktuellen Manuskript nicht mehr vorhanden ist.
- `Bis Final? = JA` bedeutet damit: die konkrete Korrekturform ist im finalen Stand noch nachweisbar.
- Semantisch ähnliche, aber später nochmals umformulierte Fassungen zählen **nicht** als `JA`.

Dieser Check hat eine frühere Zuordnung korrigiert: Beispiel **22** war zunächst als final-stabil markiert. Tatsächlich wurden die beiden Nachher-Sätze später zu `Mit jedem Dokument wurde die Sache langweiliger, und Daniel mochte langweilige Erklärungen.` zusammengezogen. Die in Beispiel 22 dokumentierte konkrete Nachher-Fassung ist daher ebenfalls ein Zwischenstand.

| Beispiel | Kapitel | Quelle-Commit | Datei | Bis Final? | Hinweis |
|---:|:---:|---|---|:---:|---|
| 01 | 14 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 02 | 16 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 03 | 17 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 04 | 17 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 05 | 18 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 06 | 20 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 07 | 26 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 08 | 26 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 09 | 31 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 10 | 36 | `79c75bd0d234de9c62135024e717df9beb891998` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 11 | 34 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 12 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 13 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 14 | 35 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 15 | 36 | `c6ed4ce82ea132fe82a5be38b47d7facc6b79a2f` | `MANUSKRIPT/04_BAUSTEIN_07.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 16 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 17 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Charakteristische entfernte Formulierung im aktuellen Final nicht vorhanden. |
| 18 | 43 | `ca4d50191b95f58ba1b99d61da9bf846141111ec` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 19 | Prolog | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | `Der Knall war kurz und trocken.` ist im finalen Prolog vorhanden. |
| 20 | 1 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | `Normaler Dienstag.` ist im aktuellen Final nicht vorhanden. |
| 21 | 1 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 22 | 2 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Später erneut verdichtet: Die zwei Nachher-Sätze wurden im Final zu `Mit jedem Dokument wurde die Sache langweiliger, und Daniel mochte langweilige Erklärungen.` zusammengezogen. |
| 23 | 2 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Später im Reader-Pass `2d1529f957075da72201978ce16d3c25b1b8004b` erneut gekürzt; die konkrete Nachher-Fassung ist nur ein Zwischenstand. |
| 24 | 3 | `01960472682349a7dd59fcebe2f528932dd20a46` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | `Dann blieb er an den Zeitstempeln hängen.` direkt im aktuellen Final nachgewiesen. |
| 25 | 4 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | JA | `Das Thema war für sie beendet.` ist im aktuellen Final nicht vorhanden. |
| 26 | 6 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Die Kapitel-6-Szene wurde in späteren Reader-/Ausbau-Pässen erneut überarbeitet; die konkrete Nachher-Fassung ist nicht final. |
| 27 | 6 | `353419537bd78a8908b4307ba3255d2d461e6674` | `MANUSKRIPT/01_BAUSTEINE_01_02.md` | NEIN | Der Kapitelabschluss wurde später erweitert/neu gefasst; die konkrete Nachher-Fassung ist ein Zwischenstand. |
| 28 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 29 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 30 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 31 | 1 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 32 | 7 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 33 | 9 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 34 | 10 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 35 | 13 | `044f433ca29b8446c7e72f3e9e7c01b7c614785b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 36 | 21 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Charakteristische entfernte Formulierung `Keine Geschichte. Keine Namen. Kein moralischer Schluss.` im aktuellen Final nicht vorhanden. |
| 37 | 23 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 38 | 24 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Nachanalyse direkt im aktuellen Final nachgewiesen. |
| 39 | 26 | `d9d418d2b916f6472d48adb8a1e2a876c4ff6b4c` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | `Im Moment meinte er jedes Wort.` direkt im aktuellen Final nachgewiesen. |
| 40 | 27 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 41 | 29 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/03_BAUSTEINE_05_06.md` | JA | Verdichtete Kosten-/Nutzen-Passage direkt im aktuellen Final nachgewiesen. |
| 42 | 40 | `492537b3e9175e4519a674dd1024badcd6a4dd93` | `MANUSKRIPT/05_BAUSTEINE_08_09.md` | JA | Verdichtete Hochspannungsfassung direkt im aktuellen Final nachgewiesen. |
| 43 | 6 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 44 | 6 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 45 | 8 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 46 | 18 | `7836a2df945d45a95c9d5d0c7eeeb67885e7972b` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Nachher-Fassung direkt im aktuellen Final nachgewiesen. |
| 47 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Eine Hand hielt die Waffe ruhig genug.` direkt im aktuellen Final nachgewiesen. |
| 48 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Ein paar Meter entfernt ...` direkt im aktuellen Final nachgewiesen. |
| 49 | 1 | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | Reduzierte `Vielleicht`-Fassung direkt im aktuellen Final nachgewiesen. |
| 50 | Prolog | `5ffa95b403eaeddc5ab6d34155462d344b3de133` | `AUSNAHMEZUSTAND_FINAL.md` | JA | `Es fiel kein zweiter Schuss. / Erst jetzt trat er ...` direkt im aktuellen Final nachgewiesen. |

## Bestandsübersicht

- **46 von 50** Korpusbeispielen: konkrete Nachher-Fassung bzw. Entfernung ist im aktuellen finalen Manuskript direkt nachweisbar.
- **4 von 50**: später erneut überarbeitet (`22`, `23`, `26`, `27`).
- Diese vier bleiben bewusst im Rohkorpus, weil sie reale Korrekturschritte dokumentieren; sie sind als **Zwischenstand** gekennzeichnet.
- Der frühere Befund `47/50` wurde durch den direkten Final-Check auf `46/50` korrigiert.

Damit ist die Provenienz der positiven Korpusbeispiele dokumentiert und gegen den aktuellen kanonischen Manuskriptstand gegengeprüft. Weitere Interpretation erfolgt hier nicht.