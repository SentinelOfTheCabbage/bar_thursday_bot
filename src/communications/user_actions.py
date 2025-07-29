from telebot import TeleBot, types

from src.db_connector import save_users_visit
from src.helper import is_bar_thursday
from src.word_generator import get_code_word

def setup(bot: TeleBot):
    @bot.message_handler(func=lambda msg: msg.chat.id == msg.from_user.id)
    def message_handler(message: types.Message):
        user_id = message.from_user.id
        code_word = get_code_word()
        print(user_id, message.from_user.username)
        if not is_bar_thursday():
            bot.send_message(
                user_id,
                "Погожди, барный четверг либо уже закончился, либо будет чуть позже =(",
            )
        elif message.text in (f'/start {code_word}', code_word):
            save_users_visit(user_id)
            bot.send_message(user_id, "Пометил присутствие!")
        else:
            bot.send_message(user_id, "Пометил карандашиком хулигана =)")
