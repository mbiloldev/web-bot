import os

from aiogram import Bot, Dispatcher, executor, types

import config
from foykey import foymenu
from keyboards import adminmenu
from config import BOT_TOKEN

bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum {message.from_user.full_name} botimga tashrif buyurganingizdan bag'oyatda xursandman !",
        reply_markup=foymenu),
    if message.from_user.id == int(6182560423):
        await message.answer_sticker('CAACAgIAAxkBAAMpZBAAAfUO9xqQuhom1S8wBMW98ausAAI4CwACTuSZSzKxR9LZT4zQLwQ')
        await message.answer(f'Assalomu alaykum adminstrator Muhammadbilol botga xush kelibsiz !',
                             reply_markup=adminmenu),


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Buyruqlar:\n/start - Botni ishga tushirish\n/help - Yordam")


@dp.message_handler(text="Ilovani yuklash 📲")
async def send_apk(message: Message):
    await message.answer_document('BQACAgIAAxkBAANTZg_ILpJtFKrqY5T5_U6NewgAATIWAAI7QgACpaVASKuWEly6brNENAQ',
                                  caption='Bu ilova faqat Android uchun !', )


@dp.message_handler(text="Admin-panel ilovasini yuklash ! 📲")
async def send_apk(message: Message):
    await message.answer_document('BQACAgIAAxkBAANVZg_IqiCmFz54vzg7Pxi8fHGMg4MAAvdHAAITD4FIvfIJsEoFiFI0BA',
                                  caption='Bu ilova faqat Android uchun !', )


@dp.message_handler(text='Saytni korish 💻')
async def send_photo(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIBR2YSWGGr5hFMCvonP-v1fzzlS1PrAAKm1TEbEw-BSOv2qBFWXQhjAQADAgADeQADNAQ',
                               caption='Web-siteniochish uchun tugmani bosing 👇', reply_markup=)


@dp.message_handler(text="Admin Panelni ko'rish 💻")
async def send_photo(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIBR2YSWGGr5hFMCvonP-v1fzzlS1PrAAKm1TEbEw-BSOv2qBFWXQhjAQADAgADeQADNAQ',
                               caption='Web-siteniochish uchun tugmani bosing 👇', reply_markup=admin)


executor.start_polling(dp, skip_updates=True)
