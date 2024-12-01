import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.user import user


from config import TOKEN



async def main():
    bot = Bot(token=TOKEN,
              #default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )
    
    dp = Dispatcher()
    dp.include_routers(user)
    dp.shutdown.register(shutdown)
    
    await dp.start_polling(bot)


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
