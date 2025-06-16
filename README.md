# pythonanywhere
pythonantwhere網址:https://xaibai.pythonanywhere.com/
# 旅遊行程規劃網站教學

這個專案是一個基於 **Flask** 框架開發的簡易 **旅遊行程規劃網站**，網站整合了 **AI 助理**，可以幫助用戶規劃個性化的旅遊行程。用戶可以選擇旅遊天數、選擇景點並加入行程，並且與 **AI 助理** 互動，獲得旅遊建議和資訊。

## 目錄

1. [功能介紹](#功能介紹)
2. [技術架構](#技術架構)
3. [安裝與運行](#安裝與運行)
    - [前提條件](#前提條件)
    - [安裝依賴](#安裝依賴)
    - [配置 API 金鑰](#配置-api-金鑰)
    - [啟動 Flask 伺服器](#啟動-flask-伺服器)
4. [部署到PythonAnywhere](#PythonAnywhere)
    - [創建PythonAnywhere帳戶](#創建PythonAnywhere帳戶)
    - [創建新的Web](#創建新的Web)
    - [配置 WSGI 設定](#配置WSGI設定)
    - [上傳檔案到 PythonAnywhere](#上傳檔案到PythonAnywhere)
    - [配置靜態資源與模板](#配置靜態資源與模板)
    - [安裝所需的 Python 套件](#安裝所需的Python套件)
5. [更新 flask_app.py 和 API 金鑰配置](#更新flask_app.py和API金鑰配置)
    - [配置 GROQ API 金鑰](#配置GROQ_API金鑰)
    - [設置環境變數](#設置環境變數)
    - [配置 Google Maps API 金鑰](#配置Google_Maps_API金鑰)
    - [更新 itinerary.html 中的 Google 地圖嵌入](#更新itinerary.html中的Google地圖嵌入)
7. [程式碼結構](#程式碼結構)
    - [`flask_app.py`](#flask_apppy)
    - [`index.html`](#indexhtml)
    - [`itinerary.html`](#itineraryhtml)
8. [AI 助理介紹](#ai-助理介紹)
    - [如何與 AI 助理互動](#如何與-ai-助理互動)
9. [注意事項](#注意事項)
10. [常見問題與解決方案](#常見問題與解決方案)

---

## 功能介紹

這個旅遊行程規劃網站的功能有：

1. **首頁 (`index.html`)**
   - 用戶可以在首頁選擇他們希望的旅遊天數，並且根據選擇的天數進入行程規劃頁面。

2. **行程規劃 (`itinerary.html`)**
   - 用戶可以選擇他們想要的景點並加入他們的行程中。每個景點都顯示詳細的資訊（如描述、費用等），並且用戶可以選擇加入行程的天數。

3. **AI 助理 (AI 助理 API)**
   - AI 助理利用 Groq API 提供的 LLaMA 模型來與用戶進行對話，回答有關旅遊的問題或提供景點建議。

4. **地圖功能**
   - 每個景點都會顯示對應的 Google 地圖，讓用戶可以查看景點的位置，並進行導航。

---

## 技術架構

這個專案的技術架構如下：

- **後端框架**: Flask
  - 用於處理前端請求、渲染頁面和與 AI 助理進行交互。
  
- **前端技術**: 
  - HTML5: 用來構建頁面結構。
  - CSS: 用於頁面樣式設計，控制佈局和顏色。
  - JavaScript: 用於頁面的動態交互，如加入行程、與 AI 聊天等。

- **AI 助理技術**: 
  - 使用 Groq 提供的 LLaMA 模型 API 來實現聊天和旅遊建議功能。
  
- **地圖服務**: 
  - 使用 Google Maps Embed API 來嵌入景點地圖。

---

## 安裝與運行

### 前提條件

- 確保你的系統上已經安裝 **Python 3.x**。
- 你需要一個有效的 **Groq API 金鑰** 來使用 AI 助理。

### 安裝依賴

首先，創建一個虛擬環境來安裝所需的 Python 依賴：

```bash
python -m venv venv
```
啟動虛擬環境：
在 Windows 上：
```
venv\Scripts\activate
```
在 Mac/Linux 上：
```
source venv/bin/activate
```
然後安裝 Flask 和 Requests：
```
pip install flask requests
```
---
### 配置 API 金鑰
在 flask_app.py 中，你需要替換以下代碼中的 GROQ_API_KEY 為你從 Groq 獲得的 API 金鑰。找到這一行並進行替換：
```
GROQ_API_KEY = "你的Groq API金鑰"
```
### 啟動 Flask 伺服器
當所有依賴安裝完成並且 API 金鑰配置正確後，使用以下命令來啟動 Flask 伺服器：
```
python flask_app.py
```
伺服器啟動後，你可以在瀏覽器中訪問 http://localhost:5000 來查看網站。

---

### 部署 Flask 應用到 PythonAnywhere
這部分將指導你如何將你的 Flask 應用 部署到 PythonAnywhere，並配置 GROQ API 和 Google Maps API。
### 創建 PythonAnywhere 帳戶
1.訪問 PythonAnywhere 並註冊一個帳戶。
2.登入後，進入 Web 標籤頁面來創建新的 Web 應用。
### 創建新的 Web
1.在 Web 頁面中，點擊 Add a new web app 按鈕。
2.選擇 Flask 作為 Web 應用框架，並選擇你所使用的 Python 版本（建議選擇 Python 3.x）。
3.完成後，PythonAnywhere 會自動創建一個新的 Web 應用並提供一個初始配置。
### 配置 WSGI 設定
1.當你創建 Web 應用後，會看到一個配置頁面，找到 WSGI configuration file 並點擊。
2.打開這個 WSGI 配置文件，通常它位於 /var/www/yourusername_pythonanywhere_com_wsgi.py。
3.修改這個文件，指向你的 Flask 應用，像這樣：
```
import sys
path = '/home/yourusername/yourproject'  # 替換為你的專案目錄
if path not in sys.path:
    sys.path.insert(0, path)

from flask_app import app as application  # 替換為你的主 Python 檔案名稱
```

---

### 上傳檔案到 PythonAnywhere
1.進入 PythonAnywhere 的 Files 頁面，創建一個新的目錄來存放你的專案檔案，例如 
```
/home/yourusername/yourproject/
```
上傳以下檔案到該目錄：
1.flask_app.py（後端程式）
2.index.html（首頁）
3.itinerary.html（行程規劃頁面）
如果你有靜態資源（如 CSS），請創建一個 static 目錄並上傳相應的檔案。
### 配置靜態資源與模板
Flask 預期將靜態檔案（如 CSS 和 JavaScript）放在 static/ 目錄下，將模板檔案放在 templates/ 目錄下。確保你的目錄結構如下：
```
/home/yourusername/yourproject/
    flask_app.py
    /templates/
        index.html
        itinerary.html
    /static/
        /css/
            style.css
```
   - index.html 和 itinerary.html 放在 templates/ 資料夾中。
   - 如果有 CSS 文件，請將它們放在 static/css/ 資料夾中。
### 安裝所需的 Python 套件
在 PythonAnywhere 的 Consoles 頁面，打開一個新的 Bash 終端，並運行以下命令來安裝 Flask 和 Requests：
```
pip install --user flask requests
```
這將會在 PythonAnywhere 上安裝所需的 Python 套件。

---

## 更新 flask_app.py 和 API 金鑰配置
### 配置 GROQ API 金鑰
1.登入 GROQ 並創建帳戶，然後取得你的 GROQ API 金鑰。
2.在 PythonAnywhere 上配置環境變數，將 GROQ API 金鑰 存儲為環境變數。
設置環境變數：
   - 進入 PythonAnywhere 的 Web 頁面，找到 Environment Variables 部分。
   - 新增一個環境變數，名稱為 GROQ_API_KEY，並將它的值設為你的 GROQ API 金鑰。
在 flask_app.py 中讀取環境變數：
```
import os

# 讀取 GROQ API 金鑰
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# 確保 API 金鑰存在
if not GROQ_API_KEY:
    raise ValueError("GROQ API 金鑰未設置，請設定環境變數 'GROQ_API_KEY'")
```
### 配置 Google Maps API 金鑰
1.登入 Google Cloud Console 並創建專案。
2.啟用 Google Maps JavaScript API 和 Geocoding API，然後生成金鑰。
3.設置 Google Maps API 金鑰的環境變數：
   - 在 PythonAnywhere 的 Web 頁面，新增環境變數，名稱為 GOOGLE_MAPS_API_KEY，並將其值設為你從 Google Cloud Console 獲得的金鑰。
在 flask_app.py 中讀取 Google Maps API 金鑰：
```
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
```
### 更新 itinerary.html 中的 Google 地圖嵌入：
在 itinerary.html 中，將 iframe 的 src 屬性替換為使用 環境變數 動態生成的 Google Maps API 金鑰：
```
<iframe id="mapIframe" width="100%" height="300" loading="lazy" allowfullscreen
  referrerpolicy="no-referrer-when-downgrade"
  src="https://www.google.com/maps/embed/v1/place?key={{ GOOGLE_MAPS_API_KEY }}&q=陽明山國家公園"></iframe>
```
這樣，你就不需要將 API 金鑰硬編碼到 HTML 中，金鑰會從環境變數中動態讀取。
## 程式碼結構
這是專案中的主要程式碼結構：

### flask_app.py

這個檔案是網站的後端核心，負責處理請求並與 AI 助理進行交互。
```
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
```
這段程式碼實現了兩個功能：

1.渲染首頁 (/ 路由)。

2.接收來自前端的 AI 聊天請求，並將請求轉發到 Groq API 來獲取回答 (/api/ai-chat 路由)。

### index.html
首頁頁面，允許用戶選擇旅遊天數，並開始規劃行程。
```
<form action="itinerary.html" method="GET">
    <label for="days">請選擇旅遊天數：</label>
    <select name="days" id="days">
        <option value="1">1 天</option>
        <option value="2">2 天</option>
        <option value="3">3 天</option>
        <option value="4">4 天</option>
        <option value="5">5 天</option>
    </select>
    <button class="highlight-btn" type="submit">開始規劃</button>
</form>
```
### itinerary.html
行程規劃頁面，顯示所有景點，讓用戶選擇想要參加的景點並加入行程。
```
<div class="activity">
    <h3>陽明山國家公園</h3>
    <p>自然景觀優美，是著名的休閒勝地。</p>
    <p>費用：約 NT$800</p>
    <label>選擇天數：</label>
    <select class="day-select">
        <option value="1">第 1 天</option>
        <option value="2">第 2 天</option>
    </select>
    <button class="add-btn" data-name="陽明山國家公園" data-price="800">加入行程</button>
</div>
```
---

## AI 助理介紹
AI 助理是基於 Groq API 的 LLaMA 模型，它可以與用戶進行對話，根據用戶的需求提供景點推薦、旅遊建議等。

### 如何與 AI 助理互動
在行程規劃頁面，你可以與 AI 助理進行對話，AI 助理會根據你的問題給出回應。舉個例子：

用戶可以詢問：「有什麼台北的必去景點？」

AI 助理會根據你的問題，給出相關的建議或回答。
### 注意事項
API 金鑰：請記得替換 flask_app.py 中的 GROQ_API_KEY，這是 Groq API 的認證金鑰，沒有它 AI 助理無法運行。

網頁顯示：確保網頁的前端和後端能夠正確協同工作，所有的靜態資源（如 CSS 和 JavaScript）必須正確加載。

錯誤處理：如果在請求 AI 助理或加載頁面時遇到錯誤，可以檢查伺服器的日誌，或者檢查 API 是否可用。
### 常見問題與解決方案
1.無法連接到 AI 助理：
(1).請確保 API 金鑰正確並且 Groq API 沒有遇到故障。
2.前端無法顯示地圖：
(1).檢查 Google Maps API 的金鑰和配置，確保能正確嵌入地圖。
3.無法連接到 GROQ API:
(1).確保你在 flask_app.py 中正確設置了 GROQ API 金鑰。
(2).檢查你是否設置了環境變數 GROQ_API_KEY，並且 PythonAnywhere 上的網絡連接沒有被阻擋。
4. Google 地圖顯示錯誤
(1).確保你在 Google Cloud Console 中啟用了 Maps JavaScript API 和 Geocoding API，並且 API 金鑰設置正確。
(2).確保 API 金鑰在 PythonAnywhere 上設置為環境變數並正確加載。
5.API 金鑰洩漏
(1).永遠不要將 API 金鑰直接寫入程式碼中，使用環境變數來保護金鑰。
