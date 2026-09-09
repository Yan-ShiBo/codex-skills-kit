#!/usr/bin/env python3
"""Validate repository manifests and inventory invariants."""

from __future__ import annotations

import json
from pathlib import Path

from capability_router import check_rendered_file, render_markdown, validate_registry


ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    manifest = load("manifest/install-manifest.json")
    policy = load("manifest/selection-policy.json")
    skills = load("inventory/skills.json")
    plugins = load("inventory/plugins.json")
    lock = load("inventory/skills-lock.json")
    registry = load("manifest/capability-registry.json")

    assert manifest["schema_version"] == 2
    assert manifest["install_root"] == "~/.codex/skills"
    assert len(manifest["sources"]) == 12
    assert all(len(source["ref"]) == 40 for source in manifest["sources"])
    assert all(source["items"] for source in manifest["sources"])

    items = [item for source in manifest["sources"] for item in source["items"]]
    assert all(
        isinstance(item.get("snapshot_hash"), str)
        and len(item["snapshot_hash"]) == 64
        for item in items
    )
    destinations = [item["destination"] for item in items]
    skill_destinations = {
        item["destination"] for item in items if not item.get("runtime_support")
    }
    retired = {item["name"] for item in manifest["retired_skills"]}
    assert len(destinations) == len(set(destinations))
    assert len(skill_destinations) == 62
    assert len(retired) == 30
    assert retired.isdisjoint(skill_destinations)
    assert {
        "_shared",
        "academic-research-suite",
        "agent-reach",
        "code-review",
        "diagnosing-bugs",
        "gstack",
        "hatch-pet",
        "jupyter-notebook",
        "to-spec",
        "to-tickets",
    }.issubset(destinations)
    assert {
        "caveman",
        "diagnose",
        "docx",
        "gh-fix-ci",
        "pdf",
        "pptx",
        "review",
        "to-issues",
        "to-prd",
        "write-a-skill",
        "xlsx",
        "zoom-out",
    }.isdisjoint(skill_destinations)

    selectors = {item["selector"] for item in manifest["plugins"]}
    assert policy["install_root"] == manifest["install_root"]
    assert {item["name"] for item in policy["retired_skills"]} == retired
    assert "superpowers@openai-curated" in selectors
    assert "pdf@openai-primary-runtime" in selectors

    assert skills
    assert plugins
    assert all(item["name"] for item in skills)
    assert all(item["name"] for item in plugins)
    assert all(item["layer"] in {"codex", "system"} for item in skills)
    assert all("/.agents/skills/" not in item["path"] for item in skills)
    active_top_level = {
        item["path"].split("/")[3]
        for item in skills
        if item["layer"] == "codex" and item["path"].startswith("~/.codex/skills/")
    }
    assert retired.isdisjoint(active_top_level)
    destination_sources = {
        item["destination"]: source["source"]
        for source in manifest["sources"]
        for item in source["items"]
    }
    for item in skills:
        if item["layer"] != "codex":
            continue
        top_level = item["path"].split("/")[3]
        assert item["source"] == destination_sources[top_level]

    user_names = {item["name"] for item in skills if item["layer"] == "codex"}
    system_names = {item["name"] for item in skills if item["layer"] == "system"}
    enabled_plugin_names = {
        item["name"] for item in plugins if item["configured_enabled"]
    }
    assert user_names.isdisjoint(system_names)
    assert user_names.isdisjoint(enabled_plugin_names)
    assert len(user_names) == 120
    assert len(system_names) == 6

    assert lock["install_root"] == manifest["install_root"]
    assert set(lock["skills"]) == skill_destinations

    validate_registry(registry, skills, plugins, manifest)
    check_rendered_file(ROOT, registry, render_markdown(registry))

    print(
        json.dumps(
            {
                "sources": len(manifest["sources"]),
                "install_items": len(destinations),
                "user_install_targets": len(skill_destinations),
                "retired_skills": len(retired),
                "skill_entries": len(skills),
                "user_skill_entries": len(user_names),
                "system_skill_entries": len(system_names),
                "plugin_skill_entries": len(plugins),
                "unique_plugin_skill_names": len(
                    {item["name"] for item in plugins}
                ),
                "configured_plugins": len(selectors),
                "router_categories": len(registry["categories"]),
                "router_entries": len(registry["entries"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
