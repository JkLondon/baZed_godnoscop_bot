from unittest import result
from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from uuid import uuid4
from description import make_description
from posts import get_posts

app = Client(
    "my_bot",
    bot_token="5231895048:AAGqiPyjFWWLri15YJu5sepzMWI2C1HWBfU"
)

@app.on_inline_query()
async def answer(client, inline_query):
    results = await get_posts()
    await inline_query.answer(
        results=results
    )
        


app.run() 
