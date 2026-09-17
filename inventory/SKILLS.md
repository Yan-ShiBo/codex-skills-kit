# Installed Skills Inventory

- Active skill entries: **126**
- Unique skill names: **126**
- Generated: **2026-09-17**
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

- **academic-research-suite**: Plan academic research or experiments, review literature, and draft or review scholarly manuscripts using the relevant ARS workflow.

## Panniantong/agent-reach

- **agent-reach**: Retrieve social posts, video transcripts, feeds, or other platform content using Agent Reach backends; configure those backends when requested.

## anthropics/skills

- **frontend-design**: Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't read as templated defaults.
- **mcp-builder**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
- **webapp-testing**: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

## davila7/claude-code-templates

- **planning-with-files**: Maintain a durable plan and handoff for work spanning sessions or complex dependencies when persistent task state is useful.

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
- **gstack**: Select a gstack workflow when the user requests the suite or needs help choosing one of its workflows.
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
- **ship**: Prepare and publish the requested commit or PR using the repository's checks and release conventions. (gstack)
- **skillify**: Codify the most recent successful /scrape flow into a permanent browser-skill on disk. (gstack)
- **spec**: Turn vague intent into a precise, executable spec in five phases. (gstack)
- **sync-gbrain**: Keep gbrain current with this repo's code and refresh agent search guidance in CLAUDE.md. Wraps the gstack-gbrain-sync orchestrator with state (gstack)
- **unfreeze**: Clear the freeze boundary set by /freeze, allowing edits to all directories again. (gstack)

## github/awesome-copilot

- **markdown-to-html**: Convert Markdown to HTML using the repository's renderer and desired output style.

## hyhmrright/brooks-lint

- **brooks-audit**: Audit module dependencies and architectural boundaries when a codebase architecture assessment is requested.
- **brooks-debt**: Assess and prioritize technical debt with the Brooks taxonomy when a debt assessment is requested.
- **brooks-health**: Produce a codebase health assessment using Brooks architecture, debt, and testing evidence.
- **brooks-review**: Review a PR for architectural decay and maintenance risks using Brooks criteria.
- **brooks-sweep**: Run the combined Brooks architecture, debt, review, and test workflow when a codebase audit with automatic fixes is requested.
- **brooks-test**: Assess test quality, coverage of behavior, and reliability using Brooks review criteria.

## jimliu/baoyu-skills

