from asyncio import sleep

from aiogram.types import ContentTypes, CallbackQuery, ChatPermissions
from aiogram.utils.exceptions import (
    MethodIsNotAvailable, MessageToDeleteNotFound
)

from app.misc import dp, bot
from app.utils import check_joined_user


@dp.message_handler(content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def _(message):
    await bot.delete_message(message.chat.id, message.message_id)

    try:
        await message.chat.restrict(
            message.from_user.id,
            permissions=ChatPermissions(can_send_messages=False)
        )
    except MethodIsNotAvailable:
        pass

    await message.answer(
        f"""Hello, {message.from_user.first_name}!
Please, press the button below to prove that you are not a bot.
Otherwise, you gonna be kicked""",
        reply_markup=check_joined_user()
    )
    await sleep(60)
    try:
        await bot.delete_message(message.chat.id, message.message_id+1)
    except MessageToDeleteNotFound:
        pass
    else:
        await bot.kick_chat_member(message.chat.id, message.from_user.id)


@dp.message_handler(content_types=[ContentTypes.LEFT_CHAT_MEMBER], state="*")
async def _(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(lambda c: c.data == "joined_is_user", state="*")
async def _(c: CallbackQuery):
    await bot.delete_message(c.message.chat.id, c.message.message_id)
    try:
        await c.message.chat.restrict(
            c.message.from_user.id,
            permissions=ChatPermissions(can_send_messages=True)
        )
    except MethodIsNotAvailable:
        pass
