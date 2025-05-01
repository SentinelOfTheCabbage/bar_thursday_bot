import asyncio
from telethon import TelegramClient
from telebot import TeleBot, types

from src import *
from src.service import make_flask_handler

bot = TeleBot(TOKEN, threaded=False)
words = None

BOT_ID = bot.get_me().id


@bot.chat_member_handler()
def chat_member_inviting(chat_member_update: types.ChatMemberUpdated):
    new_member = chat_member_update.new_chat_member
    status = new_member.status
    user_id = new_member.user.id
    if status == "member":  # member/kicked
        if not new_member.user.is_bot:
            save_users_visit(user_id)


@bot.my_chat_member_handler()
async def bot_inviting(chat_member_update: types.ChatMemberUpdated):
    new_member_id = chat_member_update.new_chat_member.user.id
    is_bot_just_added_to_chat = BOT_ID == new_member_id

    if is_bot_just_added_to_chat:
        pass
    else:
        pass


@bot.message_handler(content_types=["new_chat_members"])
def new_chat_member_handler(message: types.Message):
    user_id = message.new_chat_members[0].id

    if BOT_ID == user_id:
        print("bot added to chat")
    else:
        save_users_visit(user_id)
        print("someone added to chat")


@bot.message_handler(content_types=["left_chat_member"])
def left_chat_member_handler(message: types.Message):
    left_user_id = message.left_chat_member.id

    if BOT_ID == left_user_id:
        print("bot kicked from chat")


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


@bot.message_handler(func=lambda msg: msg.chat.id == msg.from_user.id)
def message_handler(message: types.Message):
    user_id = message.from_user.id
    code_word = get_code_word()

    if not is_bar_thursday():
        bot.send_message(
            user_id,
            "Погоди, барный четверг либо уже закончился, либо будет чуть позже =(",
        )
    elif message.text in (f'/start {code_word}', code_word):
        save_users_visit(user_id)
        bot.send_message(user_id, "Пометил присутствие!")
    else:
        bot.send_message(user_id, "Пометил карандашиком хулигана =)")


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
