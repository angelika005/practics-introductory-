from aiogram import Bot, Dispatcher, types
import asyncio
from users import users_router
from bot_cmd_list import private

bot = Bot(token='7282888811:AAEebWuZDOrekkGm_8GNqZfTdcpDkco0ev8')
dp = Dispatcher()
dp.include_router(users_router)
allowed_upd = ['message, inline_query, callback_query']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=allowed_upd)


asyncio.run(main())
