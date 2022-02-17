from aiogram import types

from loader import dp


async def bot_start(msg: types.Message):
    await msg.answer('Hello world!')
