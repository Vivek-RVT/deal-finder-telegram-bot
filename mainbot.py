import telegram

# Bot token and group chat ID
bot_token = "7554246388:AAH1Gm3ceRjWgKar1Flr_HnHrMfI4nhl2wA"
group_chat_id = "-1002472380202"

# Initialize the bot
bot = telegram.Bot(token=bot_token)

# Function to send a message
def send_deal_to_group(deal_message):
    try:
        bot.send_message(chat_id=group_chat_id, text=deal_message)
        print("Deal sent successfully!")
    except Exception as e:
        print(f"Failed to send deal: {e}")

# Example: Sending a test deal message
deal_message = "🔥 Amazing Deal: Buy 1 Get 1 Free on Shoes! 🛒 Grab it now at https://example.com/deal"
send_deal_to_group(deal_message)
