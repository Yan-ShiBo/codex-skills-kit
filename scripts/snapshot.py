#!/usr/bin/env python3
"""Generate the reproducible Codex skills inventory and install manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tomllib
from collections import defaultdict
from datetime import date
from pathlib import Path


SOURCE_REFS = {
    "Imbad0202/academic-research-skills-codex": "60b836f19705b9b42225b9f2cc3423f632c52e17",
    "anthropics/skills": "fa0fa64bdc967915dc8399e803be67759e1e62b8",
    "davila7/claude-code-templates": "e4efa5367903f06d8be0320b88a95c1224b87f7e",
    "garrytan/gstack": "a3259400a366593e0c909dd9ac3e59752efd2488",
    "github/awesome-copilot": "26fe2d126bf79aafb38f43344d450b69632200f8",
    "hyhmrright/brooks-lint": "141f45ebb70bfa5a67e0dc8ee33b56e40067836d",
    "jimliu/baoyu-skills": "6b7a2e417500561a5ecdd0b168332f4142584617",
    "mattpocock/skills": "9603c1cc8118d08bc1b3bf34cf714f62178dea3b",
    "nextlevelbuilder/ui-ux-pro-max-skill": "f8ac5e1266dba8354ea96e19994d9f4345e7ec31",
    "openai/skills": "49f948faa9258a0c61caceaf225e179651397431",
    "vercel-labs/skills": "777599e1159e401b11ce4c8a57c20f09a8f1596e",
}

EXTRA_SKILLS = {
    "academic-research-suite": (
        "Imbad0202/academic-research-skills-codex",
        "skills/academic-research-suite",
    ),
    "brooks-audit": ("hyhmrright/brooks-lint", "skills/brooks-audit"),
    "brooks-debt": ("hyhmrright/brooks-lint", "skills/brooks-debt"),
    "brooks-health": ("hyhmrright/brooks-lint", "skills/brooks-health"),
    "brooks-review": ("hyhmrright/brooks-lint", "skills/brooks-review"),
    "brooks-sweep": ("hyhmrright/brooks-lint", "skills/brooks-sweep"),
    "brooks-test": ("hyhmrright/brooks-lint", "skills/brooks-test"),
    "code-review": ("mattpocock/skills", "skills/engineering/code-review"),
    "diagnosing-bugs": (
        "mattpocock/skills",
        "skills/engineering/diagnosing-bugs",
    ),
    "hatch-pet": ("openai/skills", "skills/.curated/hatch-pet"),
    "jupyter-notebook": ("openai/skills", "skills/.curated/jupyter-notebook"),
    "mcp-builder": ("anthropics/skills", "skills/mcp-builder"),
    "planning-with-files": (
        "davila7/claude-code-templates",
        "cli-tool/components/skills/productivity/planning-with-files",
    ),
    "to-spec": ("mattpocock/skills", "skills/engineering/to-spec"),
    "to-tickets": ("mattpocock/skills", "skills/engineering/to-tickets"),
    "webapp-testing": ("anthropics/skills", "skills/webapp-testing"),
}

SUPERPOWERS_PLUGIN_SKILLS = {
    "brainstorming",
    "dispatching-parallel-agents",
    "executing-plans",
    "finishing-a-development-branch",
    "receiving-code-review",
    "requesting-code-review",
    "subagent-driven-development",
    "systematic-debugging",
    "test-driven-development",
    "using-git-worktrees",
    "using-superpowers",
    "verification-before-completion",
    "writing-plans",
    "writing-skills",
}

RETIRED_SKILLS = {
    "caveman": "Removed upstream; no current skill has the same terse-response semantics.",
    "diagnose": "Replaced upstream by diagnosing-bugs.",
    "design-an-interface": "Upstream explicitly classifies it as deprecated.",
    "qa": "Upstream explicitly classifies it as deprecated.",
    "request-refactor-plan": "Upstream explicitly classifies it as deprecated.",
    "ubiquitous-language": "Upstream explicitly classifies it as deprecated.",
    "gh-fix-ci": "Replaced by the enabled GitHub plugin skill.",
    "docx": "Replaced by the enabled Documents runtime plugin.",
    "pdf": "Replaced by the enabled PDF runtime plugin.",
    "pptx": "Replaced by the enabled Presentations runtime plugin.",
    "review": "Replaced upstream by code-review.",
    "xlsx": "Replaced by the enabled Spreadsheets runtime plugin.",
    "to-issues": "Replaced upstream by to-tickets.",
    "to-prd": "Replaced upstream by to-spec.",
    "write-a-skill": "Removed upstream and superseded by Codex's built-in skill-creator.",
    "zoom-out": "Removed upstream; the current wayfinder skill is not semantically equivalent.",
    **{
        name: "Provided byte-for-byte by the enabled Superpowers plugin."
        for name in SUPERPOWERS_PLUGIN_SKILLS
    },
}

FALLBACK_PLUGIN_SELECTORS = [
    "github@openai-curated",
    "documents@openai-primary-runtime",
    "spreadsheets@openai-primary-runtime",
    "presentations@openai-primary-runtime",
    "hyperframes@openai-curated",
    "computer-use@openai-bundled",
    "superpowers@openai-curated",
    "figma@openai-curated",
    "biorender@openai-curated",
    "canva@openai-curated",
    "nvidia@openai-curated",
    "pdf@openai-primary-runtime",
    "chrome@openai-bundled",
    "template-creator@openai-primary-runtime",
    "sites@openai-bundled",
    "visualize@openai-bundled",
]

PATH_OVERRIDES = {
    ("mattpocock/skills", "teach"): "skills/productivity/teach",
}


def parse_frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    if not text.startswith("---"):
        return path.parent.name, ""
    try:
        block = text.split("---", 2)[1]
    except IndexError:
        return path.parent.name, ""

    name_match = re.search(r"(?m)^name:\s*[\"']?(.+?)[\"']?\s*$", block)
    name = name_match.group(1).strip() if name_match else path.parent.name
    description = ""
    lines = block.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^description:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip()
        if value in {">", "|", ">-", "|-"}:
            parts = []
            for following in lines[index + 1 :]:
                if following and not following[0].isspace():
                    break
                parts.append(following.strip())
            description = " ".join(part for part in parts if part)
        else:
            description = value.strip("\"'")
        break
    return name, re.sub(r"\s+", " ", description).strip()


def folder_hash(folder: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in folder.rglob("*") if p.is_file()):
        relative = path.relative_to(folder).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def attach_snapshot_hashes(manifest: dict, codex_home: Path) -> None:
    """Bind every install item to the bytes currently installed from its pinned ref."""
    skills_root = codex_home / "skills"
    for source in manifest["sources"]:
        for item in source["items"]:
            folder = skills_root / item["destination"]
            item["snapshot_hash"] = folder_hash(folder) if folder.is_dir() else None


def sanitized_path(path: Path, home: Path) -> str:
    try:
        return "~/" + path.relative_to(home).as_posix()
    except ValueError:
        return path.as_posix()


def enabled_plugin_selectors(codex_home: Path) -> list[str]:
    config = codex_home / "config.toml"
    if not config.exists():
        return FALLBACK_PLUGIN_SELECTORS
    try:
        data = tomllib.loads(config.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError):
        return FALLBACK_PLUGIN_SELECTORS
    plugins = data.get("plugins", {})
    enabled = sorted(
        selector
        for selector, settings in plugins.items()
        if isinstance(settings, dict) and settings.get("enabled") is True
    )
    return enabled or FALLBACK_PLUGIN_SELECTORS


def load_source_lock(output: Path, home: Path) -> dict:
    repository_lock = output / "inventory" / "skills-lock.json"
    if repository_lock.exists():
        return json.loads(repository_lock.read_text(encoding="utf-8"))
    legacy_lock = home / ".agents" / ".skill-lock.json"
    if legacy_lock.exists():
        return json.loads(legacy_lock.read_text(encoding="utf-8"))
    return {"skills": {}}


def build_install_manifest(lock: dict, plugin_selectors: list[str]) -> dict:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill_name, metadata in lock.get("skills", {}).items():
        if skill_name in RETIRED_SKILLS:
            continue
        source = metadata["source"]
        if source not in SOURCE_REFS:
            continue
        source_path = metadata.get("source_path")
        if not source_path:
            skill_path = Path(metadata["skillPath"])
            source_path = (
                "." if skill_path.parent == Path(".") else skill_path.parent.as_posix()
            )
        source_path = PATH_OVERRIDES.get((source, skill_name), source_path)
        item = {
            "name": skill_name,
            "source_path": source_path,
            "destination": skill_name,
            "snapshot_hash": metadata.get("skillFolderHash"),
        }
        if skill_name == "planning-with-files":
            item["single_file"] = "SKILL.md"
        grouped[source].append(item)

    for skill_name, (source, source_path) in EXTRA_SKILLS.items():
        if not any(item["name"] == skill_name for item in grouped[source]):
            item = {
                "name": skill_name,
                "source_path": source_path,
                "destination": skill_name,
                "snapshot_hash": None,
            }
            if skill_name == "planning-with-files":
                item["single_file"] = "SKILL.md"
            grouped[source].append(item)

    grouped["hyhmrright/brooks-lint"].append(
        {
            "name": "_brooks-shared",
            "source_path": "skills/_shared",
            "destination": "_shared",
            "runtime_support": True,
            "snapshot_hash": None,
        }
    )

    sources = [
        {
            "source": source,
            "url": f"https://github.com/{source}.git",
            "ref": SOURCE_REFS[source],
            "items": sorted(items, key=lambda item: item["name"]),
        }
        for source, items in sorted(grouped.items())
    ]
    return {
        "schema_version": 2,
        "snapshot_date": date.today().isoformat(),
        "install_root": "~/.codex/skills",
        "description": "Reproducible source manifest for Yan-ShiBo's curated Codex skills setup.",
        "sources": sources,
        "plugins": [{"selector": selector} for selector in plugin_selectors],
        "retired_skills": [
            {
                "name": name,
                "scope": "top_level_destination",
                "reason": reason,
            }
            for name, reason in sorted(RETIRED_SKILLS.items())
        ],
        "notes": [
            "User-managed skills install only to ~/.codex/skills.",
            "Codex system and plugin skills remain in Codex-managed locations.",
            "Third-party source code is downloaded from its original repository.",
            "Replacement backups are stored under ~/.codex/skill-backups, outside the active skills directory.",
        ],
    }


def inventory_skills(
    codex_home: Path,
    home: Path,
    lock: dict,
    manifest: dict,
) -> list[dict]:
    lock_sources = {
        name: metadata.get("source") for name, metadata in lock.get("skills", {}).items()
    }
    destination_sources = {
        item["destination"]: source["source"]
        for source in manifest["sources"]
        for item in source["items"]
    }
    inventory = []
    root = codex_home / "skills"
    if not root.exists():
        return inventory
    for skill_file in sorted(root.rglob("SKILL.md")):
        name, description = parse_frontmatter(skill_file)
        relative = skill_file.relative_to(root)
        layer = "system" if relative.parts[0] == ".system" else "codex"
        source = "Codex built-in" if layer == "system" else None
        if layer == "codex":
            top_level = relative.parts[0]
            source = (
                destination_sources.get(top_level)
                or lock_sources.get(top_level)
                or lock_sources.get(name)
            )
        inventory.append(
            {
                "name": name,
                "description": description,
                "layer": layer,
                "source": source,
                "path": sanitized_path(skill_file, home),
                "content_sha256": hashlib.sha256(skill_file.read_bytes()).hexdigest(),
            }
        )
    return inventory


def inventory_plugins(codex_home: Path, home: Path, selectors: list[str]) -> list[dict]:
    cache = codex_home / "plugins" / "cache"
    enabled_names = {selector.split("@", 1)[0] for selector in selectors}
    inventory = []
    if not cache.exists():
        return inventory
    for skill_file in sorted(cache.rglob("SKILL.md")):
        relative = skill_file.relative_to(cache)
        if len(relative.parts) < 5:
            continue
        marketplace, plugin, version = relative.parts[:3]
        name, description = parse_frontmatter(skill_file)
        inventory.append(
            {
                "name": name,
                "description": description,
                "marketplace": marketplace,
                "plugin": plugin,
                "version": version,
                "configured_enabled": plugin in enabled_names,
                "path": sanitized_path(skill_file, home),
                "content_sha256": hashlib.sha256(skill_file.read_bytes()).hexdigest(),
            }
        )
    return inventory


def render_skills_markdown(skills: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        grouped[skill["source"] or skill["layer"]].append(skill)
    lines = [
        "# Installed Skills Inventory",
        "",
        f"- Active skill entries: **{len(skills)}**",
        f"- Unique skill names: **{len({skill['name'] for skill in skills})}**",
        f"- Generated: **{date.today().isoformat()}**",
        "- User-managed root: **`~/.codex/skills`**",
        "",
        "Plugin-managed skills are listed separately and are not duplicated here.",
        "",
    ]
    for source in sorted(grouped):
        unique = {entry["name"]: entry for entry in grouped[source]}
        lines.extend([f"## {source}", ""])
        for name in sorted(unique):
            description = unique[name]["description"] or "(No frontmatter description.)"
            lines.append(f"- **{name}**: {description}")
        lines.append("")
    return "\n".join(lines)


def render_plugins_markdown(plugins: list[dict], selectors: list[str]) -> str:
    grouped: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for plugin in plugins:
        grouped[(plugin["marketplace"], plugin["plugin"], plugin["version"])].append(plugin)
    lines = [
        "# Plugin Skill Inventory",
        "",
        f"- Configured plugin selectors: **{len(selectors)}**",
        f"- Cached plugin skill entries: **{len(plugins)}**",
        f"- Unique cached plugin skill names: **{len({item['name'] for item in plugins})}**",
        f"- Generated: **{date.today().isoformat()}**",
        "",
        "## Configured plugins",
        "",
        *[f"- `{selector}`" for selector in selectors],
        "",
        "## Cached packages",
        "",
        "Cache entries can include old or connector-specific variants; configuration is authoritative.",
        "",
    ]
    for marketplace, plugin, version in sorted(grouped):
        entries = grouped[(marketplace, plugin, version)]
        state = (
            "plugin configured"
            if any(item["configured_enabled"] for item in entries)
            else "cache only"
        )
        lines.extend([f"### {plugin}", "", f"`{marketplace}` / `{version}` / **{state}**", ""])
        for item in sorted(entries, key=lambda value: value["name"]):
            description = item["description"] or "(No frontmatter description.)"
            lines.append(f"- **{item['name']}**: {description}")
        lines.append("")
    return "\n".join(lines)


def render_repositories_markdown(manifest: dict) -> str:
    lines = [
        "# Source Repositories",
        "",
        f"Snapshot date: **{manifest['snapshot_date']}**",
        "",
        "| Repository | Top-level install targets | Pinned commit |",
        "| --- | ---: | --- |",
    ]
    for source in manifest["sources"]:
        count = sum(1 for item in source["items"] if not item.get("runtime_support"))
        commit = source["ref"]
        lines.append(
            f"| [{source['source']}](https://github.com/{source['source']}) | {count} | "
            f"[`{commit[:12]}`](https://github.com/{source['source']}/commit/{commit}) |"
        )
    lines.extend(["", "Plugin packages are resolved by Codex marketplaces; see `PLUGINS.md`.", ""])
    return "\n".join(lines)


def build_lock(manifest: dict, skills: list[dict]) -> dict:
    content_hashes = {
        item["name"]: item["content_sha256"]
        for item in skills
        if item["layer"] == "codex"
    }
    entries = {}
    for source in manifest["sources"]:
        for item in source["items"]:
            if item.get("runtime_support"):
                continue
            entries[item["name"]] = {
                "source": source["source"],
                "ref": source["ref"],
                "source_path": item["source_path"],
                "destination": f"~/.codex/skills/{item['destination']}",
                "skill_md_sha256": content_hashes.get(item["name"]),
            }
    return {
        "schema_version": 1,
        "snapshot_date": manifest["snapshot_date"],
        "install_root": manifest["install_root"],
        "skills": dict(sorted(entries.items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    codex_home = args.codex_home.expanduser().resolve()
    home = codex_home.parent
    output = args.output.resolve()
    lock = load_source_lock(output, home)
    selectors = enabled_plugin_selectors(codex_home)
    manifest = build_install_manifest(lock, selectors)
    attach_snapshot_hashes(manifest, codex_home)
    skills = inventory_skills(codex_home, home, lock, manifest)
    plugins = inventory_plugins(codex_home, home, selectors)

    (output / "manifest").mkdir(parents=True, exist_ok=True)
    (output / "inventory").mkdir(parents=True, exist_ok=True)
    payloads = {
        output / "manifest" / "install-manifest.json": manifest,
        output / "inventory" / "skills.json": skills,
        output / "inventory" / "plugins.json": plugins,
        output / "inventory" / "skills-lock.json": build_lock(manifest, skills),
    }
    for path, payload in payloads.items():
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output / "inventory" / "SKILLS.md").write_text(render_skills_markdown(skills), encoding="utf-8")
    (output / "inventory" / "PLUGINS.md").write_text(render_plugins_markdown(plugins, selectors), encoding="utf-8")
    (output / "inventory" / "REPOSITORIES.md").write_text(render_repositories_markdown(manifest), encoding="utf-8")

    print(json.dumps({
        "codex_skill_entries": len(skills),
        "unique_skill_names": len({item["name"] for item in skills}),
        "plugin_skill_entries": len(plugins),
        "unique_plugin_skill_names": len({item["name"] for item in plugins}),
        "source_repositories": len(manifest["sources"]),
        "install_items": sum(len(source["items"]) for source in manifest["sources"]),
        "retired_skills": len(manifest["retired_skills"]),
    }, indent=2))


if __name__ == "__main__":
    main()
