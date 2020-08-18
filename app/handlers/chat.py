from aiogram.types import ContentTypes, CallbackQuery

from app.utils import check_joined_user
from app.misc import dp, bot
from asyncio import sleep


@dp.message_handler(content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def _(message):
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer(
        message.from_user.id, reply_markup=check_joined_user()
    )

    await sleep(60)

    try:
        await bot.delete_message(message.chat.id, message.message_id + 1)
    except Exception as e:
        print(e)
    else:
        await bot.kick_chat_member(message.chat.id, message.from_user.id)


@dp.message_handler(content_types=[ContentTypes.LEFT_CHAT_MEMBER], state="*")
async def _(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.callback_query_handler(text="joined_is_user", state="*")
async def _(call: CallbackQuery):
    print("hey")
    await bot.delete_message(call.message.chat.id, call.message.message_id)
