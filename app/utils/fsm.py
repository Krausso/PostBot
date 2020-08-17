from aiogram.dispatcher.filters.state import State, StatesGroup


class Main(StatesGroup):
    wait_menu = State()


class ID_group(StatesGroup):
    channel_ID = State()


class CreatePost(StatesGroup):
    choose_channel = State()
    get_post = State()


__all__ = ["ID_group", "CreatePost", "Main"]
