#!/usr/bin/env python3
"""Apply reviewed, hash-bound instruction edits without replacing unknown files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path, PurePosixPath


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    path = PurePosixPath(relative)
    if not path.parts or path.is_absolute() or ".." in path.parts or "\\" in relative or ":" in relative:
        raise ValueError(f"Unsafe customization path: {relative}")
    target = root.joinpath(*path.parts)
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Customization escapes root: {relative}")
    return target


def transform(data: bytes, entry: dict, rules: dict) -> bytes:
    current = digest(data)
    if current == entry["after_sha256"]:
        return data
    if current != entry["before_sha256"]:
        raise ValueError(f"Content changed; review before customizing: {entry['path']}")
    result = render(data, entry, rules)
    if digest(result) != entry["after_sha256"]:
        raise ValueError(f"Customization result mismatch: {entry['path']}")
    return result


def render(data: bytes, entry: dict, rules: dict) -> bytes:
    text = data.decode("utf-8-sig").replace("\r\n", "\n")
    for name in entry["rules"]:
        rule = rules[name]
        if rule["op"] == "file":
            text = rule["text"]
        elif rule["op"] == "replace":
            expected = rule.get("count", 1)
            if text.count(rule["old"]) != expected:
                raise ValueError(f"Ambiguous replacement {name}: {entry['path']}")
            text = text.replace(rule["old"], rule["text"])
        elif rule["op"] == "span":
            if text.count(rule["start"]) != 1:
                raise ValueError(f"Ambiguous span {name}: {entry['path']}")
            start = text.index(rule["start"])
            end = text.index(rule["end"], start) + (len(rule["end"]) if rule.get("include_end") else 0)
            text = text[:start] + rule["text"] + text[end:]
        else:
            raise ValueError(f"Unknown customization operation: {rule['op']}")
    return text.encode("utf-8")


def validate_spec(spec: dict) -> None:
    if spec["schema_version"] != 1:
        raise ValueError("Unsupported customization schema")
    seen = set()
    for entry in spec["files"]:
        safe_path(Path.cwd(), entry["path"])
        if entry["path"] in seen:
            raise ValueError(f"Duplicate customization: {entry['path']}")
        seen.add(entry["path"])
        if any(name not in spec["rules"] for name in entry["rules"]):
            raise ValueError(f"Unknown rule: {entry['path']}")
        for key in ("before_sha256", "after_sha256"):
            if len(entry[key]) != 64 or any(c not in "0123456789abcdef" for c in entry[key]):
                raise ValueError(f"Invalid hash: {entry['path']}")


def apply_to_item(source: Path, destination: str, spec: dict) -> int:
    """Customize a staged upstream directory before the installer replaces it."""
    pending = []
    prefix = destination + "/"
    for entry in spec["files"]:
        if entry["path"].startswith(prefix):
            target = safe_path(source, entry["path"][len(prefix):])
            pending.append((target, transform(target.read_bytes(), entry, spec["rules"])))
    for target, content in pending:
        target.write_bytes(content)
    return len(pending)


def apply_installed(spec: dict, codex_home: Path, *, apply: bool = False, include_preferences: bool = False) -> dict:
    validate_spec(spec)
    skills_root = codex_home / "skills"
    pending = []
    for entry in spec["files"]:
        target = safe_path(skills_root, entry["path"])
        old = target.read_bytes()
        new = transform(old, entry, spec["rules"])
        if old != new:
            pending.append((target, Path("skills") / entry["path"], new))
    if include_preferences:
        target = safe_path(codex_home, "AGENTS.md")
        old = target.read_bytes() if target.exists() else b""
        new = spec["global_preferences"].encode("utf-8")
        if old not in (b"", new):
            raise ValueError("AGENTS.md is nonempty and differs; merge it explicitly before applying preferences")
        if old != new:
            pending.append((target, Path("AGENTS.md"), new))
    result = {"reviewed_files": len(spec["files"]), "pending": len(pending), "applied": apply}
    if not apply or not pending:
        return result
    backups = codex_home / "skill-backups"
    backups.mkdir(parents=True, exist_ok=True)
    backup_root = Path(tempfile.mkdtemp(prefix="instructions-" + datetime.now().strftime("%Y%m%d-") , dir=backups))
    # All preimages were validated before the first write.
    for target, relative, content in pending:
        backup = safe_path(backup_root, relative.as_posix())
        if target.exists():
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    result["backup"] = str(backup_root)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex"))
    parser.add_argument("--spec", type=Path, default=Path(__file__).resolve().parents[1] / "manifest/customizations.json")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--include-preferences", action="store_true")
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    print(json.dumps(apply_installed(spec, args.codex_home.resolve(), apply=args.apply, include_preferences=args.include_preferences), indent=2))


if __name__ == "__main__":
    main()
