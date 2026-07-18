# Installed Skills Inventory

- Active skill entries: **125**
- Unique skill names: **125**
- Generated: **2026-07-18**
- User-managed root: **`~/.codex/skills`**

Plugin-managed skills are listed separately and are not duplicated here.

## Codex built-in

- **imagegen**: Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.
- **openai-docs**: Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex surfaces, needs up-to-date official documentation with citations, help choosing the latest model for a use case, latest/current/default-model prompting guidance, or model upgrade and prompt-upgrade guidance; use OpenAI docs MCP tools for non-Codex docs questions, use the Codex manual helper first for broad Codex self-knowledge, and restrict fallback browsing to official OpenAI domains.
- **plugin-creator**: Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, valid manifest defaults, and personal-marketplace entries by default. Use when Codex needs to create a new personal plugin, add optional plugin structure, generate or update marketplace entries for plugin ordering and availability metadata, or update an existing local plugin during development with the CLI-driven cachebuster and reinstall flow.
- **review-agent**: Perform a read-only, defect-first review of a specified code change and return every actionable finding. Use when another agent delegates review of uncommitted changes, a base-branch diff, a commit, or custom review instructions.
- **skill-creator**: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.
- **skill-installer**: Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

## Imbad0202/academic-research-skills-codex

- **academic-research-suite**: Codex-native Academic Research Skills suite for deep research, academic paper writing, manuscript review, full research-to-paper pipelines, and experiment planning or validation. Use when the user asks for deep research, literature review, systematic review, meta-analysis, research question refinement, academic paper drafting, paper revision, citation or integrity checks, reviewer simulation, peer review, editorial decision letters, research-to-paper workflows, experiment execution planning, statistical interpretation, or human study protocol support. Korean triggers include 논문 심사, 논문 수정, 초록 작성, 체계적 문헌고찰, and 연구부터 논문까지. Also use for Claude-style ARS command aliases such as /ars-plan, ars-plan, /ars-outline, /ars-abstract, /ars-lit-review, /ars-citation-check, /ars-disclosure, /ars-format-convert, /ars-3w, /ars-revision-coach, /ars-revision, /ars-reviewer, /ars-mark-read, /ars-unmark-read, /ars-cache-invalidate, /ars-rebuttal-audit, and /ars-full. This skill vendors ARS role prompts, references, templates, and shared handoff schemas under ars/.

## anthropics/skills

- **frontend-design**: Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults.
- **mcp-builder**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- **webapp-testing**: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

## davila7/claude-code-templates

- **planning-with-files**: Implements Manus-style file-based planning for complex tasks. Creates task_plan.md, findings.md, and progress.md. Use when starting complex multi-step tasks, research projects, or any task requiring >5 tool calls.

## garrytan/gstack

