from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext

def unmute_command(update: Update, context: CallbackContext):
    if update.message.chat.type not in ['group', 'supergroup']:
        update.message.reply_text("This command can only be used in groups.")
        return
    
    if not update.message.reply_to_message:
        update.message.reply_text("You must reply to a message to unmute the user.")
        return

    # Check if the user issuing the command is an admin
    chat_member = context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        update.message.reply_text("You don't have the privileges to execute this command.")
        return

    user_id = update.message.reply_to_message.from_user.id

    permissions = ChatPermissions(can_send_messages=True)

    context.bot.restrict_chat_member(
        chat_id=update.message.chat.id,
        user_id=user_id,
        permissions=permissions
    )
    update.message.reply_text(f"User has been unmuted.")
  
