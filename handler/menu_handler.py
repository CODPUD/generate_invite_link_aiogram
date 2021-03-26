from misc import dp, bot
from aiogram import types
import database
import markup
from config import admins
import string
import random
from aiogram.types.input_file import InputFile

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
        user_id = message.from_user.id
        if in_database(user_id):
                if user_id in admins:
                        await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}", reply_markup=markup.keyboard_categories(user_id))
                else:
                        await bot.send_message(message.from_user.id, f"Добро пожаловать, {message.from_user.first_name}!", reply_markup=markup.keyboard_categories(user_id))
        else:
                if user_id in admins:
                        await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}", reply_markup=markup.keyboard_categories(user_id))
                else:
                        link = message.get_args()
                        if link != "": 
                                if link == database.get_invite_link():
                                        await bot.send_message(message.from_user.id, f"Добро пожаловать, {message.from_user.first_name}!", reply_markup=markup.keyboard_categories(user_id))
                                        database.add_user(message.from_user.id)
                                        database.delete_invite_link()
                                else:
                                        await bot.send_message(message.from_user.id, f"У вас нет доступа к боту!")
                        else:
                                await bot.send_message(message.from_user.id, f"У вас нет доступа к боту!")

@dp.message_handler(lambda msg: msg.text == "Сгенерировать инвайт ссылку")
async def generate_invite(message: types.Message):
        if message.from_user.id in admins:
                letters = string.ascii_letters
                numbers = "".join(list(map(str, [i for i in range(10)])))
                all_chars = letters + numbers
                invite_link = "".join([random.choice(all_chars) for _ in range(10)])
                bot_info = await bot.get_me()
                #f"https://t.me/{bot_info['username']}?start={invite_link}"
                await bot.send_message(message.from_user.id, f"https://t.me/{bot_info['username']}?start={invite_link}")
                database.add_invite_link(invite_link)

@dp.message_handler()
async def sendWelcome(message: types.Message):
        user_id = message.from_user.id
        if in_categories_database(message.text):
                await bot.send_document(user_id, InputFile(path_or_bytesio="docs.pdf") )
        else:
                if in_database(user_id) or (user_id in admins):
                        await bot.send_message(user_id, "Меню: ", reply_markup=markup.keyboard_categories(user_id))

def in_database(user_id):
        is_exist = False
        for i in database.get_all_users():
                if user_id in i:
                        is_exist = True
                        break
        return is_exist

def in_categories_database(text):
        is_exist = False
        for i in database.get_all_categories():
                if text in i:
                        is_exist = True
                        break
        return is_exist