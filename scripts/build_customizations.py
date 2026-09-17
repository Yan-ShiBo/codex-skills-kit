#!/usr/bin/env python3
"""Compile the reviewed instruction edits against pristine installed source files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from customize import digest, render

ROOT = Path(__file__).resolve().parents[1]

DESCRIPTIONS = {
    "academic-research-suite": "Plan academic research or experiments, review literature, and draft or review scholarly manuscripts using the relevant ARS workflow.",
    "baoyu-diagram": "Create technical diagrams with the Baoyu SVG templates and export workflow when those formats are requested.",
    "baoyu-electron-extract": "Extract resources or JavaScript from an installed Electron application's ASAR archive for authorized inspection.",
    "baoyu-image-gen": "Generate images through a specified Baoyu API provider or saved batch prompts when that backend is requested.",
    "baoyu-post-to-wechat": "Publish an article or image post to a WeChat Official Account when the user requests publication.",
    "baoyu-post-to-x": "Publish a post or article to X using the configured Baoyu workflow when requested.",
    "baoyu-translate": "Translate articles or files with optional glossaries and quick, normal, or publication-quality modes.",
    "baoyu-wechat-summary": "Retrieve and summarize WeChat group conversations through an already configured wx-cli backend.",
    "baoyu-youtube-transcript": "Retrieve a YouTube transcript and video metadata for a supplied video or transcript request.",
    "brooks-audit": "Audit module dependencies and architectural boundaries when a codebase architecture assessment is requested.",
    "brooks-debt": "Assess and prioritize technical debt with the Brooks taxonomy when a debt assessment is requested.",
    "brooks-health": "Produce a codebase health assessment using Brooks architecture, debt, and testing evidence.",
    "brooks-review": "Review a PR for architectural decay and maintenance risks using Brooks criteria.",
    "brooks-sweep": "Run the combined Brooks architecture, debt, review, and test workflow when a codebase audit with automatic fixes is requested.",
    "brooks-test": "Assess test quality, coverage of behavior, and reliability using Brooks review criteria.",
    "hatch-pet": "Create or repair a Codex desktop pet sprite sheet and its metadata, then validate the animation assets.",
    "markdown-to-html": "Convert Markdown to HTML using the repository's renderer and desired output style.",
    "ui-ux-pro-max": "Consult the UI/UX design catalog for interface styles, typography, color, or interaction choices when design guidance is needed.",
}

GSTACK_CONTEXT = """## Codex Execution Context

Use the workflow sections needed for the requested outcome. The user's scope and
current host mode govern execution; a skill does not override them. Reuse existing
decisions and authorization. Ask only about consequential unresolved choices.

Resolve executables from the installed gstack directory and use tools available in
this host. Initialize only variables and dependencies needed by the next command.
If a subagent tool is unavailable, perform a scoped check here. Do not create a new
user task merely to emulate the upstream Agent tool.

Run relevant checks; reuse passing results on unchanged inputs. End when the
requested result and required checks pass. Additional audits, upgrades, telemetry,
memory synchronization, checkpoint commits, and publication need a task reason.
Use status-based waits only for a known active operation, bounded by its deadline;
stop on success, failure, or a blocker, and respect service retry hints.

