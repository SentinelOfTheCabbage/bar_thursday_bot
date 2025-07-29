from telebot import TeleBot, types

from src.consts import MASTER_ADMIN_ID
from src.db_connector import add_admin, is_admin, is_not_admin

def setup(bot: TeleBot):

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


    @bot.message_handler(commands=["promote"], func=is_not_admin)
    def promote_user(message: types.Message):
        user_id = message.from_user.id
        notification = (
            f"Юзер @{message.from_user.username} (id=`{user_id}`) хочет получить админ-права."
            "Для выдачи прав введите:\n"
            f"/promote {user_id}"
        )
        response = "Админ получил запрос на выдачу прав"
        bot.send_message(MASTER_ADMIN_ID, notification)
        bot.send_message(user_id, response)
