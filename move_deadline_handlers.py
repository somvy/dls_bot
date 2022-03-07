from aiogram.types import Message
from aiogram.types.message import ContentType

from bot import deadlines_info
from bot import dp
from secret_token_script import validate_token
from states import DeadlineForm


@dp.message_handler(content_types=ContentType.TEXT, state=DeadlineForm.token)
async def token(message: Message):
    # read token, validate it
    if not validate_token(message.text):
        await message.reply("wrong token")
    else:
        deadlines_info[message.from_user.id] = {}
        await message.reply("token ok, enter stepik_id")
        await DeadlineForm.stepik_id.set()


@dp.message_handler(content_types=ContentType.TEXT, state=DeadlineForm.stepik_id)
async def stepik_id(message: Message):
    deadlines_info[message.from_user.id]["stepik_id"] = message.text
    await message.reply("enter hw name")
    await DeadlineForm.homework_name.set()


@dp.message_handler(content_types=ContentType.TEXT, state=DeadlineForm.homework_name)
async def homework_name(message: Message):
    deadlines_info[message.from_user.id]["hw_name"] = message.text
    await message.reply("enter new deadline")
    await DeadlineForm.new_deadline.set()


@dp.message_handler(content_types=ContentType.TEXT, state=DeadlineForm.new_deadline)
async def new_deadline(message: Message):
    deadlines_info[message.from_user.id]["new_deadline"] = message.text
    await message.reply("enter thread")
    # buttons?
    await DeadlineForm.thread.set()


@dp.message_handler(content_types=ContentType.TEXT, state=DeadlineForm.thread)
async def thread(message: Message):
    deadlines_info[message.from_user.id]["thread"] = message.text
    # write to db, google sheets
    # text = sum((f"{k}:{v}" for k, v in deadlines_info[message.from_user.id].items()))
    await message.reply("all ok")
    await DeadlineForm.ready.set()
