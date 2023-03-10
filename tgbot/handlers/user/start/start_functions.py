from aiogram import types
from aiogram.types import ReplyKeyboardRemove


async def send_list_guest_commands(message: types.Message):
    text = ("<b>List Commands:</b>\n\n"
            "/start - ๐ค Bot launch\n"
            # "/info - ๐ก Info center\n"
            "/events - ๐ Events\n"
            "/become_client - ๐ผ Switch to client\n"
            "/language - ๐ Change language\n\n"
            "/code1 - ๐ Enter the first code word\n"
            "/code2 - ๐ Enter the second code word")
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


async def send_list_client_commands(message: types.Message):
    text = ("<b>List Commands:</b>\n\n"
            "/start - ๐ค Bot launch\n"
            # "/info - ๐ก Info center\n"
            "/my_referral - ๐ช Referral links\n"
            "/balance - ๐ช Balance\n"
            "/team - ๐ฎ Team\n"
            "/events - ๐ Events\n"
            # "/add_payment - ๐งพ Add payment\n"
            "/settings - โ Settings\n"
            "/language - ๐ Change language\n\n"
            "/code1 - ๐ Enter the first code word\n"
            "/code2 - ๐ Enter the second code word")
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
