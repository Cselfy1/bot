import asyncio
import os 
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_command_list import listOfCommands
from aiogram.types import BotCommandScopeAllPrivateChats 

#token
load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN')) 
dp = Dispatcher() 

#run
async def main():
    dp.include_routers(user_group_router)
    dp.include_routers(user_private_router)
    await bot.set_my_commands(commands=listOfCommands, scope=BotCommandScopeAllPrivateChats()) 
    await dp.start_polling(bot) 


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("End of work")