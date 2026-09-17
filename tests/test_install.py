from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import install


class InstallerTests(unittest.TestCase):
    def test_windows_extended_paths_preserve_drives_and_unc_shares(self):
        cases = {
            r"C:\Users\example\..\cache": r"\\?\C:\Users\cache",
            r"\\server\share\cache": r"\\?\UNC\server\share\cache",
            r"\\?\C:\cache": r"\\?\C:\cache",
            r"\\?\UNC\server\share\cache": r"\\?\UNC\server\share\cache",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(install.windows_extended_path(source), expected)

    def test_install_and_backup_handle_long_paths_and_cleanup(self):
        manifest = {
            "sources": [{
                "source": "example/skills",
                "ref": "a" * 40,
                "items": [{"name": "sample", "destination": "sample", "source_path": "skills/sample"}],
            }],
        }
        archive_root = "skills-" + "a" * 40
        deep_member = archive_root + "/plugins/" + "/".join(["nested-reference-directory"] * 10) + "/workflow.yml"
        deep_skill_path = "/".join(["nested-reference-directory"] * 10) + "/notes.txt"
        self.assertGreater(len(deep_member), 260)
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, "w") as bundle:
            bundle.writestr(archive_root + "/skills/sample/SKILL.md", b"sample skill\n")
            bundle.writestr(archive_root + "/skills/sample/" + deep_skill_path, b"deep reference\n")
            bundle.writestr(deep_member, b"unselected upstream content\n")
        staging_roots = []

        def download_fixture(url, destination):
            staging_roots.append(destination.parent)
            destination.write_bytes(payload.getvalue())

        temp_root = tempfile.gettempdir()
        if os.name == "nt":
            temp_root = install.windows_extended_path(temp_root)
        with tempfile.TemporaryDirectory(dir=temp_root) as temp:
            readable_home = Path(temp) / "codex"
            codex_home = readable_home
            if os.name == "nt":
                # Existing callers supply ordinary paths, even when children are long.
                unprefixed = str(codex_home)
                unprefixed = "\\\\" + unprefixed[8:] if unprefixed.startswith("\\\\?\\UNC\\") else unprefixed[4:]
                codex_home = Path(unprefixed)
            backup_relative = Path("backups") / ("backup-" * 18) / ("archive-" * 16)
            backup_root = codex_home / backup_relative
            with mock.patch.object(install, "download", side_effect=download_fixture), contextlib.redirect_stdout(io.StringIO()):
                install.install_sources(manifest, codex_home, False, False, backup_root)
                install.install_sources(manifest, codex_home, False, False, backup_root)
                self.assertEqual(len(staging_roots), 1, "An existing installation must still be skipped")
                (readable_home / "skills/sample/SKILL.md").write_bytes(b"user customization\n")
                install.install_sources(manifest, codex_home, False, True, backup_root)
            self.assertEqual((readable_home / "skills/sample/SKILL.md").read_bytes(), b"sample skill\n")
            self.assertEqual((readable_home / "skills/sample" / deep_skill_path).read_bytes(), b"deep reference\n")
            self.assertEqual((readable_home / backup_relative / "sample/SKILL.md").read_bytes(), b"user customization\n")
            self.assertEqual((readable_home / backup_relative / "sample" / deep_skill_path).read_bytes(), b"deep reference\n")
        self.assertEqual(len(staging_roots), 2)
        for staging_root in staging_roots:
            self.assertFalse(staging_root.exists(), "Long archive members must not prevent temporary directory cleanup")


if __name__ == "__main__":
    unittest.main()
