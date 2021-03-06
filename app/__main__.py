from aiogram import executor, Dispatcher, types
from app.misc import dp, bot
import app.handlers  # noqa: F401


async def start(dispatcher: Dispatcher):
    await bot.set_my_commands([
        types.BotCommand(command="/start", description="Begin conversation"),
    ])

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=start)
