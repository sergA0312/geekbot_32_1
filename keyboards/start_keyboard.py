import telebot
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    )
''')
conn.commit()

# Инициализация бота
bot = good_nurik_bot. good_nurik_botBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    
    # Запись пользователя в базу данных
    cursor.execute('INSERT INTO users (id, username, first_name, last_name) VALUES (?, ?, ?, ?)', (user_id, username, first_name, last_name))
    conn.commit()
    
    bot.reply_to(message, 'Вы были записаны в базу данных.')

# Запуск бота
bot.polling()
