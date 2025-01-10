import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

def save_chat_id(chat_id):
    with open("chat_ids.txt", "a") as f:
        f.write(f"{chat_id}\n")

@bot.message_handler(content_types=['new_chat_members'])
def new_chat_member(message):
    for new_member in message.new_chat_members:
        if new_member.id == bot.get_me().id:  # Проверяем, что это бот
            save_chat_id(message.chat.id)  # Сохраняем идентификатор чата

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Сохраняем идентификатор чата, если это приватный чат или группа
    save_chat_id(message.chat.id)

def send_startup_message():
    with open("chat_ids.txt", "r") as f:
        chat_ids = f.readlines()
    
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id.strip(), "Бот включен и готов к работе!")
        except Exception as e:
            print(f"Не удалось отправить сообщение в чат {chat_id.strip()}: {e}")

# Вызов функции при старте бота
send_startup_message()

# Запуск бота
bot.polling()