#!/usr/bin/env python3
"""Validate repository manifests and inventory invariants."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    manifest = load("manifest/install-manifest.json")
    skills = load("inventory/skills.json")
    plugins = load("inventory/plugins.json")

    assert manifest["schema_version"] == 1
    assert len(manifest["sources"]) == 12
    assert all(len(source["ref"]) == 40 for source in manifest["sources"])
    assert all(source["items"] for source in manifest["sources"])

    destinations = [
        item["destination"]
        for source in manifest["sources"]
        for item in source["items"]
    ]
    assert len(destinations) == len(set(destinations))
    assert "_shared" in destinations
    assert "academic-research-suite" in destinations
    assert "gstack" in destinations

    assert skills
    assert plugins
    assert all(item["name"] for item in skills)
    assert all(item["name"] for item in plugins)

    print(
        json.dumps(
            {
                "sources": len(manifest["sources"]),
                "install_items": len(destinations),
                "skill_entries": len(skills),
                "plugin_skill_entries": len(plugins),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
