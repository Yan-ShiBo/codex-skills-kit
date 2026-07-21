# Plugin Skill Inventory

- Configured plugin selectors: **16**
- Cached plugin skill entries: **132**
- Unique cached plugin skill names: **115**
- Generated: **2026-07-21**

## Configured plugins

- `biorender@openai-curated`
- `canva@openai-curated`
- `chrome@openai-bundled`
- `computer-use@openai-bundled`
- `documents@openai-primary-runtime`
- `figma@openai-curated`
- `github@openai-curated`
- `hyperframes@openai-curated`
- `nvidia@openai-curated`
- `pdf@openai-primary-runtime`
- `presentations@openai-primary-runtime`
- `sites@openai-bundled`
- `spreadsheets@openai-primary-runtime`
- `superpowers@openai-curated`
- `template-creator@openai-primary-runtime`
- `visualize@openai-bundled`

## Cached packages

Cache entries can include old or connector-specific variants; configuration is authoritative.

### chrome

`openai-bundled` / `26.715.52143` / **plugin configured**

- **control-chrome**: Control the user's Chrome browser for tasks that depend on existing Chrome state: tabs, logged-in sessions, or extensions. Prefer purpose-built connectors, APIs, or CLIs when available.

### chrome

`openai-bundled` / `latest` / **plugin configured**

- **control-chrome**: Control the user's Chrome browser for tasks that depend on existing Chrome state: tabs, logged-in sessions, or extensions. Prefer purpose-built connectors, APIs, or CLIs when available.

### computer-use

`openai-bundled` / `26.715.31925` / **plugin configured**

- **computer-use**: Control Windows apps from ChatGPT

### sites

`openai-bundled` / `0.1.30` / **plugin configured**

- **sites-building**: Use Sites to build websites, including landing pages, portfolios, dashboards, portals, trackers, hubs, and internal tools. Always use Sites when the project contains `.openai/hosting.json`.
- **sites-hosting**: Host websites with Sites. Always use after `sites-building`, and use for website publishing, deployment, hosting management, or projects containing `.openai/hosting.json`.

### visualize

`openai-bundled` / `1.0.12` / **plugin configured**

- **visualize**: Create visualizations and interactive tools in conversation. Use when asked to show how something works, make simulators or labs, maps, plots, charts or graphs, comparisons, scenarios, adjustable inputs, and exploration.

### canva

`openai-curated` / `d6169bef` / **plugin configured**

- **canva-branded-presentation**: Create on-brand Canva presentations from a brief, outline, existing Canva doc, or design link. Use when the user wants a branded slide deck, wants to turn notes into a presentation, or needs a presentation generated in Canva with the right brand kit and a clear slide plan.
- **canva-resize-for-all-social-media**: Resize a Canva design into standard social media formats and prepare export-ready results. Use when the user wants one Canva design adapted across multiple social platforms such as Facebook, Instagram, and LinkedIn, especially when they want all variants produced in one pass.
- **canva-translate-design**: Translate the text in a Canva design into another language while preserving the original layout as much as possible. Use when the user wants a localized or translated version of an existing Canva design and expects the original file to remain unchanged.

### figma

`openai-curated` / `d6169bef` / **plugin configured**

- **figma-code-connect**: Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.
- **figma-create-new-file**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard, /figma-create-new-file slides Q3 Review)
- **figma-generate-design**: Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, or any composed multi-section view in Figma from code or a description. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.
- **figma-generate-diagram**: MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
- **figma-generate-library**: Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.
- **figma-implement-motion**: Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design — user mentions "implement this motion", "add animation from Figma", "animate this component", provides a Figma URL whose node is animated, or when `get_design_context` returns motion data or instructs you to call `get_motion_context`.
- **figma-swiftui**: SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a Figma design into SwiftUI (design → code), or pushing SwiftUI views / screens / tokens back into a Figma file (code → design). Triggers on phrases like 'implement this Figma design in SwiftUI', 'build this screen in Swift', 'push this SwiftUI view to Figma', 'mirror my Swift code in a Figma file', or whenever a Figma URL appears alongside `.swift` files / an `.xcodeproj`. Routes to a direction-specific reference doc; loads alongside `figma-use` for the code → design path.
- **figma-use**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
- **figma-use-figjam**: This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
- **figma-use-motion**: Motion / animation context for the `use_figma` MCP tool — animating Figma nodes via manual keyframes, animation styles, easing, and timeline duration. Load alongside figma-use whenever a task involves adding, editing, or inspecting animation on a node.
- **figma-use-slides**: This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

