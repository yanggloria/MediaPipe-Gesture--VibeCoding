from pathlib import Path

from flask import Flask, Response

app = Flask(__name__)


def apply_custom_version(html: str) -> str:
    """Apply the requested version on top of the original template.

    Version notes:
    - Index-finger-only writing instead of thumb-index pinch writing.
    - Smoother handwriting using quadratic curve smoothing.
    - Slightly lighter pink-purple writing background.
    - Other interface and features remain unchanged.
    """
    replacements = [
        (
            "vctx.fillStyle = 'rgba(5, 3, 20, 0.72)';",
            "vctx.fillStyle = 'rgba(12, 8, 34, 0.58)';",
        ),
        (
            "mainGlow.addColorStop(0, `rgba(251, 113, 194, ${0.42 + breath * 0.18})`);",
            "mainGlow.addColorStop(0, `rgba(251, 113, 194, ${0.32 + breath * 0.12})`);",
        ),
        (
            "mainGlow.addColorStop(0.35, `rgba(192, 80, 235, ${0.32 + breath * 0.14})`);",
            "mainGlow.addColorStop(0.35, `rgba(192, 80, 235, ${0.24 + breath * 0.10})`);",
        ),
        (
            "mainGlow.addColorStop(0.7, `rgba(88, 28, 135, ${0.22 + breath * 0.08})`);",
            "mainGlow.addColorStop(0.7, `rgba(88, 28, 135, ${0.15 + breath * 0.06})`);",
        ),
        (
            "gA.addColorStop(0, `rgba(244, 114, 182, ${0.35 + breath * 0.2})`);",
            "gA.addColorStop(0, `rgba(244, 114, 182, ${0.25 + breath * 0.14})`);",
        ),
        (
            "gA.addColorStop(0.6, `rgba(168, 85, 247, ${0.12 + breath * 0.1})`);",
            "gA.addColorStop(0.6, `rgba(168, 85, 247, ${0.08 + breath * 0.07})`);",
        ),
        (
            "gB.addColorStop(0, `rgba(139, 92, 246, ${0.30 + breath * 0.15})`);",
            "gB.addColorStop(0, `rgba(139, 92, 246, ${0.22 + breath * 0.10})`);",
        ),
        (
            "gB.addColorStop(0.5, `rgba(217, 70, 239, ${0.12 + breath * 0.1})`);",
            "gB.addColorStop(0.5, `rgba(217, 70, 239, ${0.08 + breath * 0.07})`);",
        ),
        (
            """            const indexTip = hand[8];
            const thumbTip = hand[4];
            
            // 2D 灵敏捏合检测
            const dx = indexTip.x - thumbTip.x;
            const dy = indexTip.y - thumbTip.y;
            const dist2D = Math.hypot(dx, dy);
            const rawPinching = dist2D < 0.045; // 稳定好写的阈值""",
            """            const indexTip = hand[8];
            const wrist = hand[0];
            const indexMcp = hand[5];
            const middleTip = hand[12];
            const middleMcp = hand[9];
            const ringTip = hand[16];
            const ringMcp = hand[13];
            const pinkyTip = hand[20];
            const pinkyMcp = hand[17];

            const distanceFromWrist = point => Math.hypot(point.x - wrist.x, point.y - wrist.y);
            const fingerRatio = (tip, mcp) => distanceFromWrist(tip) / Math.max(distanceFromWrist(mcp), 0.0001);
            const rawPinching =
                fingerRatio(indexTip, indexMcp) > 1.35 &&
                fingerRatio(middleTip, middleMcp) < 1.35 &&
                fingerRatio(ringTip, ringMcp) < 1.35 &&
                fingerRatio(pinkyTip, pinkyMcp) < 1.35;""",
        ),
        (
            """                dctx.save();
                dctx.beginPath();
                dctx.moveTo(lastPen.x, lastPen.y);
                dctx.lineTo(drawX, drawY);
                dctx.strokeStyle = inkColor;
                dctx.lineWidth = 6;
                dctx.shadowColor = inkShadowColor;
                dctx.shadowBlur = 8;
                dctx.stroke();
                dctx.restore();
                lastPen = { x: drawX, y: drawY };""",
            """                const smoothFactor = 0.5;
                const smoothX = lastPen.x + (drawX - lastPen.x) * smoothFactor;
                const smoothY = lastPen.y + (drawY - lastPen.y) * smoothFactor;
                const midX = (lastPen.x + smoothX) / 2;
                const midY = (lastPen.y + smoothY) / 2;

                dctx.save();
                dctx.beginPath();
                dctx.moveTo(lastPen.midX ?? lastPen.x, lastPen.midY ?? lastPen.y);
                dctx.quadraticCurveTo(lastPen.x, lastPen.y, midX, midY);
                dctx.strokeStyle = inkColor;
                dctx.lineWidth = 6;
                dctx.shadowColor = inkShadowColor;
                dctx.shadowBlur = 8;
                dctx.stroke();
                dctx.restore();
                lastPen = { x: smoothX, y: smoothY, midX, midY };""",
        ),
        (
            """        function isPinchingHand(hand) {
            if (!hand) return false;
            const indexTip = hand[8];
            const thumbTip = hand[4];
            const dist2D = Math.hypot(indexTip.x - thumbTip.x, indexTip.y - thumbTip.y);
            return dist2D < 0.045;
        }""",
            """        function isPinchingHand(hand) {
            if (!hand) return false;
            const wrist = hand[0];
            const indexTip = hand[8];
            const indexMcp = hand[5];
            const middleTip = hand[12];
            const middleMcp = hand[9];
            const ringTip = hand[16];
            const ringMcp = hand[13];
            const pinkyTip = hand[20];
            const pinkyMcp = hand[17];

            const distanceFromWrist = point => Math.hypot(point.x - wrist.x, point.y - wrist.y);
            const fingerRatio = (tip, mcp) => distanceFromWrist(tip) / Math.max(distanceFromWrist(mcp), 0.0001);

            return fingerRatio(indexTip, indexMcp) > 1.35 &&
                fingerRatio(middleTip, middleMcp) < 1.35 &&
                fingerRatio(ringTip, ringMcp) < 1.35 &&
                fingerRatio(pinkyTip, pinkyMcp) < 1.35;
        }""",
        ),
    ]

    for old, new in replacements:
        html = html.replace(old, new)
    return html


@app.route('/')
def index():
    template_path = Path(app.root_path) / 'templates' / 'index_v4.html'
    html = template_path.read_text(encoding='utf-8')
    return Response(apply_custom_version(html), mimetype='text/html; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
