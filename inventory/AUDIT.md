# Skills Audit

Audit date: **2026-07-18**

## Result

- 61 top-level user-managed install targets from 11 pinned repositories
- 119 discoverable user-managed skill entries plus 6 Codex system entries
- 16 configured plugins and 131 cached plugin skill entries (114 unique cached names)
- No name overlap between user-managed skills, Codex system skills, and skills cached for enabled plugins
- 30 retired top-level destinations, all moved out of active discovery with recoverable backups

## Target profile

This setup is optimized for a research engineer working on Python/PyTorch implementations of stochastic control, reinforcement learning, PAC approximation, SOS/formal verification, reproducible Jupyter experiments, remote GPU/solver execution, and academic publication.

The governing rule is simple: user-managed skills live in `~/.codex/skills`; system and plugin skills stay in their Codex-managed locations.

Retirement rules are scoped to top-level destinations. A current nested skill such as `gstack/qa` or `gstack/review` remains owned by the pinned gstack suite even though an obsolete top-level skill once used the same name.

## Added

- **jupyter-notebook** from [`openai/skills`](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook): official templates and helpers for clean, reproducible notebooks.
- **hatch-pet** was already installed, but is now correctly sourced from [`openai/skills`](https://github.com/openai/skills/tree/main/skills/.curated/hatch-pet) instead of being an untracked local item.

## Updated upstream names

The latest pinned `mattpocock/skills` tree no longer contains seven paths from the previous lock. Four have direct semantic successors and are replaced in the install manifest:

| Previous name | Current name |
| --- | --- |
| `diagnose` | `diagnosing-bugs` |
| `review` | `code-review` |
| `to-issues` | `to-tickets` |
| `to-prd` | `to-spec` |

The replacements were verified against their frontmatter and workflow bodies, not inferred from similar-looking names.

Three removed skills were not remapped:

- `caveman`: no current upstream skill preserves its terse-response semantics.
- `zoom-out`: `wayfinder` is a multi-session decision-planning workflow, not a broader-context command.
- `write-a-skill`: Codex already provides the built-in `skill-creator`, so keeping an obsolete duplicate would add ambiguity.

## Retired: upstream deprecated

The upstream maintainer places these under `skills/deprecated` and describes them as skills no longer used:

- `design-an-interface`
- `qa`
- `request-refactor-plan`
- `ubiquitous-language`

Evidence: [`mattpocock/skills/skills/deprecated`](https://github.com/mattpocock/skills/tree/main/skills/deprecated).

## Retired: exact plugin duplicates

The local `SKILL.md` files for these 14 skills were byte-for-byte identical to the enabled Superpowers plugin copies, so the user-level copies added no capability:

- `brainstorming`
- `dispatching-parallel-agents`
- `executing-plans`
- `finishing-a-development-branch`
- `receiving-code-review`
- `requesting-code-review`
- `subagent-driven-development`
- `systematic-debugging`
- `test-driven-development`
- `using-git-worktrees`
- `using-superpowers`
- `verification-before-completion`
- `writing-plans`
- `writing-skills`

## Retired: plugin replacements

- `gh-fix-ci` is supplied by the enabled GitHub plugin.
- `docx` is replaced by the enabled Documents runtime plugin.
- `pdf` is replaced by the enabled PDF runtime plugin.
- `pptx` is replaced by the enabled Presentations runtime plugin.
- `xlsx` is replaced by the enabled Spreadsheets runtime plugin.

These replacements avoid ambiguous triggers and use the Codex runtime integrations that are updated with the app.

## Evaluated but not added

| Candidate | Decision |
| --- | --- |
| `scientific-writing` | Rejected because `academic-research-suite` already covers the same research and writing chain. |
| `latex-paper-en` | Rejected because the installed academic suite already covers LaTeX drafting, review, citations, and formatting. |
| `python-testing-patterns` | Rejected globally because generic pytest advice can conflict with this user's strict remote-only, serial, solver/GPU, and temporary-directory rules. |
| `experiment-plan` | Rejected because both the academic suite and the research repository already define claim-driven experiment planning. |

## Safety and recovery

No retired or replaced directory is permanently erased during reconciliation. Old copies are moved to timestamped backup roots outside active skill discovery. The legacy `.agents/skills` tree is likewise moved only after every agents-only item has been copied into the Codex root.

## Installation validation

The complete manifest is installed into an isolated Codex home before local reconciliation. Validation checks every source path at its pinned commit, the exact destination set, JSON invariants, Python compilation, and PowerShell syntax.
