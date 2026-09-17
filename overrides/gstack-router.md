---
name: gstack
description: Select a gstack workflow when the user requests the suite or needs help choosing one of its workflows.
---

# gstack Router

Choose the workflow that matches the requested outcome. This router does not run startup checks, upgrade tools, configure telemetry, or modify project routing.

| Requested outcome | Workflow |
| --- | --- |
| Explore an idea or write a spec | `office-hours/SKILL.md` or `spec/SKILL.md` |
| Review a plan | the matching `plan-*-review/SKILL.md` |
| Run the full plan-review pipeline | `autoplan/SKILL.md` |
| Diagnose a bug | `investigate/SKILL.md` |
| Review changes | `review/SKILL.md` |
| Test a web app | `qa/SKILL.md` or report-only `qa-only/SKILL.md` |
| Check visual design | `design-review/SKILL.md` |
| Prepare a PR | `ship/SKILL.md` |
| Merge and deploy | `land-and-deploy/SKILL.md` |
| Post-deploy monitoring | `canary/SKILL.md` |
| Save or restore a handoff | `context-save/SKILL.md` or `context-restore/SKILL.md` |

For other named gstack commands, read that command's `SKILL.md` directly. If no workflow adds useful guidance, complete the task directly. A request to push does not imply deployment, version changes, a retrospective, or a full review pipeline.
