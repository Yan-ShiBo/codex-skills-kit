# Codex Skills Kit

一套可复现、可一键安装的 Codex 能力包，覆盖科研、编程、调试、测试、代码审查、产品设计、文档办公、数据处理、浏览器自动化、内容创作和发布工作流。

仓库记录当前可用的 skills、Codex 插件、上游来源和锁定版本，并提供 Windows、macOS 与 Linux 安装脚本。第三方 skill 源码仍从原作者仓库下载，本仓库不重新分发这些源码。

## 包含内容

当前快照日期为 **2026-07-18**：

- **61 个用户级顶层安装目标**，来自 **11 个 GitHub 上游仓库**
- 其中 `gstack` 是一个包含 59 个入口的完整技能套件，因此共可发现 **119 个用户 `SKILL.md` 条目**
- **6 个 Codex 系统技能**：图像生成、OpenAI 文档、插件创建、技能创建、技能安装和内部审查
- **16 个已配置 Codex 插件**，提供 GitHub、Figma、Office、浏览器、桌面控制、网站发布等集成能力
- 插件缓存快照包含 **131 个条目 / 114 个唯一名称**；实际启用状态以 Codex 配置为准

完整逐项清单：

- [用户与系统 skills](inventory/SKILLS.md)
- [Codex 插件 skills](inventory/PLUGINS.md)
- [上游仓库与锁定 commit](inventory/REPOSITORIES.md)

