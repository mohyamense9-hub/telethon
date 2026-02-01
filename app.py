from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    html = "<h2>Live Codes</h2>"
    for m in messages[::-1]:
        html += f"<pre>{m['time']}\n{m['text']}</pre><hr>"
    return html

@app.route("/push", methods=["POST"])
def push():
    text = request.json.get("text")
    messages.append({
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S")
    })
    return "OK"

app.run(host="0.0.0.0", port=10000)
