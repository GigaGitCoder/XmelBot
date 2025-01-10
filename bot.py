from functions import *
import telebot
from telebot import types
from colorama import Fore
import yaml
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
print(Fore.WHITE + rf""" __   __                     _   ____            _               __        ___  
 \ \ / /                    | | |  _ \          | |             /_ |      / _ \ """ + Fore.BLUE + rf"""
  \ V /   _ __ ___     ___  | | | |_) |   ___   | |_    __   __  | |     | | | |
   > <   | '_ ` _ \   / _ \ | | |  _ <   / _ \  | __|   \ \ / /  | |     | | | | """ + Fore.RED + rf"""
  / . \  | | | | | | |  __/ | | | |_) | | (_) | | |_     \ V /   | |  _  | |_| |
 /_/ \_\ |_| |_| |_|  \___| |_| |____/   \___/   \__|     \_/    |_| (_)  \___/ """ + Fore.CYAN + """
      
     — https://github.com/GigaGitCoder """ + Fore.YELLOW + "— Apache-2.0 license " + Fore.RED +
"— by Hunter " + Fore.RESET + "\n")

bot = telebot.TeleBot(os.getenv('TOKEN'))  # BOTs TOKEN

AI_deb = ""
Creator_ID = os.getenv('C_ID') # Bot Creator ID
Logs_Group_ID = os.getenv('L_G_ID') # Logs Group ID
Logs_An_Thread_ID = os.getenv('L_A_T_ID') # Logs /an Thread ID
Logs_Notif_Thread_ID = os.getenv('L_N_T_ID') # Logs /notif Thread ID
Logs_Status_Thread_ID = os.getenv('L_S_T_ID') # Logs /status Thread ID
Logs_Flood_Thread_ID = os.getenv('L_F_T_ID') # Logs /* and * Thread ID

'''To find out thread_id's make:

    bot.reply_to(message, message.reply_to_message.message_thread_id)

    Here's your thread_id'''

def normalize_text(text):
    return ' '.join(text.strip().split())

def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix/Linux/Mac
    else:
        os.system('clear')

def escape_formating(text):
    return text.replace('_', '\\_').replace('.', '\\.').replace(':', '\\:').replace('#', '\\#').replace('-', '\\-').replace('(', '\\(').replace(')', '\\)').replace('!', '\\!').replace('**', '*').replace('=', '\\=').replace('<', '\\<').replace('>', '\\>')

