from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

vote = CallbackData("vote", "message_id", "action")


def check_joined_user():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Я человек",
            callback_data="joined_is_user"
        )
    )
    return keyboard


def get_vote_key(message_id, like=0, dislike=0):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(f"🔥 {like}",
                              callback_data=vote.new(message_id=message_id, action="like")),
         InlineKeyboardButton(f"👎 {dislike}",
                              callback_data=vote.new(message_id=message_id, action="dislike"))
         ]
    ])
