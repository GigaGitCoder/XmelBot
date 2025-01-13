from colorama import Fore
import telebot
import os
from datetime import datetime
from dotenv import load_dotenv
from functions import escape_formating

load_dotenv()
print(Fore.WHITE + rf""" __   __                     _   ____            _               __        ___  
 \ \ / /                    | | |  _ \          | |             /_ |      / _ \ """ + Fore.BLUE + rf"""
  \ V /   _ __ ___     ___  | | | |_) |   ___   | |_    __   __  | |     | | | |
   > <   | '_ ` _ \   / _ \ | | |  _ <   / _ \  | __|   \ \ / /  | |     | | | | """ + Fore.RED + rf"""
  / . \  | | | | | | |  __/ | | | |_) | | (_) | | |_     \ V /   | |  _  | |_| |
 /_/ \_\ |_| |_| |_|  \___| |_| |____/   \___/   \__|     \_/    |_| (_)  \___/ """ + Fore.CYAN + """
      
    — https://github.com/GigaGitCoder/XmelBot """ + Fore.YELLOW + "— Apache-2.0 license " + Fore.RED +
"— XmelBot_v1.0 " + Fore.RESET)

print(Fore.RED + """
                 ⚠️  ONLY FOR TECHNICAL WORKS WITH BOT⚠️
      """ + Fore.RESET)

stime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Creator_ID = int(os.getenv('C_ID'))

bot = telebot.TeleBot(os.getenv('TOKEN'))  # BOTs TOKEN

@bot.message_handler(func=lambda message: True)
def anytime(message):
    bot.send_message(message.chat.id, escape_formating("*В боте производятся тех. работы 🛠*"), parse_mode="MarkdownV2")

bot.polling(none_stop=True)

etime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
bot.send_message(Creator_ID, f"⚠️Отчёт по тех.работе⚠️\n\nВремя начала: {stime}\n\nВремя конца: {etime}")