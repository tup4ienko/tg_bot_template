from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class IsPrivate(BoundFilter):
    async def check(self, message: Union[Message, CallbackQuery]):
        if isinstance(message, Message):
            return message.chat.type == types.ChatType.PRIVATE
        elif isinstance(message, CallbackQuery):
            call = message
            return call.message.chat.type == types.ChatType.PRIVATE
