from flask import app
from telebot import TeleBot

from src.communications import setup_communications
from src.consts import *
from src.service import make_flask_handler

bot = TeleBot(TOKEN, threaded=False)
words = None

setup_communications(bot)

if __name__ == "__main__":
    if MODE == WorkingMode.POLLING:
        bot.polling(allowed_updates=["chat_member", "message"])
    elif MODE == WorkingMode.WEB_HOOK:
        secret = "wabalabadabdab"
        bot.set_webhook(
            "https://neildub.pythonanywhere.com/{}".format(SECRET), max_connections=1
        )
        make_flask_handler(bot)
        app.run()
