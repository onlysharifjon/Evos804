from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📲Telefon raqamini yuborish!', request_contact=True)
        ]
    ], resize_keyboard=True
)