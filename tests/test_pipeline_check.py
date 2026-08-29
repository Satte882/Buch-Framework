from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import pipeline_check  # noqa: E402
import scene_readiness  # noqa: E402

PIPELINE_CONFIG = pipeline_check.load_config(ROOT / "config" / "pipeline_contract.yml")
SCENE_CONFIG = scene_readiness.load_config(ROOT / "config" / "scene_readiness.yml")


BOOK_IDEA = """# BOOK_IDEA
working_title: Testroman
genre: Psychothriller
core_conflict: Sicherheit gegen legitime Selbstbestimmung
central_question: Wann wird Schutz selbst zum Kontrollproblem?
mechanism: Ein erfolgreiches Schutzsystem verschiebt schrittweise die Entscheidungsmacht.
promise_to_reader: Schneller Thriller mit moralischer Reibung.
non_goals: Kein allwissender Bösewicht und keine Technikmagie.
irreversible_decisions_open: no
"""

STORY_PACKAGE = """# STORY_PACKAGE
working_title: Testroman
version: v0.1
premise_summary: Ein wirksames Schutzsystem verändert nach Erfolgen die legitime Entscheidungsmacht.
core_conflict_summary: Sicherheit und Selbstbestimmung sind gleichzeitig legitim.
central_question: Wann wird Schutz selbst zum Kontrollproblem?
mechanism_summary: Jeder Erfolg senkt die Schwelle für den nächsten Eingriff.
protagonist_arc_summary: Vorsicht → Akzeptanz → bewusste Grenzverschiebung → Verantwortung.
plot_architecture_summary: Fünf Eskalationsstufen mit Reversal und offenem Nachhall.
reversal_summary: Die Erfolge bleiben real, ihre institutionelle Bedeutung kippt.
information_architecture_summary: Leser akzeptiert Nutzen zuerst und erkennt den Preis verzögert.
character_functions_summary: Protagonist, Gegenfigur und unabhängige Betroffene besitzen eigene Ziele.
story_decisions_open: no
"""

CHARACTERS = """# CHARACTERS
version: v0.1
story_package_version: v0.1
roster_summary: Alex trägt die Entscheidung; Bea vertritt eine gleichwertige Gegenlogik.
relationship_baseline_summary: Alex und Bea vertrauen einander fachlich, gewichten Risiken aber unterschiedlich.
open_character_decisions: no
"""

RESEARCH = """# RESEARCH_REGISTER
register_status: ready

| ID | Frage | Betroffene Szene(n) | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung |
|---|---|---|---|---|---|---|
| R-001 | Wie funktioniert die reale Freigabekette? | S-001 | high | resolved | Fachquelle A | Für den Roman gilt eine zweistufige Freigabe. |
| R-002 | Welche Oberfläche zeigt das System? | S-004 | low | open |  |  |
"""

CHARACTER_STATE = """# CHARACTER_STATE
scene_id: S-001
character: Alex
status: ready
knows_before: Die Freigabe ist formal zweistufig.
believes_before: Das Verfahren schützt vor vorschnellen Eingriffen.
wants_now: Einen belastbaren Hinweis prüfen.
fears_or_avoids: Einen Unbeteiligten unnötig zu belasten.
relationship_state: Fachliches Vertrauen zu Bea bei unterschiedlicher Risikogewichtung.
must_not_know_yet: Dass das System später ausgeweitet wird.
knows_after: Der Hinweis ist real, aber noch nicht ausreichend.
believes_after: Das Verfahren ist langsam, aber weiterhin begründbar.
relationship_change: unchanged
decision_or_commitment: Alex bleibt beim regulären Weg.
"""

SCENE = """# SCENE_PLAN
scene_id: S-001
title: Der schnelle Weg
story_function: Ausgangsgrenze des Protagonisten konkret zeigen.
pov: Alex
location_time: Lagebüro am Dienstagmorgen.
characters_present: Alex; Bea
goal: Einen belastbaren Hinweis rechtzeitig prüfen.
conflict: Der schnellere Weg wäre praktisch, ist aber noch nicht ausreichend begründet.
decision: Alex bleibt beim regulären Prüfweg.
consequence: Die Spur bleibt offen und Zeit geht verloren.
reader_before: Der Leser kennt Alex noch nicht.
reader_after: Alex wägt Tempo gegen Eingriffsrisiko ab.
must_not_reveal: Die spätere Ausweitung des Systems.
character_state_status: ready
research_status: ready
story_decisions_open: no
narrative_weight: medium
experience_status: human_reviewed_ready
pressure_progression: Ein zunächst plausibler Hinweis wird dringlicher, während die Beleglage dünn bleibt.
observable_actions: Alex prüft Akten, stellt Gegenfragen und verwirft eine Abkürzung.
alternatives_in_scene: Bea benennt einen realistisch schnelleren Weg, der ebenfalls nachvollziehbar bleibt.
consequence_carrier: Eine Frist läuft sichtbar weiter, während die Spur offen bleibt.
space_or_procedure_anchors: Zweistufige Freigabe, Lagebüro, dokumentierter Prüfpfad.
relationship_or_psychology_carrier: Bea akzeptiert die Entscheidung, bleibt fachlich aber skeptisch.
character_state_refs: character_states/S-001_Alex.md
research_refs: R-001
"""


