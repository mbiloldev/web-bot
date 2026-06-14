from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

adminmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Saytni korish 💻'),
            KeyboardButton(text="Admin Panelni ko'rish 💻"),
        ],
        [
            KeyboardButton(text='Web-site oching 📱', web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/")),
            KeyboardButton(text='Web-site admin panelni oching 👨‍💻',web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/admin/login/?next=/admin/"))

        ],
        [
            KeyboardButton(text='Ilovani yuklash 📲'),
            KeyboardButton(text='Admin-panel ilovasini yuklash ! 📲')
        ],

    ],
    resize_keyboard=True
)
