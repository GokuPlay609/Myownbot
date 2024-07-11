from telegram import Update
from telegram.ext import CallbackContext

async def modules_command(update: Update, context: CallbackContext):
    active_commands = [
        "start", "help", "eval", "ban", "kick", "mute", "unmute", "promote", "myinfo"
        # Add more commands as needed
    ]
    command_list = "\n".join(active_commands)
    message = f"Active commands:\n\n{command_list}"

    await update.message.reply_text(message)
