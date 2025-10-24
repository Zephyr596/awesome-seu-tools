# 贡献指南

欢迎贡献！请按照以下流程提交你的工具或改进：

1. Fork 仓库并新建分支：
   git checkout -b feat/<简短描述>

2. 在对应目录添加你的工具
   - tools/scripts/…（脚本）
   - tools/web/…（网页/前端）
   - tools/windows/…（Windows 脚本）
   - tools/linux/…（Linux 相关）

3. 在工具目录添加 README.md（说明用途、依赖、示例）
4. 编写清晰的提交信息（建议使用 Conventional Commits 风格）
5. 提交并发起 Pull Request

代码风格与规范
- Python：遵循 PEP8，尽量写文档字符串和简单的单元测试（可选）
- Shell：写注释并注明兼容的 shell（bash/zsh）
- 若涉及敏感信息（账号/密码/cookie），请勿提交到仓库

许可
本仓库默认使用 MIT 许可。提交即表示同意将代码在 MIT 许可下发布。
