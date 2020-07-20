import config
import telebot
import datetime
import time
import schedule

from datetime import datetime, timedelta

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['Бот здесь?'])
def start(message):
        bot.send_message(config.channel_name, 'Я здесь')

if __name__ == '__main__':
     bot.infinity_polling()

def rasp():
    f = open('events.txt')
    events = ''
    x = f.readline() # 1-ая строка файла
    y = datetime.now() + timedelta(minutes=30) # Добавляем ко времени 30 минут
    time = y.strftime("%H:%M") # Формат Часы(24):Минуты
    while x != 'exit':
        if len(x) > 6:
            if x[0:5] == time and str(datetime.today().isoweekday()) == x[6]:
                events = events+x[8:len(x)-1]+', '
                x = f.readline()
            else:
                x = f.readline()
        else:
            x = f.readline()
    if len(events) > 2:
        bot.send_message(config.channel_name, 'Ивент(ы): '+events[0:len(events)-2]+'\nНачнется(утся) через 30 минут.')
    f.close()

schedule.every(1).minutes.do(rasp)

while True:
    schedule.run_pending()
    time.sleep(1)