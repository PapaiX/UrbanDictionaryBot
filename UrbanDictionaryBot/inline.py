from Data import Data
from UrbanDictionaryBot.heart import ud_search, rand
from pyrogram import Client
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


# Inline System
@Client.on_inline_query()
async def answer(udbot, query):
    if query.query in ["", "-"]:  # "-" Due to Library. Code Error
        await query.answer(
            results=[
                InlineQueryResultArticle(
                    title=f"Urban Dictionary Bot",
                    input_message_content=InputTextMessageContent(
                        "This is Urban Dictionary Bot. You can search any word or words sequence or even get random word here! \n\n**Ways** \n\n"
                        + Data.HELP
                    ),
                    url="https://t.me/OMG_info",
                    description="Welcome Aboard Homie!",
                    thumb_url="https://te.legra.ph/file/a9890c6b0888d84a9138e.jpg",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🔍 Search Words 🔍",
                                    switch_inline_query_current_chat="",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "♥ creator ♥",
                                    url="https://t.me/shado_hackers",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "🎨 Support Group 🎨",
                                    url="https://t.me/OMG_info",
                                )
                            ],
                        ]
                    ),
                )
            ],
            switch_pm_text="🔍 Know More",
            switch_pm_parameter="ntng",
            cache_time=1
        )
    elif query.query.lower() == "-r":
        word, rand_string = await rand()
        await query.answer(
            results=[
                InlineQueryResultArticle(
                    title=f"Random Word: {word}",
                    input_message_content=InputTextMessageContent(rand_string),
                    url="https://t.me/OMG_info",
                    description="Any Random Word",
                    thumb_url="https://te.legra.ph/file/a9890c6b0888d84a9138e.jpg",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🔍 Search More 🔍",
                                    switch_inline_query_current_chat="",
                                )
                            ]
                        ]
                    ),
                )
            ],
            switch_pm_text="🔍 Search More Words",
            switch_pm_parameter="ntng",
            cache_time=1
        )

    else:
        string = query.query
        try:
            the_word, rep = await ud_search(string)
            if rep == "Query Not Found: Doesn't exist in Urban Dictionary":
                word = "Query Not Found"
                description = "Couldn't found it! :("
            elif rep == "Don't try to search paragraphs":
                word = "Query Not Found"
                description = "Don't search paragraphs! :("
            else:
                word = the_word
                description = f'Definition of "{word}"'
            if len(word.split()) <= 3:
                switch = f'Definition of "{word}"'
            else:
                switch = "🔍 Search More"
            await query.answer(
                results=[
                    InlineQueryResultArticle(
                        title=f"{word}",
                        input_message_content=InputTextMessageContent(rep),
                        url="https://t.me/OMG_info",
                        description=description,
                        thumb_url="https://te.legra.ph/file/a9890c6b0888d84a9138e.jpg",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "Search More", switch_inline_query_current_chat=""
                                    )
                                ]
                            ]
                        ),
                    )
                ],
                switch_pm_text=switch,
                switch_pm_parameter="ntng",
                cache_time=1,
            )
        except:  # ValueException isn't defined bt used in that Pypi project. Sed
            pass
            # print("Library Bug. Try again")
