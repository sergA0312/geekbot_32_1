from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database
from const import START_MENU_TEXT
from keyboards.start_keyboard import (
    start_kb,
    admin_select_user_keyboard
)


async def start_button(message: types.Message):
    print(message)
    Database().sql_insert_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    with open("/Users/adiletsaparbek/PycharmProjects/geek_32_1/media/images.png", "rb") as photo:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=START_MENU_TEXT,
            reply_markup=await start_kb()
        )
    # with open("/Users/adiletsaparbek/PycharmProjects/geek_32_1/media/0c675a8e1061478d2b7b21b330093444.gif",
    #           "rb") as animation:
    #     await bot.send_animation(
    #         chat_id=message.chat.id,
    #         animation=animation,
    #         caption=START_MENU_TEXT,
    #         reply_markup=await start_kb()
    #     )


async def secret_word(message: types.Message):
    if message.from_user.id == 1150258083:
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Welcome home master {message.from_user.username}",
            reply_markup=await admin_select_user_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_message_handler(secret_word, lambda word: "dorei" in word.text)