- **autoplan**: Auto-review pipeline — reads the full CEO, design, eng, and DX review skills from disk and runs them sequentially with auto-decisions using 6 decision principles. (gstack)
- **benchmark**: Performance regression detection using the browse daemon. (gstack)
- **benchmark-models**: Cross-model benchmark for gstack skills. (gstack)
- **browse**: Fast headless browser for QA testing and site dogfooding. (gstack)
- **canary**: Post-deploy canary monitoring. (gstack)
- **careful**: Safety guardrails for destructive commands. (gstack)
- **codex**: OpenAI Codex CLI wrapper — three modes. (gstack)
- **context-restore**: Restore working context saved earlier by /context-save. (gstack)
- **context-save**: Save working context. (gstack)
- **cso**: Chief Security Officer mode. (gstack)
- **design-consultation**: Design consultation: understands your product, researches the landscape, proposes a complete design system (aesthetic, typography, color, layout, spacing, motion), and generates font+color preview... (gstack)
- **design-html**: Design finalization: generates production-quality Pretext-native HTML/CSS. (gstack)
- **design-review**: Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems, AI slop patterns, and slow interactions — then fixes them. (gstack)
- **design-shotgun**: Design shotgun: generate multiple AI design variants, open a comparison board, collect structured feedback, and iterate. (gstack)
- **devex-review**: Live developer experience audit. (gstack)
- **diagram**: Turn an English description (or mermaid source) into a diagram triplet: the source, an editable .excalidraw file you can open (gstack)
- **document-generate**: Generate missing documentation from scratch for a feature, module, or entire project. (gstack)
- **document-release**: Post-ship documentation update. (gstack)
- **freeze**: Restrict file edits to a specific directory for the session. (gstack)
- **gstack**: Router for the gstack skill suite. (gstack)
- **gstack-openclaw-ceo-review**: Use when asked to review a plan, challenge a proposal, run a CEO review, poke holes in an approach, think bigger about scope, or decide whether to expand or reduce the plan.
- **gstack-openclaw-investigate**: Use when asked to debug, fix a bug, investigate an error, or do root cause analysis, and when users report errors, stack traces, unexpected behavior, or say something stopped working.
- **gstack-openclaw-office-hours**: Use when asked to brainstorm, evaluate whether an idea is worth building, run office hours, or think through a new product idea or design direction before any code is written.
- **gstack-openclaw-retro**: Weekly engineering retrospective. Analyzes commit history, work patterns, and code quality metrics with persistent history and trend tracking. Team-aware with per-person contributions, praise, and growth areas. Use when asked for weekly retro, what shipped this week, or engineering retrospective.
- **gstack-upgrade**: Upgrade gstack to the latest version.
- **guard**: Full safety mode: destructive command warnings + directory-scoped edits. (gstack)
- **hackernews-frontpage**: Scrape the Hacker News front page (titles, points, comment counts).
- **health**: Code quality dashboard. (gstack)
- **investigate**: Systematic debugging with root cause investigation. (gstack)
- **ios-clean**: Remove the DebugBridge SPM package and all #if DEBUG wiring from an iOS app. (gstack)
- **ios-design-review**: Visual design audit for iOS apps on real hardware. (gstack)
- **ios-fix**: Autonomous iOS bug fixer. (gstack)
- **ios-qa**: Live-device iOS QA for SwiftUI apps. (gstack)
- **ios-sync**: Regenerate the iOS debug bridge against the latest upstream gstack templates. (gstack)
- **land-and-deploy**: Land and deploy workflow. (gstack)
- **landing-report**: Read-only queue dashboard for workspace-aware ship. (gstack)
- **learn**: Manage project learnings.
- **make-pdf**: Turn any markdown file into a publication-quality PDF. (gstack)
- **office-hours**: YC Office Hours — two modes. (gstack)
- **open-gstack-browser**: Launch GStack Browser — AI-controlled Chromium with the sidebar extension baked in.
- **pair-agent**: Pair a remote AI agent with your browser. (gstack)
- **plan-ceo-review**: CEO/founder-mode plan review. (gstack)
- **plan-design-review**: Designer's eye plan review — interactive, like CEO and Eng review. (gstack)
- **plan-devex-review**: Interactive developer experience plan review. (gstack)
- **plan-eng-review**: Eng manager-mode plan review. (gstack)
- **plan-tune**: Self-tuning question sensitivity + developer psychographic for gstack (v1: observational). (gstack)
- **qa**: Systematically QA test a web application and fix bugs found. (gstack)
- **qa-only**: Report-only QA testing. (gstack)
- **retro**: Weekly engineering retrospective. (gstack)
- **review**: Pre-landing PR review. (gstack)
- **scrape**: Pull data from a web page. (gstack)
- **setup-browser-cookies**: Import cookies from your real Chromium browser into the headless browse session. (gstack)
- **setup-deploy**: Configure deployment settings for /land-and-deploy.
- **setup-gbrain**: Set up gbrain for this coding agent: install the CLI, initialize a local PGLite or Supabase brain, register MCP, capture per-remote trust policy. (gstack)
- **ship**: Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. (gstack)
- **skillify**: Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack)
- **spec**: Turn vague intent into a precise, executable spec in five phases. (gstack)
- **sync-gbrain**: Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack)
- **unfreeze**: Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack)

## github/awesome-copilot

- **markdown-to-html**: Convert Markdown files to HTML similar to `marked.js`, `pandoc`, `gomarkdown/markdown`, or similar tools; or writing custom script to convert markdown to html and/or working on web template systems like `jekyll/jekyll`, `gohugoio/hugo`, or similar web templating systems that utilize markdown documents, converting them to html. Use when asked to "convert markdown to html", "transform md to html", "render markdown", "generate html from markdown", or when working with .md files and/or web a templating system that converts markdown to HTML output. Supports CLI and Node.js workflows with GFM, CommonMark, and standard Markdown flavors.

## hyhmrright/brooks-lint

