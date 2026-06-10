# AGENTS.md

## 项目目标

这个项目是一个本地运行的浏览器手势交互演示。Flask 只负责提供页面，前端通过摄像头、MediaPipe Hands、MediaPipe Pose 和 Three.js 实现两类体验：

- 模式 A：右手凌空写字，左手拖动超长画布并切换画笔颜色。
- 模式 B：用手势缩放、旋转并进入 Three.js 粒子星云球。

## 技术栈

- Python 3
- Flask
- HTML / CSS / JavaScript
- Tailwind CSS CDN
- Three.js r128 CDN
- MediaPipe Hands CDN
- MediaPipe Pose CDN
- Browser Web APIs：`getUserMedia`、Canvas 2D、WebGL、`requestAnimationFrame`

## 目录结构

```text
MediaPipe-Gesture--VibeCoding-main/
  app.py
  templates/
    index_v4.html
  AGENTS.md
  TODO.md
  README.md
```

## 运行命令

```powershell
cd C:\Users\YYY\Desktop\codex-project\MediaPipe-Gesture--VibeCoding_index_finger_write_light_bg_smooth\MediaPipe-Gesture--VibeCoding-main
python app.py
```

启动后访问：

```text
http://localhost:5001
```

## 测试命令

当前项目没有自动化测试。修改后至少执行：

```powershell
python -m py_compile app.py
```

涉及前端交互时，还需要在浏览器手动验证：

- `http://localhost:5001` 能正常打开。
- 浏览器能请求摄像头权限。
- 模式 A 能识别右手写字、左手拖动画布、左手连续握拳两次切换颜色。
- 模式 B 能缩放、旋转星云球，双手大幅张开时能进入粒子球内部。
- 控制面板、骨骼 HUD、FPS 状态不遮挡主要画面。

## 代码风格

- 保持 Flask 后端简单，除非明确需要，不要把前端逻辑迁入后端。
- 前端目前是单文件原生 JavaScript，修改时优先遵循现有函数和状态变量组织方式。
- Canvas 层级要保持清晰：WebGL 背景、摄像头画面、写字轨迹、HUD 骨骼层各司其职。
- 手势阈值、帧率节流、画布尺寸和视觉透明度属于体验敏感参数，修改时要说明原因。
- UI 文案目前以中文为主，可以保留中英混排的科技终端风格。
- 添加注释时只解释不直观的手势、坐标或渲染逻辑，避免重复代码字面含义。

## 每次任务开始前必须阅读

每次开始新任务时，先阅读以下文件：

```text
AGENTS.md
TODO.md
README.md
```

## 修改流程

- 修改代码前，先给出简短计划。
- 每完成一个阶段后，更新 `TODO.md`。
- 修改完成后，说明改了哪些文件、为什么改、如何测试。
- 如果无法测试，要明确说明原因。

## 禁止事项

- 不要擅自安装新依赖。
- 不要擅自大规模重构。
- 不要擅自删除、移动或重命名核心文件。
- 不要擅自改变端口、路由、摄像头权限策略或 CDN 来源。
- 不要把密钥、账号、个人隐私信息写入项目。
- 不要执行破坏性 Git 操作，除非用户明确要求。
- 不要提交、推送或创建 PR，除非用户明确要求。
