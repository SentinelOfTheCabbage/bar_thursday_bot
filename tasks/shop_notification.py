from telebot import TeleBot

from src import TOKEN, CHAT_ID

bot = TeleBot(TOKEN)

message = (
    "<b>Кхе-кхе! Коллеги</b>🥃\n<i>*привстал, поднял бокал, готовится к тосту*</i>\n\n"
    "Пора закупиться одним из представленных видов спиртного!"
)
drinks="🍻🥂🍷🍾🍸🍹"

bot.send_message(CHAT_ID, message, parse_mode="html")
bot.send_message(CHAT_ID, drinks)
