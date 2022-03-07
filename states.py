from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup

welcome_state = State()


class DeadlineForm(StatesGroup):
    init = State()
    token = State()
    stepik_id = State()
    homework_name = State()
    new_deadline = State()
    thread = State()
    ready = State()
