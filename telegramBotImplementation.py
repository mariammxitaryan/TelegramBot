import time
import requests
from datetime import datetime
import telebot
from teleg_data import token

API_URL = "https://yobit.net/api/3/ticker/btc_usd"

def fetch_btc_price() -> float | None:
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["btc_usd"]["sell"]
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"[{datetime.now()}] Error fetching BTC price: {e}")
        return None

def format_price_message(price: float) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"{timestamp}\nSell BTC price: {price}"

def handle_price_request(bot: telebot.TeleBot, chat_id: int) -> None:
    price = fetch_btc_price()
    if price is not None:
        message = format_price_message(price)
    else:
        message = "Sorry, I couldn't retrieve the price right now. Please try again later."
    bot.send_message(chat_id, message)

def start_bot(token: str) -> None:
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def on_start(message):
        bot.send_message(
            message.chat.id,
            "Hello friend! Send 'price' to find out the current BTC/USD sell price."
        )

    @bot.message_handler(func=lambda msg: True, content_types=["text"])
    def on_text(message):
        text = message.text.strip().lower()
        if text == "price":
            handle_price_request(bot, message.chat.id)
        else:
            bot.send_message(
                message.chat.id,
                "Invalid command. Please send 'price'."
            )

    print("Bot is polling. Press Ctrl+C to stop.")
    while True:
        try:
            bot.polling(non_stop=True, interval=1, timeout=60)
        except Exception as e:
            print(f"[{datetime.now()}] Bot polling exception: {e}")
            time.sleep(5)
            print("Re-starting polling...")

if __name__ == '__main__':
    start_bot(token)