### github

`openai-curated` / `d6169bef` / **plugin configured**

- **gh-address-comments**: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.
- **gh-fix-ci**: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.
- **github**: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.
- **yeet**: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.

### hyperframes

`openai-curated` / `d6169bef` / **plugin configured**

- **gsap**: GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), position parameter, labels, nesting, playback), and performance (transforms, will-change, quickTo). Use when writing GSAP animations in HyperFrames compositions.
- **hyperframes**: Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML. Use when asked to build any HTML-based video content, add captions or subtitles synced to audio, generate text-to-speech narration, create audio-reactive animation (beat sync, glow, pulse driven by music), add animated text highlighting (marker sweeps, hand-drawn circles, burst lines, scribble, sketchout), or add transitions between scenes (crossfades, wipes, reveals, shader transitions). Covers composition authoring, timing, media, and the full video production workflow. For CLI commands (init, lint, preview, render, transcribe, tts) see the hyperframes-cli skill.
- **hyperframes-cli**: HyperFrames CLI tool — hyperframes init, lint, inspect, preview, render, transcribe, tts, doctor, browser, info, upgrade, compositions, docs, benchmark. Use when scaffolding a project, linting, validating, inspecting visual layout in compositions, previewing in the studio, rendering to video, transcribing audio, generating TTS, or troubleshooting the HyperFrames environment.
- **hyperframes-registry**: Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, and registry discovery.
- **website-to-hyperframes**: Capture a website and create a HyperFrames video from it. Use when: (1) a user provides a URL and wants a video, (2) someone says "capture this site", "turn this into a video", "make a promo from my site", (3) the user wants a social ad, product tour, or any video based on an existing website, (4) the user shares a link and asks for any kind of video content. Even if the user just pastes a URL — this is the skill to use.

### linear

`openai-curated` / `2cb26e7b` / **cache only**

- **linear**: Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

### nvidia

`openai-curated` / `d6169bef` / **plugin configured**

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

### superpowers

`openai-curated` / `d6169bef` / **plugin configured**

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

### data-analytics

`openai-curated-remote` / `0.2.8-13ceeea1f599` / **cache only**

