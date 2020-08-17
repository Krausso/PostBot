from aiogram.types import Message
from app.misc import dp


@dp.message_handler(commands="start", state="*")
async def _(message: Message):
    await message.answer("Здравствуйте!")
