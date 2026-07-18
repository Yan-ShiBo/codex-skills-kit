# Codex Skills Kit

这是我在 **2026-07-18** 使用的 Codex skills 与插件配置快照。它针对 Python/PyTorch 科研、随机控制、强化学习、PAC 近似、SOS/形式化验证、可复现实验、Jupyter Notebook 和学术写作做了去重与筛选。

## 整理结果

- **61 个用户级顶层安装目标**，来自 **11 个 GitHub 上游仓库**
- 这些目标包含 **119 个可发现的用户 `SKILL.md` 条目**；加上 6 个 Codex 系统内置条目，本地活动清单共 **125 项**
- **16 个已启用 Codex 插件**，由 Codex 自己管理
- 插件缓存快照包含 **131 个条目 / 114 个唯一名称**；缓存可能保留旧版本，启用配置才是权威状态
- **30 个退役项**：4 个上游明确 deprecated、14 个 Superpowers 插件重复项、5 个其他插件替代项、7 个上游移除或改名项
- 新增 OpenAI 官方 `jupyter-notebook`
- 将 4 个旧入口更新为 `diagnosing-bugs`、`code-review`、`to-spec`、`to-tickets`
- 将 `hatch-pet` 归入正确的 `openai/skills` 上游来源

唯一的用户级活动安装目录是：

```text
~/.codex/skills
```

Codex 系统 skills 仍位于 `~/.codex/skills/.system`，插件 skills 仍位于 Codex 管理的插件缓存。本仓库不会把插件内容复制进用户级目录，也不使用 `~/.agents/skills` 作为活动目录。

退役清单只作用于 `~/.codex/skills/<name>` 顶层目标；例如当前 `gstack` 套件内部的 `qa`、`review` 仍属于该套件，不会被同名旧顶层入口的退役规则误删。

完整选择依据见 [selection-policy.json](manifest/selection-policy.json) 和 [AUDIT.md](inventory/AUDIT.md)。

## 一键安装

Windows PowerShell：

```powershell
irm https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.ps1 | iex
```

macOS / Linux：

```bash
curl -fsSL https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.sh | bash
```

安装器从原作者仓库下载清单锁定的 commit，并统一安装到 `~/.codex/skills`。默认不会覆盖已存在的同名 skill；插件按 best-effort 方式恢复。安装完成后重启 Codex。

## 更新与清理

克隆仓库后可以使用完整参数：

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

- `--force` / `-Force`：用锁定版本替换已有 skill。
- `--prune-retired` / `-PruneRetired`：将清单中的退役 skill 移出活动目录。
- `--latest` / `-Latest`：使用上游 `main`，会降低严格复现能力。
- `--skip-plugins` / `-SkipPlugins`：不尝试恢复插件。
- `scripts/reconcile.py --apply`：先补齐 `.agents/skills` 中仅存的项目，再将整个旧活动目录移入备份。

替换和清理不会永久删除旧文件。备份位于活动目录之外：

```text
~/.codex/skill-backups/<timestamp>/
~/.agents/skill-backups/<timestamp>/
```

这样 Codex 不会把备份误识别为重复 skills，必要时也可恢复。

## 筛选说明

现有 `academic-research-suite` 已覆盖深度研究、文献综述、论文写作、审稿、实验规划、统计解释和复现验证，因此没有继续加入高度重叠的 `scientific-writing`、`latex-paper-en` 或 `experiment-plan`。

OpenAI 官方 `jupyter-notebook` 提供可复现 Notebook 模板与辅助脚本，补足当前项目对薄 Notebook、清空输出和结构化实验入口的要求。通用 `python-testing-patterns` 虽然质量较高，但可能与项目更严格的远端串行执行、临时目录和 solver/GPU 边界冲突，因此没有加入全局配置。

上游已移除的 `caveman` 与 `zoom-out` 没有同义替代，未强行映射到行为不同的新 skill。`write-a-skill` 则由 Codex 内置 `skill-creator` 覆盖。

## 仓库内容

- [SKILLS.md](inventory/SKILLS.md)：当前 Codex 活动 skills
- [PLUGINS.md](inventory/PLUGINS.md)：已配置插件与缓存观察结果
- [REPOSITORIES.md](inventory/REPOSITORIES.md)：上游仓库和锁定 commit
- [AUDIT.md](inventory/AUDIT.md)：新增、替换、退役、去重和保留理由
- [install-manifest.json](manifest/install-manifest.json)：安装器使用的机器清单
- [selection-policy.json](manifest/selection-policy.json)：用户画像和筛选规则
- [skills-lock.json](inventory/skills-lock.json)：Codex 原生安装目标的可复现锁文件
- `scripts/snapshot.py`：重新生成清单
- `scripts/reconcile.py`：安全整理旧目录
- `scripts/verify.py`：校验清单与目录不变量

## 安全与许可证

- 清单不保存 API Key、Cookie、登录状态或本机绝对路径。
- 第三方 skills 从各自原始 GitHub 仓库下载，并遵循各自许可证。
- ZIP 解包会拒绝越界路径。
- 本仓库的安装器和清单工具使用 MIT License。
