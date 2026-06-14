# 🤖 Web-Bot

> Saytingiz bilan foydalanuvchilar o'rtasida ko'prik bo'luvchi aqlli Telegram bot.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=flat-square&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 Loyiha haqida

**Web-Bot** — bu shaxsiy veb-sayt bilan Telegram o'rtasida integratsiya qiluvchi bot. Saytdan kelgan so'rovlarni qabul qiladi, qayta ishlaydi va real vaqtda Telegram orqali javob beradi. Saytingizni **24/7 jonli va interaktiv** qiladi.

---

## ✨ Imkoniyatlar

- 🌐 **Sayt integratsiyasi** — veb-sayt bilan webhook orqali bog'lanish
- 📩 **Avtomatik javoblar** — foydalanuvchi so'rovlariga tezkor javob
- 🔔 **Real-time bildirishnomalar** — saytdagi yangiliklar haqida xabar
- 🛡️ **Xavfsizlik** — token asosida autentifikatsiya
- ⚡ **Tez va ishonchli** — async arxitektura

---

## 🛠️ Texnologiyalar

| Texnologiya | Maqsad |
|-------------|--------|
| `Python 3.10+` | Asosiy dasturlash tili |
| `aiogram` / `python-telegram-bot` | Telegram Bot API |
| `FastAPI` / `Flask` | Webhook server |
| `aiohttp` | Asinxron HTTP so'rovlar |
| `dotenv` | Muhit o'zgaruvchilari |

---

## 🚀 O'rnatish

### 1. Reponi klonlash

```bash
git clone https://github.com/username/web-bot.git
cd web-bot
```

### 2. Virtual muhit yaratish

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Kerakli paketlarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. `.env` faylini sozlash

```bash
cp .env.example .env
```

`.env` faylini oching va quyidagi qiymatlarni kiriting:

```env
BOT_TOKEN=your_telegram_bot_token
WEBHOOK_URL=https://yourdomain.com/webhook
SECRET_KEY=your_secret_key
PORT=8000
```

### 5. Botni ishga tushirish

```bash
python main.py
```

---

## ⚙️ Sozlash

### Webhook ulash

```bash
python setup_webhook.py
```

### Polling rejimida ishga tushirish (test uchun)

```bash
python main.py --polling
```

---

## 📁 Loyiha tuzilmasi

```
web-bot/
├── 📄 main.py              # Asosiy fayl
├── 📄 config.py            # Sozlamalar
├── 📄 requirements.txt     # Paketlar ro'yxati
├── 📄 .env.example         # Muhit o'zgaruvchilari namunasi
├── 📁 handlers/            # Bot handlerlari
│   ├── start.py
│   ├── messages.py
│   └── webhook.py
├── 📁 utils/               # Yordamchi funksiyalar
│   ├── logger.py
│   └── helpers.py
└── 📁 tests/               # Testlar
    └── test_bot.py
```

---

## 🔗 Sayt bilan integratsiya

Saytingizdan botga so'rov yuborish uchun:

```javascript
// JavaScript (frontend)
fetch('https://yourdomain.com/webhook', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    event: 'new_message',
    data: { name: 'Ali', message: 'Salom!' }
  })
});
```

```python
# Python (backend)
import requests

requests.post('https://yourdomain.com/webhook', json={
    'event': 'new_message',
    'data': {'name': 'Ali', 'message': 'Salom!'}
})
```

---

## 🧪 Testlar

```bash
pytest tests/ -v
```

---

## 📋 Muhit talablari

- Python **3.10** yoki undan yuqori
- Telegram Bot Token ([BotFather](https://t.me/BotFather) orqali oling)
- HTTPS domenli server (webhook uchun)

---

## 🤝 Hissa qo'shish

Pull request va issue'lar xush kelibsiz! Katta o'zgarishlar uchun avval `issue` oching.

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/yangi-imkoniyat`)
3. O'zgarishlarni commit qiling (`git commit -m 'feat: yangi imkoniyat qo'shildi'`)
4. Push qiling (`git push origin feature/yangi-imkoniyat`)
5. Pull Request oching

---

## 📄 Litsenziya

Bu loyiha [MIT](LICENSE) litsenziyasi ostida tarqatiladi.

---

## 📬 Muallif

**Sizning ismingiz** — [@it_mentor_uz](https://t.me/it_mentor_uz)

⭐ Agar loyiha foydali bo'lsa, **star** bosishni unutmang!
