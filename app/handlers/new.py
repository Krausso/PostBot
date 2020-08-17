from aiogram.types import Message, ContentType, CallbackQuery
from app.misc import dp, bot
from app.utils.keyboard import get_channel_key
from app.utils import CreatePost
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import Unauthorized
from app.utils import Main


@dp.message_handler(commands="new", state="*")
async def _(message: Message):
    await message.answer("Choose your channel", reply_markup=get_channel_key(message.from_user.id))
    await CreatePost.choose_channel.set()


@dp.callback_query_handler(state=CreatePost.choose_channel)
async def _(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()
    await state.update_data(chosen_channel=call.data)
    res = await bot.get_chat(call.data)
    await call.message.edit_text(f"Send post for posting {res.title}")
    await CreatePost.get_post.set()


@dp.message_handler(content_types=ContentType.ANY, state=CreatePost.get_post)
async def _(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        await message.send_copy(chat_id=data["chosen_channel"])
    except Unauthorized:
        await message.answer("I`m not admin in your channel!")
    else:
        await Main.wait_menu.set()



