from app.misc import dp, user
from aiogram import types


@dp.message_handler(commands="start", state="*")
async def start(message: types.Message):
    if not user.check_user(message.from_user.id):
        # Пользователь не найден в БД
        user.add_user(user_id=message.from_user.id,
                      first_name=message.from_user.first_name,
                      username=message.from_user.username)

    await message.answer("Hello!")
