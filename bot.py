from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler. This is a simple handler to start the bot.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your group management bot. Use /help to see what I can do.')

# Define a help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('I can help manage your group! Here are the commands:\n'
                              '/start - Start the bot\n'
                              '/help - Get help\n'
                              '/kick @username - Kick a user from the group\n'
                              '/ban @username - Ban a user from the group')

# Define a kick command handler
def kick(update: Update, context: CallbackContext) -> None:
    """Kick a user from the group."""
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    context.bot.kick_chat_member(chat_id, user_id)
    update.message.reply_text('User has been kicked!')

# Define a ban command handler
def ban(update: Update, context: CallbackContext) -> None:
    """Ban a user from the group."""
    chat_id = update.message.chat_id
    user_id = update.message.reply_to_message.from_user.id
    context.bot.ban_chat_member(chat_id, user_id)
    update.message.reply_text('User has been banned!')

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7305707562:AAEhc7yRWjLqS2BMvlpwmpg7w9KdDbM9YZg", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("kick", kick, filters=Filters.reply))
    dispatcher.add_handler(CommandHandler("ban", ban, filters=Filters.reply))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
    
