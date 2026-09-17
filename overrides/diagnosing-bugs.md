---
name: diagnosing-bugs
description: Diagnose a bug or performance regression using targeted evidence, a useful reproduction, and a verified fix.
---

# Bug Diagnosis

Identify the reported symptom and inspect the relevant code, logs, recent changes, or measurements. Use the smallest available feedback loop that distinguishes the bug from expected behavior. A missing runnable environment does not prevent useful static investigation; state what cannot be verified.

Form hypotheses from evidence and test the most informative one first. Minimize a reproduction only while it helps identify the cause or build a regression check. Do not require a fixed number of hypotheses or randomized runs. For intermittent bugs, select a bounded sample appropriate to the observed failure rate and available budget.

Fix the cause within the requested scope. Add a regression test where it exercises the actual failure; use the original reproduction otherwise. For performance, compare the same workload and environment before and after.

Run the affected checks after the fix and remove temporary instrumentation. Reuse passing evidence until relevant inputs change. Finish once the symptom is addressed and the important checks pass; record larger architectural concerns as follow-up findings rather than invoking another workflow automatically.

Ask for missing access, data, or a decision only when it blocks further useful work. Report the evidence, attempted approaches, and exact remaining requirement.
