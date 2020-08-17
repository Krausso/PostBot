from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.utils import ID_group
from app.misc import dp


@dp.message_handler(commands="set", state="*")
async def _(message: Message):
    await ID_group.channel_ID.set()
    await message.answer("Forward message from your channel")


@dp.message_handler(content_types=ContentType.ANY, state=ID_group.channel_ID)
async def _(message, state: FSMContext):
    try:
        print(message.forward_from_chat.type)
    except AttributeError:
        await message.answer(
            "Incorrect prompt.\nForward message from your channel"
        )
    else:
        if message.forward_from_chat.type == "channel":
            async with state.proxy() as data:
                data['channel_id'] = message.forward_from_chat.id

            await message.answer("Registration completed")
