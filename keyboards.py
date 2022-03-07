from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

button_help = KeyboardButton("/help")
button_token = KeyboardButton("/get_token")
button_move_deadline = KeyboardButton("/move_deadline")

kb_help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_help)

kb_welcome = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_move_deadline)
