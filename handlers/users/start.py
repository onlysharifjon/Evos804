from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("<b>EVOS | Доставка</b> botiga xush kelibsiz!")
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki +998XX XXXXXXX ko'rinishida yozing.

https://evos.uz/uz/about/    
    ''')

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    await message.reply(reply_markup=ReplyKeyboardRemove(), text='Telefon raqamingiz qabul qilindi✅')
    await message.answer('<b>🛒 Asosiy Menyu</b>')
    await message.answer('Marhamat buyurtma berishingiz mumkin!')

