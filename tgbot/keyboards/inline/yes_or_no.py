from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yes_or_now_keyboard = InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text="✅",
                                         callback_data='True'
                                     ),
                                     InlineKeyboardButton(
                                         text="❌",
                                         callback_data='False'
                                     )
                                 ],
                             ]
                         )