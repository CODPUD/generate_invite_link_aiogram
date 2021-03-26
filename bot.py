from aiogram import executor
from misc import dp
import handler
import database, markup

if __name__ == "__main__":
    database.create_rand_categories()
    executor.start_polling(dp, skip_updates=True)