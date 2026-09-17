## Tests for the Requested Change

Use the repository's existing test commands and fixtures. Select checks that exercise the affected behavior; include shared or integration checks when the change affects their contracts. Read only enough test examples to follow local conventions.

For documentation or prompt-only changes, validate the relevant structure, links, references, or runnable examples. Do not bootstrap a test framework or create application tests solely to ship a prose change.

Fix failures caused by the change, then rerun affected checks. Previously passing checks remain valid when their inputs and environment have not changed. Broaden testing when new evidence exposes additional risk or repository CI requires it.

Report actual results and material gaps. An unavailable paid evaluation or external service is not evidence that it passed, nor a reason to repeatedly rerun unrelated local checks.
