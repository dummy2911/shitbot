#!/usr/bin/env python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Братуха")
    update.message.reply_text('Эй братуха')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text, update)
    update.message.reply_text(user_text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Поехали, начал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота и он будет работать пока мы его не остановим 
    mybot.idle()

if __name__ == "__main__":
    main()