- **analyze-data-quality**: Assess whether structured data, query results, dashboards, or analytical evidence are trustworthy enough to use. Use when the task is to check data quality, reconcile conflicting sources or metric definitions, or decide whether evidence is safe to cite.
- **build-dashboard**: Build source-backed dashboards for monitoring performance, exploring drivers, or acting on product and business metrics. Use when the task needs a dashboard, scorecard, or monitoring view with clear metrics, filters, source definitions, and QA.
- **build-report**: Build polished analytical reports for executive, product, business, or technical audiences. Use when the task needs a durable answer-first narrative with evidence-backed findings, visuals or tables, caveats, and source context.
- **create-data-context**: Create, update, inspect, or repair Data Analytics semantic layers. Use when the user asks to save data context or create a semantic layer that future Data Analytics work can inspect and cite.
- **design-kpis**: Design KPI frameworks, metric definitions, targets, guardrails, and measurement plans for product or business decisions. Use when success metrics, drivers, guardrails, targets, or the measurement approach need to be defined or improved.
- **gather-business-context**: Gather business context from connected or provided sources so downstream analysis starts with the right framing. Use when an analytical question depends on missing context, such as what a metric means, what changed recently, or which sources should be checked. If the same prompt asks for diagnosis, recommendation, or a deliverable, gather context first and continue to the focused skill.
- **index**: Route Data Analytics plugin-level requests and broad analytics work to the right focused workflow. Use when Data Analytics is at-mentioned, or for analytics requests involving data, metrics, dashboards, reports, charts, notebooks, spreadsheets, KPIs, market sizing, or semantic layers.
- **jupyter-notebooks**: Create, edit, or validate reproducible SQL or Python notebooks. Use for notebooks, SQL/Python scratchpads, reproducible exploration, audit trails, or runnable companions where the analysis should be reviewable or rerunnable.
- **kpi-reporting**: Prepare KPI readouts, scorecards, WBR/MBR/QBR updates, and executive summaries from quantitative business or product metrics; use when the task is to report status, compare against targets, explain validated drivers, and state operating implications.
- **market-sizing**: Estimate market, segment, or opportunity size with transparent assumptions and uncertainty. Use for TAM/SAM/SOM, sizing scenarios, or comparing the scale of possible opportunities.
- **metric-diagnostics**: Diagnose why a metric changed or differs from expectation. Use when the task is to identify likely drivers of a metric movement, anomaly, gap, or discrepancy.
- **product-business-analysis**: Analyze product or business data to support a decision or recommendation. Use when a decision depends on metric-backed evidence, such as choosing a direction, prioritizing an opportunity, evaluating a change, segmenting users, sizing tradeoffs, or deciding what to do next.
- **publish-artifact-to-sites**: Publish a validated Data Analytics report or dashboard artifact through Sites. Use automatically for durable artifacts in any positively identified Work Mode when the full Sites lifecycle is callable, or in ChatGPT Desktop outside Work Mode only after an explicit Sites request or acceptance of the optional post-handoff sharing offer.
- **report-to-google-doc**: Narrow conversion skill. Invoke only when the user explicitly asks to convert an existing local or blob-hosted HTML analytics report into a Google Doc, DOCX, or shareable document.
- **report-to-google-slides**: Narrow conversion skill. Invoke only when the user explicitly asks to convert an existing HTML analytics report into a native Google Slides deck.
- **report-to-pdf**: Narrow conversion skill. Invoke only when the user explicitly asks to convert an existing Data Analytics report, dashboard, or inline chart export into a PDF artifact.
- **validate-data**: Validate whether an analysis is accurate, well-supported, and ready to share or use for a decision. Use when reviewing methodology, calculations, comparisons, visuals, caveats, or conclusions.
- **visualize-data**: Design, build, revise, or QA quantitative charts and figures. Use when an analytical answer needs visual judgment, whether for an inline answer, report, dashboard, notebook, or artifact.

### figma

`openai-curated-remote` / `2.0.16` / **plugin configured**

- **figma-code-connect**: Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.
- **figma-create-new-file**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard, /figma-create-new-file slides Q3 Review)
- **figma-design-to-code**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool. You MUST trigger this skill whenever the user wants to implement, build, port, or code up a Figma design as code. Example prompts (not exhaustive) are 'implement this Figma design', 'build this screen from Figma', 'turn this Figma into code', 'design to code'. This skill provides critical instructions and steps to the agent on how to correctly implement Figma designs in code and must NOT be skipped.
- **figma-generate-design**: Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, or any composed multi-section view in Figma from code or a description. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.
- **figma-generate-diagram**: MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
- **figma-generate-library**: Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.
- **figma-implement-motion**: Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design — user mentions "implement this motion", "add animation from Figma", "animate this component", provides a Figma URL whose node is animated, or when `get_design_context` returns motion data or instructs you to call `get_motion_context`.
- **figma-swiftui**: SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a Figma design into SwiftUI (design → code), or pushing SwiftUI views / screens / tokens back into a Figma file (code → design). Triggers on phrases like 'implement this Figma design in SwiftUI', 'build this screen in Swift', 'push this SwiftUI view to Figma', 'mirror my Swift code in a Figma file', or whenever a Figma URL appears alongside `.swift` files / an `.xcodeproj`. Routes to a direction-specific reference doc; loads alongside `figma-use` for the code → design path.
- **figma-use**: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
- **figma-use-figjam**: This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
- **figma-use-motion**: Motion / animation context for the `use_figma` MCP tool — animating Figma nodes via manual keyframes, animation styles, easing, and timeline duration. Load alongside figma-use whenever a task involves adding, editing, or inspecting animation on a node.
- **figma-use-slides**: This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.

