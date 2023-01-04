from typing import Union

from aiogram import types, Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.filters.private_chat import IsPrivate
from tgbot.misc.throttling import rate_limit


@rate_limit(1)
async def handler_spam(message: Union[Message, CallbackQuery]):
    """
    The function catches the text, does not end up in handlers.
    Also spam protection.
    """
    text = "Dude, I'm still working on new features."

    if isinstance(message, Message):
        await message.answer(text)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.answer(text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(handler_spam, IsPrivate(), state="*", content_types=types.ContentTypes.ANY)
