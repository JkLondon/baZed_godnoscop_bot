import configparser
from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from uuid import uuid4
from description import make_description
from posts import get_posts
config = configparser.ConfigParser()
config.read("config.ini")

app = Client(
    "bazedgod",
    bot_token=config["pyrogram"]["bot_token"]
)

@app.on_inline_query()
async def answer(client, inline_query):
    results = await get_posts()
    await inline_query.answer(
        results=results
    )
        


app.run() 
