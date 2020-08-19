import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from app.config import BOT_TOKEN
from app.models import User, Chanel

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    validate_token=True,
    parse_mode=types.ParseMode.HTML
)
storage = RedisStorage2(host="107.21.208.11", password="foobared")
dp = Dispatcher(bot=bot, storage=storage)

user = User()
channel = Chanel()
