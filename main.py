from aiogram import executor

from loader import dp

import middlewares
import filters
import handlers


async def on_startup(dispatcher):
    middlewares.setup(dispatcher)
    filters.setup(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
