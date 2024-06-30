from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
import media_handlers

from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

load_dotenv()

app = Client(
    'botToSaveFilebot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN'),
)

# Register file handlers
media_handlers.register_handler(app)

if __name__ == "__main__":
    app.run()
