import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class IgnoreGroupUpdatesMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            if types.ChatType.PRIVATE != update.message.chat.type:
                raise CancelHandler()
