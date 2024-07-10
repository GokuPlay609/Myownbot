import config
from telegram import Update
from telegram.ext import ContextTypes

async def eval_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != config.OWNER_ID:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    # Extract the code to evaluate
    code = update.message.text.split(' ', 1)[1]

    try:
        # Evaluate the code
        result = eval(code)
        await update.message.reply_text(f"Result: {result}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
      
