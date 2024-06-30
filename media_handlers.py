from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def manage_document(client, message):
    await message.reply(
            'Pirateando ne safado!!!'
    )

async def manage_sticker(client, message):
    await message.reply(
            'Sticker bonito, continue assim chimpanze'
    )

async def manage_audio(client, message):
    await message.reply(
            'Ha, não começou o podcast'
    )

async def manage_photo(client, message):
    await message.reply(
            'Espero que não seja nudes'
    )

async def manage_video(client, message):
    await message.reply(
            'Videozinho né safado, espero que seja nudes'
    )

async def manage_animation(client, message):
    await message.reply(
            'Gifzinho ou videozinho sem áudio hmmm, safado(a)'
    )

def register_handler(app: Client):
    app.on_message(filters.document)(manage_document)
    app.on_message(filters.sticker)(manage_sticker)
    app.on_message(filters.audio | filters.voice)(manage_audio)
    app.on_message(filters.photo)(manage_photo)
    app.on_message(filters.video)(manage_video)
    app.on_message(filters.animation)(manage_animation)
    


