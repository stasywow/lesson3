import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def main():
    mybot = Updater("", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("hello", nice))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))



    dp.add_handler(MessageHandler(Filters.command, unknown))
    
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Привет!'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text("Кококо")

def nice(bot, update):
    text = 'Кококо'
    print(text)
    update.message.reply_text(text)

def planet(bot, update, args):
    print(args)
    plan = ''.join(args)
    plan = plan.capitalize()
    print(plan)
#    user_text = update_message.text
#    plan = user_text.split(' ')
    date = datetime.datetime.now()

    right_date = date.strftime('%Y/%m/%d')
    print(right_date)
    plan_time = getattr(ephem,plan)(right_date)
    print(plan_time)
    text_const = ephem.constellation(plan_time)
    print(text_const)
    update.message.reply_text(text_const)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


main()
