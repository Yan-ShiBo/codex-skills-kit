---
name: ship
description: Prepare and publish the requested commit or PR using the repository's checks and release conventions. (gstack)
---

# Ship the Requested Change

Establish the target branch, requested publication, and task-owned diff. Respect an explicit request to push the current branch; otherwise use the repository's branch/PR conventions. Preserve unrelated working-tree changes and existing commit history.

Inspect the remote state before publishing. Fetch when needed to establish the base or resolve divergence. Merge, rebase, squash, or split commits only when the requested workflow or repository convention calls for it; an ordinary push is not authorization to rewrite history.

Use [sections/tests.md](sections/tests.md) for affected checks and
[sections/test-coverage.md](sections/test-coverage.md) for meaningful test gaps.
Fix change-related failures and rerun affected checks. Successful evidence remains
valid for unchanged inputs. A full specialist review pipeline is optional unless
the user or repository requires it.

Update versions, changelogs, generated artifacts, and release notes only when the
repository's release rules or requested publication requires them. For a workspace
using the gstack release queue, inspect the existing queue and the documented
`gstack-version-bump`/`gstack-next-version` tools before allocating a version.
Do not create TODO lists, enable telemetry, sync memories, or upgrade tools as a
side effect of shipping.

Review the final diff for scope, credentials, and accidental generated files.
Commit task-owned paths and publish using the user's existing authorization.
For a PR, reuse an existing PR for the branch; summarize the actual change and
verification. Publishing review comments or merging/deploying requires that work
to be part of the request.

Verify the remote commit or PR. If required CI is running, follow that known run
with completion events or bounded status checks; stop on a terminal result.
When a wait ends before completion, report the pending run without claiming it
passed or silently scheduling monitoring. Finish with the result link and any
material limitation.
