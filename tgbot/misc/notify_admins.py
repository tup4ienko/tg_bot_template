import logging

from aiogram import Dispatcher, Bot

from tgbot.config import load_config


async def on_startup_notify(bot: Bot):
    config = load_config()
    admin_ids = config.tg_bot.admin_ids
    for admin in admin_ids:
        try:
            await bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
