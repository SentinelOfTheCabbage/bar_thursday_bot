from telebot import TeleBot, types

from src import *
from src.service import make_flask_handler

bot = TeleBot(TOKEN, threaded=False)
words = None


@bot.message_handler(commands=["word"], func=is_admin)
def get_word(message: types.Message):
    response_pattern = (
        "<i>Кодовое слово:</i>\n<blockquote><b>{code_word}</b></blockquote>"
    )
    response = response_pattern.format(code_word=get_code_word())
    bot.send_message(message.from_user.id, response, parse_mode="html")


@bot.message_handler(commands=["promote"], func=is_admin)
def promote_admin(message: types.Message):
    user_id = message.from_user.id
    target_id = message.text[8:].strip()
    if len(target_id) == 0:
        bot.send_message(user_id, "Вы забыли указать user_id в запросе")
    elif target_id.isdecimal():
        add_admin(int(target_id))
        bot.send_message(user_id, f"Юзер {target_id} успешно добавлен в админы")
    else:
        bot.send_message(user_id, f"Не существует юзера с таким id")


@bot.message_handler(commands=["promote"], func=lambda m: not is_admin(m))
def promote_user(message: types.Message):
    user_id = message.from_user.id
    notification = (
        f"Юзер @{message.from_user.username} хочет получить админ-права."
        "Для выдачи прав введите:\n"
        f"/promote {user_id}"
    )
    response = "Админ получил запрос на выдачу прав"
    bot.send_message(MASTER_ADMIN_ID, notification)
    bot.send_message(user_id, response)


@bot.message_handler(
    func=lambda message: message.chat.id == message.from_user.id,
)
def message_handler(message: types.Message):
    user_id = message.from_user.id
    code_word = get_code_word()

    if not is_bar_thursday():
        bot.send_message(
            user_id,
            "Погоди, барный четверг либо уже закончился, либо будет чуть позже =(",
        )
    elif message.text == code_word:
        save_users_visit(user_id)
        bot.send_message(user_id, "Пометил карандашиком присутствие!")
    else:
        bot.send_message(user_id, "Пометил карандашиком хулигана =)")


if __name__ == "__main__":
    if MODE == WorkingMode.POLLING:
        bot.polling()
    elif MODE == WorkingMode.WEB_HOOK:
        secret = "wabalabadabdab"
        bot.set_webhook(
            "https://neildub.pythonanywhere.com/{}".format(SECRET), max_connections=1
        )
        make_flask_handler(bot)