def unauthorized_access(message):
    if message.chat.type != 'private':
        bot.send_message(Logs_Group_ID, escape_formating(f"⚠️ Отсутствие прав {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n```💬Message\n{message.text}```\n\n#Flood_Rights_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")
    else:
        bot.send_message(Logs_Group_ID, escape_formating(f"⚠️ Отсутствие прав {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n```💬Message\n{message.text}```\n\n#Flood_Rights_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")

def load_admin_ids():
    try:
        with open("admin_list.yaml", 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or []
    except FileNotFoundError:
        return []  # If null

def deb_refresh():
    global AI_deb
    AI_deb = open(rf"states.txt", 'r', encoding='utf-8').read()

def new_group(chat_id, message):
    chat_type = "group"
    chat_name = message.chat.title

    try:
        with open("users.yaml", "r", encoding="utf-8") as f:
            existing_ids = yaml.safe_load(f) or []
    except FileNotFoundError:
        existing_ids = []

    existing_chat = next((item for item in existing_ids if item['id'] == str(chat_id)), None)

    if existing_chat is None:
        new_chat = {
            'id': str(chat_id),
            'chat_type': chat_type,
            'chat_name': chat_name
        }
        existing_ids.append(new_chat)

        with open("users.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)

def new_user(chat_id, message):
    chat_type = "private"
    chat_name = message.from_user.username

    try:
        with open("users.yaml", "r", encoding="utf-8") as f:
            existing_ids = yaml.safe_load(f) or []
    except FileNotFoundError:
        existing_ids = []

    existing_chat = next((item for item in existing_ids if item['id'] == str(chat_id)), None)

    if existing_chat is None:
        new_chat = {
            'id': str(chat_id),
            'chat_type': chat_type,
            'chat_name': chat_name
        }
        existing_ids.append(new_chat)

        with open("users.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)

def save_chat_id_ad(chat_id, message):
    # Определяем тип чата и имя чата
    chat_type = "private" if message.chat.type == "private" else "group"
    chat_name = message.chat.username if message.chat.username else message.chat.title

    try:
        with open("ad_check.yaml", "r", encoding="utf-8") as f:
            existing_ids = yaml.safe_load(f) or []
    except FileNotFoundError:
        existing_ids = []

    existing_chat = next((item for item in existing_ids if item['id'] == str(chat_id)), None)

    if existing_chat is None:
        new_chat = {
            'id': str(chat_id),
            'chat_type': chat_type,
            'chat_name': chat_name
        }
        existing_ids.append(new_chat)

        if message.chat.type != 'private':
            bot.send_message(Logs_Group_ID, escape_formating(f"📣 Уведомления ✅ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n#Notif_Logs"), message_thread_id=Logs_Notif_Thread_ID, parse_mode="MarkdownV2")
        else:
            bot.send_message(Logs_Group_ID, escape_formating(f"📣 Уведомления ✅ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n#Notif_Logs"), message_thread_id=Logs_Notif_Thread_ID, parse_mode="MarkdownV2")


        with open("ad_check.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)
        bot.reply_to(message, "🔈 Теперь этот чат получает уведомления/объявления от бота!")

    else:
        existing_ids.remove(existing_chat)

        if message.chat.type != 'private':
            bot.send_message(Logs_Group_ID, escape_formating(f"📣 Уведомления были ❌ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n#Notif_Logs"), message_thread_id=Logs_Notif_Thread_ID, parse_mode="MarkdownV2")
        else:
            bot.send_message(Logs_Group_ID, escape_formating(f"📣 Уведомления были ❌ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n#Notif_Logs"), message_thread_id=Logs_Notif_Thread_ID, parse_mode="MarkdownV2")


        with open("ad_check.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)
        bot.reply_to(message, "🔇 Вы отключили получение уведомлений/объявлений от бота в этом чате!")

def save_chat_id_status(chat_id, message):
    chat_type = "private" if message.chat.type == "private" else "group"
    chat_name = message.chat.username if message.chat.username else message.chat.title

    try:
        with open("status_check.yaml", "r", encoding="utf-8") as f:
            existing_ids = yaml.safe_load(f) or []
    except FileNotFoundError:
        existing_ids = []

    existing_chat = next((item for item in existing_ids if item['id'] == str(chat_id)), None)

    if existing_chat is None:
        new_chat = {
            'id': str(chat_id),
            'chat_type': chat_type,
            'chat_name': chat_name
        }
        existing_ids.append(new_chat)
        
        if message.chat.type != 'private':
            bot.send_message(Logs_Group_ID, escape_formating(f"⚙️ Статус-чек ✅ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n#Status_Logs"), message_thread_id=Logs_Status_Thread_ID, parse_mode="MarkdownV2")
        else:
            bot.send_message(Logs_Group_ID, escape_formating(f"⚙️ Статус-чек ✅ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n#Status_Logs"), message_thread_id=Logs_Status_Thread_ID, parse_mode="MarkdownV2")

        with open("status_check.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)
        bot.reply_to(message, "🔈 Теперь этот чат получает уведомления/объявления от бота!")

    else:
        existing_ids.remove(existing_chat)

        if message.chat.type != 'private':
            bot.send_message(Logs_Group_ID, escape_formating(f"⚙️ Статус-чек ❌ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n#Status_Logs"), message_thread_id=Logs_Status_Thread_ID, parse_mode="MarkdownV2")
        else:
            bot.send_message(Logs_Group_ID, escape_formating(f"⚙️ Статус-чек ❌ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n#Status_Logs"), message_thread_id=Logs_Status_Thread_ID, parse_mode="MarkdownV2")

        with open("status_check.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_ids, f, allow_unicode=True)
        bot.reply_to(message, "🔇 Вы отключили получение уведомлений/объявлений от бота в этом чате!")



def send_startup_message():
    with open("status_check.yaml", "r", encoding="utf-8") as f:
        chat_ids_load = yaml.safe_load(f) or []
    chat_ids = [chat['id'] for chat in chat_ids_load]

    if chat_ids is not []:
        for chat_id in chat_ids:
            try:
                bot.send_message(chat_id.strip(), "Бот включен и готов к работе! 😎")
            except Exception as e:
                print(f"Не удалось отправить сообщение в чат {chat_id.strip()}: {e}")

def send_shutdown_message():
    with open("status_check.yaml", "r", encoding="utf-8") as f:
        chat_ids_load = yaml.safe_load(f) or []
    chat_ids = [chat['id'] for chat in chat_ids_load]

    if chat_ids is not []:
        for chat_id in chat_ids:
            try:
                bot.send_message(chat_id.strip(), "Бот временно выключен! 😢")
            except Exception as e:
                print(f"Не удалось отправить сообщение в чат {chat_id.strip()}: {e}")

@bot.message_handler(content_types=['new_chat_members'])
def new_chat_member(message):
    new_group(message.chat.id, message)

@bot.message_handler(commands=['start', 'help', 'info'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    new_user(message.from_user.id, message)
    bot.reply_to(message, f"""Привет {message.from_user.first_name}! Я бот-помощник, могу помочь тебе с твоими вопросами.\n\nЯ имею несколько команд:
\n/an <запрос> - Нейронка отвечает на ваш запрос\n/status - Включает или выключает уведомления о работе бота\n/notif - Включает или выключает сообщения от бота или его администраторов\n/members - Выводит информацию об участниках группы\n/help - Выводит информацию о боте и его командах""", reply_markup=markup)

@bot.message_handler(commands=['an'])
def answer(message):
    new_user(message.from_user.id, message)
    global AI_deb
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if len(message.text.split()) == 1:
        bot.reply_to(message, f"Ввеите вопрос после команды, я не могу отвечать на пустой запрос 😁", reply_markup=markup)
    else:
        count = int(open(rf"Request_Counter.txt", 'r', encoding='utf-8').read())
        if message.text.split()[0] == "/an@ChatHelper24_Bot":
            message.text = "/an " + f"{message.text.split("/an@ChatHelper24_Bot ")[1]}"
        print(Fore.CYAN + f"\n\nЗапрос #{count} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} " + Fore.YELLOW + "Новый запрос от" + Fore.RED + f" @{message.from_user.username} (id: {message.from_user.id})", end="")
        print(Fore.YELLOW + " из группы:" + Fore.RED + f" {message.chat.title} (id: {message.chat.id})" if message.chat.type != 'private' else "")
        print(Fore.RED + "Текст запроса:" + Fore.MAGENTA + f"\n{message.text.split("/an ")[1]}\n")
        rep = AI_answer(
            request_theme = "TG helper", # Нужна только для логов
            prompt = f"""Ты бот-помощник в телеграмме, будь вежливым, отвечай на любой вопрос пользователя, ВАЖНО: в личных сообщениях отвечай развернуто, а в группах старайся давать краткий, но полный ответ; используй эмодзи в своих сообщениях, в своих сообщениях не используй никакого форматирования, на вопросы про тових поддержку/создателя отвечай что связаться можно по этому нику в телеграмме: @IgorXmel.
            Вот дополниельная информация по чату в котором ты находишься в виде json: 
            {message}""", # Нужен для того чтобы бот понимал как отвечать пользователю. Здесь можно ограничить его, чтобы он не отвечал на какие то вопросы не по теме к примеру
            text = f"{message.text.split("/an ")[1]}",
            deb = AI_deb
        )
        print(Fore.CYAN + f"\nЗапрос #{count} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} " + Fore.YELLOW + "Ответ бота на запрос от" + Fore.RED + f" @{message.from_user.username}" + Fore.MAGENTA + f":\n{normalize_text(rep)}\n\n" + Fore.RESET)
        open(f"Request_Counter.txt", 'w', encoding='utf-8').write(str(count+1))
        data = [{'request_id': f"#{count}"},
                {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'time': datetime.now().strftime("%H:%M:%S"),
            'chat_type': message.chat.type,
            'user_id': message.from_user.id,
            'username': f"@{message.from_user.username}",
            'request': message.text.split("/an ")[1],
            'answer': normalize_text(rep)
        }]

        if message.chat.type != 'private':
            bot.send_message(Logs_Group_ID, escape_formating(f'''🔔 Запрос #{count} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n```👤Request\n{message.text.split("/an ")[1]}\n```\n\n```🤖Response\n{rep}\n```\n\n```💾yaml\n{data}\n```\n\n#An_Logs'''), message_thread_id=Logs_An_Thread_ID, parse_mode="MarkdownV2")
        else:
            bot.send_message(Logs_Group_ID, escape_formating(f'''🔔 Запрос #{count} {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n```👤Request\n{message.text.split("/an ")[1]}\n```\n\n```🤖Response\n{rep}\n```\n\n```💾yaml\n{data}\n```\n\n#An_Logs'''), message_thread_id=Logs_An_Thread_ID, parse_mode="MarkdownV2")
            
        with open("requests.yaml", "r", encoding="utf-8") as f:
            existing_requests = yaml.safe_load(f) or []
        existing_requests.append(data)
        with open("requests.yaml", "w", encoding="utf-8") as f:
            yaml.dump(existing_requests, f, allow_unicode=True, default_flow_style=False)
        bot.reply_to(message, escape_formating(f"💬 Ответ на ваш запрос (Уникальный номер: #{count+1}):\n\n{rep}"), reply_markup=markup, parse_mode="MarkdownV2")

@bot.message_handler(commands=['members'])
def list_members(message):
    new_user(message.from_user.id, message)
    chat_id = message.chat.id
    
    admins = bot.get_chat_administrators(chat_id)
    admin_list = [f"@{admin.user.username} (id: `{admin.user.id}`)" for admin in admins if admin.user.username]

    member_count = bot.get_chat_members_count(chat_id)
    members = []
    
    for i in range(member_count):
        try:
            member = bot.get_chat_member(chat_id, i)
            if member.user.username:
                members.append(f"@{member.user.username} (id: `{member.user.id}`)")
        except Exception as e:
            pass

    # Формируем ответ
    response = "Участники группы:\n\n"
    
    if admin_list:
        response += "👑Администраторы:\n" + "\n".join(admin_list) + "\n\n"
    else:
        response += "👑Администраторов нет.\n\n"
    
    if members:
        response += "👤Участники:\n" + "\n".join(members) + "\n\n"
    else:
        response += "👤Участников нет.\n\n"
    

    if message.chat.type != 'private':
        bot.send_message(Logs_Group_ID, escape_formating(f"👥 Список участников {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n```👤Request\n{message.text}```\n\n```🤖Response\n🧮 Ответ: {response}```\n\n#Flood_Members_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")
    else:
        bot.send_message(Logs_Group_ID, escape_formating(f"👥 Список участников {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n```👤Request\n{message.text}```\n\n```🤖Response\n🧮 Ответ: {response}```\n\n#Flood_Members_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")

    bot.reply_to(message, escape_formating(response), parse_mode="MarkdownV2")

@bot.message_handler(commands=['status'])
def status(message):
    new_user(message.from_user.id, message)
    if message.chat.type == 'private' or any(admin.user.id == message.from_user.id for admin in bot.get_chat_administrators(message.chat.id)):
        save_chat_id_status(message.chat.id, message)

    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам чата")
        unauthorized_access(message)

@bot.message_handler(commands=['notif'])
def notif(message):
    new_user(message.from_user.id, message)
    if message.chat.type == 'private' or any(admin.user.id == message.from_user.id for admin in bot.get_chat_administrators(message.chat.id)):
        save_chat_id_ad(message.chat.id, message)
    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам чата")
        unauthorized_access(message)

@bot.message_handler(commands=['adhelp'])
def adhelp(message):
    new_user(message.from_user.id, message)
    admin_ids = load_admin_ids()
    user_id = message.from_user.id
    
    if any(admin['id'] == user_id for admin in admin_ids):
        bot.reply_to(message, f"Приветствую, @{message.from_user.username}! Вот список Админ-команд:\n/ad <all/id> <msg> - Отправить сообщение на все id из ad_check.yaml или на определенный id чата\n/aid - Вкл/Выкл логирование для ии обработки\n/usl - Список всех людей и групп которые пользовались ботом\n\n⚠️ Project Team Only:\n/cls - Очищает консоль на стороне сервера\n/stop - Останавливает бота\n/addad <id> <username> - Добавить администратора\n/remad <id> <username> - Убрать администратора\n/lstad - Список всех администраторов")

    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам")
        unauthorized_access(message)

@bot.message_handler(commands=['aid'])
def AIdebug(message):
    new_user(message.from_user.id, message)
    admin_ids = load_admin_ids()
    user_id = message.from_user.id
    
    if any(admin['id'] == user_id for admin in admin_ids):
        global AI_deb
        deb_refresh()
        if AI_deb == "0":
            AI_deb = 1
            open(f"states.txt", 'w', encoding='utf-8').write(str(AI_deb))
            bot.reply_to(message, "AI debug ✅")
        else:
            AI_deb = 0
            open(f"states.txt", 'w', encoding='utf-8').write(str(AI_deb))
            bot.reply_to(message, "AI debug ❌")

    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам")
        unauthorized_access(message)

@bot.message_handler(commands=['usl'])
def usl(message):
    new_user(message.from_user.id, message)
    admin_ids = load_admin_ids()
    user_id = message.from_user.id
    
    if any(admin['id'] == user_id for admin in admin_ids):
        with open("users.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        private_ids = []
        group_ids = []

        for entry in data:
            if entry['chat_type'] == 'private':
                private_ids.append(f"@{entry['chat_name']} (id: `{entry['id']}`)")
            elif entry['chat_type'] == 'group':
                group_ids.append(f"{entry['chat_name']} (id: `{entry['id']}`)")

        # Форматируем ответ
        private_users = "\n".join(private_ids) if private_ids else "Нет пользователей."
        group_chats = "\n".join(group_ids) if group_ids else "Нет групп."

        bot.reply_to(message, escape_formating(f"👤Users:\n{private_users}\n\n👥Groups:\n{group_chats}"), parse_mode="MarkdownV2")

    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам")
        unauthorized_access(message)

@bot.message_handler(commands=['ad'])
def ad(message):
    new_user(message.from_user.id, message)
    admin_ids = load_admin_ids()
    user_id = message.from_user.id
    
    if any(admin['id'] == user_id for admin in admin_ids):
        if message.text.split()[0] == "/ad@ChatHelper24_Bot":
            message.text = "/ad " + f"{message.text.split("/ad@ChatHelper24_Bot ")[1]}"
        if len(message.text.split()) == 1:
            bot.reply_to(message, "Напишите команду в таком виде: /ad <id/all> <текст>")
        else:
            if message.text.split()[1] != "all":
                try:
                    int(message.text.split()[1])
                    bot.send_message(message.text.split()[1], message.text.split(f"/ad {message.text.split()[1]} ")[1])
                    bot.reply_to(message, f"Сообщение отправлено на id: {message.text.split()[1]}")
                except Exception as ValueError:
                    bot.reply_to(message, "❓ Неправильно ввели id чата")

            else:
                with open("ad_check.yaml", "r", encoding="utf-8") as f:
                    chat_ids_load = yaml.safe_load(f) or []
                chat_ids = [chat['id'] for chat in chat_ids_load]

                counter = 0
                for chat_id in chat_ids:
                    try:
                        bot.send_message(chat_id.strip(), message.text.split(f"/ad {message.text.split()[1]} ")[1])
                        counter += 1
                    except Exception as e:
                        print(Fore.RED + f"Не удалось отправить сообщение в чат {chat_id.strip()}: {e}" + Fore.RESET)
                
                bot.reply_to(message, f"Сообщение отправлено {counter} пользователям бота")

    else:
        bot.reply_to(message, "✋ Эта команда доступна только администраторам")
        unauthorized_access(message)


@bot.message_handler(commands=['stop'])
def stop(message):
    new_user(message.from_user.id, message)
    if message.from_user.id == Creator_ID:
        send_shutdown_message()
        print(Fore.RED + "\nБот останавливается через Админ-панель" + Fore.RESET)
        bot.reply_to(message, "🔌 Бот выключается...")
        bot.stop_bot()
        
    else:
        bot.reply_to(message, "⚠️ Эта команда доступна только команде проекта")
        unauthorized_access(message)

@bot.message_handler(commands=['cls'])
def cls(message):
    new_user(message.from_user.id, message)
    if message.from_user.id == Creator_ID:
        clear_console()
        
    else:
        bot.reply_to(message, "⚠️ Эта команда доступна только команде проекта")
        unauthorized_access(message)

@bot.message_handler(commands=['addad'])
def addad(message):
    new_user(message.from_user.id, message)
    if message.from_user.id == Creator_ID:
        try:
            username = message.text.split()[2]
            id = int(message.text.split()[1])
        except IndexError:
            bot.reply_to(message, "Пожалуйста, укажите ID и username.")
            return

        try:
            with open("admin_list.yaml", "r", encoding="utf-8") as f:
                existing_ids = yaml.safe_load(f) or []
        except FileNotFoundError:
            existing_ids = []

        existing_chat = next((item for item in existing_ids if item['id'] == str(id) or item['username'] == username), None)

        if existing_chat is None:
            new_admin = {
                'id': id,
                'username': username
            }

            existing_ids.append(new_admin)

            bot.send_message(Logs_Group_ID, escape_formating(f"🛂 Админ добавлен ✅ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n👤 {username} (id: `{id}`)\n\n#Flood_Adm_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")

            with open("admin_list.yaml", "w", encoding="utf-8") as f:
                yaml.dump(existing_ids, f, allow_unicode=True)
            bot.reply_to(message, escape_formating(f"Теперь {username} (id: `{id}`) является администратором. ✅"), parse_mode="MarkdownV2")
            bot.send_message(id, f"🛂 Вас назначили администратором бота ✅\n\nЧтобы ознакомиться с командами напишите: /adhelp")
        else:
            bot.reply_to(message, escape_formating(f"Администратор с ID `{id}` или username {username} уже существует."), parse_mode="MarkdownV2")

    else:
        bot.reply_to(message, "⚠️ Эта команда доступна только команде проекта")
        unauthorized_access(message)

@bot.message_handler(commands=['remad'])
def remad(message):
    new_user(message.from_user.id, message)
    if message.from_user.id == Creator_ID:
        try:
            identifier = message.text.split()[1]  # ID or username
        except IndexError:
            bot.reply_to(message, "Пожалуйста, укажите ID или username.")
            return

        try:
            with open("admin_list.yaml", "r", encoding="utf-8") as f:
                existing_ids = yaml.safe_load(f) or []
        except FileNotFoundError:
            existing_ids = []

        existing_chat = next((item for item in existing_ids if item['id'] == int(identifier) or item['username'] == identifier), None)

        if existing_chat is not None:
            existing_ids.remove(existing_chat)

            bot.send_message(Logs_Group_ID, escape_formating(f"🛂 Админ убран ❌ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n👤 {existing_chat['username']} (id: `{existing_chat['id']}`)\n\n#Flood_Adm_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")
            bot.send_message(existing_chat['id'], f"🛂 Вы больше больше не является администратором бота ❌")

            with open("admin_list.yaml", "w", encoding="utf-8") as f:
                yaml.dump(existing_ids, f, allow_unicode=True)
            bot.reply_to(message, escape_formating(f"Теперь {existing_chat['username']} (id: `{existing_chat['id']}`) не является администратором.❌"), parse_mode="MarkdownV2")
        else:
            bot.reply_to(message, "Администратор с таким ID или username не найден.")

    else:
        bot.reply_to(message, "⚠️ Эта команда доступна только команде проекта")
        unauthorized_access(message)

@bot.message_handler(commands=['lstad'])
def lstad(message):
    new_user(message.from_user.id, message)
    if message.from_user.id == Creator_ID:
        try:
            with open("admin_list.yaml", "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or []
        except FileNotFoundError:
            data = []

        admin_list = [f"{entry['username']} (id: `{entry['id']}`)" for entry in data if 'username' in entry]

        response = ""
        
        if admin_list:
            response += "📋 Список администраторов:\n" + "\n".join(admin_list) + "\n\n"
        else:
            response += "📋 Администраторов нет.\n\n"

        bot.reply_to(message, escape_formating(response), parse_mode="MarkdownV2")
    else:
        bot.reply_to(message, "⚠️ Эта команда доступна только команде проекта")
        unauthorized_access(message)

@bot.message_handler(func=lambda message: True)
def anytime(message):
    new_user(message.from_user.id, message)
    if message.chat.type != 'private':
        bot.send_message(Logs_Group_ID, escape_formating(f"💬 Сообщение {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n👥 {message.chat.title} (id: `{message.chat.id}`)\n\n```💬Message\n{message.text}```\n\n#Flood_Msg_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")
    else:
        bot.send_message(Logs_Group_ID, escape_formating(f"💬 Сообщение {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n👤 @{message.from_user.username} (id: `{message.from_user.id}`)\n\n```💬Message\n{message.text}```\n\n#Flood_Msg_Logs"), message_thread_id=Logs_Flood_Thread_ID, parse_mode="MarkdownV2")
    bot.send_message(message.chat.id, " *Команда не распознана*😔", parse_mode="MarkdownV2")

send_startup_message()
deb_refresh()

bot.polling(none_stop=True)

print(Fore.RED + "Бот остановлен!" + Fore.RESET)
send_shutdown_message()