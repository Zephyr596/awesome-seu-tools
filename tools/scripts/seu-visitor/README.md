# seuVisitor 校园访客预约助手

> 自动化辅助东南大学访客预约流程的脚本工具，基于社区项目 [Zephyr596/seuVisitor](https://github.com/Zephyr596/seuVisitor)。

## 背景
- 东南大学访客预约流程通常需要通过 "智慧东大" 小程序或网页反复填写表单，手工处理既耗时又容易出错。
- 社区项目 [Zephyr596/seuVisitor](https://github.com/Zephyr596/seuVisitor) 提供了批量化处理脚本，并配套了浏览器油猴脚本辅助表单填写。
- 本目录收录了常用的自动化脚本与用户脚本，并进一步改造为**本地 JSON 配置**版本，避免额外部署数据库。

## 功能特性
- `auto_local.py`：使用 Selenium 批量提交访客预约表单，访客信息存放于本地 JSON 文件。
- `run_with_logging.sh`：在 Linux 环境下执行自动化脚本并写入执行日志，方便定时任务监控。
- `seuVisitor.user.js`：油猴脚本，一键在浏览器中填充预约表单，适合临时手工操作。
- `sync_upstream.sh`：按需同步原仓库源码，了解最新实现或继续扩展功能。

## 环境要求
- Python 3.9 及以上版本。
- 已安装 Chrome/Chromium 浏览器与对应版本的 Chromedriver。
- 依赖包：`selenium`（建议使用虚拟环境管理依赖）。

```bash
cd tools/scripts/seu-visitor
python -m venv .venv
source .venv/bin/activate
pip install selenium
```

## 准备访客信息
1. 复制模板文件并填写个人信息：
   ```bash
   cp user_info_template.json user_info.json
   ```
2. 将 `user_info.json` 中的占位内容替换为真实数据。可配置多个 `profiles`，脚本会逐个提交。
3. 根据需要调整 `card` 字段（如一卡通号、工作证号），便于在理由描述中引用。

> **提示**：`user_info.json` 存放敏感个人信息，请妥善保管，并避免提交至公共仓库。

## 运行自动化脚本
```bash
# 默认读取当前目录下的 user_info.json，并启用 Headless 模式
python auto_local.py

# 指定配置文件并在前台打开浏览器窗口
python auto_local.py --profiles /path/to/user_info.json --no-headless

# 搭配日志脚本，适用于 cron 任务
./run_with_logging.sh --profiles /path/to/user_info.json
```

脚本执行完成后，会在终端输出每个账号的处理状态；如使用 `run_with_logging.sh`，额外在 `log.txt` 中记录成功或失败。

## 油猴脚本使用方法
1. 在浏览器安装 Tampermonkey 或 Violentmonkey 扩展。
2. 通过“创建新脚本”将 `seuVisitor.user.js` 的内容复制粘贴进去并保存。
3. 手动填写脚本顶部的变量（车牌、宿舍、导员信息等），随后打开预约表单即可自动填充。

## 同步上游源码（可选）
若需了解原项目的完整实现，可在可联网环境运行：

```bash
./sync_upstream.sh
```

同步成功后，上游源码会存放至 `tools/scripts/seu-visitor/upstream/` 目录。

## 常见问题
| 问题 | 解决方法 |
| --- | --- |
| ChromeDriver 版本不匹配 | 访问 [Chrome for Testing](https://chromedriver.chromium.org/downloads) 下载与本地浏览器版本一致的驱动，放入 `PATH` 中。 |
| Selenium 启动失败 | 确认机器上已安装 Chrome/Chromium，必要时在 `auto_local.py` 中自定义驱动路径。 |
| 表单字段 ID 变化 | 预约系统升级后可能调整控件 ID，可根据浏览器开发者工具更新脚本中的 XPath。 |
| 多人批量提交需求 | 在 `user_info.json` 中维护多条 `profiles` 数据，脚本会依次提交。 |

## 维护信息
- 维护者：社区协作（原作者：Zephyr596）
- 参考链接：
  - [GitHub 仓库：Zephyr596/seuVisitor](https://github.com/Zephyr596/seuVisitor)
  - [东南大学访客预约平台](https://visitor.seu.edu.cn/)（需校内访问）

## 许可
- 上游仓库采用的许可以其 README/LICENCE 为准。
- 本目录整合内容遵循 `awesome-seu-tools` 默认的 MIT 许可。
