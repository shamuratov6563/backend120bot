from aiogram import Dispatcher, types, Bot, F
from aiogram.filters.command import Command
import asyncio
from dotenv import load_dotenv
import os
import re
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

ADMIN_ID = 385419373
load_dotenv()  
TOKEN = os.getenv('TOKEN')

class Register(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()
    bio = State()


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def message_handler(message: types.Message):
    await message.answer(text="Assalomu aleykum, botimizga xush " \
    "kelibsiz, ro'yhatdan o'tish uchn /register tugmasini bosing")


@dp.message(Command('register'))
async def start_register(message: types.Message, state: FSMContext):
    await message.answer(text="Ro'yhatdan o'tish boshlandi, ismingizni kiriting:") 
    await state.set_state(Register.full_name)


@dp.message(Register.full_name)
async def start_register(message: types.Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer('Yoshingizni kiriting')
    await state.set_state(Register.age)


@dp.message(Register.age)
async def start_register(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():   
        return await message.answer(text="Yosh faqat sonlardan iborat bo'lsin") 
    await state.update_data(age=age)
    await message.answer('Telefon raqamingizni kiriting')
    await state.set_state(Register.phone_number)

@dp.message(Register.phone_number)
async def start_register(message: types.Message, state: FSMContext):
    phone_number = message.text
    if not re.match(r'\+998[0-9]{9}', phone_number):
        return message.answer(text="Telefon raqam notogri kiritildi")
    await state.update_data(phone_number=phone_number)
    await message.answer("O'zingiz haqingizda kamida 150 ta belgidan iborat matn yozing")
    await state.set_state(Register.bio)


@dp.message(Register.bio)
async def start_register(message: types.Message, state: FSMContext):
    bio = message.text
    await state.update_data(bio=bio)

    register_data = await state.get_data()

    full_name = register_data.get('full_name')
    age = register_data.get('age')
    phone_number = register_data.get('phone_number')
    bio = register_data.get('bio')

    message_str = f"""
    Kandidat ma'lumotlari:

    Ismi: {full_name} 
    Yoshi: {age}
    Telefon raqami: {phone_number}
    Biografiya: {bio}
    """
   
    await message.answer(text="Arizangiz muvofaqiyatli jo'natildi")
    await bot.send_message(chat_id=ADMIN_ID, text=message_str)
    await state.clear()




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
