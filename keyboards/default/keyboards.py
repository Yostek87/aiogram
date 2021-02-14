from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Потрібна консультація")
        ],
        [
            KeyboardButton(text="Запис до спеціаліста")
        ],

    ],
    resize_keyboard=True
)
