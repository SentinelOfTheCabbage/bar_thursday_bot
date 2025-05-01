from telebot import TeleBot

from src import CHAT_ID


def make_poll(bot: TeleBot):
    bot.send_poll(
        CHAT_ID,
        "Кто пойдет на Барный четверг сегодня?",
        ["Я[ndex]", "Нет[фликс]"],
        is_anonymous=False,
    )
