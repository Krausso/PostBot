from app.misc import channel, user
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.models import User, Chanel


def get_channel_key(user_id):
    key = InlineKeyboardMarkup()
    owner = user.get(User.user_id == user_id)
    for item in channel.select().where(Chanel.owner == owner.id):
        key.add(InlineKeyboardButton(text=item.channel_name, callback_data=item.channel_id))
    return key
