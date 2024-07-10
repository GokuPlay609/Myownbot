import datetime
from telegram import Update
from telegram.ext import ContextTypes

async def mute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type not in ['group', 'supergroup']:
        await update.message.reply_text("This command can only be used in groups.")
        return
    
    if not update.message.reply_to_message:
        await update.message.reply_text("You must reply to a message to mute the user.")
        return
    
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a duration in seconds to mute the user.")
        return
    
    # Check if the user is an admin
    chat_member = await context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        await update.message.reply_text("You don't have the privileges to execute this command.")
        return

    duration = int(context.args[0])
    until_date = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    user_id = update.message.reply_to_message.from_user.id
    await context.bot.restrict_chat_member(
        chat_id=update.message.chat.id,
        user_id=user_id,
        permissions={'can_send_messages': False},
        until_date=until_date
    )
    await update.message.reply_text(f"User has been muted for {duration} seconds.")
  
