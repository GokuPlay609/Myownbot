import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)

TOKEN = 'YOUR_BOT_TOKEN'
MONGO_URI = 'ongodb://localhost:27017/'
MONGO_DB = 'telegram_bot'
MONGO_COLLECTION = 'users'
MONGO_SUDO_COLLECTION = 'udo_users'
OWNER_ID = 123456789  # Replace with your Telegram user ID

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]
sudo_collection = db[MONGO_SUDO_COLLECTION]

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Group Management Bot!")
    user_id = update.effective_user.id
    username = update.effective_user.username
    collection.insert_one({'user_id': user_id, 'username': username})

def kick(update, context):
    try:
        user_id = int(context.args[0])
        context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="User kicked successfully!")
        collection.delete_one({'user_id': user_id})
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error kicking user!")

def ban(update, context):
    try:
        user_id = int(context.args[0])
        context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="User banned successfully!")
        collection.delete_one({'user_id': user_id})
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error banning user!")

def promote(update, context):
    try:
        user_id = int(context.args[0])
        context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="User promoted successfully!")
        collection.update_one({'user_id': user_id}, {'$set': {'role': 'admin'}})
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error promoting user!")

def get_users(update, context):
    users = collection.find()
    user_list = []
    for user in users:
        user_list.append(f"{user['username']} ({user['user_id']})")
    context.bot.send_message(chat_id=update.effective_chat.id, text="\n".join(user_list))

def eval(update, context):
    user_id = update.effective_user.id
    if user_id == OWNER_ID or sudo_collection.find_one({'user_id': user_id}):
        try:
            code = '.join(context.args)
            result = eval(code)
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")
        except Exception as e:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {e}")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have permission to run eval commands!")

def add_sudo(update, context):
    if update.effective_user.id == OWNER_ID:
        try:
            user_id = int(context.args[0])
            sudo_collection.insert_one({'user_id': user_id})
            context.bot.send_message(chat_id=update.effective_chat.id, text="User added to sudo list!")
        except Exception:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error adding user to sudo list!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have permission to add users to the sudo list!")

def remove_sudo(update, context):
    if update.effective_user.id == OWNER_ID:
        try:
            user_id = int(context.args[0])
            sudo_collection.delete_one({'user_id': user_id})
            context.bot.send_message(chat_id=update.effective_chat.id, text="User removed from sudo list!")
        except Exception:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error removing user from sudo list!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have permission to remove users from the sudo list!")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('kick', kick))
    dp.add_handler(CommandHandler('ban', ban))
    dp.add_handler(CommandHandler('promote', promote))
    dp.add_handler(CommandHandler('get_users', get_users
