import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from support import on_startup
from handlers import start
from handlers.callbacks import callback_trial, callback_adult, callback_young


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(callback_trial.router)
    dp.include_router(callback_adult.router)
    dp.include_router(callback_young.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup())


if __name__ == '__main__':
    asyncio.run(main())
