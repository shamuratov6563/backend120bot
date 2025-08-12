from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  
TOKEN = os.getenv('TOKEN')


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
