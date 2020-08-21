from aiogram.types import CallbackQuery, Message, ContentType
from aiogram.utils.exceptions import MessageNotModified

from app.misc import dp, storage
from app.utils import get_vote_key, vote


@dp.channel_post_handler(content_types=ContentType.ANY, state="*")
async def _(message: Message):
    await storage.set_data(chat=message.chat.id, user=message.message_id, data={"like": [], "dislike": []})
    await message.edit_reply_markup(reply_markup=get_vote_key(message_id=message.message_id))


@dp.callback_query_handler(vote.filter(action=['like', 'dislike']), state="*")
async def _(call: CallbackQuery, callback_data: dict):
    data = await storage.get_data(chat=call.message.chat.id, user=call.message.message_id)
    message_id = call.message.message_id
    user_id = call.from_user.id
    action = callback_data['action']
    dislike = data["dislike"]
    like = data["like"]
    
    if user_id in dislike and action == "like":  # User press the btn like
        dislike.remove(user_id)
        like.append(user_id)
        await call.answer(f"Your vote is save!")

    elif user_id in like and action == "dislike":  # User press the btn dislike
        like.remove(user_id)
        dislike.append(user_id)
        await call.answer(f"Your vote is save!")

    else:
        if user_id not in like and user_id not in dislike:
            if action == "like":
                like.append(user_id)
            else:
                dislike.append(user_id)
            await call.answer(f"Your vote is save!")
        else:
            await call.answer("You are already voted!")

    await storage.update_data(chat=call.message.chat.id,
                              user=call.message.message_id,
                              data={"like": like, "dislike": dislike})

    await call.message.edit_reply_markup(reply_markup=get_vote_key(message_id=message_id,
                                                                   like=len(like),
                                                                   dislike=len(dislike)))


@dp.errors_handler(exception=MessageNotModified)
async def _(update, error):
    return True
