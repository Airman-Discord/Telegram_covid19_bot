from dotenv import load_dotenv, find_dotenv
from os import environ
from covid import Covid
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler

load_dotenv(find_dotenv())
token = environ.get('token')

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f" Hi! I'm a Covid19 Telegram bot, name your input by country")

def api(update: Update, context: CallbackContext):
    covid19 = Covid(update.message.text)
    update.message.reply_chat_action("typing")
    result = covid19.get_latest()

    if result == False:
        chat = "Country not Found"
    else:
        chat = f'''
    Country: ***{result['country']}***
Confirmed: {result['status'][-1]['confirms']}
Deaths: {result['status'][-1]['deaths']}
Recovered: {result['status'][-1]['recovered']}
Active: {result['status'][-1]['active']}
Source: [Covid19api](https://api.covid19api.com/country/{result['country']})'''
    update.message.reply_markdown(chat)

bot = Updater(token)

bot.dispatcher.add_handler(CommandHandler('start', hello))
bot.dispatcher.add_handler(MessageHandler(None, api))


bot.start_polling()
bot.idle()

