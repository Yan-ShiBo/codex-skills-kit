---
name: agent-reach
description: Retrieve social posts, video transcripts, feeds, or other platform content using Agent Reach backends; configure those backends when requested.
metadata:
  homepage: https://github.com/Panniantong/Agent-Reach
---

# Agent Reach

Choose this skill when its platform-specific CLI or API is useful. Ordinary public-page reading and web search can use the available browser, search tool, or dedicated connector directly. A URL alone does not require Agent Reach.

For a multi-backend platform, reuse a recent `agent-reach doctor --json` result or check once when backend availability is unknown. A null `active_backend` means unverified, not necessarily missing. Verify the selected backend with a task-relevant read and require actual content before claiming success.

Read only the relevant reference:

| Task | Reference |
| --- | --- |
| Exa search | [search](references/search.md) |
| Social platforms, including Bilibili | [social](references/social.md) |
| LinkedIn and jobs | [career](references/career.md) |
| GitHub | [development](references/dev.md) |
| Web pages and RSS | [web](references/web.md) |
| Video subtitles and podcasts | [video](references/video.md) |
| Xueqiu | [finance](references/finance.md) |

If the platform is absent, inspect `opencli list` and its platform help. Adapter presence does not establish login or content availability. Follow a documented fallback after a failed read; stop retrying when credentials, access, or unsupported functionality are the cause.

Use only an existing user-authorized browser session or explicitly supplied credentials. Do not auto-extract browser cookies. Twitter CLI credentials must be set in the child process without logging their values. For Xiaohongshu, OpenCLI uses the user's existing session; manual cookie import belongs to the MCP/legacy backend, not Chrome. Login requirements do not authorize posting or other writes.

For installation or upgrades, consult the upstream guide for that task. Existing authorization for a named installation remains valid. Check versions during maintenance or when diagnosing compatibility, not after unrelated retrieval tasks.

Keep backend configuration in `~/.agent-reach/` and temporary retrieval output in the OS temporary directory. User-requested deliverables belong at the requested destination.
