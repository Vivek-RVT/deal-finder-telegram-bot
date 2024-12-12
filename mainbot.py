import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time

# Telegram bot configurations
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# Function to get product details and prices from Amazon
def get_amazon_price(product_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', {'id': 'priceblock_ourprice'}) or soup.find('span', {'id': 'priceblock_dealprice'})
        if price:
            return float(price.text.replace('₹', '').replace(',', '').strip())
    except Exception as e:
        print(f"Amazon Error: {e}")
    return None

# Function to get product details and prices from Flipkart
def get_flipkart_price(product_url):
    try:
        response = requests.get(product_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('div', {'class': '_30jeq3'})
        if price:
            return float(price.text.replace('₹', '').replace(',', '').strip())
    except Exception as e:
        print(f"Flipkart Error: {e}")
    return None

# Function to format and send the deal message to Telegram
def send_deal_to_telegram(product_name, best_price, platform, product_url):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = (
        f"🚨 **Deal Alert!** 🚨\n\n"
        f"🛒 **{product_name}**\n"
        f"💰 **Best Price**: ₹{best_price} ({platform})\n"
        f"🔗 [Buy Now]({product_url})\n\n"
        f"🔥 Limited stock! Hurry up!"
    )
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")

# Main function to find and send the best deals
def find_best_deals():
    product_urls = {
        "Laptop": {
            "Amazon": "https://www.amazon.in/s?k=laptop",
            "Flipkart": "https://www.flipkart.com/search?q=laptop"
        },
        "Smartphone": {
            "Amazon": "https://www.amazon.in/s?k=smartphone",
            "Flipkart": "https://www.flipkart.com/search?q=smartphone"
        }
    }

    for product_name, urls in product_urls.items():
        amazon_price = get_amazon_price(urls["Amazon"])
        flipkart_price = get_flipkart_price(urls["Flipkart"])

        # Compare prices and find the best deal
        prices = {"Amazon": amazon_price, "Flipkart": flipkart_price}
        best_platform = min(prices, key=lambda k: prices[k] if prices[k] is not None else float('inf'))
        best_price = prices[best_platform]

        # Send the deal if a valid price is found
        if best_price is not None:
            send_deal_to_telegram(product_name, best_price, best_platform, urls[best_platform])

# Run the bot periodically
if __name__ == "__main__":
    while True:
        find_best_deals()
        time.sleep(3600)  # Run every hour
