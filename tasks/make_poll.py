from telebot import TeleBot

from src import TOKEN, CHAT_ID

bot = TeleBot(TOKEN)

bot.send_poll(
    CHAT_ID,
    "Кто пойдет на Барный четверг сегодня?",
    ["Я[ndex]", "Нет[фликс]"],
    is_anonymous=False,
)
