## Coverage of Changed Behavior

Inspect whether existing tests exercise the changed behavior and important failure cases. Add tests for a concrete regression risk, not to increase the test-file count.

Use measured coverage and thresholds only when the repository defines them. Do not estimate a numerical coverage percentage from a diagram or impose a generic 60/80/100 percent gate.

For test-only, documentation, or configuration-only changes, choose relevant checks rather than manufacturing application paths. Record any meaningful uncovered behavior and its impact. Once the requested behavior and required checks pass, continue the authorized delivery workflow.

Create a test-plan artifact only when downstream QA needs it or the user asks for one.
