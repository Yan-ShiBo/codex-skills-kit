#!/usr/bin/env python3
"""Generate a sanitized inventory and install manifest from a Codex profile."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


SOURCE_REFS = {
    "vercel-labs/skills": "be0dd25b4a8665894a56f45ef582cc02ca802c39",
    "obra/superpowers": "6fd4507659784c351abbd2bc264c7162cfd386dc",
    "garrytan/gstack": "c7ae63201ab193a7dc7fb7e0d81238645111ffac",
    "mattpocock/skills": "694fa30311e02c2639942308513555e61ee84a6f",
    "anthropics/skills": "57546260929473d4e0d1c1bb75297be2fdfa1949",
    "nextlevelbuilder/ui-ux-pro-max-skill": "b7e3af80f6e331f6fb456667b82b12cade7c9d35",
    "jimliu/baoyu-skills": "441ca307a60c594e8eda0ac156609503687544c0",
    "github/awesome-copilot": "b4b9beb69d9e8b21c0dfcfd9c86a835997b6a83b",
    "Imbad0202/academic-research-skills-codex": "763bccdf5d4187a779354d801b69b3cf591eea41",
    "hyhmrright/brooks-lint": "8501ba4411a9db67bcf42080b0380953b7fc90a9",
    "openai/skills": "a8924c2a35cfa290458852c4fad17c9133054c2e",
    "davila7/claude-code-templates": "6772ba97d5b016c87f70610429c7c44df934cfe1",
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
    "docx": ("anthropics/skills", "skills/docx"),
    "gh-fix-ci": ("openai/skills", "skills/.curated/gh-fix-ci"),
    "mcp-builder": ("anthropics/skills", "skills/mcp-builder"),
    "pdf": ("anthropics/skills", "skills/pdf"),
    "planning-with-files": (
        "davila7/claude-code-templates",
        "cli-tool/components/skills/productivity/planning-with-files",
    ),
    "pptx": ("anthropics/skills", "skills/pptx"),
    "webapp-testing": ("anthropics/skills", "skills/webapp-testing"),
    "xlsx": ("anthropics/skills", "skills/xlsx"),
}

PLUGIN_SELECTORS = [
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
    "chrome@openai-bundled",
    "browser@openai-bundled",
    "google-drive@openai-curated-remote",
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

    lines = block.splitlines()
    description = ""
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


def sanitized_path(path: Path, home: Path) -> str:
    try:
        return "~/" + path.relative_to(home).as_posix()
    except ValueError:
        return path.as_posix()


def build_install_manifest(lock: dict) -> dict:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill_name, metadata in lock.get("skills", {}).items():
        source = metadata["source"]
        skill_path = Path(metadata["skillPath"])
        source_path = "." if skill_path.parent == Path(".") else skill_path.parent.as_posix()
        source_path = PATH_OVERRIDES.get((source, skill_name), source_path)
        grouped[source].append(
            {
                "name": skill_name,
                "source_path": source_path,
                "destination": skill_name,
                "snapshot_hash": metadata.get("skillFolderHash"),
            }
        )

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

    # The six Brooks skills reference ../_shared at runtime.
    grouped["hyhmrright/brooks-lint"].append(
        {
            "name": "_brooks-shared",
            "source_path": "skills/_shared",
            "destination": "_shared",
            "runtime_support": True,
            "snapshot_hash": None,
        }
    )

    sources = []
    for source in sorted(grouped):
        sources.append(
            {
                "source": source,
                "url": f"https://github.com/{source}.git",
                "ref": SOURCE_REFS[source],
                "items": sorted(grouped[source], key=lambda item: item["name"]),
            }
        )

    return {
        "schema_version": 1,
        "snapshot_date": "2026-06-16",
        "description": "Reproducible source manifest for Yan-ShiBo's Codex skills setup.",
        "sources": sources,
        "plugins": [{"selector": selector} for selector in PLUGIN_SELECTORS],
        "notes": [
            "Codex system skills are bundled with Codex and are not downloaded.",
            "Third-party skill source code is downloaded from its original repository.",
            "Plugin installation is best-effort because connectors may require login.",
        ],
    }


def inventory_skills(codex_home: Path, home: Path, lock: dict) -> list[dict]:
    lock_sources = {
        name: metadata.get("source")
        for name, metadata in lock.get("skills", {}).items()
    }
    inventory = []
    roots = [
        ("codex", codex_home / "skills"),
        ("agents", home / ".agents" / "skills"),
    ]
    for root_type, root in roots:
        if not root.exists():
            continue
        for skill_file in sorted(root.rglob("SKILL.md")):
            name, description = parse_frontmatter(skill_file)
            relative = skill_file.relative_to(root)
            layer = "system" if relative.parts[0] == ".system" else root_type
            if layer == "system":
                source = "Codex built-in"
            else:
                source = lock_sources.get(name) or lock_sources.get(relative.parts[0])
                if name in EXTRA_SKILLS:
                    source = EXTRA_SKILLS[name][0]
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


def inventory_plugins(codex_home: Path, home: Path) -> list[dict]:
    cache = codex_home / "plugins" / "cache"
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
                "path": sanitized_path(skill_file, home),
                "content_sha256": hashlib.sha256(skill_file.read_bytes()).hexdigest(),
            }
        )
    return inventory


def render_skills_markdown(skills: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for skill in skills:
        key = skill["source"] or skill["layer"]
        grouped[key].append(skill)

    unique_names = {skill["name"] for skill in skills}
    lines = [
        "# Installed Skills Inventory",
        "",
        f"- Skill entries: **{len(skills)}**",
        f"- Unique skill names: **{len(unique_names)}**",
        f"- Generated: **2026-06-16**",
        "",
        "The same skill can appear in both `~/.codex/skills` and `~/.agents/skills`.",
        "",
    ]
    for source in sorted(grouped):
        entries = grouped[source]
        unique = {}
        for entry in entries:
            unique.setdefault(entry["name"], entry)
        lines.extend([f"## {source}", ""])
        for name in sorted(unique):
            description = unique[name]["description"] or "(No description in frontmatter.)"
            lines.append(f"- **{name}**: {description}")
        lines.append("")
    return "\n".join(lines)


def render_plugins_markdown(plugins: list[dict]) -> str:
    grouped: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for plugin in plugins:
        grouped[
            (plugin["marketplace"], plugin["plugin"], plugin["version"])
        ].append(plugin)

    lines = [
        "# Plugin Skill Inventory",
        "",
        f"- Cached plugin skill entries: **{len(plugins)}**",
        f"- Unique plugin skill names: **{len({item['name'] for item in plugins})}**",
        f"- Generated: **2026-06-16**",
        "",
        "Cache entries can include local and remote variants of the same plugin.",
        "",
    ]
    for key in sorted(grouped):
        marketplace, plugin, version = key
        lines.extend([f"## {plugin}", ""])
        lines.append(f"`{marketplace}` / `{version}`")
        lines.append("")
        for item in sorted(grouped[key], key=lambda value: value["name"]):
            description = item["description"] or "(No description in frontmatter.)"
            lines.append(f"- **{item['name']}**: {description}")
        lines.append("")
    return "\n".join(lines)


def render_repositories_markdown(manifest: dict) -> str:
    lines = [
        "# Source Repositories",
        "",
        f"Snapshot date: **{manifest['snapshot_date']}**",
        "",
        "| Repository | Installed items | Pinned commit |",
        "| --- | ---: | --- |",
    ]
    for source in manifest["sources"]:
        skill_count = sum(
            1 for item in source["items"] if not item.get("runtime_support")
        )
        commit = source["ref"]
        lines.append(
            f"| [{source['source']}](https://github.com/{source['source']}) "
            f"| {skill_count} | [`{commit[:12]}`](https://github.com/{source['source']}/commit/{commit}) |"
        )

    lines.extend(
        [
            "",
            "## Plugin Packages",
            "",
            "Plugin versions are resolved by the user's configured Codex marketplaces.",
            "",
        ]
    )
    lines.extend(f"- `{item['selector']}`" for item in manifest["plugins"])
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    codex_home = args.codex_home.expanduser().resolve()
    home = codex_home.parent
    output = args.output.resolve()
    lock_path = home / ".agents" / ".skill-lock.json"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))

    skills = inventory_skills(codex_home, home, lock)
    plugins = inventory_plugins(codex_home, home)
    manifest = build_install_manifest(lock)

    (output / "manifest").mkdir(parents=True, exist_ok=True)
    (output / "inventory").mkdir(parents=True, exist_ok=True)

    (output / "manifest" / "install-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "inventory" / "skills.json").write_text(
        json.dumps(skills, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "inventory" / "plugins.json").write_text(
        json.dumps(plugins, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output / "inventory" / "SKILLS.md").write_text(
        render_skills_markdown(skills), encoding="utf-8"
    )
    (output / "inventory" / "PLUGINS.md").write_text(
        render_plugins_markdown(plugins), encoding="utf-8"
    )
    (output / "inventory" / "REPOSITORIES.md").write_text(
        render_repositories_markdown(manifest), encoding="utf-8"
    )

    print(
        json.dumps(
            {
                "codex_skill_entries": sum(
                    1 for item in skills if item["layer"] in {"codex", "system"}
                ),
                "agent_skill_entries": sum(
                    1 for item in skills if item["layer"] == "agents"
                ),
                "unique_skill_names": len({item["name"] for item in skills}),
                "plugin_skill_entries": len(plugins),
                "unique_plugin_skill_names": len({item["name"] for item in plugins}),
                "source_repositories": len(manifest["sources"]),
                "install_items": sum(
                    len(source["items"]) for source in manifest["sources"]
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
