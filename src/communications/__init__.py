from telebot import TeleBot

from .invites import setup as setup_invites
from .admin_actions import setup as setup_admin_actions
from .admin_promoting import setup as setup_admin_promotings
from .user_actions import setup as setup_user_actions

def setup_communications(bot: TeleBot):
    setup_invites(bot)
    setup_admin_actions(bot)
    setup_admin_promotings(bot)
    setup_user_actions(bot)
