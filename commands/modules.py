from telegram import Update
from telegram.ext import ContextTypes

async def modules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    active_modules = [
        "start", "ban", "kick", "mute", "unmute", "myinfo", "eval", "promote"
        # Add more command names as needed
    ]

    module_list = "\n".join(active_modules)
    message = f"Active modules/commands:\n\n{module_list}"

    await update.message.reply_text(message)
