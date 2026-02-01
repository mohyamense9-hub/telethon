import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Server is running ✅"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    print("وصلت رسالة:", data)   # هتظهر في Logs بتاعة Railway

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