## 一键安装

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.sh | bash
```

安装完成后重启 Codex，使新 skills 进入下一次会话的可用技能列表。

## 能力地图

| 能力方向 | 主要 skills 与插件 | 可以完成的工作 |
| --- | --- | --- |
| 科研与学术 | `academic-research-suite`、`jupyter-notebook`、`planning-with-files`、Documents、PDF、Presentations | 文献综述、研究问题、实验规划、Notebook、论文起草、审稿、修订和成果汇报 |
| 软件研发 | `diagnosing-bugs`、`tdd`、`code-review`、`prototype`、`mcp-builder`、`frontend-design` | 需求澄清、原型、实现、调试、测试驱动开发、MCP 服务和前端开发 |
| 架构与质量 | `brooks-audit`、`brooks-debt`、`brooks-health`、`brooks-review`、`brooks-sweep`、`brooks-test` | 架构审计、技术债评估、测试质量、PR 审查和代码库健康报告 |
| 端到端交付 | `gstack` 的 59 个技能入口 | 从产品讨论、计划审查和实现，到 QA、发布、部署、监控和复盘 |
| 写作与知识管理 | `edit-article`、`writing-*`、`obsidian-vault`、`handoff`、`teach` | 文章构思、结构化写作、编辑、知识库管理、上下文交接和教学 |
| 图片与视觉内容 | `baoyu-image-gen`、`baoyu-diagram`、`baoyu-infographic`、`baoyu-comic`、`hatch-pet`、Imagegen | 图片、封面、图表、信息图、漫画、文章插图和 Codex 动画宠物 |
| UI/UX 与设计工具 | `ui-ux-pro-max`、`frontend-design`、Figma、Canva、BioRender、Hyperframes | UI 方案、设计系统、设计转代码、演示设计、科学插图和交互动效 |
| 文档与数据 | Documents、PDF、Presentations、Spreadsheets、`markdown-to-html`、`baoyu-markdown-to-html` | Word、PDF、PPT、Excel、Markdown、HTML 和结构化数据处理 |
| 浏览器与桌面自动化 | Chrome、Computer Use、`webapp-testing`、`baoyu-url-to-markdown` | 操作登录态网页、控制 Windows 应用、网页 QA、抓取和内容归档 |
| 内容发布 | `baoyu-post-to-wechat`、`baoyu-post-to-weibo`、`baoyu-post-to-x`、`release-skills`、Sites | 发布公众号、微博、X、GitHub Release 和网站 |
| GitHub 工作流 | GitHub 插件、`setup-pre-commit`、`git-guardrails-claude-code`、`triage` | Issue/PR 管理、CI 修复、评论处理、提交保护和发布变更 |

## 科研与 Notebook

### `academic-research-suite`

完整的研究到论文工作流，包括：

- 深度研究、文献综述、系统综述和 meta-analysis
- 研究问题、论文结构、摘要和章节起草
- 引用检查、学术诚信检查和格式转换
- 审稿人模拟、同行评审、返修信和编辑决定
- 实验计划、统计解释、复现验证和人类研究协议

### `jupyter-notebook`

用于创建、整理和编辑 `.ipynb`，提供干净 Notebook 模板与生成脚本，适合实验、探索、教程和可复现计算记录。

### 相关能力

- `planning-with-files`：使用文件维护复杂任务的计划、发现和进度
- Documents / PDF / Presentations：把研究结果整理为论文、报告、PDF 和演示文稿
- Spreadsheets / Visualize：分析实验表格、构建图表和交互式可视化
- `make-pdf`：把 Markdown 转成出版质量 PDF

## 软件工程与代码质量

### 开发、调试与测试

- `diagnosing-bugs`：为困难 bug 和性能回归建立可重复的诊断闭环
- `tdd`：按 red-green-refactor 完成功能或修复
- `code-review`：同时从仓库规范和需求规格两个维度审查变更
- `prototype`：用一次性原型回答设计或交互问题
- `webapp-testing`：使用 Playwright 验证 Web 应用、截图和浏览器日志
- `setup-pre-commit`：配置 Husky、lint-staged、格式化、类型检查和测试
- `git-guardrails-claude-code`：阻止高风险 Git 操作
- `mcp-builder`：使用 Python 或 TypeScript 构建 MCP Server
- `frontend-design`：构建具有明确视觉方向的前端界面

### Brooks 代码库质量套件

| Skill | 用途 |
| --- | --- |
| `brooks-audit` | 模块依赖、分层、循环引用和架构结构审计 |
| `brooks-debt` | 识别、分类并排序技术债与重构机会 |
| `brooks-health` | 汇总架构、技术债、测试和 PR 质量健康度 |
| `brooks-review` | 面向维护性、设计退化和代码异味的 PR 审查 |
| `brooks-test` | 测试覆盖、测试设计和测试代码质量审查 |
| `brooks-sweep` | 一次运行完整 Brooks 审计链 |

## gstack：59 个端到端研发技能

`gstack` 不是单一命令，而是一套覆盖产品、工程、设计、QA、发布和运维的工作流。`gstack` 本身负责路由，内部技能按用途分为：

| 分组 | 包含的 skills |
| --- | --- |
| 产品与计划 | `office-hours`、`spec`、`autoplan`、`plan-ceo-review`、`plan-design-review`、`plan-devex-review`、`plan-eng-review`、`plan-tune`、`gstack-openclaw-ceo-review`、`gstack-openclaw-office-hours` |
| 实现与交付 | `codex`、`review`、`ship`、`land-and-deploy`、`landing-report`、`canary`、`document-generate`、`document-release`、`make-pdf` |
| 调试、质量与安全 | `investigate`、`gstack-openclaw-investigate`、`health`、`benchmark`、`benchmark-models`、`devex-review`、`cso`、`careful`、`guard`、`freeze`、`unfreeze` |
| 设计 | `design-consultation`、`design-html`、`design-review`、`design-shotgun`、`diagram` |
| 浏览器与 QA | `browse`、`qa`、`qa-only`、`scrape`、`open-gstack-browser`、`pair-agent`、`setup-browser-cookies`、`hackernews-frontpage`、`skillify` |
| iOS | `ios-clean`、`ios-design-review`、`ios-fix`、`ios-qa`、`ios-sync` |
| 上下文、学习与配置 | `context-save`、`context-restore`、`learn`、`retro`、`gstack-openclaw-retro`、`setup-deploy`、`setup-gbrain`、`sync-gbrain`、`gstack-upgrade`、`gstack` |

## 写作、知识与项目规划

| Skill | 用途 |
| --- | --- |
| `writing-fragments` | 收集未经组织的素材和观点 |
| `writing-beats` | 把素材组织成读者经历的叙事节拍 |
| `writing-shape` | 按段落塑造文章结构 |
| `edit-article` | 重构、精简和润色已有文章 |
| `grill-me` | 通过连续追问澄清计划和设计 |
| `grill-with-docs` | 在追问过程中同步形成 ADR 与术语文档 |
| `to-spec` | 把当前讨论整理为可发布的规格说明 |
| `to-tickets` | 把规格拆成带依赖关系的垂直切片 tickets |
| `triage` | 分类、验证并形成适合代理执行的 Issue/PR 简报 |
| `handoff` | 把当前上下文压缩成可交接文档 |
| `obsidian-vault` | 搜索、创建和组织 Obsidian 笔记 |
| `teach` | 在当前工作区内讲解技能或概念 |
| `scaffold-exercises` | 创建课程练习、题目、答案和讲解结构 |
| `improve-codebase-architecture` | 扫描代码库并生成可视化架构改进报告 |

## 图片、内容与社交发布

Baoyu 技能组包含 22 个顶层安装目标：

| 分组 | 包含的 skills |
| --- | --- |
| 图片与视觉生成 | `baoyu-article-illustrator`、`baoyu-comic`、`baoyu-cover-image`、`baoyu-diagram`、`baoyu-image-gen`、`baoyu-infographic`、`baoyu-slide-deck`、`baoyu-xhs-images` |
| 获取与处理素材 | `baoyu-compress-image`、`baoyu-electron-extract`、`baoyu-youtube-transcript`、`baoyu-url-to-markdown`、`baoyu-danger-x-to-markdown` |
| 写作与转换 | `baoyu-format-markdown`、`baoyu-markdown-to-html`、`baoyu-translate`、`baoyu-wechat-summary` |
| 平台发布 | `baoyu-post-to-wechat`、`baoyu-post-to-weibo`、`baoyu-post-to-x`、`release-skills` |
| 生成后端 | `baoyu-danger-gemini-web` |

此外还包括：

- `hatch-pet`：生成、修复和打包 Codex 动画宠物 spritesheet
- `ui-ux-pro-max`：覆盖多种技术栈的 UI/UX 样式、配色、字体、可访问性、动效和图表知识库
- `markdown-to-html`：使用 CommonMark/GFM 等工作流把 Markdown 转成 HTML
- `find-skills`：继续发现和安装其他可用 skills

## Codex 系统技能

这些技能随 Codex 管理，不由安装器覆盖：

| Skill | 用途 |
| --- | --- |
| `imagegen` | 生成或编辑位图、插画、纹理和透明背景素材 |
| `openai-docs` | 查询 OpenAI 产品、API 和 Codex 官方文档 |
| `plugin-creator` | 创建 Codex 插件结构和 manifest |
| `skill-creator` | 创建或更新符合 Codex 约定的 skill |
| `skill-installer` | 从精选列表或 GitHub 仓库安装 skills |
| `review-agent` | 为其他代理提供只读、缺陷优先的代码审查 |

## 已配置的 Codex 插件

插件保留在 Codex 自己管理的插件目录中，不复制到用户 skills 目录。

| 插件 | 主要能力 |
| --- | --- |
| `github@openai-curated` | GitHub 仓库、Issue、PR、评论、CI 修复和发布变更 |
| `figma@openai-curated` | Figma 文件、组件库、FigJam、Slides、设计转代码和动效 |
| `canva@openai-curated` | 品牌演示、社交媒体尺寸适配和设计翻译 |
| `biorender@openai-curated` | 科研与生命科学插图工作流 |
| `hyperframes@openai-curated` | GSAP 动效、Hyperframes CLI/Registry 和网站转交互帧 |
| `nvidia@openai-curated` | NVIDIA AI-Q、Dynamo、cuOpt、NeMoClaw、Omniverse 与 Physical AI 工作流 |
| `chrome@openai-bundled` | 使用用户现有登录态和标签页控制 Chrome |
| `computer-use@openai-bundled` | 控制 Windows 桌面应用 |
| `documents@openai-primary-runtime` | 创建、编辑、审阅和批注 Word 文档 |
| `pdf@openai-primary-runtime` | 读取、创建、渲染和检查 PDF |
| `presentations@openai-primary-runtime` | 创建和编辑 PowerPoint/Google Slides |
| `spreadsheets@openai-primary-runtime` | 创建、分析和验证表格，并控制活动 Excel |
| `template-creator@openai-primary-runtime` | 创建可复用的个人或团队模板 |
| `visualize@openai-bundled` | 创建交互式图表、模拟器、地图和可视化工具 |
| `sites@openai-bundled` | 构建、保存和部署网站 |
| `superpowers@openai-curated` | brainstorming、计划、TDD、调试、并行代理、代码审查和分支收尾 |

插件的所有缓存技能名称和版本见 [PLUGINS.md](inventory/PLUGINS.md)。

## 完整的 61 个顶层安装目标

<details>
<summary>按上游仓库展开</summary>

### Imbad0202/academic-research-skills-codex

`academic-research-suite`

### anthropics/skills

`frontend-design`、`mcp-builder`、`webapp-testing`

### davila7/claude-code-templates

`planning-with-files`

### garrytan/gstack

`gstack`（内部展开为 59 个技能入口）

### github/awesome-copilot

`markdown-to-html`

### hyhmrright/brooks-lint

`brooks-audit`、`brooks-debt`、`brooks-health`、`brooks-review`、`brooks-sweep`、`brooks-test`

### jimliu/baoyu-skills

`baoyu-article-illustrator`、`baoyu-comic`、`baoyu-compress-image`、`baoyu-cover-image`、`baoyu-danger-gemini-web`、`baoyu-danger-x-to-markdown`、`baoyu-diagram`、`baoyu-electron-extract`、`baoyu-format-markdown`、`baoyu-image-gen`、`baoyu-infographic`、`baoyu-markdown-to-html`、`baoyu-post-to-wechat`、`baoyu-post-to-weibo`、`baoyu-post-to-x`、`baoyu-slide-deck`、`baoyu-translate`、`baoyu-url-to-markdown`、`baoyu-wechat-summary`、`baoyu-xhs-images`、`baoyu-youtube-transcript`、`release-skills`

### mattpocock/skills

`code-review`、`diagnosing-bugs`、`edit-article`、`git-guardrails-claude-code`、`grill-me`、`grill-with-docs`、`handoff`、`improve-codebase-architecture`、`migrate-to-shoehorn`、`obsidian-vault`、`prototype`、`scaffold-exercises`、`setup-matt-pocock-skills`、`setup-pre-commit`、`tdd`、`teach`、`to-spec`、`to-tickets`、`triage`、`writing-beats`、`writing-fragments`、`writing-shape`

### nextlevelbuilder/ui-ux-pro-max-skill

`ui-ux-pro-max`

### openai/skills

`hatch-pet`、`jupyter-notebook`

### vercel-labs/skills

`find-skills`

</details>

## 典型组合工作流

### 科研与论文

```text
academic-research-suite
  -> jupyter-notebook
  -> Spreadsheets / Visualize
  -> Documents / PDF / Presentations
