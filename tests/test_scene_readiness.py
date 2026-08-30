import json
import unittest
from pathlib import Path

from scripts.scene_readiness import evaluate, load_config, parse_fields


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "scene_readiness.yml"
CORPUS_PATH = ROOT / "tests" / "corpus" / "scene_readiness_normalfall.json"


def valid_scene(**overrides):
    fields = {
        "scene_id": "X_01",
        "title": "Die Entscheidung",
        "story_function": "verschiebt die Handlung durch eine irreversible Wahl",
        "pov": "Protagonist",
        "location_time": "Besprechungsraum, Montag 08:10, unmittelbar nach Szene X_00",
        "characters_present": "Protagonist, Gegenfigur",
        "goal": "eine Entscheidung vor Fristablauf treffen",
        "conflict": "die schnellere Option erzeugt ein reales Gegenrisiko",
        "decision": "Protagonist wählt die begrenzte Option",
        "consequence": "der operative Weg wird enger und die Beziehung zur Gegenfigur belastet",
        "reader_before": "beide Optionen sind plausibel",
        "reader_after": "die Entscheidung ist verständlich, aber nicht sauber",
        "must_not_reveal": "none - diese Testszene hat kein späteres Geheimnis",
        "character_state_status": "ready",
        "research_status": "ready",
        "story_decisions_open": "no",
        "narrative_weight": "high",
        "experience_status": "pending_human_review",
        "pressure_progression": "Frist, Gegenbeleg, Entscheidung, unmittelbare Rückmeldung",
        "observable_actions": "Akte prüfen; Rückfrage; Gegenoption testen; Entscheidung ausführen",
        "alternatives_in_scene": "die langsamere saubere Option bleibt real verfügbar",
        "consequence_carrier": "Zugriff wird protokolliert und Gegenfigur reagiert auf die Entscheidung",
        "space_or_procedure_anchors": "ein konkreter Raum, ein konkreter Zugriffspfad und ein sichtbarer Timer sind festgelegt",
        "relationship_or_psychology_carrier": "Gegenfigur widerspricht; Protagonist begrenzt die Maßnahme trotzdem",
        "beat_refs": "BT001; BT002",
        "character_state_refs": "character_states/X_01_protagonist.md",
        "research_refs": "none - keine offenen plotrelevanten Fakten",
    }
    fields.update(overrides)
    lines = ["# SCENE_PLAN", ""] + [f"{key}: {value}" for key, value in fields.items()]
    return "\n".join(lines) + "\n"


class SceneReadinessMechanicsTests(unittest.TestCase):
    def test_pre_g2_scene_reaches_human_gate_but_is_not_auto_approved(self):
        result = evaluate(valid_scene(), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "READY_FOR_HUMAN_GATE")
        self.assertNotEqual(result.status, "APPROVE")
        self.assertEqual(result.issues, [])

    def test_post_g2_experience_status_is_also_mechanically_valid(self):
        result = evaluate(
            valid_scene(experience_status="human_reviewed_ready"),
            load_config(CONFIG_PATH),
        )
        self.assertEqual(result.status, "READY_FOR_HUMAN_GATE")
        self.assertEqual(result.issues, [])

    def test_parser_reads_machine_fields_without_parsing_prose(self):
        fields = parse_fields(valid_scene())
        self.assertEqual(fields["scene_id"], "X_01")
        self.assertEqual(fields["story_decisions_open"], "no")
        self.assertEqual(fields["beat_refs"], "BT001; BT002")

    def test_missing_required_field_blocks(self):
        text = valid_scene().replace(
            "consequence_carrier: Zugriff wird protokolliert und Gegenfigur reagiert auf die Entscheidung\n",
            "",
        )
        result = evaluate(text, load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any("consequence_carrier" in issue for issue in result.issues))

    def test_missing_beat_refs_blocks(self):
        text = valid_scene().replace("beat_refs: BT001; BT002\n", "")
        result = evaluate(text, load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any("beat_refs" in issue for issue in result.issues))

    def test_open_story_decision_blocks(self):
        result = evaluate(valid_scene(story_decisions_open="yes"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertIn("open story decisions block prose", result.issues)

    def test_unresolved_research_status_blocks(self):
        result = evaluate(valid_scene(research_status="open"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertIn("research blockers are not closed", result.issues)

    def test_character_state_dependency_blocks_when_not_ready(self):
        result = evaluate(valid_scene(character_state_status="open"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertIn("character state is not ready", result.issues)

    def test_invalid_experience_status_blocks(self):
        result = evaluate(valid_scene(experience_status="ready"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any("experience_status" in issue for issue in result.issues))

    def test_placeholder_blocks(self):
        result = evaluate(valid_scene(location_time="<Ort später festlegen>"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any("location_time" in issue for issue in result.issues))

    def test_not_applicable_requires_reason(self):
        result = evaluate(valid_scene(research_refs="none - keine Recherche nötig"), load_config(CONFIG_PATH))
        self.assertEqual(result.status, "READY_FOR_HUMAN_GATE")
        result_bad = evaluate(valid_scene(research_refs="none -"), load_config(CONFIG_PATH))
        self.assertEqual(result_bad.status, "BLOCK")


class RetrospectiveCorpusTests(unittest.TestCase):
    def test_normalfall_validation_corpus_is_fixed_and_contains_false_negative(self):
        data = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "0.1")
        self.assertEqual(len(data["cases"]), 8)
        outcomes = {case["retrospective_gate"] for case in data["cases"]}
        self.assertIn("PASS_FALSE_NEGATIVE", outcomes)
        self.assertIn("BLOCK", outcomes)
        self.assertTrue(data["method"]["no_reclassification_to_make_gate_look_better"])


if __name__ == "__main__":
    unittest.main()
