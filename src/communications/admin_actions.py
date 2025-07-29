from telebot import TeleBot, types

from src.db_connector import is_admin
from src.word_generator import generate_qr_code, get_code_word

def setup(bot: TeleBot):
    @bot.message_handler(commands=["word"], func=is_admin)
    def get_word(message: types.Message):
        user_id = message.from_user.id

        response_pattern = "<i>Кодовое слово:</i>\n<blockquote><b>{code_word}</b></blockquote>"
        code_word = get_code_word()
        filename = generate_qr_code(code_word=code_word)

        response = response_pattern.format(code_word=code_word)
        bot.send_message(user_id, response, parse_mode="html")
        with open(filename, 'rb') as photo:
            bot.send_photo(user_id, photo)
