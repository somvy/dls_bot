from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


deadlines_info = {}

with open("secrets.txt", "r") as f:
    API_TOKEN = f.readline()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
