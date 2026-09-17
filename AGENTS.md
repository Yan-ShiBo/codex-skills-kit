# Codex Skills Kit

This repository restores pinned upstream skills plus reviewed personal customizations.

- Change `overrides/` and `manifest/customizations.json` for personal instructions. Upstream commit pins and before/after hashes distinguish upstream content from customized content.
- `scripts/customize.py` previews or applies customizations to an existing installation. It backs up changed files and rejects unknown content; do not bypass a mismatch with a new hash without reviewing the diff.
- `scripts/snapshot.py` generates inventories. Preserve unrelated plugin snapshots when only editing skills; plugin cache presence does not prove a channel is operational.
- Relevant validation: `python scripts/verify.py`, `python scripts/capability_router.py --check`, and `python -m unittest discover -s tests -v`. These checks use local disposable fixtures and can be run without additional approval.
- Never commit authentication data, local backups, or browser sessions. Publishing this kit does not authorize publishing user data.
