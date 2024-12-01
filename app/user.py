from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
# from middlewares import BaseMiddleware

from app.generator import generate
from app.states import Work

user = Router()

# user.message.middleware(BaseMiddleware())

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот!')

@user.message(Work.process)
async def stop(message: Message):
    await message.answear('Stop')

@user.message()
async def ai(message: Message, state: FSMContext):
    await state.set_state(Work.process)
    res = await generate(message.text)
    #print(res.choices[0].message.content)
    await message.answer(res.choices[0].message.content)
    await state.clear()