from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Message

API_ID = 26047145   # ← Replace with your actual api_id
API_HASH = "3864baec5159bcacbd4ccbbc48a4afa6"  # ← Replace with your actual api_hash
BOT_TOKEN = "7970747968:AAGs5qYbIQixAMvyzESmmHeb4kGigTotRjA"  # ← Replace with your bot token

bot = Client("LudoMiniAppBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply(
        "🎲 *Welcome to Ludo by Gaurave!*\nClick below to play the game inside Telegram 👇",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    text="🎮 Start Ludo Game",
                    web_app=WebAppInfo(url="https://ludobygaurave.onrender.com")
                )
            ]]
        ),
        quote=True
    )


bot.run()