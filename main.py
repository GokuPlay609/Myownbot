from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging
import config

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your group management bot.')

def main():
    app = ApplicationBuilder().token(config.TOKEN).build()
    
    # Add command handlers
    from commands.start import start_command
    from commands.help import help_command
    from commands.eval import eval_command
    from commands.ban import ban_command
    from commands.kick import kick_command
    from commands.mute import mute_command
    from commands.myinfo import myinfo_command

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("eval", eval_command))
    app.add_handler(CommandHandler("ban", ban_command))
    app.add_handler(CommandHandler("kick", kick_command))
    app.add_handler(CommandHandler("mute", mute_command, pass_args=True))
    app.add_handler(CommandHandler("myinfo", myinfo_command))

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), myinfo_command))

    app.run_polling()

if __name__ == '__main__':
    main()
  
