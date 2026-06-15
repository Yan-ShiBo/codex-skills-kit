# Codex Skills Kit

这是我在 **2026-06-16** 使用的 Codex skills 与插件配置快照。仓库只保存来源、路径、版本和安装脚本，不重新分发第三方 skill 源码。

## 当前规模

- **85 个独立安装项**，来自 **12 个 GitHub 仓库**
- `~/.codex/skills` 中有 **148 个 SKILL.md 入口**
- `~/.agents/skills` 中有 **127 个 SKILL.md 入口**
- 两个目录合计 **145 个不重复 skill 名称**
- 插件缓存有 **72 个入口、57 个不重复名称**
- Codex 自带的 6 个系统 skills 只记录，不重复安装

数字不同是正常的：部分 skills 同时存在于 Codex 和通用 Agent 目录；`gstack` 一个安装项内部又包含大量子 skills；插件也可能同时缓存本地版和远程版。

## 一键安装

### Windows PowerShell

```powershell
irm https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/Yan-ShiBo/codex-skills-kit/main/install.sh | bash
```

安装完成后重启 Codex。

### 本地克隆后安装

```powershell
git clone https://github.com/Yan-ShiBo/codex-skills-kit.git
cd codex-skills-kit
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

```bash
git clone https://github.com/Yan-ShiBo/codex-skills-kit.git
cd codex-skills-kit
./install.sh
```

默认行为：

- 从原作者仓库下载固定 commit，保证快照可复现
- 已存在的 skill 不覆盖
- 尝试恢复 Codex 插件；需要登录或市场权限的连接器可能需要手动确认

常用参数：

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Latest
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Force
powershell -ExecutionPolicy Bypass -File .\install.ps1 -SkipPlugins
```

```bash
./install.sh --latest
./install.sh --force
./install.sh --skip-plugins
```

## 主要来源

| 来源 | 数量 | 内容 |
| --- | ---: | --- |
| `mattpocock/skills` | 29 | 工程、TDD、写作、规划与生产力 |
| `jimliu/baoyu-skills` | 22 | 图像、文章、翻译、社交平台发布 |
| `obra/superpowers` | 14 | 调试、TDD、计划执行与代码审查 |
| `anthropics/skills` | 7 | DOCX、PDF、PPTX、XLSX、MCP、前端和 Web 测试 |
| `hyhmrright/brooks-lint` | 6 | 架构、技术债、测试和代码质量审查 |
| 其他 7 个仓库 | 7 | gstack、学术研究、UI/UX、Markdown、CI 等 |

完整仓库与 commit 信息见 [REPOSITORIES.md](inventory/REPOSITORIES.md)。

## 仓库内容

- [SKILLS.md](inventory/SKILLS.md)：按上游仓库整理的完整 skill 名单与说明
- [PLUGINS.md](inventory/PLUGINS.md)：插件缓存中的 skills 与版本
- [REPOSITORIES.md](inventory/REPOSITORIES.md)：上游仓库、数量和固定 commit
- [install-manifest.json](manifest/install-manifest.json)：安装器使用的机器可读清单
- [skills-lock.json](inventory/skills-lock.json)：原始 `skills` CLI 锁文件快照
- `scripts/snapshot.py`：从本机 Codex 配置重新生成清单
- `scripts/verify.py`：校验清单完整性

## 安全与许可证

- 仓库不包含 API Key、Cookie、登录状态或本机绝对路径。
- 第三方 skills 始终从其原始 GitHub 仓库下载，并遵循各自许可证。
- 本仓库中的安装器和清单生成工具使用 MIT License。
- `-Force` 不直接删除旧 skill，而是将旧目录重命名为带时间戳的备份。
