from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import config

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start_command(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your group management bot.')

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
    from commands.myinfo import myinfo_command

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("eval", eval_command))
    dispatcher.add_handler(CommandHandler("ban", ban_command))
    dispatcher.add_handler(CommandHandler("kick", kick_command))
    dispatcher.add_handler(CommandHandler("mute", mute_command, pass_args=True))
    dispatcher.add_handler(CommandHandler("myinfo", myinfo_command))

    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), myinfo_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