def gate(gate_id: str, artifacts: str, next_step: str) -> str:
    return f"""# GATE_RECORD
gate_id: {gate_id}
artifacts: {artifacts}
decision: APPROVE
decided_by: human
date: 2026-08-29
open_blockers: no
next_step: {next_step}
"""


def write_valid_project(root: Path) -> None:
    (root / "gates").mkdir(parents=True)
    (root / "scenes").mkdir(parents=True)
    (root / "character_states").mkdir(parents=True)
    (root / "BOOK_IDEA.md").write_text(BOOK_IDEA, encoding="utf-8")
    (root / "STORY_PACKAGE.md").write_text(STORY_PACKAGE, encoding="utf-8")
    (root / "CHARACTERS.md").write_text(CHARACTERS, encoding="utf-8")
    (root / "RESEARCH_REGISTER.md").write_text(RESEARCH, encoding="utf-8")
    (root / "gates" / "G0.md").write_text(
        gate("G0", "BOOK_IDEA.md", "STORY_PACKAGE.md ausarbeiten"), encoding="utf-8"
    )
    (root / "gates" / "G1.md").write_text(
        gate("G1", "STORY_PACKAGE.md", "Figuren- und Recherche-Basis anlegen"), encoding="utf-8"
    )
    (root / "gates" / "G2.md").write_text(
        gate("G2", "CHARACTERS.md; RESEARCH_REGISTER.md", "Erste Szene planen"), encoding="utf-8"
    )
    (root / "scenes" / "S-001.md").write_text(SCENE, encoding="utf-8")
    (root / "character_states" / "S-001_Alex.md").write_text(
        CHARACTER_STATE, encoding="utf-8"
    )


class PipelineEndToEndTests(unittest.TestCase):
    def test_g0_to_g2_allows_scene_planning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "READY_FOR_SCENE_PLANNING")
            self.assertFalse(result.issues)

    def test_complete_first_scene_reaches_g3_but_is_not_approved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            result = pipeline_check.evaluate_project(
                root, PIPELINE_CONFIG, SCENE_CONFIG, "scenes/S-001.md"
            )
            self.assertEqual(result.status, "READY_FOR_G3")
            self.assertFalse(result.issues)
            self.assertNotEqual(result.status, "APPROVE")

    def test_missing_human_gate_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "gates" / "G1.md").unlink()
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("missing human gate record" in item for item in result.issues))

    def test_non_approved_gate_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            text = (root / "gates" / "G2.md").read_text(encoding="utf-8")
            (root / "gates" / "G2.md").write_text(
                text.replace("decision: APPROVE", "decision: REWORK"), encoding="utf-8"
            )
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("decision must be one of" in item for item in result.issues))

    def test_open_story_decision_blocks_before_scene_planning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            text = (root / "STORY_PACKAGE.md").read_text(encoding="utf-8")
            (root / "STORY_PACKAGE.md").write_text(
                text.replace("story_decisions_open: no", "story_decisions_open: yes"),
                encoding="utf-8",
            )
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")

    def test_scene_research_ref_must_be_resolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            research = (root / "RESEARCH_REGISTER.md").read_text(encoding="utf-8")
            research = research.replace(
                "| R-001 | Wie funktioniert die reale Freigabekette? | S-001 | high | resolved | Fachquelle A | Für den Roman gilt eine zweistufige Freigabe. |",
                "| R-001 | Wie funktioniert die reale Freigabekette? | S-001 | high | open |  |  |",
            )
            (root / "RESEARCH_REGISTER.md").write_text(research, encoding="utf-8")
            result = pipeline_check.evaluate_project(
                root, PIPELINE_CONFIG, SCENE_CONFIG, "scenes/S-001.md"
            )
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("R-001 is still open" in item for item in result.issues))

    def test_scene_character_state_ref_must_exist_and_match_scene(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            (root / "character_states" / "S-001_Alex.md").unlink()
            result = pipeline_check.evaluate_project(
                root, PIPELINE_CONFIG, SCENE_CONFIG, "scenes/S-001.md"
            )
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("character state missing" in item for item in result.issues))

    def test_story_title_and_character_version_are_cross_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_valid_project(root)
            story = (root / "STORY_PACKAGE.md").read_text(encoding="utf-8")
            (root / "STORY_PACKAGE.md").write_text(
                story.replace("working_title: Testroman", "working_title: Anderer Titel"),
                encoding="utf-8",
            )
            result = pipeline_check.evaluate_project(root, PIPELINE_CONFIG, SCENE_CONFIG)
            self.assertEqual(result.status, "BLOCK")
            self.assertTrue(any("different working_title" in item for item in result.issues))


if __name__ == "__main__":
    unittest.main()