### github

`openai-curated-remote` / `0.1.8-2841cf9749ae` / **plugin configured**

- **gh-address-comments**: Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.
- **gh-fix-ci**: Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.
- **github**: Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.
- **yeet**: Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.

### gmail

`openai-curated-remote` / `0.1.5` / **cache only**

- **gmail**: Manage Gmail inbox triage, mailbox search, thread summaries, action extraction, reply drafting, and email forwarding through connected Gmail data. Use when the user wants to inspect a mailbox or thread, search email with Gmail query syntax, summarize messages, extract decisions and follow-ups, prepare replies or forwarded messages, or organize messages with explicit confirmation before send, archive, delete, or label actions.
- **gmail-inbox-triage**: Triage a Gmail inbox into actionable buckets such as urgent, needs reply soon, waiting, and FYI using connected Gmail data. Use when the user asks to triage the inbox, rank what needs attention, find what still needs a reply, or separate important mail from noise.

### google-drive

`openai-curated-remote` / `0.1.10` / **cache only**

- **google-docs**: Prompt- and template-complete Google Docs creation and editing with explicit-instruction-authoritative structural preservation, including semantic roles, relationships, comparison dimensions, and instructed extensions; full-topology native-copy routing; source-grounded per-tab adaptation for past/example references; style-preserving hyperlink and table edits; canonical smart-chip-first authoring for dates and relevant supported people or Google resources; a file-backed advisory trusted read before existing-document writes; automatic protected-control awareness; direct connector APIs by default; DOCX-first import only when no supplied Google Doc template/reference constrains the output; and checked-in code mode only for exact native dropdown mutation. Use when Codex must create, edit, fill, adapt, redesign, or verify Google Docs without overriding explicit user/template instructions, adding unrequested document scope, or carrying stale reference facts into a new deliverable.
- **google-drive**: Use connected Google Drive as the single entrypoint for Drive, Docs, Sheets, and Slides work. Use when the user wants to find, fetch, organize, share, export, copy, or delete Drive files, or summarize and edit Google Docs, Google Sheets, and Google Slides through one unified Google Drive plugin.
- **google-drive-comments**: Write, reply to, and resolve Google Drive comments on Docs, Sheets, Slides, and Drive files with evidence-backed location context. Use when the user asks to leave comments, review a file with comments, respond to comment threads, or resolve Drive comments.
- **google-sheets**: Analyze and edit connected Google Sheets with range precision. Use when the user wants to create Google Sheets, find a spreadsheet, inspect tabs or ranges, search rows, plan formulas, create or repair charts, clean or restructure tables, write concise summaries, or make explicit cell-range updates.
- **google-slides**: Route Google Slides authoring requests and derive a design system from a native template or reference deck. Use this skill when the user provides an existing native Google Slides deck as a template, reference, or prior-period source, or asks to edit, update, repair, restyle, or clean up an existing native Google Slides deck. Use the Presentations skill instead for net-new presentation creation when no existing native Google Slides deck must be followed.

### openai-templates

`openai-curated-remote` / `0.1.0` / **cache only**

