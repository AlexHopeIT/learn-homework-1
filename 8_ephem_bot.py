"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

today_date = str(datetime.date.today()).replace("-", "/")
planets = {'Mars': ephem.Mars(today_date), 
           'Venus': ephem.Venus(today_date), 
           'Saturn': ephem.Saturn(today_date), 
           'Jupiter': ephem.Jupiter(today_date),
           'Neptune': ephem.Neptune(today_date), 
           'Uranus': ephem.Uranus(today_date), 
           'Mercury': ephem.Mercury(today_date)}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)     

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def about_planet(update, context):
    planet = update.message.text.split()[1]
    data_of_planet = planets.get(planet, None)
    if data_of_planet!=None:
        constellation = ephem.constellation(planets[planet])
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text('Такой планеты нет в моей базе')

def main():
    mybot = Updater("6683903410:AAHBpMm1mSZD_53wuwT6Aot5FBElBdMRDKY", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", about_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
