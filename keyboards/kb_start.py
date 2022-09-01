from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_key_kb():
    builder = InlineKeyboardBuilder()
    button_get = InlineKeyboardButton(text=f'⭐️Записаться на пробное занятие', callback_data=f'trial_lesson')
    builder.add(button_get)
    return builder
