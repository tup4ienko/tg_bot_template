from aiogram import types, Bot


async def set_user_start_commands(chat_id: int, bot: Bot):
    await bot.set_my_commands(commands=[
        types.BotCommand("start", "🤖 Bot launch"),
    ],
        scope=types.BotCommandScopeChat(chat_id=chat_id),
    )
