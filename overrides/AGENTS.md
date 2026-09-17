# Personal Working Preferences

- Complete the requested outcome and its relevant verification. Stop when those pass; expand scope only for a concrete dependency or newly discovered failure.
- Reuse decisions and authorization already given in the conversation. Ask only for information or approval that would change the next action; continue independent work while an answer is pending.
- Select skills by the requested deliverable, not by incidental words or URLs. Read the relevant workflow or reference, not the whole suite.
- Prefer the project's existing tests. Rerun affected checks after a change or failure; successful checks on unchanged inputs remain valid.
- Wait only for a known running operation or required user input. Use completion events or bounded status checks, stop on terminal results, and respect service retry hints. Do not sleep to appear thorough.
- Keep reusable skill changes in the Skills Kit customization manifest so reinstalling the pinned upstream sources preserves them. System and plugin packages are managed by Codex.
