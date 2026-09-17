---
name: code-review
description: Review a specified diff, branch, or PR for behavioral regressions, missing requirements, and consequential test gaps.
---

# Change Review

Establish the intended change and comparison. Use the user's ref, the PR base, or the obvious working-tree diff; state the assumption if needed. Ask only when multiple plausible comparisons would produce materially different reviews. Include uncommitted changes when they are the review target.

Read the affected code, relevant callers, and applicable project rules. Compare requirements from the request or available issue/spec; a missing issue-tracker setup is not a blocker. Do not create project configuration to perform a review.

Prioritize correctness, regressions, data integrity, security, and test gaps that could hide a bug. Style heuristics are not findings unless they cause a concrete maintenance or behavior problem. Use existing tests or a focused reproduction where it resolves uncertainty.

An independent review can help for a large or risky change when a subagent tool is available. Otherwise perform the review in the current context. Do not create user-visible tasks as substitutes for subagents.

Report actionable findings by severity with file/line evidence, impact, and the triggering conditions. Mark uncertain claims as such. If no issues are found, say so and mention material validation gaps. Do not change code or publish comments unless requested.
