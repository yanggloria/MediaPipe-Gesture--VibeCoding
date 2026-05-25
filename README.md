# MediaPipe Gesture VibeCoding

这是一个基于 Flask、MediaPipe Hands、MediaPipe Pose 和 Three.js 的网页端手势交互程序。

程序通过摄像头实时识别手部和身体关键点，实现手势写字、画布拖动、颜色切换和量子星云粒子交互等效果。

## 项目功能

- 摄像头实时识别手部关键点；
- 摄像头实时识别身体骨骼关键点；
- 模式 A：手势写字画布；
- 模式 B：量子星云球交互；
- 左手拖动画布翻页；
- 左手连续握拳两次切换画笔颜色；
- 双手张开、握拳、挥动控制星云球缩放、旋转和推进；
- 页面采用赛博科技风格界面。

## 当前仓库内容说明

本仓库目前包含两部分内容：

```text
MediaPipe-Gesture--VibeCoding/
├── app.py
├── README.md
├── templates/
│   └── index_v4.html
└── releases/
    └── MediaPipe-Gesture--VibeCoding_index_finger_write_smooth_original_bg.zip
```

### 1. 根目录代码

根目录中的 `app.py` 和 `templates/index_v4.html` 是 Flask 项目的基础运行结构。

`app.py` 使用 Flask 加载 `templates/index_v4.html`：

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_v4.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
```

### 2. 最终修改版压缩包

最终修改版已经打包保存在：

```text
releases/MediaPipe-Gesture--VibeCoding_index_finger_write_smooth_original_bg.zip
```

这个压缩包是当前项目的最终版本备份。

## 最终修改版说明

最终版本是在原始代码基础上完成的修改，主要改动如下：

### 1. 写字方式修改

原始版本：

- 需要大拇指和食指捏合才会进入写字状态。

最终版本：

- 改为只伸出食指即可写字；
- 使用食指指尖作为笔尖位置；
- 中指、无名指、小拇指收起时，程序判断为“食指写字状态”。

### 2. 写字轨迹优化

原始版本：

- 使用普通直线连接轨迹点；
- 快速移动时，字迹可能会出现折线感。

最终版本：

- 加入轨迹平滑处理；
- 使用二次贝塞尔曲线连接轨迹；
- 写字效果更加顺滑自然。

### 3. 背景画板颜色恢复

中间修改版本曾经将背景画板颜色调淡。

最终版本已经将背景画板颜色恢复为原来的深色粉紫效果，同时保留：

- 食指写字；
- 写字轨迹平滑；
- 原有左手翻页；
- 原有左手换颜色；
- 原有量子星云交互模式。

## 运行方法

先安装 Flask：

```bash
pip install flask
```

然后运行：

```bash
python app.py
```

浏览器打开：

```text
http://127.0.0.1:5001
```

首次打开时，需要允许浏览器访问摄像头。

## 使用说明

### 模式 A：写字画布

- 伸出右手食指：开始用食指指尖写字；
- 收起食指或不满足食指写字姿态：停止写字；
- 左手拖动：横向拖动画布；
- 左手连续握拳两次：切换画笔颜色；
- 点击“清除画迹”：清除当前绘制内容。

### 模式 B：量子星云球

- 单手张开 / 握拳：控制星云球大小；
- 双手张开：星云球放大，并推进进入星云核心；
- 手部左右挥动：控制星云球旋转。

## 技术栈

- Python
- Flask
- HTML / CSS / JavaScript
- MediaPipe Hands
- MediaPipe Pose
- Three.js
- Tailwind CSS CDN

## 注意事项

- 请使用 `127.0.0.1`、`localhost` 或 HTTPS 环境打开，否则浏览器可能禁止摄像头权限；
- 程序依赖 CDN 加载前端库，运行时需要联网；
- 如果摄像头无法启动，请检查浏览器权限和电脑摄像头占用情况。

## 修改记录

### 2026-05-24

- 从源项目复制 Flask 入口文件和前端模板文件；
- 修改写字触发方式：由“大拇指 + 食指捏合写字”改为“只伸食指写字”；
- 优化写字轨迹：加入平滑处理和二次贝塞尔曲线；
- 曾尝试将写字模式背景画板颜色调淡；
- 后续将背景画板颜色恢复为原来的深色粉紫效果；
- 上传最终版压缩包到 `releases/` 目录；
- 更新项目说明文档。
