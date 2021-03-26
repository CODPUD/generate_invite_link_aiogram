from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import database
from config import admins

def keyboard_admin():
    return ReplyKeyboardMarkup([["Сгенерировать инвайт ссылку"]], resize_keyboard=True)

def keyboard_categories(user_id):
    categories = database.get_all_categories()
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in categories:
        markup.insert(KeyboardButton(i[1]))
    if user_id in admins:
        markup.add(KeyboardButton("Сгенерировать инвайт ссылку"))
    return markup