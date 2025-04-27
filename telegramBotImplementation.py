import time
import requests
from datetime import datetime
import telebot
from teleg_data import token

API_URL = "https://yobit.net/api/3/ticker/btc_usd"

# -------------------------------------------------------------
# Function: fetch_btc_price
# Description:
#   Retrieves the current BTC/USD sell price from the Yobit API.
#   Makes an HTTP GET request, validates the response, and parses the JSON.
# Returns:
#   float: The sell price of BTC in USD if successful.
#   None: If any error occurs during the fetch or parsing.
# -------------------------------------------------------------
def fetch_btc_price() -> float | None:
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["btc_usd"]["sell"]
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"[{datetime.now()}] Error fetching BTC price: {e}")
        return None

# -------------------------------------------------------------
# Function: format_price_message
# Description:
#   Formats the BTC price along with a timestamp into a readable message.
# Parameters:
#   price (float): The BTC/USD sell price to include in the message.
# Returns:
#   str: A formatted string containing the current date, time, and price.
# -------------------------------------------------------------
def format_price_message(price: float) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"{timestamp}\nSell BTC price: {price}"

# -------------------------------------------------------------
# Function: handle_price_request
# Description:
#   Handles the '/price' command sent by a user.
#   Fetches the BTC price, formats the response, and sends it back.
# Parameters:
#   bot (telebot.TeleBot): The Telegram bot instance used to send messages.
#   chat_id (int): The chat identifier where the response should be sent.
# -------------------------------------------------------------
def handle_price_request(bot: telebot.TeleBot, chat_id: int) -> None:
    price = fetch_btc_price()
    if price is not None:
        message = format_price_message(price)
    else:
        message = "Sorry, I couldn't retrieve the price right now. Please try again later."
    bot.send_message(chat_id, message)

# -------------------------------------------------------------
# Function: start_bot
# Description:
#   Initializes and starts the Telegram bot.
#   Sets up command and text handlers, and begins polling.
# Parameters:
#   token (str): The Telegram bot token for authentication.
# -------------------------------------------------------------
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


# -------------------------------------------------------------
# Main Entry Point
# -------------------------------------------------------------
if __name__ == '__main__':
    start_bot(token)
