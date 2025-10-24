# awesome-seu-tools

<p align="center">
  <img src="docs/assets/seu-logo.svg" alt="东南大学 SEU 灵感徽标" width="180" />
</p>

<p align="center"><em>以东南大学校徽为灵感的仓库标识，象征开放、协作与创新。</em></p>

> 汇总东南大学（SEU）师生常用的小工具、脚本与自动化示例，方便快速查找与复用。

## 目录
- [简介](#简介)
- [仓库结构](#仓库结构)
- [工具目录](#工具目录)
  - [如何登记新工具](#如何登记新工具)
- [快速开始](#快速开始)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 简介
本仓库按照用途分类整理了适用于东南大学校园场景的脚本、命令行工具、轻量 Web 项目与操作系统脚本。每个工具都带有独立的说明文档，便于在需要时快速找到可用方案，也欢迎贡献者基于模板持续扩展工具集。

## 仓库结构
```
.
├── README.md                # 仓库概览与工具总览
├── CONTRIBUTING.md          # 贡献流程与提交规范
├── docs/                    # 模板与扩展文档
│   └── TOOL_TEMPLATE.md     # 新工具说明文档模板
└── tools/                   # 具体工具与分类目录
    ├── README.md            # 分类说明与维护要求
    └── <category>/<tool>/   # 单个工具的资料与源码
```

## 工具目录
当前已收录的工具会按照分类展示，更多工具可通过 Pull Request 补充。

| 分类 | 工具 | 简介 | 维护者 | 入口 |
| --- | --- | --- | --- | --- |
| meta | awesome-seu-tools 工具索引 | 本仓库的定位、结构与维护方式说明，便于快速了解工具集。 | 社区维护 | [查看说明](tools/meta/awesome-seu-tools/README.md) |
| scripts | seuVisitor 校园访客预约助手 | 自动化辅助东南大学访客预约流程的命令行脚本集合。 | Zephyr596 / 社区维护 | [查看说明](tools/scripts/seu-visitor/README.md) |

### 如何登记新工具
1. 在 `tools/` 下选择或创建合适的分类目录（如 `scripts/`、`web/`、`windows/`、`linux/`、`meta/` 等）。
2. 新建 `<tool-name>/` 子目录，并依据 [`docs/TOOL_TEMPLATE.md`](docs/TOOL_TEMPLATE.md) 撰写工具文档与示例。
3. 将源码、依赖说明、示例或演示资源放入同一目录，必要时提供截图或录屏。
4. 在本 README 的“工具目录”表格中新增一行，补充分类、简介与维护者信息。
5. 按照贡献指南提交 Pull Request，并在 PR 中说明工具用途与验证方式。

## 快速开始
1. 克隆仓库并进入目录：
   ```bash
   git clone <repo-url>
   cd awesome-seu-tools
   ```
2. 浏览 `tools/` 目录或主 README，找到所需工具的文档与使用说明。
3. 按照工具文档中的依赖与运行步骤进行体验。

## 贡献指南
- 阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解提交流程、代码规范与注意事项。
- 欢迎提交新工具、改进现有工具或完善文档。
- 若发现问题，可通过 Issue 反馈并附上复现步骤或截图。

## 许可证
除非另有说明，本仓库中的内容均以 MIT 许可发布。
