from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.misc import dp


@dp.callback_query_handler(text=["like", "dislike"], state="*")
async def _(call: CallbackQuery, state: FSMContext):
    await call.answer()
