from aiogram.types import Message

from bot import dp
from keyboards import kb_welcome
from messages import HELP_MESSAGE
from messages import MOVE_DEADLINE_MESSAGE
from messages import WELCOME_MESSAGE
from secret_token_script import generate_token
from states import DeadlineForm
from states import welcome_state

ADMINS_LIST = (396395930,)


@dp.message_handler(commands=["start", "restart"], state="*")
async def send_welcome(message: Message):
    await message.reply(WELCOME_MESSAGE, reply_markup=kb_welcome)
    await welcome_state.set()


@dp.message_handler(commands=["help"], state="*")
async def send_help(message: Message):
    await message.reply(HELP_MESSAGE)


@dp.message_handler(commands=["move_deadline"], state=[welcome_state, DeadlineForm.ready])
async def move_deadline(message: Message):
    await message.reply(MOVE_DEADLINE_MESSAGE)
    await DeadlineForm.token.set()


@dp.message_handler(commands=["get_userid", "userid"], state="*")
async def send_userid(message: Message):
    await message.reply(f"Your userid is {message.from_user.id}")


@dp.message_handler(commands=["get_token", "token"], state="*")
async def send_token(message: Message):
    if message.from_user.id in ADMINS_LIST:
        await message.reply(f"Token is \n {generate_token()}")
    else:
        await message.reply("ur not admin")
