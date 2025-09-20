echo "# Lark 2FA Bot

Bot đơn giản cho Lark Chat:

- Nhận tin nhắn: \`otp <mã riêng>\`
- Tìm mã bí mật tương ứng trong \`secrets.json\`
- Sinh mã TOTP hiện tại và trả về trong chat

## Cài đặt

1. Clone repo  
   \`\`\`bash
   git clone https://github.com/atmedia161/lark-2fa-bot.git
   cd lark-2fa-bot
   \`\`\`

2. Tạo môi trường ảo và cài thư viện  
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   \`\`\`

3. Điền file \`secrets.json\` với các mã riêng và secret tương ứng.

4. Chạy bot  
   \`\`\`bash
   python bot.py
   \`\`\`

5. Public server bằng \`ngrok\` hoặc deploy lên dịch vụ cloud có hỗ trợ HTTPS.

6. Tạo Custom Bot trong Lark, cấu hình webhook URL trỏ tới \`https://your-ngrok-url/lark-webhook\`, bật nhận tin nhắn.

7. Thêm bot vào nhóm chat, test gửi tin nhắn: \`otp 1234\`

## \`secrets.json\`

\`\`\`json
{
  \"1234\": \"JBSWY3DPEHPK3PXP\",
  \"5678\": \"NB2W45DFOIZA====\"
}
\`\`\`
" > README.md