- **artifact-template-analytics-dashboard**: Create a spreadsheet using the Analytics Dashboard template and its retained reference file. Use when the user selects or names Analytics Dashboard. Monitor acquisition, engagement, retention, revenue, and conversion funnel KPIs with charts.
- **artifact-template-business-review**: Create a presentation using the Business Review template and its retained reference file. Use when the user selects or names Business Review. Review business performance, KPIs, segment results, strategic priorities, decisions, and outlook.
- **artifact-template-design-report**: Create a document using the Design Report template and its retained reference file. Use when the user selects or names Design Report. Produce design reports with an executive summary, key findings, implications, recommendations, and appendix.
- **artifact-template-experiment-analysis**: Create a document using the Experiment Analysis template and its retained reference file. Use when the user selects or names Experiment Analysis. Analyze experiments with hypotheses, methodology, results, interpretation, limitations, and next steps.
- **artifact-template-financial-budget**: Create a spreadsheet using the Financial Budget template and its retained reference file. Use when the user selects or names Financial Budget. Model actuals, budget and scenario forecasts, variances, cash runway, and departmental plans.
- **artifact-template-investment-committee-memo**: Create a document using the Investment Committee Memo template and its retained reference file. Use when the user selects or names Investment Committee Memo. Prepare investment committee memos with the thesis, transaction details, financial analysis, risks, and recommendation.
- **artifact-template-legal-memorandum**: Create a document using the Legal Memorandum template and its retained reference file. Use when the user selects or names Legal Memorandum. Draft legal memoranda with the issue, brief answer, relevant facts, analysis, and conclusion.
- **artifact-template-market-trends-report**: Create a presentation using the Market Trends Report template and its retained reference file. Use when the user selects or names Market Trends Report. Communicate market or industry trends, supporting evidence, implications, and recommended responses.
- **artifact-template-minimal-letterhead**: Create a document using the Minimal Letterhead template and its retained reference file. Use when the user selects or names Minimal Letterhead. Write professional business letters with sender, recipient, message, and signature fields in a minimal letterhead layout.
- **artifact-template-operating-calendar**: Create a spreadsheet using the Operating Calendar template and its retained reference file. Use when the user selects or names Operating Calendar. Plan annual and monthly operating milestones, campaigns, launches, deadlines, and recurring events.
- **artifact-template-operating-review**: Create a presentation using the Operating Review template and its retained reference file. Use when the user selects or names Operating Review. Run weekly operating reviews with scorecards, functional updates, risks, decisions, and action items.
- **artifact-template-project-kickoff**: Create a presentation using the Project Kickoff template and its retained reference file. Use when the user selects or names Project Kickoff. Align teams on project goals, scope, roles, milestones, risks, and the working model.
- **artifact-template-project-tracker**: Create a spreadsheet using the Project Tracker template and its retained reference file. Use when the user selects or names Project Tracker. Manage workstreams, tasks, owners, status, priority, dates, launch pulse, and a Gantt schedule.
- **artifact-template-sales-pipeline**: Create a spreadsheet using the Sales Pipeline template and its retained reference file. Use when the user selects or names Sales Pipeline. Track opportunities, stages, owners, deal sizes, probabilities, forecasts, next steps, and risks.
- **artifact-template-simple-dark-mode**: Create a presentation using the Simple Dark Mode template and its retained reference file. Use when the user selects or names Simple Dark Mode. Create clean dark-mode presentations with bold typography, simple sections, charts, and imagery.
- **artifact-template-simple-light-mode**: Create a presentation using the Simple Light Mode template and its retained reference file. Use when the user selects or names Simple Light Mode. Create clean light-mode presentations with spacious typography, simple sections, charts, and imagery.
- **artifact-template-strategy-memorandum**: Create a document using the Strategy Memorandum template and its retained reference file. Use when the user selects or names Strategy Memorandum. Present strategic context, choices, rationale, risks, milestones, and a clear recommendation.
- **artifact-template-system-design**: Create a document using the System Design template and its retained reference file. Use when the user selects or names System Design. Document system architecture, requirements, components, data flows, APIs, tradeoffs, and operational considerations.
- **artifact-template-team-alignment**: Create a presentation using the Team Alignment template and its retained reference file. Use when the user selects or names Team Alignment. Facilitate team offsites and planning with context, goals, priorities, decisions, and action items.
- **artifact-template-three-statement-forecast**: Create a spreadsheet using the Three-Statement Forecast template and its retained reference file. Use when the user selects or names Three-Statement Forecast. Build an integrated income statement, balance sheet, and cash flow forecast with assumptions, checks, and an executive summary.

