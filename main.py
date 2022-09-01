import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from support import on_startup


async def main():
    bot = Bot(token=TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup())


if __name__ == '__main__':
    asyncio.run(main())
