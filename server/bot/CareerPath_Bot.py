from aiogram import Bot, Dispatcher, types
import asyncio
from users import users_router
from bot_cmd_list import private
from database.engine import create_db, drop_db, session_maker
from database.db_middleware import DataBaseSession

bot = Bot(token='7282888811:AAEebWuZDOrekkGm_8GNqZfTdcpDkco0ev8')
dp = Dispatcher()
dp.include_router(users_router)
allowed_upd = ['message, inline_query, callback_query']


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('бот лег')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=allowed_upd)


asyncio.run(main())
