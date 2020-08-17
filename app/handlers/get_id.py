from aiogram.types import Message, ContentType, ChatType

from app.utils import ID_group, Main
from app.misc import dp, channel


@dp.message_handler(commands="set", state="*")
async def _(message: Message):
    await ID_group.channel_ID.set()
    await message.answer("Forward message from your channel")


@dp.message_handler(content_types=ContentType.ANY, state=ID_group.channel_ID)
async def _(message: Message):
    try:
        if channel.add_channel(user_id=message.from_user.id,
                               channel_id=message.forward_from_chat.id,
                               name=message.forward_from_chat.title):
            await message.answer("Registration completed")
            await Main.wait_menu.set()
    except AttributeError:
        await message.answer("Incorrect prompt.\n"
                             "Forward message from your channel")
