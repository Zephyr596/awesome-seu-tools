# SEU-master-thesis LaTeX 模版

> 东南大学硕士研究生学位论文排版模版，支持学术型与专业型硕士论文撰写。

## 背景
- 解决的问题或使用场景：统一东南大学硕士学位论文的排版格式，避免手动调整版式、页眉页脚、封面信息等细节。
- 与东南大学相关的需求：遵循东南大学研究生院发布的《学位论文格式规定》，并提供独创性声明、授权书等学校要求的附件模版。

## 功能特性
- 完整的 XeLaTeX 编译链配置（XeLaTeX → BibTeX → MakeIndex → XeLaTeX ×2），输出符合学校规范的 PDF。
- 预置东南大学硕士论文常用章节结构、页边距、字体与目录样式，并兼顾学术型与专业型硕士差异。
- 集成 GB/T 7714-2015 参考文献著录格式，并提供示例 BibTeX 数据与手册。
- 附带 Windows (make.bat)、类 Unix (make.sh) 及 GNU Make 编译脚本，支持增量快速编译。

## 环境要求
- 操作系统：Windows、macOS 或任意 Linux 发行版。
- 依赖软件：完整的 TeX Live / MacTeX / MiKTeX 发行版（需包含 XeLaTeX、BibTeX、MakeIndex）。
- 可选：GNU Make（便于类 Unix 平台执行 `make` 增量编译）。

## 快速开始
```bash
# 1. 拉取或更新模版仓库（首次使用可通过下方脚本自动完成）
bash scripts/sync_from_upstream.sh

# 2. 进入模版目录并尝试编译示例论文
cd tools/latex/seu-master-thesis/upstream
./make.sh
```

```bash
# 或在 Windows PowerShell 中使用批处理脚本
cd tools\latex\seu-master-thesis\upstream
./make.bat
```

> **提示**：首次运行前请确保本地已安装 XeLaTeX 与相关字体，模板会在 `build/` 目录生成 PDF。

## 使用说明
1. 运行 `scripts/sync_from_upstream.sh` 将上游仓库同步到 `upstream/` 目录（需要可访问 GitHub 的网络环境）。
2. 阅读 `upstream/manual.pdf`，了解模板参数、章节示例与编译说明。
3. 在 `upstream/thesis.tex`（或对应主文件）中填写个人与论文信息，可通过 `cfg/` 目录修改封面字段。
4. 将章节内容按照模板示例放入 `chapters/` 目录，使用 `\input{}` 引入。
5. 使用 `make.sh`、`make.bat` 或 `make` 编译，必要时运行 `make clean` 清理缓存。
6. 参考 `bibliography/` 提供的示例 BibTeX，确保文献条目符合 GB/T 7714-2015 要求。

若需要额外指南，可结合模板自带的 `附件1-3`（东南大学官方格式说明、独创性声明、参考文献规范）进行核对。

## 常见问题
| 问题 | 解决方法 |
| --- | --- |
| 编译时提示缺少字体或宏包 | 通过 TeX Live Manager 或 MiKTeX Console 安装缺失宏包，或确认使用 XeLaTeX 引擎。 |
| 参考文献格式不符合要求 | 使用模板自带的 `seu.bst`（基于 GB/T 7714-2015）并确保在主文件中加载对应样式。 |
| 需要更新至上游最新版本 | 重新运行 `scripts/sync_from_upstream.sh`，脚本会以浅克隆方式同步 `main` 分支到 `upstream/` 目录。 |

## 维护信息
- 维护者：社区维护
- 参考链接：
  - [GitHub 仓库](https://github.com/TouchFishPioneer/SEU-master-thesis)
  - [项目主页（若有）](https://github.com/TouchFishPioneer)

## 许可
原项目以 GPL-3.0 许可发布。由于未直接分发模板源码，本目录保留脚本与文档，使用模板时请遵守上游许可条款。
