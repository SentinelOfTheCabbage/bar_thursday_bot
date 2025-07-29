from telebot import TeleBot, types

from src.db_connector import save_users_visit


def setup(bot: TeleBot):
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

