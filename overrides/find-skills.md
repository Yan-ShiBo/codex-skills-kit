---
name: find-skills
description: Find an installable skill when the user asks to discover or extend agent capabilities.
---

# Find Skills

Start with available skills and connectors. If they already cover the requested capability, explain the match. Ordinary requests to perform a task are not requests to install tools.

For a missing capability, search the requested source or use `npx skills find <query>`. Read the candidate's actual instructions, dependency requirements, maintenance state, and authorization boundaries. Popularity is supporting evidence, not a minimum threshold or proof of quality.

Recommend the smallest relevant option and disclose setup requirements. Use the available skill installer when installation is requested. Inspect and preserve the user's destination conventions; this kit uses `~/.codex/skills`. Do not update unrelated skills or add duplicate plugin capabilities.
