import telegram

# Bot token and group ID
BOT_TOKEN = "7554246388:AAH1Gm3ceRjWgKar1Flr_HnHrMfI4nhl2wA"
GROUP_ID = "-1002472380202"

# Initialize bot
bot = telegram.Bot(token=BOT_TOKEN)

# Send a test message to the group
try:
    bot.send_message(chat_id=GROUP_ID, text="Hello, this is a test message from Deal Finder Bot!")
    print("Message sent successfully!")
except Exception as e:
    print(f"Error: {e}")
