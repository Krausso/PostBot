import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from app.config import BOT_TOKEN, REDIS_HOST, REDIS_PASS, REDIS_PORT
from app.models import User

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    validate_token=True,
    parse_mode=types.ParseMode.HTML
)

storage = RedisStorage2(host=REDIS_HOST,
                        password=REDIS_PASS,
                        port=REDIS_PORT)

dp = Dispatcher(bot=bot, storage=storage)

user = User()
