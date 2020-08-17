from aiogram import executor
from app.misc import dp
import app.handlers  # noqa: F401

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
