from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.error import NetworkError, TelegramError
import logging
import time
import config

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your group management bot.')

def error_handler(update: Update, context: CallbackContext):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def handle_network_error(updater):
    while True:
        try:
            updater.start_polling()
            updater.idle()
            break
        except NetworkError as e:
            logger.error(f"NetworkError occurred: {e}. Retrying in 5 seconds...")
            time.sleep(5)
        except TelegramError as e:
            logger.error(f"TelegramError occurred: {e}. Retrying in 5 seconds...")
            time.sleep(5)

def main():
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Add command handlers
    from commands.start import start_command
    from commands.help import help_command
    from commands.eval import eval_command
    from commands.ban import ban_command
    from commands.kick import kick_command
    from commands.mute import mute_command
    from commands.unmute import unmute_command
    from commands.promote import promote_command
    from commands.myinfo import myinfo_command, count_messages
    
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("eval", eval_command))
    dispatcher.add_handler(CommandHandler("ban", ban_command))
    dispatcher.add_handler(CommandHandler("kick", kick_command))
    dispatcher.add_handler(CommandHandler("mute", mute_command, pass_args=True))
    dispatcher.add_handler(CommandHandler("unmute", unmute_command))
    dispatcher.add_handler(CommandHandler("promote", promote_command, pass_args=True))
    dispatcher.add_handler(CommandHandler("myinfo", myinfo_command))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), count_messages))
    

    # Log all errors
    dispatcher.add_error_handler(error_handler)

    handle_network_error(updater)

if __name__ == '__main__':
    main()
