from aiogram.dispatcher.filters.state import State, StatesGroup


class ID_group(StatesGroup):
    channel_ID = State()


__all__ = ["ID_group"]
