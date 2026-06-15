# Plugin Skill Inventory

- Cached plugin skill entries: **72**
- Unique plugin skill names: **57**
- Generated: **2026-06-16**

Cache entries can include local and remote variants of the same plugin.

## browser

`openai-bundled` / `26.602.40724`

- **control-in-app-browser**: Control the in-app Browser. Use to open, navigate, inspect, test, click, type, screenshot, or verify local targets such as localhost, 127.0.0.1, ::1, file://, the current in-app browser tab, and websites shown side by side inside Codex.

## chrome

`openai-bundled` / `26.602.40724`

- **control-chrome**: Control the user's Chrome browser for tasks that depend on existing Chrome state: tabs, logged-in sessions, cookies, or extensions. Prefer purpose-built connectors, APIs, or CLIs when available.

## computer-use

`openai-bundled` / `26.602.40724`

- **computer-use**: Control Windows apps from Codex

## canva

`openai-curated` / `c6ea566d`

- **canva-branded-presentation**: Create on-brand Canva presentations from a brief, outline, existing Canva doc, or design link. Use when the user wants a branded slide deck, wants to turn notes into a presentation, or needs a presentation generated in Canva with the right brand kit and a clear slide plan.
- **canva-resize-for-all-social-media**: Resize a Canva design into standard social media formats and prepare export-ready results. Use when the user wants one Canva design adapted across multiple social platforms such as Facebook, Instagram, and LinkedIn, especially when they want all variants produced in one pass.
- **canva-translate-design**: Translate the text in a Canva design into another language while preserving the original layout as much as possible. Use when the user wants a localized or translated version of an existing Canva design and expects the original file to remain unchanged.

## figma

`openai-curated` / `c6ea566d`

- **figma-code-connect**: Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.
- **figma-create-new-file**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard, /figma-create-new-file slides Q3 Review)
- **figma-generate-design**: Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, or any composed multi-section view in Figma from code or a description. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.
- **figma-generate-diagram**: MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
- **figma-generate-library**: Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.
- **figma-use**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
- **figma-use-figjam**: This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
- **figma-use-slides**: This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

## github

`openai-curated` / `c6ea566d`

- **gh-address-comments**: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.
- **gh-fix-ci**: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.
- **github**: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.
- **yeet**: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.

## hyperframes

`openai-curated` / `c6ea566d`

- **gsap**: GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), position parameter, labels, nesting, playback), and performance (transforms, will-change, quickTo). Use when writing GSAP animations in HyperFrames compositions.
- **hyperframes**: Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML. Use when asked to build any HTML-based video content, add captions or subtitles synced to audio, generate text-to-speech narration, create audio-reactive animation (beat sync, glow, pulse driven by music), add animated text highlighting (marker sweeps, hand-drawn circles, burst lines, scribble, sketchout), or add transitions between scenes (crossfades, wipes, reveals, shader transitions). Covers composition authoring, timing, media, and the full video production workflow. For CLI commands (init, lint, preview, render, transcribe, tts) see the hyperframes-cli skill.
- **hyperframes-cli**: HyperFrames CLI tool — hyperframes init, lint, inspect, preview, render, transcribe, tts, doctor, browser, info, upgrade, compositions, docs, benchmark. Use when scaffolding a project, linting, validating, inspecting visual layout in compositions, previewing in the studio, rendering to video, transcribing audio, generating TTS, or troubleshooting the HyperFrames environment.
- **hyperframes-registry**: Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, and registry discovery.
- **website-to-hyperframes**: Capture a website and create a HyperFrames video from it. Use when: (1) a user provides a URL and wants a video, (2) someone says "capture this site", "turn this into a video", "make a promo from my site", (3) the user wants a social ad, product tour, or any video based on an existing website, (4) the user shares a link and asks for any kind of video content. Even if the user just pastes a URL — this is the skill to use.

## linear

`openai-curated` / `2cb26e7b`

- **linear**: Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

## nvidia

`openai-curated` / `c6ea566d`

- **aiq-deploy**: Use when asked to install, deploy, run, validate, troubleshoot, or stop NVIDIA AI-Q Blueprint infrastructure.
- **aiq-research**: Use when asked to run deep research or AI-Q research through a reachable NVIDIA AI-Q Blueprint backend.
- **cuopt-user-rules**: Base rules for end users calling NVIDIA cuOpt (routing/LP/MILP/QP/install/server). Not for cuOpt internals — use cuopt-developer for those.
- **dynamo-interconnect-check**: Validate that a Dynamo deployment's NIXL/UCX/NCCL interconnect is ready for disaggregated serving over RDMA/NVLink. Use after recipe-runner brings a deployment up (especially disagg/multi-node) to confirm the KV transport is correct; use troubleshoot for diagnosing already-failed pods.
- **dynamo-router-starter**: Start or patch Dynamo router modes and run router endpoint smoke checks. Use for round-robin, KV-aware, least-loaded, or device-aware routing setup; use recipe-runner for recipe deployment and troubleshoot for failure diagnosis.
- **nemoclaw-user-get-started**: Installs NemoClaw, launches a sandbox, and runs the first agent prompt. Use when onboarding, installing, or launching a NemoClaw sandbox for the first time. Trigger keywords - nemoclaw quickstart, install nemoclaw openclaw sandbox, nemohermes quickstart, hermes agent nemoclaw, run hermes openshell sandbox, nemoclaw prerequisites, nemoclaw supported platforms, nemoclaw hardware software, nemoclaw windows wsl2 setup, nemoclaw install windows docker desktop.
- **omniverse-cad-to-simready**: Coordinate the end-to-end CAD/source-asset to SimReady workflow. Use for broad requests such as CAD to SimReady, source asset to simulation-ready USD, or prop packaging that require conversion, material/physics assignment, SimReady conformance, validation, and optional package creation; deploy or verify Content Agents services first when property assignment is enabled; route single-stage work through nested references.
- **omniverse-realtime-viewer**: Use as the top-level router for Omniverse Realtime Viewer USD app requests and focused viewer reference documents.
- **omniverse-usd-performance-tuning**: Top-level workflow skill for USD performance diagnosis and optimization. Use for slow loading, high memory, low FPS, or 'optimize my scene' requests; delegates auth/runtime setup to Phase 0 owners.
- **physical-ai-infrastructure-setup-and-resilient-scaling**: Use when the user wants to set up, scale, validate, or harden NVIDIA physical AI infrastructure for synthetic data generation workflows across local MicroK8s or Azure AKS, including Kubernetes clusters, inference endpoint deployment, OSMO deployment, workload submission readiness, and infrastructure failure recovery. Trigger keywords: physical ai infrastructure, resilient scaling, SDG infrastructure, microk8s, azure aks, NVCF deployment, NIM Operator, OSMO deploy, workflow scaling. Don't trigger for: OSMO log summarization or workload-only operations unless infrastructure setup, scaling, validation, or recovery is requested.
- **physical-ai-neural-reconstruction**: Router for NVIDIA NuRec/NRE: USDZ rendering, NCore conversion, 3DGS, gRPC sensor sim, PhysicalAI HF datasets. Do NOT use for SimReady or infra setup.