"""


def build(source_root: Path) -> dict:
    rules: dict = {}
    by_path: dict[str, list[str]] = {}

    def attach(path: str, name: str, rule: dict) -> None:
        if name in rules and rules[name] != rule:
            raise ValueError(f"Conflicting rule: {name}")
        rules[name] = rule
        by_path.setdefault(path, []).append(name)

    def replace(path: str, old: str, new: str) -> None:
        name = f"{path}:{len(by_path.get(path, []))}"
        attach(path, name, {"op": "replace", "old": old, "text": new})

    def file(path: str, asset: str) -> None:
        attach(path, asset, {"op": "file", "text": (ROOT / "overrides" / asset).read_text(encoding="utf-8")})

    for name in ("agent-reach", "planning-with-files", "code-review", "diagnosing-bugs", "find-skills"):
        file(f"{name}/SKILL.md", f"{name}.md")
    file("gstack/SKILL.md", "gstack-router.md")
    file("gstack/AGENTS.md", "gstack-agents.md")
    file("gstack/ship/SKILL.md", "gstack-ship.md")
    file("gstack/ship/sections/tests.md", "gstack-tests.md")
    file("gstack/ship/sections/test-coverage.md", "gstack-coverage.md")

    for name, description in DESCRIPTIONS.items():
        path = f"{name}/SKILL.md"
        text = (source_root / path).read_text(encoding="utf-8-sig")
        block = re.search(r"(?ms)^description:.*?(?=^[A-Za-z_-]+:|^---)", text)
        if not block:
            raise ValueError(f"Missing description: {path}")
        replace(path, block.group(), "description: " + description + "\n")

    for source in sorted((source_root / "gstack").rglob("SKILL.md")):
        path = source.relative_to(source_root).as_posix()
        if path in ("gstack/SKILL.md", "gstack/ship/SKILL.md"):
            continue
        text = source.read_text(encoding="utf-8")
        start = "\n## Preamble (run first)\n"
        if start not in text:
            continue
        footer = text.index("## Plan Status Footer", text.index(start))
        end = text.index("\n\n", footer + len("## Plan Status Footer") + 2)
        end_marker = text[footer:end]
        attach(path, "gstack-preamble", {"op": "span", "start": start, "end": end_marker, "include_end": True, "text": GSTACK_CONTEXT.rstrip()})

    path = "gstack/land-and-deploy/SKILL.md"
    replace(path, "Poll every 30 seconds, up to 30 minutes. Show a progress message every 2 minutes:", "Watch the known CI run with completion notifications when available; otherwise use bounded status checks with backoff. Stop on a terminal result or the workflow deadline, and report meaningful changes:")
    replace(path, "Poll every 30 seconds:", "Check the known deployment until it reaches a terminal state, using bounded waits and backoff:")
    replace(path, "Render deploys typically take 2-5 minutes. Poll every 30 seconds.", "Follow the Render deployment status; stop when ready or failed, with a bounded deadline.")
    replace(path, "Vercel and Netlify deploy automatically on merge. No explicit deploy trigger needed. Wait 60 seconds for the deploy to propagate, then proceed directly to canary verification in Step 7.", "Vercel and Netlify deploy automatically on merge. Inspect the deployment status or target revision; once it is ready, proceed to Step 7. Do not add a fixed propagation sleep.")
    replace(path, "{Wait for deploy workflow / Wait 60s / Skip}", "{Watch deploy status / Check readiness / Skip}")

    path = "gstack/spec/SKILL.md"
    replace(path, 'Files the issue,\noptionally spawns a Claude Code agent in a fresh worktree, and lets /ship close\nthe source issue on merge. Use when asked to "spec this out", "file an issue",\n"write up a ticket", "make this a GitHub issue", or "turn this into a backlog item".', 'Draft an executable specification, or publish it as an issue when requested.\nFor a local-only spec, use available requirements, the relevant discovery questions\nand template below, then save at the requested workspace path and finish. Issue\ndeduplication, publication gates, external quality scoring, archive synchronization\nand agent-launch sections apply only when those operations are part of the request.')
    replace(path, "**Step 1a (always):** Ask until you can crisply answer all five:", "**Step 1a (when requirements are missing):** Use existing context first; ask only for consequential gaps among these five:")
    replace(path, 'Present a full draft issue and ask: **"Does this accurately capture what you want?\nWhat did I get wrong?"** Iterate until the user confirms.', "Review the draft against the user's requirements. Ask for review only when an\nunresolved choice or requested approval changes the next action; reuse approval\nalready given for an actionable spec.")
    replace(path, "| `--execute` | conditional default (see Phase 5) |", "| `--execute` | opt-in |")
    attach(path, "spec-dispatch", {"op": "span", "start": "Read `GSTACK_PLAN_MODE` from the environment", "end": "#### File the issue (always)", "include_end": True, "text": "Use the current host's plan/execution mode and the user's requested deliverable. A spec request defaults to a local spec. File an issue only when publication was requested; launch another agent only when delegation was requested and the host supports it. Reuse existing authorization. Skip issue creation and agent-launch sections for a local-only spec.\n\n#### File the issue (when requested)"})
    replace(path, "1. **NEVER produce an issue after the first message.** Always start with Phase 1.", "1. Gather missing requirements when they affect the issue. If the user already supplied an actionable spec, proceed without a mandatory discovery round.")
    replace(path, "**HARD GATE:** Do NOT produce an issue after the first message. Always start with\nPhase 1. Do NOT propose implementation. Your only output is a spec — filed as a\nGitHub issue, archived locally, and optionally piped to a spawned agent.", "Produce the requested spec from the requirements already available. Use discovery\nonly for missing information that changes the result. Save a local spec by default;\npublish an issue or launch another agent only when the user requests those actions.")
    replace(path, "The user's first message after this prompt is their initial request. Begin Phase 1\nimmediately — do NOT ask them to repeat themselves.", "Use the user's existing request and start at the first phase still needed.")

    path = "gstack/plan-eng-review/SKILL.md"
    replace(path, "5. **Completeness check:** Is the plan doing the complete version or a shortcut? With AI-assisted coding, the cost of completeness (100% test coverage, full edge case handling, complete error paths) is 10-100x cheaper than with a human team. If the plan proposes a shortcut that saves human-hours but only saves minutes with CC+gstack, recommend the complete version. Boil the ocean.", "5. **Completion check:** Does the plan deliver the requested behavior and verify relevant failure paths? Require additional coverage only for a concrete risk or project requirement. Stop when the agreed outcome and relevant checks pass.")

    path = "baoyu-translate/SKILL.md"
    replace(path, "| Not found | **MUST** run first-time setup (see below) — do NOT silently use defaults |", "| Not found | Use the request and documented defaults; ask only for an unresolved target language or other consequential choice. |")
    attach(path, "translation-preferences", {"op": "span", "start": "### First-Time Setup (BLOCKING)", "end": "## Defaults", "text": "### Optional Saved Preferences\n\nUse [first-time setup](references/config/first-time-setup.md) only when the user wants to save reusable defaults. An absent EXTEND.md does not block a translation.\n\n"})

    path = "baoyu-image-gen/SKILL.md"
    replace(path, "## Step 0: Load Preferences ⛔ BLOCKING", "## Load Available Preferences")
    replace(path, "This step MUST complete before any image generation — generation is blocked until EXTEND.md exists.", "Use the requested provider and model or existing preferences. Missing EXTEND.md alone does not block generation.")
    replace(path, "- **Found** → load, parse, apply. If `default_model.[provider]` is null → ask model only.", "- **Found**: load applicable settings; honor the user's current provider/model choice.")
    replace(path, "- **Not found** → run first-time setup (`references/config/first-time-setup.md`) using AskUserQuestion to collect provider + model + quality + save location. Save EXTEND.md, then continue. Do not generate images before this completes.", "- **Not found**: use the configured backend and documented defaults. Ask only when credentials, provider cost, or an ambiguous model choice blocks execution. Save preferences only when requested.")

    optional = "Use the current request and documented defaults; save reusable preferences only when requested."
    for name in ("baoyu-cover-image", "baoyu-comic", "baoyu-xhs-images"):
        path = f"{name}/SKILL.md"
        text = (source_root / path).read_text(encoding="utf-8")
        replacements = {
            " ⛔ BLOCKING if not found": " (optional)",
            " ⛔ BLOCKING (interactive only)": " (optional)",
            " ⛔ BLOCKING": " (optional)",
            "Not found → run first-time setup → MUST complete before other steps": "Not found → use request settings and defaults",
            "Not found → First-Time Setup (optional) → Save EXTEND.md → Continue": "Not found → Use request settings and defaults → Continue",
            "Not found → First-Time Setup (optional)": "Not found → Use request settings and defaults",
            "Complete setup → Save EXTEND.md → Continue": "Continue without a preferences file",
            "If EXTEND.md is not found, first-time setup is **blocking** — complete it before any content analysis or style/tone questions.": optional,
            "| Not found | ⛔ Run first-time setup ([references/config/first-time-setup.md](references/config/first-time-setup.md)) → save EXTEND.md → continue |": "| Not found | " + optional + " |",
            "| Not found | ⛔ Run first-time setup ([references/config/first-time-setup.md](references/config/first-time-setup.md)) → Save → Continue |": "| Not found | " + optional + " |",
            "**CRITICAL**: If not found, complete setup BEFORE any other steps or questions.": optional,
            "- **Not found + interactive** → run first-time setup (see `references/config/first-time-setup.md`) and save before anything else. Do NOT analyze content or ask style questions until preferences exist — this keeps first-run behavior predictable.": "- **Not found + interactive**: " + optional,
            "The next run re-triggers first-time setup.": "Run setup only when reusable preferences are requested.",
        }
        for old, new in replacements.items():
            count = text.count(old)
            if count:
                attach(path, f"preferences:{path}:{len(by_path.get(path, []))}", {"op": "replace", "old": old, "text": new, "count": count})
                text = text.replace(old, new)

    path = "baoyu-comic/references/workflow.md"
    attach(path, "comic-preferences", {"op": "span", "start": "**When EXTEND.md Not Found**", "end": "**EXTEND.md Supports**", "text": "**When EXTEND.md Not Found**: " + optional + "\n\n"})
    path = "baoyu-post-to-wechat/SKILL.md"
    replace(path, "Found → read, parse, apply. Not found → run first-time setup (`references/config/first-time-setup.md`) before anything else.", "Found: apply saved settings. Missing: use request settings and documented defaults; resolve credentials and consequential publication options before publishing.")
    replace(path, "Check and load EXTEND.md (see \"Preferences\" above). If not found, complete first-time setup before any other questions. Resolve and cache for later steps: `default_theme`, `default_color`, `default_author`, `need_open_comment`, `only_fans_can_comment`.", "Use EXTEND.md when present. Otherwise prepare the content using defaults and resolve only missing credentials or consequential publication choices. Cache the theme, color, author and comment settings needed for this post.")

    # Adapt the surviving command examples to this kit's actual installation root.
    for path, names in list(by_path.items()):
        if not path.startswith("gstack/"):
            continue
        text = render((source_root / path).read_bytes(), {"path": path, "rules": names}, rules).decode("utf-8")
        old = ".claude/skills/gstack"
        count = text.count(old)
        if count:
            attach(path, f"codex-path:{path}", {"op": "replace", "old": old, "text": ".codex/skills/gstack", "count": count})
        old = "<!-- AUTO-GENERATED from SKILL.md.tmpl — do not edit directly -->\n<!-- Regenerate: bun run gen:skill-docs -->"
        if old in text:
            replace(path, old, "<!-- Customized by Codex Skills Kit; maintain the pinned customization manifest. -->")

    entries = []
    for path, names in sorted(by_path.items()):
        data = (source_root / path).read_bytes()
        entry = {"path": path, "rules": names, "before_sha256": digest(data)}
        updated = render(data, entry, rules)
        entry.update(after_sha256=digest(updated), before_bytes=len(data), after_bytes=len(updated))
        entries.append(entry)
    return {"schema_version": 1, "audit_date": "2026-09-16", "rules": rules, "files": entries, "global_preferences": (ROOT / "overrides/AGENTS.md").read_text(encoding="utf-8")}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True, help="Pristine skill root, before customizations")
    args = parser.parse_args()
    spec = build(args.source_root)
    path = ROOT / "manifest/customizations.json"
    path.write_bytes((json.dumps(spec, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    print(json.dumps({"files": len(spec["files"]), "before_bytes": sum(e["before_bytes"] for e in spec["files"]), "after_bytes": sum(e["after_bytes"] for e in spec["files"])}, indent=2))


if __name__ == "__main__":
    main()
