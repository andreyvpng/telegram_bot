from telegram import *
from settings import *
import time

bot = telegramBot(SETTINGS_TOKEN)

def handle_updates(updates):
    global bot
    for update in updates:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        if text == "/start":
            bot.send_message("Welcome!", chat)
        else:
            bot.send_message(text, chat)

def main():
    last_update_id = None
    while True:
        updates = bot.get_updates(last_update_id)
        if len(updates) > 0:
            last_update_id = bot.get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

main()