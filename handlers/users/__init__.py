from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .start import bot_start


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
