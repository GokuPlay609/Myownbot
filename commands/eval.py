import logging
import io
from telegram import Update
from telegram.ext import CallbackContext
import config

logger = logging.getLogger(__name__)

def eval_command(update: Update, context: CallbackContext):
    if update.message.from_user.id != config.OWNER_ID:
        update.message.reply_text("You do not have permission to use this command.")
        return

    try:
        code = update.message.text.split(' ', 1)[1]
    except IndexError:
        update.message.reply_text("Please provide the code to evaluate.")
        return

    try:
        # Capture the output of the eval command
        old_stdout = io.StringIO()
        exec(code, {'__builtins__': {}})
        result = old_stdout.getvalue()
        old_stdout.close()
        
        if len(result) == 0:
            result = "Code executed successfully with no output."

        update.message.reply_text(f"Output:\n{result}")
    except Exception as e:
        logger.error(f"Error executing eval command: {e}")
        update.message.reply_text(f"Error executing eval command: {e}")

