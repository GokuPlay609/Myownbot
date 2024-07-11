from telegram import Update
from telegram.ext import CallbackContext

def myinfo_command(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_info = (
        f"User ID: {user.id}\n"
        f"Username: @{user.username}\n"
        f"First name: {user.first_name}\n"
        f"Last name: {user.last_name}\n"
        f"Messages sent: {context.user_data.get('message_count', 0)}"
    )
    update.message.reply_text(user_info)

def count_messages(update: Update, context: CallbackContext):
    context.user_data['message_count'] = context.user_data.get('message_count', 0) + 1
