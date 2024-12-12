from telegram.ext import Updater, MessageHandler, Filters

def get_chat_id(update, context):
    chat_id = update.message.chat_id
    print(f"Chat ID: {chat_id}")
    update.message.reply_text(f"Group Chat ID: {chat_id}")

updater = Updater("7554246388:AAH1Gm3ceRjWgKar1Flr_HnHrMfI4nhl2wA")
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, get_chat_id))

updater.start_polling()
updater.idle()
