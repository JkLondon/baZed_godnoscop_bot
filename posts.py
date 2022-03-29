
import asyncio
import configparser
from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from description import make_description
config = configparser.ConfigParser()
config.read("config.ini")

api_id = config["pyrogram"]["api_id"]
api_hash = config["pyrogram"]["api_hash"]
async def get_posts():
	horoscope = {
		"ОВЕН": "♈️Овен",
		"ТЕЛЕЦ": "♉️Телец",
		"БЛИЗНЕЦЫ": "♊️Близнецы",
		"РАК": "♋️Рак",
		"ВЕСЫ": "♎️Весы",
		"РЫБЫ": "♓️Рыбы",
		"СКОРПИОН": "♏️Скорпион",
		"СТРЕЛЕЦ": "♐️Стрелец",
		"ВОДОЛЕЙ": "♒️Водолей",
		"ДЕВА": "♍️Дева",
		"ЛЕВ": "♌️Лев",
		"КОЗЕРОГ": "♑️Козерог"
	}

	app = Client(
		"sniper",
		api_id=api_id,
		api_hash=api_hash
	)
	await app.start()
	posts = []
	with app:
		async for message in app.iter_history("godnoscop", limit = 12):
			raw_text = message.text
			raw_text_arr = raw_text.split()
			title = horoscope[raw_text_arr[0][:-1]]
			input_message_content_text = "**" + title + "** - "
			input_message_content_text += "__" + " ".join(raw_text_arr[1:3]) + "__\n"
			input_message_content_text += " ".join(raw_text_arr[3:])
			description = make_description(" ".join(raw_text_arr[3:]))
			post = InlineQueryResultArticle(
                title=title,
                input_message_content=InputTextMessageContent(
                    input_message_content_text
                ),
                description=description,
            )
			posts.append(post)
		await app.stop()
	return posts[::-1]
	