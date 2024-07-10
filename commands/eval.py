import logging
import io
from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext
import config

logger = logging.getLogger(__name__)

def eval_command(update: Update, context: CallbackContext):
    if update.message.from_user.id != config.OWNER_ID:
        update.message.reply_text("You don't have permission to use this command.")
        return

    try:
        code = ' '.join(context.args)
        result = str(eval(code))
        logger.info("Executed eval command by user %s: %s", update.message.from_user.id, code)

        if len(result) > 4095:
            with io.BytesIO(result.encode()) as file:
                file.name = "eval.txt"
                update.message.reply_document(file)
        else:
            update.message.reply_text(f"Result:\n{result}")

    except Exception as e:
        logger.error("Error executing eval command: %s", e)
        update.message.reply_text(f"Error: {e}")
