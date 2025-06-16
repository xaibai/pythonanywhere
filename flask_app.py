from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 首頁：渲染你的旅遊網站
@app.route('/')
def index():
    return render_template('index.html')

# AI 助理 API（包 Groq）
@app.route('/api/ai-chat', methods=['POST'])
def ai_chat():
    user_message = request.json.get("message")

    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    GROQ_API_KEY = "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"  # ← 請替換

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "你是一個旅遊行程規劃助理，請用繁體中文回答。"},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    try:
        res = requests.post(GROQ_API_URL, headers=headers, json=payload)
        data = res.json()
        reply = data['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ 錯誤：{str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
