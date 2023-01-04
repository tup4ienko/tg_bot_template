from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from tgbot.filters.private_chat import IsPrivate
from tgbot.misc.bot_commands_menu import set_user_start_commands
from tgbot.misc.throttling import rate_limit


@rate_limit(1)
async def bot_start(message: types.Message, state: FSMContext, bot: Bot):
    await state.finish()
    telegram_id = message.from_user.id
    await set_user_start_commands(telegram_id, bot)
    await message.answer("You send /start")


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, IsPrivate(), CommandStart(), state="*")

