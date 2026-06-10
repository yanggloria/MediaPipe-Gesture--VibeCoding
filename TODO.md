# TODO.md

## 当前目标

将完整项目发布到新建的 GitHub 仓库，并在发布阶段完成后记录远端仓库信息和验证结果。

## 已完成任务

- 已确认当前源码文件只有 `app.py` 和 `templates/index_v4.html`。
- 已确认项目是 Flask 提供静态模板，前端负责 MediaPipe 手势识别、Canvas 绘制和 Three.js 星云渲染。
- 已创建 `AGENTS.md`，记录项目目标、技术栈、目录结构、运行命令、测试命令、代码风格和禁止事项。
- 已创建基础 `README.md`，记录项目介绍、安装方法、启动方法、测试方法和目录说明。
- 已复查 `AGENTS.md`、`TODO.md`、`README.md`，确认覆盖用户要求。
- 已完成本轮任务开始前的 `AGENTS.md`、`TODO.md`、`README.md` 阅读。
- 已确认本机没有 `gh` CLI，改用 Composio GitHub 连接执行新建仓库和提交。
- 已完成 GitHub 连接授权，目标账号为 `yang081691-star`。
- 已新建私有 GitHub 仓库：`yang081691-star/MediaPipe-Gesture-VibeCoding`。
- 已尝试本机 `git push`，但 Windows Git 未获取到 GitHub 凭据，返回 `SEC_E_NO_CREDENTIALS`。
- 已确认继续使用已授权的 Composio GitHub API 上传完整项目文件。

## 待完成任务

- 将完整项目文件上传到仓库默认分支。
- 验证远端仓库文件结构。
- 发布完成后更新本文件，记录仓库 URL。

## 当前问题

- 项目没有 `requirements.txt`，运行前需要确认本机已安装 Flask。
- 前端依赖 CDN，离线环境下 Tailwind、Three.js、MediaPipe 可能无法加载。
- 摄像头权限通常要求通过 `localhost`、`127.0.0.1` 或 HTTPS 访问。
- 当前没有自动化前端测试，涉及手势体验的改动需要浏览器和摄像头手动验证。

## 下一步计划

通过 Composio GitHub API 将完整项目文件提交到 GitHub 仓库。
