from telegram import Update
from telegram.ext import CallbackContext

# A simple dictionary to keep track of the number of messages sent by users
user_message_count = {}

def myinfo_command(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_id = user.id
    user_info = f"User ID: {user_id}\nUsername: {user.username}\nFirst Name: {user.first_name}\nLast Name: {user.last_name}"
    
    # Update the message count for the user
    user_message_count[user_id] = user_message_count.get(user_id, 0) + 1
    message_count = user_message_count[user_id]
    
    user_info += f"\nMessages Sent: {message_count}"
    
    update.message.reply_text(user_info)
