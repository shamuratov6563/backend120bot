TOKEN='8029255360:AAFShxoJ5YbEwGIeuk61Fi3QTRRl-xdWrks'


from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
import asyncio

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command('start'))
async def hello_func(message: types.Message):
    await message.reply(text=f"Assalomu aleykum, {message.from_user.first_name} {message.from_user.last_name or ''}  botimizga xush kelibsiz!")

@dp.message()
async def echo_msg(message: types.Message):
    
    await message.answer(text=message.text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())