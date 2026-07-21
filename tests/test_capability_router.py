from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from capability_router import (  # noqa: E402
    check_rendered_file,
    load_inputs,
    render_markdown,
    validate_registry,
)


class CapabilityRouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry, cls.skills, cls.plugins, cls.install_manifest = load_inputs(ROOT)

    def validate(self, registry: dict) -> None:
        validate_registry(
            registry,
            self.skills,
            self.plugins,
            self.install_manifest,
        )

    def test_repository_registry_is_valid_and_rendered(self) -> None:
        self.validate(self.registry)
        rendered = render_markdown(self.registry)
        check_rendered_file(ROOT, self.registry, rendered)

    def test_unknown_l1_candidate_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["categories"][0]["candidates"] = ["missing-capability"]
        with self.assertRaisesRegex(ValueError, "unknown candidate"):
            self.validate(registry)

    def test_malformed_l1_candidate_is_rejected_cleanly(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["categories"][0]["candidates"] = [{"id": "baseline-direct"}]
        with self.assertRaisesRegex(ValueError, "unknown candidate"):
            self.validate(registry)

    def test_unknown_inventory_target_is_rejected(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["entries"][1]["target"]["name"] = "missing-skill"
        with self.assertRaisesRegex(ValueError, "absent from inventory/skills.json"):
            self.validate(registry)

    def test_manager_type_cannot_be_automatic(self) -> None:
        registry = copy.deepcopy(self.registry)
        gstack = next(item for item in registry["entries"] if item["id"] == "gstack")
        gstack["invocation"] = "auto"
        with self.assertRaisesRegex(ValueError, "manager-type capabilities must be explicit-only"):
            self.validate(registry)

    def test_category_cannot_expose_more_than_three_candidates(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["categories"][0]["candidates"] = [
            "baseline-direct",
            "academic-research-suite",
            "jupyter-notebook",
            "planning-with-files",
        ]
        with self.assertRaisesRegex(ValueError, "candidates must contain 1 to 3"):
            self.validate(registry)

    def test_generated_router_path_cannot_escape_inventory(self) -> None:
        registry = copy.deepcopy(self.registry)
        registry["generated_markdown"] = "../CAPABILITY_ROUTER.md"
        with self.assertRaisesRegex(ValueError, "safe repository-relative path"):
            self.validate(registry)


if __name__ == "__main__":
    unittest.main()
