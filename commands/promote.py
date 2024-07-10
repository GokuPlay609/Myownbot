from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext
import config

def promote_command(update: Update, context: CallbackContext):
    if update.message.chat.type not in ['group', 'supergroup']:
        update.message.reply_text("This command can only be used in groups.")
        return
    
    if not context.args:
        update.message.reply_text("Please provide the username or user ID of the person you want to promote.")
        return
    
    username = context.args[0]
    user_id = None

    # Fetch user ID from username
    if username.startswith('@'):
        try:
            user = context.bot.get_chat_member(update.message.chat.id, username)
            user_id = user.user.id
        except Exception as e:
            update.message.reply_text("Couldn't find the user. Please ensure the username is correct.")
            return
    else:
        user_id = int(username)

    # Check if the user issuing the command is an admin
    chat_member = context.bot.get_chat_member(update.message.chat.id, update.message.from_user.id)
    if chat_member.status not in ['administrator', 'creator']:
        update.message.reply_text("You don't have the privileges to execute this command.")
        return

    # Promote user to admin
    context.bot.promote_chat_member(
        chat_id=update.message.chat.id,
        user_id=user_id,
        can_change_info=True,
        can_delete_messages=True,
        can_invite_users=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_promote_members=True
    )
    update.message.reply_text(f"User has been promoted to admin.")
