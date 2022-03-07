from aiogram import executor

import basic_handlers
import move_deadline_handlers
from bot import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