## superpowers

`openai-curated` / `c6ea566d`

- **brainstorming**: You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.
- **dispatching-parallel-agents**: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
- **executing-plans**: Use when you have a written implementation plan to execute in a separate session with review checkpoints
- **finishing-a-development-branch**: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup
- **receiving-code-review**: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
- **requesting-code-review**: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
- **subagent-driven-development**: Use when executing implementation plans with independent tasks in the current session
- **systematic-debugging**: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **test-driven-development**: Use when implementing any feature or bugfix, before writing implementation code
- **using-git-worktrees**: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback
- **using-superpowers**: Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions
- **verification-before-completion**: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
- **writing-plans**: Use when you have a spec or requirements for a multi-step task, before touching code
- **writing-skills**: Use when creating new skills, editing existing skills, or verifying skills work before deployment

## canva

`openai-curated-remote` / `1.0.2`

- **canva-branded-presentation**: Create on-brand Canva presentations from a brief, outline, existing Canva doc, or design link. Use when the user wants a branded slide deck, wants to turn notes into a presentation, or needs a presentation generated in Canva with the right brand kit and a clear slide plan.
- **canva-resize-for-all-social-media**: Resize a Canva design into standard social media formats and prepare export-ready results. Use when the user wants one Canva design adapted across multiple social platforms such as Facebook, Instagram, and LinkedIn, especially when they want all variants produced in one pass.
- **canva-translate-design**: Translate the text in a Canva design into another language while preserving the original layout as much as possible. Use when the user wants a localized or translated version of an existing Canva design and expects the original file to remain unchanged.

## figma

`openai-curated-remote` / `2.0.9`

- **figma-code-connect**: Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.
- **figma-create-new-file**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard, /figma-create-new-file slides Q3 Review)
- **figma-generate-design**: Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, or any composed multi-section view in Figma from code or a description. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.
- **figma-generate-diagram**: MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
- **figma-generate-library**: Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.
- **figma-use**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
- **figma-use-figjam**: This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
- **figma-use-slides**: This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

## github

`openai-curated-remote` / `0.1.2`

- **gh-address-comments**: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.
- **gh-fix-ci**: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.
- **github**: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.
- **yeet**: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.

## google-drive

`openai-curated-remote` / `0.1.6`

- **google-docs**: Connector-first Google Docs creation and editing in local Codex plugin sessions, with direct native create and batchUpdate workflows for simple docs, DOCX-first import for polished deliverables, target-document checks, smart chip and building-block reconstruction, connector-readback verification, and reference routing for formatting, citations, tables, and write-safety.
- **google-drive**: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work. Use when the user wants to find, fetch, organize, share, export, copy, or delete Drive files, or summarize and edit Google Docs, Google Sheets, and Google Slides through one unified Google Drive plugin.
- **google-drive-comments**: Write, reply to, and resolve Google Drive comments on Docs, Sheets, Slides, and Drive files with evidence-backed location context. Use when the user asks to leave comments, review a file with comments, respond to comment threads, or resolve Drive comments.
- **google-sheets**: Analyze and edit connected Google Sheets with range precision. Use when the user wants to create Google Sheets, find a spreadsheet, inspect tabs or ranges, search rows, plan formulas, create or repair charts, clean or restructure tables, write concise summaries, or make explicit cell-range updates.
- **google-slides**: Google Slides work for finding, reading, summarizing, creating, importing, template following, visual cleanup, source-deck adaptation, structural repair, and content edits in native Slides decks.

## documents

`openai-primary-runtime` / `26.601.10930`

- **documents**: Create, edit, redline, and comment on `.docx`, Word, and Google Docs-targeted document artifacts inside the container, with a strict render-and-verify workflow. Use `render_docx.py` to generate page PNGs (and optional PDF) for visual QA, then iterate until layout is flawless before delivering the final document.

## presentations

`openai-primary-runtime` / `26.601.10930`

- **Presentations**: Build PowerPoint PPTX decks with artifact-tool presentation JSX

## spreadsheets

`openai-primary-runtime` / `26.601.10930`

- **Spreadsheets**: Use this skill when a user requests to create, modify, analyze, visualize, or work with spreadsheet files (`.xlsx`, `.xls`, `.csv`, `.tsv`) or Google Sheets-targeted spreadsheet artifacts with formulas, formatting, charts, tables, and recalculation.
