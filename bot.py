from flask import Flask, request, jsonify
import pyotp
import json
import os

app = Flask(__name__)

# Load secrets mapping
SECRETS_FILE = 'secrets.json'
if not os.path.exists(SECRETS_FILE):
    raise RuntimeError(f"Missing {SECRETS_FILE}")
with open(SECRETS_FILE, 'r') as f:
    otp_secrets = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return "Lark 2FA Bot is up."

@app.route('/lark-webhook', methods=['POST'])
def lark_webhook():
    data = request.json

    try:
        user_msg = data['event']['text'].strip()
    except KeyError:
        return jsonify({"msg_type": "text", "content": {"text": "Không nhận tin nhắn được"}})

    if user_msg.lower().startswith("otp "):
        code = user_msg[4:].strip()
        secret = otp_secrets.get(code)
        if secret:
            totp = pyotp.TOTP(secret).now()
            reply = f"🔐 Mã 2FA cho '{code}' là: {totp}"
        else:
            reply = f"❌ Không tìm thấy mã 2FA cho '{code}'"
    else:
        reply = "📌 Gửi theo cú pháp: `otp <mã>`"

    return jsonify({
        "msg_type": "text",
        "content": {"text": reply}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
