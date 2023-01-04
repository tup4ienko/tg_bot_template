from aiogram import types
from aiogram.types import ReplyKeyboardRemove


async def send_list_guest_commands(message: types.Message):
    text = ("<b>List Commands:</b>\n\n"
            "/start - 🤖 Bot launch\n"
            # "/info - 💡 Info center\n"
            "/events - 📅 Events\n"
            "/become_client - 💼 Switch to client\n"
            "/language - 🌎 Change language\n\n"
            "/code1 - 🔑 Enter the first code word\n"
            "/code2 - 🗝 Enter the second code word")
    await message.answer(text, reply_markup=ReplyKeyboardRemove())


async def send_list_client_commands(message: types.Message):
    text = ("<b>List Commands:</b>\n\n"
            "/start - 🤖 Bot launch\n"
            # "/info - 💡 Info center\n"
            "/my_referral - 🪝 Referral links\n"
            "/balance - 🪙 Balance\n"
            "/team - 🎮 Team\n"
            "/events - 📅 Events\n"
            # "/add_payment - 🧾 Add payment\n"
            "/settings - ⚙ Settings\n"
            "/language - 🌎 Change language\n\n"
            "/code1 - 🔑 Enter the first code word\n"
            "/code2 - 🗝 Enter the second code word")
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
