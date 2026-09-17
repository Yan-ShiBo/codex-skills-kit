# Installed gstack Package

This is the pinned gstack source with Codex Skills Kit customizations.
Use the requested skill directly; the root SKILL.md is a selection aid.

Keep personal instruction changes in the Skills Kit customization manifest.
Upstream SKILL.md files are generated from templates; running upstream generation
or upgrading gstack can invalidate the customization hashes. Review and rebase the
customizations when changing the upstream pin.

Only build tools needed for the task. gstack's Bash setup requires Git Bash/MSYS
on Windows; native PowerShell cannot execute Bash snippets directly. Resolve
scripts relative to this installed directory and check runtime availability.

For upstream code changes, use `bun test` or the Windows subset
`bun run test:windows` as appropriate. Prompt-only customization does not require
building the browser, running cross-model benchmarks, or invoking a review suite.
