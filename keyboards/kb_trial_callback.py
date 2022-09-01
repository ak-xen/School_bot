from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_key_kb():
    builder = InlineKeyboardBuilder()
    button_adult = InlineKeyboardButton(text=f'👱‍♂️👩‍🦳Взрослый',
                                        callback_data=f'adult')
    button_young = InlineKeyboardButton(text=f'🧒👦Ребенок',
                                        callback_data=f'young')
    builder.add(button_adult, button_young)
    return builder
