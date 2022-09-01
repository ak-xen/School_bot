from aiogram import Router, types
from aiogram.filters import Command
from keyboards import kb_start

start_router = Router()


@start_router.message(Command(commands=['start']))
async def cmd_start(message: types.Message):
    await message.answer("Привет, я бот школы 'Linguistic Universe'.\n"
                         "Я помогу тебе быть в курсе всех последних новостей."
                         "Так же, если ты еще не оставил заявку ты можешь сделать это,"
                         "прямо сейчас!", reply_markup=kb_start.get_key_kb().as_markup())
