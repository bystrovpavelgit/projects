""" simple telegramm bot """
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,
    'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    """ function to greet user """
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")

def talk_to_me(update, context):
    """ function to talk to the user"""
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    """ main function """
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dispatch = mybot.dispatcher
    dispatch.add_handler(CommandHandler("start", greet_user))
    dispatch.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