- **brooks-audit**: Architecture audit that maps module dependencies, checks layering integrity, and flags structural decay across a codebase, drawing on twelve classic engineering books. Triggers when: user asks to audit architecture, review folder/module structure, check for circular imports, understand how the codebase is organized, or asks "does this follow clean architecture?" or "why does everything depend on everything?". Also triggers for onboarding requests: "explain this codebase to a new developer" or "give me a codebase tour" (use onboarding mode). Do NOT trigger for: PR-level code review (use brooks-review) or line-level refactoring questions — this skill analyzes structural/module-level concerns, not individual functions.
- **brooks-debt**: Tech debt assessment that identifies, classifies, and prioritizes maintainability problems — helping teams build a refactoring roadmap — drawing on twelve classic engineering books. Triggers when: user asks about tech debt, refactoring priorities, what to clean up first, or asks "why is this so hard to change?", "what should we fix first?", or "how do I justify refactoring to management?". Do NOT trigger for: server health checks, HTTP /health endpoints, Kubernetes probes, database health, or application uptime — "health" in those contexts is infrastructure, not code quality. Also not for single-function refactoring questions.
- **brooks-health**: Combined codebase health dashboard that scores a project across all four quality dimensions — PR quality, architecture, tech debt, and test quality — in a single pass, drawing on twelve classic engineering books. Triggers when: user wants an overall quality assessment, asks "how healthy is this codebase?", "run all the checks", "I need a health score before the release", or wants to onboard a new team with a quality overview. Do NOT trigger for: server health checks, HTTP health endpoints, Kubernetes liveness/readiness probes, database health, or application uptime. Also do not trigger when the user specifically requests only one dimension — use the corresponding focused skill instead (brooks-review / brooks-audit / brooks-debt / brooks-test).
- **brooks-review**: PR code review that surfaces decay risks, design smells, and maintainability issues with concrete Symptom → Source → Consequence → Remedy findings, drawing on twelve classic engineering books. Triggers when: user asks to review code, check a PR, shares a diff or pastes code asking "does this look right?" / "any issues here?" / "ready to merge?", or asks for feedback on a function, class, or file. Also triggers when user mentions: code smells / refactoring / clean architecture / DDD / SOLID principles / Hyrum's Law / deep modules / tactical programming / conceptual integrity / Brooks's Law / Mythical Man-Month / second system effect. Do NOT trigger for: questions about how to write code from scratch, language syntax questions, or framework/tool questions where no existing code is shared.
- **brooks-sweep**: Full-sweep mode: runs a unified analysis across all quality dimensions — code decay, architecture, tech debt, and test quality — then applies fixes directly to the codebase. Safe changes are auto-applied; risky changes are confirmed before execution. Drawing on twelve classic engineering books. Triggers when: user wants to "fix everything", "sweep the codebase", "auto-fix all issues", "clean up the whole project", or asks for a single command that both diagnoses and remediates quality problems. Do NOT trigger for: read-only audits or health reports where the user only wants findings without code changes; single-dimension reviews (use the focused skill instead: brooks-review / brooks-audit / brooks-debt / brooks-test); server health checks, HTTP /health endpoints, Kubernetes probes, database health, or application uptime.
- **brooks-test**: Test quality review drawing on twelve classic engineering books — with primary focus on xUnit Test Patterns, The Art of Unit Testing, How Google Tests Software, and Working Effectively with Legacy Code — that diagnoses structural problems in an existing test suite: brittleness, mock abuse, coverage illusions, slow execution, poor readability. Triggers when: user asks about test quality, shares test files for review, or expresses frustration: "tests keep breaking whenever I change anything", "our tests take forever", "tests pass but bugs still reach production", or "we have too many mocks". Do NOT trigger for: writing new tests from scratch (use the regular test-writing workflow) or testing framework/syntax questions — this skill reviews an existing suite for structural quality problems, not individual test authoring.

## jimliu/baoyu-skills

