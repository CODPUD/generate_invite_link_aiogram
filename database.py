import sqlite3

def add_user(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_info(id integer PRIMARY KEY AUTOINCREMENT, user_id integer)''')
    cursor.execute('''SELECT * FROM user_info WHERE user_id=?''', (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute('''INSERT INTO user_info(user_id) VALUES(?)''', (user_id,))
    connection.commit()

    cursor.close()
    connection.close()

def add_invite_link(invite_link):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS invites(id integer PRIMARY KEY, invite_link text)''')
    cursor.execute('''REPLACE INTO invites VALUES(?,?)''', (1, invite_link,))
    connection.commit()

    cursor.close()
    connection.close()

def get_invite_link():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM invites")
    link = cursor.fetchone()
    cursor.close()
    connection.close
    return link[1]

def delete_invite_link():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM invites WHERE id=1''')
    connection.commit()
    cursor.close()
    connection.close()

def get_all_users():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM user_info''')
    users = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return users

def create_rand_categories():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories(id integer PRIMARY KEY AUTOINCREMENT, cars text)''')

    cursor.execute('''SELECT * FROM categories''')
    if cursor.fetchone() is None:
        cars = ["audi", "mers", "ford", "bmw", "lambo", "nexia", "matiz", "malibu", "spark"]
        for car in cars:
            cursor.execute('''INSERT INTO categories(cars) VALUES(?)''', (car, ))
    connection.commit()

    cursor.close()
    connection.close()

def get_all_categories():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM categories''')
    categories = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return categories