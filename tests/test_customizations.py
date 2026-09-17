from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from customize import apply_installed, apply_to_item, digest, render, safe_path, transform


class CustomizationTests(unittest.TestCase):
    def fixture(self):
        data = b"---\r\nname: sample\r\n---\r\nSTART\r\nold\r\nEND\r\nkeep\r\n"
        rules = {"trim": {"op": "span", "start": "START\n", "end": "END\n", "include_end": True, "text": "new\n"}}
        entry = {"path": "sample/SKILL.md", "before_sha256": digest(data), "rules": ["trim"]}
        entry["after_sha256"] = digest(render(data, entry, rules))
        return data, {"schema_version": 1, "files": [entry], "rules": rules, "global_preferences": "preferences\n"}

    def test_preserves_surrounding_content_and_is_idempotent(self):
        data, spec = self.fixture()
        entry = spec["files"][0]
        new = transform(data, entry, spec["rules"])
        self.assertEqual(new, b"---\nname: sample\n---\nnew\nkeep\n")
        self.assertEqual(transform(new, entry, spec["rules"]), new)

    def test_unknown_preimage_and_wrong_result_are_rejected(self):
        data, spec = self.fixture()
        entry = spec["files"][0]
        with self.assertRaisesRegex(ValueError, "Content changed"):
            transform(data + b"user edit", entry, spec["rules"])
        entry["after_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "result mismatch"):
            transform(data, entry, spec["rules"])

    def test_preflight_prevents_partial_install_and_preserves_preferences(self):
        data, spec = self.fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "skills/sample/SKILL.md"
            target.parent.mkdir(parents=True)
            target.write_bytes(data)
            (root / "AGENTS.md").write_text("user preferences", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "AGENTS.md"):
                apply_installed(spec, root, apply=True, include_preferences=True)
            self.assertEqual(target.read_bytes(), data)
            second = copy.deepcopy(spec["files"][0])
            second["path"] = "other/SKILL.md"
            other = root / "skills/other/SKILL.md"
            other.parent.mkdir()
            other.write_text("user-edited", encoding="utf-8")
            spec["files"].append(second)
            with self.assertRaisesRegex(ValueError, "Content changed"):
                apply_installed(spec, root, apply=True)
            self.assertEqual(target.read_bytes(), data)
            self.assertFalse((root / "skill-backups").exists())

    def test_apply_creates_recoverable_backup_and_second_run_is_noop(self):
        data, spec = self.fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            target = root / "skills/sample/SKILL.md"
            target.parent.mkdir(parents=True)
            target.write_bytes(data)
            preview = apply_installed(spec, root)
            self.assertEqual(preview["pending"], 1)
            self.assertEqual(target.read_bytes(), data)
            result = apply_installed(spec, root, apply=True, include_preferences=True)
            self.assertEqual((Path(result["backup"]) / "skills/sample/SKILL.md").read_bytes(), data)
            self.assertEqual((root / "AGENTS.md").read_text(), "preferences\n")
            self.assertEqual(apply_installed(spec, root, apply=True, include_preferences=True)["pending"], 0)

    def test_paths_cannot_escape_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            for path in ("../escape", "/absolute", "C:/absolute", "a\\b"):
                with self.assertRaises(ValueError):
                    safe_path(Path(temp), path)

    def test_staged_item_applies_only_its_own_edits(self):
        data, spec = self.fixture()
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "SKILL.md"
            target.write_bytes(data)
            self.assertEqual(apply_to_item(Path(temp), "unrelated", spec), 0)
            self.assertEqual(target.read_bytes(), data)
            self.assertEqual(apply_to_item(Path(temp), "sample", spec), 1)
            self.assertEqual(digest(target.read_bytes()), spec["files"][0]["after_sha256"])

    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_published_manifest_bytes_match_recorded_hash(self):
        """Windows autocrlf must not change the spec bytes published by Git."""
        manifest = json.loads((ROOT / "manifest/install-manifest.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "manifest").mkdir()
            shutil.copyfile(ROOT / ".gitattributes", root / ".gitattributes")
            shutil.copyfile(ROOT / "manifest/customizations.json", root / "manifest/customizations.json")
            for args in (["init", "-q"], ["-c", "core.autocrlf=true", "add", ".gitattributes", "manifest/customizations.json"]):
                subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, timeout=30)
            published = subprocess.run(
                ["git", "-C", str(root), "show", ":manifest/customizations.json"],
                check=True, capture_output=True, timeout=30,
            ).stdout
            self.assertEqual(digest(published), manifest["customizations"]["sha256"])

    @unittest.skipUnless(shutil.which("pwsh") or shutil.which("powershell"), "PowerShell unavailable")
    def test_native_powershell_matches_python_and_rejects_changed_input(self):
        data, spec = self.fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "SKILL.md").write_bytes(data)
            (root / "spec.json").write_text(json.dumps(spec), encoding="utf-8")
            quote = lambda value: "'" + str(value).replace("'", "''") + "'"
            command = (
                "$ErrorActionPreference = 'Stop'\n"
                f". {quote(ROOT / 'scripts/customize.ps1')}\n"
                f"$spec = Get-Content -Raw {quote(root / 'spec.json')} | ConvertFrom-Json\n"
                f"Set-SkillCustomization -Source {quote(root)} -DestinationName sample -Spec $spec"
            )
            executable = shutil.which("pwsh") or shutil.which("powershell")
            result = subprocess.run([executable, "-NoProfile", "-Command", command], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(digest((root / "SKILL.md").read_bytes()), spec["files"][0]["after_sha256"])
            (root / "SKILL.md").write_bytes(b"changed")
            result = subprocess.run([executable, "-NoProfile", "-Command", command], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual((root / "SKILL.md").read_bytes(), b"changed")


if __name__ == "__main__":
    unittest.main()
