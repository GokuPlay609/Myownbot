from telegram import Update
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your group management bot.')
