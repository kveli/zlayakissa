# -*- coding: utf-8 -*-

import config
import telebot
import datetime
import time
import schedule
import threading

from datetime import datetime, timedelta

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def start(message):
        bot.send_message(config.channel_name, 'Я здесь')

def rasp():
    f = open('events.txt', encoding="utf-8")
    events = ''
    x = f.readline() # 1-ая строка файла
    y = datetime.now() + timedelta(minutes=15) # Добавляем ко времени 30 минут
    time = y.strftime("%H:%M") # Формат Часы(24):Минуты
    while x != 'exit':
        if len(x) > 6:
            if x[0:5] == time[0:5] and str(datetime.today().isoweekday()) == x[6]:
                events = events+x[8:len(x)-1]+', '
                x = f.readline()
            else:
                x = f.readline()
        else:
            x = f.readline()
    if len(events) > 2:
        bot.send_message(config.channel_name, 'Через 15 минут начинается: '+events[0:len(events)-2]+'.')
    f.close()

def no_sleep():
    bot.send_message(config.channel_name_not_sleep, 'Не спать!')

schedule.every(1).minutes.do(rasp)
schedule.every(25).minutes.do(no_sleep)

def potok_1():
    while True:
        schedule.run_pending()
        time.sleep(1)

potok_1 = threading.Thread(target=potok_1)
potok_1.start()

if __name__ == '__main__':
     bot.infinity_polling()