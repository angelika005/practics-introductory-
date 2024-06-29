from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="статистика"),
            KeyboardButton(text="вакансии"),
            KeyboardButton(text="стоп")
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)

del_kbd = ReplyKeyboardRemove()