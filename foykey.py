from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

foymenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Saytni ko'rish 💻"),
            KeyboardButton(text='Ilovani yuklash 📲'),
        ],
        [
            KeyboardButton(text='Saytni oching 📱', web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/")),
        ],
    ],
    resize_keyboard=True
)
