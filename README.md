# MediaPipe Gesture VibeCoding

## 项目介绍

这是一个本地运行的浏览器手势交互演示项目。后端使用 Flask 提供页面，前端使用摄像头、MediaPipe Hands、MediaPipe Pose、Canvas 和 Three.js 实现实时手势控制。

主要功能：

- 模式 A：超长写字画布。右手控制笔迹，左手拖动画布，左手连续握拳两次切换画笔颜色。
- 模式 B：量子星云球。手势控制 Three.js 粒子球的缩放、旋转和镜头推进。
- 实时 HUD：显示手部骨骼、身体骨骼、摄像头状态、FPS、当前模式和手势状态。

## 技术栈

- Python 3
- Flask
- HTML / CSS / JavaScript
- Tailwind CSS CDN
- Three.js r128 CDN
- MediaPipe Hands CDN
- MediaPipe Pose CDN

## 安装方法

项目没有 `requirements.txt`。如果本机还没有 Flask，可以手动安装：

```powershell
python -m pip install flask
```

不要在没有确认的情况下安装其他新依赖。

## 启动方法

进入项目目录：

```powershell
cd C:\Users\YYY\Desktop\codex-project\MediaPipe-Gesture--VibeCoding_index_finger_write_light_bg_smooth\MediaPipe-Gesture--VibeCoding-main
```

启动 Flask：

```powershell
python app.py
```

浏览器打开：

```text
http://localhost:5001
```

首次打开时需要允许摄像头权限。建议使用 `localhost` 访问，因为浏览器摄像头 API 通常要求安全上下文。

## 测试方法

当前没有自动化测试。可以先做 Python 语法检查：

```powershell
python -m py_compile app.py
```

涉及前端和手势逻辑时，需要手动验证：

- 页面能正常加载。
- 摄像头权限请求正常。
- 模式 A 可以右手写字、左手拖动画布、左手连续握拳两次切换颜色。
- 模式 B 可以根据手的张开程度缩放星云球，可以左右挥手旋转，可以双手大幅张开进入球体内部。
- 骨骼 HUD 和控制面板显示正常。

## 目录说明

```text
MediaPipe-Gesture--VibeCoding-main/
  app.py
    Flask 入口文件，提供首页路由并启动本地服务。

  templates/index_v4.html
    前端主页面，包含 UI、样式、摄像头、MediaPipe、Canvas 绘制和 Three.js 交互逻辑。

  AGENTS.md
    协作规则、项目目标、技术栈、运行命令、测试命令、代码风格和禁止事项。

  TODO.md
    当前目标、已完成任务、待完成任务、当前问题和下一步计划。

  README.md
    项目介绍、安装方法、启动方法、测试方法和目录说明。
```

## 注意事项

- 前端依赖 CDN，离线时可能无法运行完整功能。
- Flask 监听端口是 `5001`。
- 后端只负责渲染页面，手势识别和视觉效果都在浏览器端完成。
- 修改代码前请先阅读 `AGENTS.md`、`TODO.md`、`README.md`。
