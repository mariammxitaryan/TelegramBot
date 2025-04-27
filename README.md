# Bitcoin Price Telegram Bot

This project is a simple Telegram bot built in Python that fetches the current Bitcoin (BTC) sell price in USD from the Yobit API and shares it with users upon request.

---

## 🚀 Features

- **Fetch Live Price:** Retrieves real-time BTC/USD sell price from [Yobit](https://yobit.net).
- **Telegram Integration:** Seamlessly interacts with users via Telegram commands.
- **Error Handling:** Gracefully handles network/API errors and informs users accordingly.
- **Modular Design:** Cleanly separated functions for fetching, formatting, and responding, making the code easy to maintain and extend.

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Installation](#-installation)
3. [Configuration](#-configuration)
4. [Usage](#-usage)
5. [Code Overview](#-code-overview)
6. [Contributing](#-contributing)

---

## 🛠️ Prerequisites

- Python 3.10 or higher
- `pip` package manager
- Telegram account and bot token

---

## ⚙️ Installation

1. **Clone the repository**

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuration

1. **Create a Telegram Bot**
   - Message [@BotFather](https://t.me/BotFather) on Telegram.
   - Use `/newbot` and follow the prompts to get your **bot token**.

2. **Set Up `teleg_data.py`**
   - In the project root, create a file named `teleg_data.py`.
   - Add your token:

     ```python
     token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
     ```

---

## 🎬 Usage

Run the bot script:

```bash
python bot.py
```

- In Telegram, search for your bot and start a conversation.
- Send the message `price` to receive the latest BTC/USD sell price.

---

## 🧐 Code Overview

```plaintext
bot.py       # Main script with bot and handlers
teleg_data.py  # File containing your Telegram bot token
requirements.txt  # Project dependencies
```

Key functions:

- `fetch_btc_price()`: Retrieves and parses the BTC price from Yobit.
- `format_price_message(price)`: Prepares a user-friendly timestamped message.
- `handle_price_request(bot, chat_id)`: Combines fetching and formatting, then sends the reply.
- `start_bot(token)`: Initializes Telegram handlers and starts polling.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---


*Happy coding!*
