# SEU Beamer Slide 幻灯片模板

> 东南大学 Beamer 幻灯片模板，适用于论文答辩、学术报告及校园活动展示，基于开源项目 [TouchFishPioneer/SEU-Beamer-Slide](https://github.com/TouchFishPioneer/SEU-Beamer-Slide)。

## 背景
- 东南大学师生在进行论文答辩、公开课或社团活动时，常常需要兼具学校视觉规范与现代设计感的幻灯片模板。
- 该项目提供了完整的 LaTeX/Beamer 模板与双语说明，覆盖从学术报告到活动展示的多种场景，并提供 Windows 与 Unix 系统的一键编译脚本。
- 将模板收录至工具集中，可方便校内成员在需要时快速下载、查看说明与同步上游更新。

## 功能特性
- 提供中文/英文双语示例页面，包含标题页、目录页、章节页与致谢页等常用版式。
- 预置东南大学校徽、主题配色与排版规范，保证视觉一致性。
- `make.bat` 与 `make.sh` 封装编译流程，Windows、macOS、Linux 用户均可一键构建 PDF 幻灯片。
- 附带 `content.tex` 示例，帮助首次使用者快速了解模板结构与常用命令。

## 环境要求
- 需要安装 LaTeX 发行版（推荐 [TeX Live](https://www.tug.org/texlive/) 2021 及以上版本）。
- 若需中文字体渲染，请确保系统已安装思源宋体/黑体或替换为本地可用字体。
- Git（可选）：用于通过同步脚本拉取或更新上游仓库。

## 快速开始
```bash
# 克隆模板至当前目录
./sync_upstream.sh

# 进入上游模板目录
cd upstream/SEU-Beamer-Slide

# 使用提供的编译脚本
./make.sh         # macOS / Linux
# 或
./make.bat        # Windows（在 PowerShell / CMD 中运行）
```

> 如果当前环境无法直接联网，也可以在联网的机器上手动下载压缩包后解压至 `upstream/SEU-Beamer-Slide/` 目录。

## 使用说明
1. 在 `content.tex` 中填写报告或答辩的实际内容，可根据示例替换章节标题、作者信息与页脚。
2. 若需自定义配色或字体，可编辑 `seuslide.sty` 中的主题配置，例如主色调、标题字体与页面背景。
3. 使用 `make.sh` 或 `make.bat` 编译 `main.tex`，生成 `output/main.pdf`。也可在 Overleaf 中新建项目并上传仓库文件进行在线编辑。
4. 生成的 PDF 即可用于答辩或展示，如需导出为图片可使用 `pdfcrop`、`pdfjam` 等工具进行进一步处理。

## 常见问题
| 问题 | 解决方法 |
| --- | --- |
| 编译时报中文字体缺失 | 在 `seuslide.sty` 中将 `\setCJKmainfont` 替换为本地已安装的字体，或安装思源宋体/黑体。 |
| 无法执行 `make.sh`/`make.bat` | 确认脚本具有可执行权限（`chmod +x make.sh`），Windows 用户可右键运行或通过命令行执行。 |
| 想在 Overleaf 使用模板 | 使用 README 中的 Overleaf 直链，或下载仓库 ZIP 后在 Overleaf 新建项目上传。 |

## 维护信息
- 维护者：社区协作（原作者：TouchFishPioneer）
- 参考链接：
  - [GitHub 仓库：TouchFishPioneer/SEU-Beamer-Slide](https://github.com/TouchFishPioneer/SEU-Beamer-Slide)
  - [Overleaf 模板入口](https://www.overleaf.com/latex/templates/seu-beamer-slide/)

## 许可
- 上游仓库使用 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html) 许可，遵循原作者授权范围。
- 本目录仅提供整合说明，除非另有说明，遵循 `awesome-seu-tools` 默认的 MIT 许可。