- **baoyu-article-illustrator**: Analyzes article structure, identifies positions requiring visual aids, generates illustrations with Type × Style × Palette three-dimension approach. Use when user asks to "illustrate article", "add images", "generate images for article", or "为文章配图".
- **baoyu-comic**: Knowledge comic creator supporting multiple art styles and tones. Creates original educational comics with detailed panel layouts and batch-capable image generation. Use when user asks to create "知识漫画", "教育漫画", "biography comic", "tutorial comic", or "Logicomix-style comic".
- **baoyu-compress-image**: Compresses images to WebP (default) or PNG with automatic tool selection. Use when user asks to "compress image", "optimize image", "convert to webp", or reduce image file size.
- **baoyu-cover-image**: Generates article cover images with 5 dimensions (type, palette, rendering, text, mood) combining 11 color palettes and 7 rendering styles. Supports cinematic (2.35:1), widescreen (16:9), and square (1:1) aspects. Use when user asks to "generate cover image", "create article cover", or "make cover".
- **baoyu-danger-gemini-web**: Generates images and text via reverse-engineered Gemini Web API. Supports text generation, image generation from prompts, reference images for vision input, and multi-turn conversations. Use when other skills need image generation backend, or when user requests "generate image with Gemini", "Gemini text generation", or needs vision-capable AI generation.
- **baoyu-danger-x-to-markdown**: Converts X (Twitter) tweets and articles to markdown with YAML front matter. Uses reverse-engineered API requiring user consent. Use when user mentions "X to markdown", "tweet to markdown", "save tweet", or provides x.com/twitter.com URLs for conversion.
- **baoyu-diagram**: Create professional, dark-themed SVG diagrams of any type — architecture diagrams, flowcharts, sequence diagrams, structural diagrams, mind maps, timelines, illustrative/conceptual diagrams, and more. Use this skill whenever the user asks for any kind of technical or conceptual diagram, visualization of a system, process flow, data flow, component relationship, network topology, decision tree, org chart, state machine, or any visual representation of structure/logic/process. Also trigger when the user says "画个图" "画一个架构图" "diagram" "flowchart" "sequence diagram" "draw me a ..." or uploads content and asks to visualize it. Output is always a standalone .svg file.
- **baoyu-electron-extract**: Extracts resources and JavaScript from any installed Electron app (`.asar` bundle), restoring original sources from `.js.map` files when available or formatting minified code with Prettier otherwise. Use when user wants to "extract Electron app", "decompile Electron", "get the source code of <app>", "inspect app.asar", "看 Electron 应用源码", "提取 .asar", or asks how a desktop Electron app is built. Skips `node_modules` and supports both macOS and Windows.
- **baoyu-format-markdown**: Formats plain text or markdown files with frontmatter, titles, summaries, headings, bold, lists, and code blocks. Use when user asks to "format markdown", "beautify article", "add formatting", or improve article layout. Outputs to {filename}-formatted.md.
- **baoyu-image-gen**: AI image generation with OpenAI GPT Image 2, Azure OpenAI, Google, OpenRouter, DashScope, Z.AI GLM-Image, MiniMax, Jimeng, Seedream, Replicate and Agnes APIs. Supports text-to-image, reference images, aspect ratios, and batch generation from saved prompt files. Sequential by default; use batch parallel generation when the user already has multiple prompts or wants stable multi-image throughput. Use when user asks to generate, create, or draw images.
- **baoyu-infographic**: Generate professional infographics with 21 layout types and 22 visual styles. Analyzes content, recommends layout×style combinations, and generates publication-ready infographics. Use when user asks to create "infographic", "信息图", "visual summary", "可视化", or "高密度信息大图".
- **baoyu-markdown-to-html**: Converts Markdown to styled HTML with WeChat-compatible themes. Supports code highlighting, math, Mermaid (rendered to PNG via headless Chrome), PlantUML, footnotes, alerts, infographics, and optional bottom citations for external links. Use when user asks for "markdown to html", "convert md to html", "md 转 html", "微信外链转底部引用", or needs styled HTML output from markdown.
- **baoyu-post-to-wechat**: Posts content to WeChat Official Account (微信公众号) via API or Chrome CDP. Supports article posting (文章) with HTML, markdown, or plain text input, and image-text posting (贴图, formerly 图文) with multiple images. Markdown article workflows default to converting ordinary external links into bottom citations for WeChat-friendly output. Use when user mentions "发布公众号", "post to wechat", "微信公众号", or "贴图/图文/文章".
- **baoyu-post-to-weibo**: Posts content to Weibo (微博). Supports regular posts with text, images, and videos, and headline articles (头条文章) with Markdown input via Chrome CDP. Use when user asks to "post to Weibo", "发微博", "发布微博", "publish to Weibo", "share on Weibo", "写微博", or "微博头条文章".
- **baoyu-post-to-x**: Posts content and articles to X (Twitter). Supports regular posts with images/videos and X Articles (long-form Markdown). In Codex, honor explicit requests for the Codex Chrome plugin/@chrome by using the Chrome Extension workflow; otherwise use Chrome Computer Use when available and fall back to real Chrome CDP scripts only when allowed. Use when user asks to "post to X", "tweet", "publish to Twitter", or "share on X".
- **baoyu-slide-deck**: Generates professional slide deck images from content. Creates outlines with style instructions, then generates individual slide images. Use when user asks to "create slides", "make a presentation", "generate deck", "slide deck", or "PPT".
- **baoyu-translate**: This skill should be used when the user asks to "translate", "翻译", "精翻", "translate article", "translate to Chinese", "translate to English", "改成中文", "改成英文", "convert to Chinese", "localize", "本地化", "refined translation", "精细翻译", "proofread translation", "快速翻译", "快翻", "这篇文章翻译一下", or provides a URL/file with translation intent. Supports three modes (quick/normal/refined) with custom glossary support.
- **baoyu-url-to-markdown**: Fetch any URL and convert to markdown using baoyu-fetch CLI (Chrome CDP with site-specific adapters). Built-in adapters for X/Twitter, YouTube transcripts, Hacker News threads, and generic pages via Defuddle. Handles login/CAPTCHA via interaction wait modes. Use when user wants to save a webpage as markdown.
- **baoyu-wechat-summary**: Summarizes WeChat group chat highlights into a structured digest using the local wx-cli binary (https://github.com/jackwener/wx-cli). Generates a normal digest by default; a roast (毒舌) version is opt-in. Maintains per-group history (history.json + history-digests.jsonl), per-user profiles, and per-group fact memory (memory.md) across runs, with privacy guardrails baked in. Use when the user asks to "总结群聊", "群聊精华", "群聊摘要", "summarize group chat", "group chat digest", mentions a WeChat group name with a time range, says "帮我看看 XX 群最近聊了什么", "XX 群有什么值得看的", or asks to "回溯画像" / "初始化画像" / "backfill profiles". Adds the roast version when the user says "毒舌版", "roast 版", "再来个毒舌的", or similar.
- **baoyu-xhs-images**: Generates infographic image card series with 12 visual styles, 8 layouts, and 3 color palettes. Breaks content into 1-10 cartoon-style image cards optimized for social media engagement. Use when user mentions "小红书图片", "小红书种草", "小绿书", "微信图文", "微信贴图", "image cards", "图片卡片", baoyu-xhs-images, or wants social media infographic series.
- **baoyu-youtube-transcript**: Downloads YouTube video transcripts/subtitles and cover images by URL or video ID. Supports multiple languages, translation, chapters, and speaker identification. Caches raw data for fast re-formatting. Use when user asks to "get YouTube transcript", "download subtitles", "get captions", "YouTube字幕", "YouTube封面", "视频封面", "video thumbnail", "video cover image", or provides a YouTube URL and wants the transcript/subtitle text or cover image extracted.
- **release-skills**: Universal release workflow. Auto-detects version files and changelogs. Supports Node.js, Python, Rust, Claude Plugin, GitHub Releases, annotated tags, historical release backfill, and generic projects. Use when user says "release", "发布", "new version", "bump version", "push", "推送", "release notes", "GitHub Release", or "回填 Release".

## mattpocock/skills

- **code-review**: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
- **diagnosing-bugs**: Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.
- **edit-article**: Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.
- **git-guardrails-claude-code**: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
- **grill-me**: A relentless interview to sharpen a plan or design.
- **grill-with-docs**: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
- **handoff**: Compact the current conversation into a handoff document for another agent to pick up.
- **improve-codebase-architecture**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **migrate-to-shoehorn**: Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.
- **obsidian-vault**: Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian.
- **prototype**: Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
- **scaffold-exercises**: Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.
- **setup-matt-pocock-skills**: Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills.
- **setup-pre-commit**: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
- **tdd**: Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests.
- **teach**: Teach the user a new skill or concept, within this workspace.
- **to-spec**: Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
- **to-tickets**: Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — edges as text in one file per ticket locally, or native blocking links on a real tracker.
- **triage**: Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs.
- **writing-beats**: Writing, exploit — assemble raw material into a journey of beats, grounding each term before a beat leans on it.
- **writing-fragments**: Writing, explore — mine raw fragments, no structure yet.
- **writing-shape**: Writing, exploit — shape raw material into an article, paragraph by paragraph.

## nextlevelbuilder/ui-ux-pro-max-skill

- **ui-ux-pro-max**: UI/UX design intelligence for web and mobile. Searchable local database with 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon entries, 16 GSAP motion presets, and 25 chart types across 22 stacks (React, Next.js, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, JavaFX, WPF, WinUI, Avalonia, Uno Platform, UWP, Three.js, and HTML/CSS). Use when designing, building, or reviewing UI: pages, components, color schemes, typography, layout, accessibility, animation, or data visualization.

## openai/skills

- **hatch-pet**: Create, repair, validate, visually QA, and package Codex-compatible animated pets and pet spritesheets from character art, generated images, company or prospect brand cues, or visual references. Use when a user wants a lightweight-worker Codex pet workflow, a non-pixel custom pet style, a prospect or company mascot pet, or a full 8x9 animated pet atlas with transparent unused cells, QA contact sheets, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.
- **jupyter-notebook**: Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

## vercel-labs/skills

- **find-skills**: Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