```

### 从需求到发布

```text
grill-with-docs
  -> to-spec
  -> to-tickets
  -> tdd / diagnosing-bugs
  -> code-review
  -> release-skills 或 gstack ship
```

### 文章与社交内容

```text
baoyu-url-to-markdown
  -> baoyu-translate / edit-article
  -> baoyu-article-illustrator / baoyu-cover-image
  -> baoyu-markdown-to-html
  -> baoyu-post-to-wechat / weibo / x
```

### 设计到网站

```text
Figma / Canva / ui-ux-pro-max
  -> frontend-design
  -> webapp-testing
  -> Sites
```

## 安装目录

所有用户管理的 skills 都安装到 Codex 原生目录：

```text
~/.codex/skills/
├── academic-research-suite/
├── gstack/
├── jupyter-notebook/
├── ...
└── .system/                 # Codex 自己管理
```

其他目录：

```text
~/.codex/plugins/cache/      # Codex 插件 skills，由 Codex 管理
~/.codex/skill-backups/      # 强制更新或清理产生的可恢复备份
~/.agents/skill-backups/     # 旧 Agent skills 目录的可恢复备份
```

`~/.agents/skills` 不作为活动安装目录，避免同一 skill 被两个根目录重复发现。

## 更新、覆盖与清理

克隆仓库后可使用完整参数：

```powershell
git clone https://github.com/Yan-ShiBo/codex-skills-kit.git
cd codex-skills-kit
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Force -PruneRetired
python .\scripts\reconcile.py --apply
```

```bash
git clone https://github.com/Yan-ShiBo/codex-skills-kit.git
cd codex-skills-kit
./install.sh --force --prune-retired
python3 ./scripts/reconcile.py --apply
```

| 参数 | 作用 |
| --- | --- |
| `--force` / `-Force` | 使用清单锁定版本替换已有 skill，旧版本进入备份 |
| `--prune-retired` / `-PruneRetired` | 把已停止使用的顶层目标移出活动目录 |
| `--latest` / `-Latest` | 使用上游 `main`，适合尝试最新版本但不保证严格复现 |
| `--skip-plugins` / `-SkipPlugins` | 跳过 Codex 插件恢复 |
| `scripts/reconcile.py --apply` | 将旧 `.agents/skills` 安全迁移到 Codex 目录与备份区 |

## 仓库文件

| 文件 | 作用 |
| --- | --- |
| [inventory/SKILLS.md](inventory/SKILLS.md) | 125 个当前用户与系统 skill 条目的名称和说明 |
| [inventory/PLUGINS.md](inventory/PLUGINS.md) | 插件选择器、缓存版本和插件 skill 说明 |
| [inventory/REPOSITORIES.md](inventory/REPOSITORIES.md) | 11 个上游仓库及锁定 commit |
| [inventory/AUDIT.md](inventory/AUDIT.md) | 版本迁移、替代关系和维护记录 |
| [manifest/install-manifest.json](manifest/install-manifest.json) | 安装器读取的机器清单、哈希和插件选择器 |
| [manifest/selection-policy.json](manifest/selection-policy.json) | 当前能力组合的适用领域和维护规则 |
| [inventory/skills-lock.json](inventory/skills-lock.json) | 61 个顶层安装目标的来源、路径和文件哈希 |
| `scripts/install.py` | 跨平台安装器核心 |
| `scripts/snapshot.py` | 从当前 Codex 环境重新生成清单 |
| `scripts/reconcile.py` | 迁移旧目录并备份停止使用的 skills |
| `scripts/verify.py` | 校验数量、来源、哈希、目录和跨层冲突 |

## 可复现性与安全

- 每个上游仓库都锁定到 40 位 commit SHA。
- 安装清单记录每个目标目录的 SHA-256 内容哈希。
- ZIP 解包会拒绝路径越界。
- `-Force` 和清理操作会先把旧目录移到时间戳备份，不直接永久删除。
- 仓库不保存 API Key、Cookie、登录状态或本机绝对路径。
- 第三方 skills 遵循各自上游许可证；本仓库安装器和清单工具使用 MIT License。

版本替代与维护记录见 [AUDIT.md](inventory/AUDIT.md)，README 只介绍当前仓库能够提供的能力。
