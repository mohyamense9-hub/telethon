import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# حفظ الرسائل مؤقتًا في قائمة
messages = []

@app.route("/")
def home():
    # صفحة HTML بسيطة تعرض كل الرسائل
    html = "<h1>Selva Panel Messages ✅</h1>"
    for msg in messages[::-1]:  # عرض الأحدث أولاً
        html += f"<p>{msg}</p><hr>"
    return render_template_string(html)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    msg = data.get("message")
    if msg:
        messages.append(msg)
        print("وصلت رسالة:", msg)
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