- **baoyu-article-illustrator**: Analyzes article structure, identifies positions requiring visual aids, generates illustrations with Type × Style × Palette three-dimension approach. Use when user asks to "illustrate article", "add images", "generate images for article", or "为文章配图".
- **baoyu-comic**: Knowledge comic creator supporting multiple art styles and tones. Creates original educational comics with detailed panel layouts and batch-capable image generation. Use when user asks to create "知识漫画", "教育漫画", "biography comic", "tutorial comic", or "Logicomix-style comic".
- **baoyu-compress-image**: Compresses images to WebP (default) or PNG with automatic tool selection. Use when user asks to "compress image", "optimize image", "convert to webp", or reduce image file size.
- **baoyu-cover-image**: Generates article cover images with 5 dimensions (type, palette, rendering, text, mood) combining 11 color palettes and 7 rendering styles. Supports cinematic (2.35:1), widescreen (16:9), and square (1:1) aspects. Use when user asks to "generate cover image", "create article cover", or "make cover".
- **baoyu-danger-gemini-web**: Generates images and text via reverse-engineered Gemini Web API. Supports text generation, image generation from prompts, reference images for vision input, and multi-turn conversations. Use when other skills need image generation backend, or when user requests "generate image with Gemini", "Gemini text generation", or needs vision-capable AI generation.
- **baoyu-danger-x-to-markdown**: Converts X (Twitter) tweets and articles to markdown with YAML front matter. Uses reverse-engineered API requiring user consent. Use when user mentions "X to markdown", "tweet to markdown", "save tweet", or provides x.com/twitter.com URLs for conversion.
- **baoyu-diagram**: Create technical diagrams with the Baoyu SVG templates and export workflow when those formats are requested.
- **baoyu-electron-extract**: Extract resources or JavaScript from an installed Electron application's ASAR archive for authorized inspection.
- **baoyu-format-markdown**: Formats plain text or markdown files with frontmatter, titles, summaries, headings, bold, lists, and code blocks. Use when user asks to "format markdown", "beautify article", "add formatting", or improve article layout. Outputs to {filename}-formatted.md.
- **baoyu-image-gen**: Generate images through a specified Baoyu API provider or saved batch prompts when that backend is requested.
- **baoyu-infographic**: Generate professional infographics with 21 layout types and 22 visual styles. Analyzes content, recommends layout×style combinations, and generates publication-ready infographics. Use when user asks to create "infographic", "信息图", "visual summary", "可视化", or "高密度信息大图".
- **baoyu-markdown-to-html**: Converts Markdown to styled HTML with WeChat-compatible themes. Supports code highlighting, math, Mermaid (rendered to PNG via headless Chrome), PlantUML, footnotes, alerts, infographics, and optional bottom citations for external links. Use when user asks for "markdown to html", "convert md to html", "md 转 html", "微信外链转底部引用", or needs styled HTML output from markdown.
- **baoyu-post-to-wechat**: Publish an article or image post to a WeChat Official Account when the user requests publication.
- **baoyu-post-to-weibo**: Posts content to Weibo (微博). Supports regular posts with text, images, and videos, and headline articles (头条文章) with Markdown input via Chrome CDP. Use when user asks to "post to Weibo", "发微博", "发布微博", "publish to Weibo", "share on Weibo", "写微博", or "微博头条文章".
- **baoyu-post-to-x**: Publish a post or article to X using the configured Baoyu workflow when requested.
- **baoyu-slide-deck**: Generates professional slide deck images from content. Creates outlines with style instructions, then generates individual slide images. Use when user asks to "create slides", "make a presentation", "generate deck", "slide deck", or "PPT".
- **baoyu-translate**: Translate articles or files with optional glossaries and quick, normal, or publication-quality modes.
- **baoyu-url-to-markdown**: Fetch any URL and convert to markdown using baoyu-fetch CLI (Chrome CDP with site-specific adapters). Built-in adapters for X/Twitter, YouTube transcripts, Hacker News threads, and generic pages via Defuddle. Handles login/CAPTCHA via interaction wait modes. Use when user wants to save a webpage as markdown.
- **baoyu-wechat-summary**: Retrieve and summarize WeChat group conversations through an already configured wx-cli backend.
- **baoyu-xhs-images**: Generates infographic image card series with 12 visual styles, 8 layouts, and 3 color palettes. Breaks content into 1-10 cartoon-style image cards optimized for social media engagement. Use when user mentions "小红书图片", "小红书种草", "小绿书", "微信图文", "微信贴图", "image cards", "图片卡片", baoyu-xhs-images, or wants social media infographic series.
- **baoyu-youtube-transcript**: Retrieve a YouTube transcript and video metadata for a supplied video or transcript request.
- **release-skills**: Universal release workflow. Auto-detects version files and changelogs. Supports Node.js, Python, Rust, Claude Plugin, GitHub Releases, annotated tags, historical release backfill, and generic projects. Use when user says "release", "发布", "new version", "bump version", "push", "推送", "release notes", "GitHub Release", or "回填 Release".

## mattpocock/skills

- **code-review**: Review a specified diff, branch, or PR for behavioral regressions, missing requirements, and consequential test gaps.
- **diagnosing-bugs**: Diagnose a bug or performance regression using targeted evidence, a useful reproduction, and a verified fix.
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

- **ui-ux-pro-max**: Consult the UI/UX design catalog for interface styles, typography, color, or interaction choices when design guidance is needed.

## openai/skills

- **hatch-pet**: Create or repair a Codex desktop pet sprite sheet and its metadata, then validate the animation assets.
- **jupyter-notebook**: Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

## vercel-labs/skills

- **find-skills**: Find an installable skill when the user asks to discover or extend agent capabilities.