### product-design

`openai-curated-remote` / `0.1.50` / **cache only**

- **audit**: Audit or critique a product flow, journey, workflow, funnel, onboarding path, checkout path, settings path, screen, or multi-step product experience by capturing screenshots first, then reporting UX, design, and accessibility findings inline from that evidence. Use Figma only when the user explicitly asks for a board. Use when the user asks to audit, review, critique, inspect, assess, analyze, evaluate, or give feedback on a product experience.
- **design-qa**: Internal prototype QA helper. Use only after a Product Design prototype, URL-to-code build, or image-to-code build has a source visual target and a rendered implementation to compare before handoff. Do not use for broad UX critique, design critique, product audits, or flow reviews; route those user-facing requests to audit.
- **get-context**: Mandatory design-brief gate for clarifying the product and outcome. Use before ideation, image-to-code builds, redesigns, or product UI work to clarify missing product information and play back the brief before proceeding.
- **ideate**: Generate image-based alternatives, remixes, or new design directions from a Product Design brief. Use when the user asks for design variants, visual exploration, remixes, or image-generated approaches from provided context.
- **image-to-code**: Implement a selected image, screenshot, mockup, or Image Gen reference as a faithful, responsive frontend.
- **index**: Use when Product Design is explicitly invoked, or when the user's main goal is to explore a design, research UX, audit or critique a flow, faithfully clone a visual source, check a built design, or share a prototype. Do not use Product Design for ordinary implementation unless the user explicitly asks for it.
- **research**: Run fast, source-grounded UX research on the highest-signal problems users are experiencing with a user-specified digital product. Use when the user asks to research user pain, UX friction, onboarding issues, docs/help problems, developer experience friction, support pain, product workflow issues, or current user complaints for a named product.
- **share**: Share a runnable prototype using the user's preferred deployment tool.
- **url-to-code**: Clone a live URL as a runnable frontend-only local app.
- **user-context**: Load or manage Product Design's saved user context. Use when the user asks to set up Product Design, get started, onboard, save product or design sources, see what Product Design remembers, update saved context, or remember Product Design preferences. Examples include product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, and general product/design notes.

### documents

`openai-primary-runtime` / `26.715.12143` / **plugin configured**

- **documents**: Create, edit, redline, and comment on `.docx`, Word, and Google Docs-targeted document artifacts inside the container, with a strict render-and-verify workflow. Use `render_docx.py` to generate page PNGs (and optional PDF) for visual QA, then iterate until layout is flawless before delivering the final document.

### pdf

`openai-primary-runtime` / `26.715.12143` / **plugin configured**

- **pdf**: Read, create, inspect, render, and verify PDF files where visual layout matters. Use Poppler rendering plus Python tools such as reportlab, pdfplumber, and pypdf for generation and extraction.

### presentations

`openai-primary-runtime` / `26.715.12143` / **plugin configured**

- **Presentations**: Create or edit PowerPoint or Google Slides decks

### spreadsheets

`openai-primary-runtime` / `26.715.12143` / **plugin configured**

- **Spreadsheets**: Create, edit, analyze, and verify standalone spreadsheet files or Google Sheets-ready workbooks, including .xlsx, .xls, .csv, and .tsv. Do not use for live controlling Microsoft Excel app or a live Excel session.
- **excel-live-control**: Control an open or active Microsoft Excel workbook through the ChatGPT add-in or connected session. Use when the user tags the Microsoft Excel app in Codex or follows up on an established live Excel task. Do not use for standalone spreadsheet files or Google Sheets.

### template-creator

`openai-primary-runtime` / `26.715.12143` / **plugin configured**

- **template-creator**: Create or update a reusable personal Codex artifact-template skill. Use when the user invokes $template-creator or asks in natural language to create a template using, from, or based on an attached Word document, PowerPoint presentation, or Excel workbook, or explicitly asks to edit or update a passed artifact-template skill. Do not use for one-off artifact creation from an existing template.
