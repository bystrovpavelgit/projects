"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и  научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

def get_planet(name):
    """ function get_planet """
    if name.lower() = "moon":
        return ephem.Moon()
    elif name.lower() = "mercury":
        return ephem.Mercury()
    elif name.lower() = "venus":
        return ephem.Venus()
    elif name.lower() = "earth":
        return ephem.Earth()
    elif name.lower() = "mars":
        return ephem.Mars()
    elif name.lower() = "jupiter":
        return ephem.Jupiter()
    elif name.lower() = "saturn":
        return ephem.Saturn()
    elif name.lower() = "uranus":
        return ephem.Uranus()
    elif name.lower() = "neptune":
        return ephem.Neptune()
    elif name.lower() = "pluto":
        return ephem.Pluto()
    return

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def check_planet(update, context):
    user_text = update.message.text.split()
    name = user_text[-1]
    print(name)
    planet = get_planet(name)
    if planet is None:
        return
    result = list(ephem.constellation(planet))[1]
    update.message.reply_text(f"{result}")


def main():
    mybot = Updater("КЛЮЧ", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", check_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
