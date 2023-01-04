from aiogram import Dispatcher
from .echo import register_echo
from .start.start import register_start


def register_user(dp: Dispatcher):
    register_start(dp)
    register_echo(dp)
