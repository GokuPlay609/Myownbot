from telegram import Update
from telegram.ext import ContextTypes

async def ban_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return
    
    if not update.message.reply_to_message:
        await update.message.reply_text("You must reply to a message to ban the user.")
        return
    
    # Check if the user is an admin
    chat_member = await context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        await update.message.reply_text("You don't have the privileges to execute this command.")
        return

    user_id = update.message.reply_to_message.from_user.id
    await context.bot.ban_chat_member(update.message.chat.id, user_id)
    await update.message.reply_text("User has been banned.")
  
