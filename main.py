from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Message
import os

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# Start Flask server in a new thread
Thread(target=run).start()

# Pyrogram bot setup
API_ID = 26047145
API_HASH = "3864baec5159bcacbd4ccbbc48a4afa6"
BOT_TOKEN = "7970747968:AAGs5qYbIQixAMvyzESmmHeb4kGigTotRjA"

bot = Client("LudoMiniAppBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply(
        "🎲 *Welcome to Ludo by Gaurave!*\nClick below to play the game inside Telegram 👇",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    text="🎮 Start Ludo Game",
                    web_app=WebAppInfo(url="https://telegram-ludo.onrender.com")
                )
            ]]
        ),
        quote=True
    )

bot.run()
