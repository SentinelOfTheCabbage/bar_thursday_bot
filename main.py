import os
from enum import Enum
import hashlib
from datetime import datetime

from telebot import TeleBot, types
import qrcode


class WorkingMode(Enum):
    POLLING = "POLLING"
    WEB_HOOK = "WEB_HOOK"


ENV_API_TOKEN_KEY = "TELEGRAM_API_KEY"
ENV_MODE_KEY = "WORK_MODE"
ENV_ENCRYPT_TOKEN_KEY = "ENCRYPT_KEY"

TOKEN = os.getenv(ENV_API_TOKEN_KEY)
# MODE = WorkingMode(os.getenv(ENV_MODE_KEY))
ENCRYPT_KEY = os.getenv(ENV_ENCRYPT_TOKEN_KEY)

bot = TeleBot(TOKEN)
bot.get_my_name()


def is_thursday():
    return datetime.now().weekday() == 3


def generate_secret(key, message):
    return hashlib.sha256(f"{message}_{key}".encode()).hexdigest()


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    if not is_thursday():
        return
    elif message.text != f"/start {generate_secret()}":
        return
    # TODO: update presence
    pass


def generate_qrcode(key: str = ENCRYPT_KEY, message: str = datetime.now().isoformat()):
    secret = generate_secret(key, message)

    link_pattern = "https://t.me/{bot_username}?start={secret}"
    link = link_pattern.format(bot_username=bot.get_me().username, secret=secret)

    filename = "file.png"
    img = qrcode.make(link)
    img.save(filename)

    return filename


def send_image(user_id, qrcode_filename):
    bot.send_chat_action(user_id, "upload_photo")
    with open(qrcode_filename, "rb") as image:
        bot.send_photo(user_id, image)


@bot.message_handler(commands=["qrcode"])
def handle_qrcode(message: types.Message):
    user_id = message.from_user.id

    if datetime.now().weekday() != 3:
        bot.send_message(user_id, "It's not thursday, my dude =(")
        return

    qrcode_filename = generate_qrcode()
    send_image(user_id, qrcode_filename)


if __name__ == "__main__":
    bot.polling()
