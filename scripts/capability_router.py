#!/usr/bin/env python3
"""Validate and render the repository's thin capability router."""

from __future__ import annotations

import argparse
import difflib
import json
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_DEPLOY_STATUS = {"built-in", "installed", "configured", "reference"}
ALLOWED_MANAGEMENT_STATUS = {"active", "cold", "disabled", "reference", "retired"}
ALLOWED_HEALTH_STATUS = {"healthy", "unverified", "degraded", "broken", "missing"}
ALLOWED_INVOCATION = {"auto", "conditional", "explicit-only", "disabled"}
ALLOWED_AUTHORIZATION = {
    "ordinary",
    "write-gated",
    "install-gated",
    "stateful-session-gated",
    "publish-gated",
    "config-gated",
}
ALLOWED_RISK = {"low", "medium", "high"}
ROUTABLE_MANAGEMENT_STATUS = {"active"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_inputs(root: Path = ROOT) -> tuple[dict, list[dict], list[dict], dict]:
    return (
        load_json(root / "manifest" / "capability-registry.json"),
        load_json(root / "inventory" / "skills.json"),
        load_json(root / "inventory" / "plugins.json"),
        load_json(root / "manifest" / "install-manifest.json"),
    )


def duplicate_values(values: list[str]) -> set[str]:
    return {value for value, count in Counter(values).items() if count > 1}


def require_text(item: dict, field: str, context: str, errors: list[str]) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{context}: {field} must be a non-empty string")
        return ""
    return value.strip()


def validate_registry(
    registry: dict,
    skills: list[dict],
    plugins: list[dict],
    install_manifest: dict,
) -> None:
    """Raise ValueError when the registry cannot produce a trustworthy router."""

    errors: list[str] = []
    if registry.get("schema_version") != 1:
        errors.append("registry: schema_version must be 1")

    require_text(registry, "snapshot_date", "registry", errors)
    require_text(registry, "source_inventory_date", "registry", errors)

    max_categories = registry.get("max_categories")
    if not isinstance(max_categories, int) or not 1 <= max_categories <= 10:
        errors.append("registry: max_categories must be an integer from 1 to 10")
        max_categories = 10

    generated_markdown = registry.get("generated_markdown")
    if not isinstance(generated_markdown, str) or not generated_markdown.endswith(".md"):
        errors.append("registry: generated_markdown must point to a Markdown file")
    else:
        generated_path = PurePosixPath(generated_markdown)
        if (
            generated_path.is_absolute()
            or ".." in generated_path.parts
            or not generated_path.parts
            or generated_path.parts[0] != "inventory"
            or "\\" in generated_markdown
        ):
            errors.append(
                "registry: generated_markdown must be a safe repository-relative path under inventory/"
            )

    require_text(
        registry,
        "native_visibility_boundary",
        "registry",
        errors,
    )

    categories = registry.get("categories")
    entries = registry.get("entries")
    if not isinstance(categories, list):
        errors.append("registry: categories must be a list")
        categories = []
    if not isinstance(entries, list):
        errors.append("registry: entries must be a list")
        entries = []

    if len(categories) > max_categories:
        errors.append(
            f"registry: {len(categories)} categories exceed max_categories={max_categories}"
        )

    entry_ids = [item.get("id") for item in entries if isinstance(item, dict)]
    entry_ids_text = [item for item in entry_ids if isinstance(item, str)]
    for duplicate in sorted(duplicate_values(entry_ids_text)):
        errors.append(f"registry: duplicate entry id {duplicate!r}")
    entries_by_id = {
        item["id"]: item
        for item in entries
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }

    skill_targets = {
        (item.get("name"), item.get("layer"))
        for item in skills
        if isinstance(item, dict)
    }
    configured_selectors = {
        item.get("selector")
        for item in install_manifest.get("plugins", [])
        if isinstance(item, dict)
    }
    plugin_targets = {
        (f"{item.get('plugin')}@{item.get('marketplace')}", item.get("name"))
        for item in plugins
        if isinstance(item, dict)
    }

    for index, entry in enumerate(entries):
        context = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{context}: entry must be an object")
            continue
        entry_id = require_text(entry, "id", context, errors)
        if entry_id:
            context = f"entry {entry_id!r}"
        for field in ("slot", "trigger", "do_not_use", "fallback", "evidence"):
            value = require_text(entry, field, context, errors)
            if field in {"trigger", "do_not_use"} and len(value) > 240:
                errors.append(f"{context}: {field} exceeds the 240-character thin-row limit")

        for field, allowed in (
            ("deploy_status", ALLOWED_DEPLOY_STATUS),
            ("management_status", ALLOWED_MANAGEMENT_STATUS),
            ("health_status", ALLOWED_HEALTH_STATUS),
            ("invocation", ALLOWED_INVOCATION),
            ("authorization", ALLOWED_AUTHORIZATION),
            ("risk", ALLOWED_RISK),
        ):
            value = entry.get(field)
            if value not in allowed:
                errors.append(f"{context}: invalid {field} {value!r}")

        manager_type = entry.get("manager_type")
        if not isinstance(manager_type, bool):
            errors.append(f"{context}: manager_type must be boolean")
        elif manager_type and entry.get("invocation") != "explicit-only":
            errors.append(f"{context}: manager-type capabilities must be explicit-only")

        target = entry.get("target")
        if not isinstance(target, dict):
            errors.append(f"{context}: target must be an object")
            continue
        kind = target.get("kind")
        if kind == "baseline":
            continue
        if kind == "skill":
            name = target.get("name")
            layer = target.get("layer")
            if (name, layer) not in skill_targets:
                errors.append(
                    f"{context}: skill target {name!r} in layer {layer!r} is absent from inventory/skills.json"
                )
            continue
        if kind == "plugin_skill":
            selector = target.get("selector")
            name = target.get("name")
            if selector not in configured_selectors:
                errors.append(
                    f"{context}: plugin selector {selector!r} is absent from the install manifest"
                )
            if (selector, name) not in plugin_targets:
                errors.append(
                    f"{context}: plugin skill {selector!r}/{name!r} is absent from inventory/plugins.json"
                )
            continue
        errors.append(f"{context}: unsupported target kind {kind!r}")

    category_ids: list[str] = []
    referenced: set[str] = set()
    for index, category in enumerate(categories):
        context = f"categories[{index}]"
        if not isinstance(category, dict):
            errors.append(f"{context}: category must be an object")
            continue
        category_id = require_text(category, "id", context, errors)
        if category_id:
            category_ids.append(category_id)
            context = f"category {category_id!r}"
        require_text(category, "task", context, errors)
        boundary = require_text(category, "boundary", context, errors)
        if len(boundary) > 180:
            errors.append(f"{context}: boundary exceeds the 180-character L1 limit")
        candidates = category.get("candidates")
        if not isinstance(candidates, list) or not 1 <= len(candidates) <= 3:
            errors.append(f"{context}: candidates must contain 1 to 3 entry ids")
            continue
        candidate_ids = [item for item in candidates if isinstance(item, str)]
        if len(candidate_ids) != len(set(candidate_ids)):
            errors.append(f"{context}: candidates contain duplicates")
        for candidate in candidates:
            if not isinstance(candidate, str) or candidate not in entries_by_id:
                errors.append(f"{context}: unknown candidate {candidate!r}")
                continue
            referenced.add(candidate)
            entry = entries_by_id[candidate]
            if entry.get("management_status") not in ROUTABLE_MANAGEMENT_STATUS:
                errors.append(
                    f"{context}: candidate {candidate!r} is not active in the thin registry"
                )
            if entry.get("invocation") == "disabled":
                errors.append(f"{context}: candidate {candidate!r} has disabled invocation")
            if entry.get("health_status") in {"broken", "missing"}:
                errors.append(
                    f"{context}: candidate {candidate!r} has non-routable health status"
                )

    for duplicate in sorted(duplicate_values(category_ids)):
        errors.append(f"registry: duplicate category id {duplicate!r}")

    unreferenced = set(entries_by_id) - referenced
    if unreferenced:
        errors.append(
            "registry: thin entries not referenced by an L1 category: "
            + ", ".join(sorted(unreferenced))
        )

    fallback = registry.get("default_fallback")
    if fallback not in entries_by_id:
        errors.append(f"registry: unknown default_fallback {fallback!r}")
    elif entries_by_id[fallback].get("target", {}).get("kind") != "baseline":
        errors.append("registry: default_fallback must target the baseline capability")

    if errors:
        raise ValueError("Capability registry validation failed:\n- " + "\n- ".join(errors))


def markdown_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def target_label(entry: dict) -> str:
    target = entry["target"]
    if target["kind"] == "baseline":
        return "Codex baseline"
    if target["kind"] == "skill":
        return f"{target['layer']} skill: `{target['name']}`"
    return f"plugin: `{target['selector']}` / `{target['name']}`"


def render_markdown(registry: dict) -> str:
    entries = {entry["id"]: entry for entry in registry["entries"]}
    lines = [
        "# Capability Router",
        "",
        "> Generated by `python scripts/capability_router.py --write`. Do not edit this file by hand.",
        "> This is a soft decision layer: it does not hide, disable, install, or change Codex-native invocation behavior.",
        "",
        f"- Router snapshot: **{registry['snapshot_date']}**",
        f"- Source inventory: **{registry['source_inventory_date']}**",
        f"- Default fallback: `{registry['default_fallback']}`",
        "",
        "## Level 0: Native Visibility Boundary",
        "",
        registry["native_visibility_boundary"],
        "",
        "Any install, login, external write, deletion, hook change, or client configuration change still requires the applicable user approval.",
        "",
        "## Level 1: Thin Router",
        "",
        "| Task type | Boundary | Candidates |",
        "| --- | --- | --- |",
    ]
    for category in registry["categories"]:
        candidates = " -> ".join(f"`{item}`" for item in category["candidates"])
        lines.append(
            f"| {markdown_cell(category['task'])} | {markdown_cell(category['boundary'])} | {candidates} |"
        )

    lines.extend(
        [
            "",
            "If no row matches, use the default fallback first. Query the full inventory only when a real capability gap remains; do not scan the whole library by default.",
            "",
            "## Level 2: Thin Registry",
            "",
            "Management, deployment, health, invocation, authorization, and risk are separate axes. `unverified` means the plugin is configured and inventoried but still needs a live check at invocation time.",
            "",
            "| ID | Capability slot | Target | Deploy / health | Invocation | Trigger and do-not-use boundary | Risk / authorization | Fallback |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for entry in registry["entries"]:
        manager = " / manager-type" if entry["manager_type"] else ""
        boundary = f"Use: {entry['trigger']} Do not use: {entry['do_not_use']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{markdown_cell(entry['id'])}`",
                    markdown_cell(entry["slot"]),
                    markdown_cell(target_label(entry)),
                    markdown_cell(
                        f"{entry['deploy_status']} / {entry['health_status']}"
                    ),
                    markdown_cell(f"{entry['invocation']}{manager}"),
                    markdown_cell(boundary),
                    markdown_cell(f"{entry['risk']} / {entry['authorization']}"),
                    markdown_cell(entry["fallback"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Maintenance Rules",
            "",
            "- Update `manifest/capability-registry.json`, then regenerate this file.",
            "- Keep Level 1 at ten categories or fewer and every category at three candidates or fewer.",
            "- A manager-type capability must remain `explicit-only`.",
            "- An installed item is not automatically healthy. Plugin health remains `unverified` until a live check succeeds.",
            "- A candidate must resolve to the pinned skill inventory or a configured plugin selector.",
            "- Preserve `baseline-direct` as a real option; more tooling is not automatically better.",
            "",
        ]
    )
    return "\n".join(lines)


def check_rendered_file(root: Path, registry: dict, rendered: str) -> None:
    path = root / registry["generated_markdown"]
    if not path.exists():
        raise ValueError(f"Generated router is missing: {path.relative_to(root)}")
    current = path.read_text(encoding="utf-8")
    if current == rendered:
        return
    diff = "".join(
        difflib.unified_diff(
            current.splitlines(keepends=True),
            rendered.splitlines(keepends=True),
            fromfile=str(path.relative_to(root)),
            tofile="generated",
            n=2,
        )
    )
    raise ValueError(
        "Generated capability router is stale. Run "
        "`python scripts/capability_router.py --write`.\n" + diff[:4000]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="regenerate the Markdown router")
    mode.add_argument("--check", action="store_true", help="validate and check generated output")
    args = parser.parse_args()

    registry, skills, plugins, install_manifest = load_inputs(ROOT)
    validate_registry(registry, skills, plugins, install_manifest)
    rendered = render_markdown(registry)
    output = ROOT / registry["generated_markdown"]
    if args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        check_rendered_file(ROOT, registry, rendered)

    print(
        json.dumps(
            {
                "categories": len(registry["categories"]),
                "registry_entries": len(registry["entries"]),
                "output": str(output.relative_to(ROOT)),
                "mode": "write" if args.write else "check",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
