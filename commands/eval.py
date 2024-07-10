from telegram import Update
from telegram.ext import CallbackContext
import config

def eval_command(update: Update, context: CallbackContext):
    if update.message.from_user.id != config.OWNER_ID:
        update.message.reply_text("You don't have permission to use this command.")
        return

    try:
        result = eval(' '.join(context.args))
        update.message.reply_text(f"Result: {result}")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
