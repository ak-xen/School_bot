from aiogram import Router, types
from keyboards import kb_trial_callback

router = Router()


@router.callback_query(text='trial_lesson')
async def get_trial_callback(callback: types.CallbackQuery):
    await callback.message.answer('Для начала давайте определимся '
                                  'кого мы будем записывать на пробное занятие!',
                                  reply_markup=kb_trial_callback.get_key_kb().as_markup())
    await callback.answer()
