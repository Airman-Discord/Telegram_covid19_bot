from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f" Hi! I'm a Covid19 Telegram bot")

bot = Updater('1767034528:AAFx5QxYONFJdj5onnzh5jm68_mqy5QHTg8')

bot.dispatcher.add_handler(CommandHandler('hi', hello))

bot.start_polling()
bot.idle()