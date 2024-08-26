from flask import Flask, request
from telebot import TeleBot, types
from src.consts import SECRET

app = Flask(__name__)

def make_flask_handler(bot: TeleBot):
    @app.route("/{}".format(SECRET), methods=["POST"])
    def telegram_webhook():
        update = types.Update.de_json(request.get_json())
        bot.process_new_updates(update)
        return "OK"
    return telegram_webhook