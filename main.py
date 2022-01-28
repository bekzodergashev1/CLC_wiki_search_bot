from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
import settings


updater = Updater(token=settings.TELEGRAM_TOKEN)


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom')
    context.bot.send_message(chat_id=update.message.chat_id, text='Assalomu alaykum')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
