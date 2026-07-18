#!/usr/bin/env python3
"""Consolidate active user skills into the Codex-native skills directory."""

from __future__ import annotations

import argparse
import json
import shutil
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_manifest() -> dict:
    return json.loads(
        (ROOT / "manifest" / "install-manifest.json").read_text(encoding="utf-8")
    )


def top_level_skills(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    return {
        path.name: path
        for path in root.iterdir()
        if path.is_dir() and path.name != ".system" and (path / "SKILL.md").exists()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--agents-home", type=Path, default=Path.home() / ".agents")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    codex_home = args.codex_home.expanduser().resolve()
    agents_home = args.agents_home.expanduser().resolve()
    codex_root = codex_home / "skills"
    agents_root = agents_home / "skills"
    manifest = load_manifest()
    retired = {item["name"]: item["reason"] for item in manifest["retired_skills"]}

    codex_skills = top_level_skills(codex_root)
    agents_skills = top_level_skills(agents_root)
    agents_only_all = set(agents_skills) - set(codex_skills)
    agents_only = sorted(agents_only_all - set(retired))
    retired_agents_only = sorted(agents_only_all & set(retired))
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    codex_backup = codex_home / "skill-backups" / timestamp / "retired"
    agents_backup = agents_home / "skill-backups" / timestamp / "skills"

    report = {
        "mode": "apply" if args.apply else "dry-run",
        "codex_root": str(codex_root),
        "agents_root": str(agents_root),
        "agents_active_count": len(agents_skills),
        "agents_only": agents_only,
        "retired_agents_only": retired_agents_only,
        "retired_present": sorted(set(codex_skills) & set(retired)),
        "copied_to_codex": [],
        "retired_moved": [],
        "agents_root_moved": None,
    }

    if not args.apply:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    codex_root.mkdir(parents=True, exist_ok=True)
    for name in agents_only:
        destination = codex_root / name
        shutil.copytree(agents_skills[name], destination)
        report["copied_to_codex"].append(name)

    for name in report["retired_present"]:
        source = codex_root / name
        codex_backup.mkdir(parents=True, exist_ok=True)
        destination = codex_backup / name
        if destination.exists():
            raise RuntimeError(f"Backup collision: {destination}")
        source.rename(destination)
        report["retired_moved"].append(name)

    if agents_root.exists():
        agents_backup.parent.mkdir(parents=True, exist_ok=True)
        if agents_backup.exists():
            raise RuntimeError(f"Backup collision: {agents_backup}")
        agents_root.rename(agents_backup)
        report["agents_root_moved"] = str(agents_backup)

    remaining_retired = sorted(set(top_level_skills(codex_root)) & set(retired))
    if remaining_retired:
        raise RuntimeError(f"Retired skills remain active: {remaining_retired}")
    if agents_root.exists():
        raise RuntimeError(f"Legacy agents skills root still exists: {agents_root}")

    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
