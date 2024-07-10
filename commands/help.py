from telegram import Update
from telegram.ext import CallbackContext

def help_command(update: Update, context: CallbackContext):
    help_text = """
    Available commands:
    /start - Start the bot
    /help - Get help
    /eval - Evaluate Python code (admin only)
    /ban - Ban a user
    /kick - Kick a user
    /mute - Mute a user for a specified duration
    /myinfo - Get your user information
    """
    update.message.reply_text(help_text)
