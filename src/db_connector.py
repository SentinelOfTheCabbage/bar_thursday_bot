import sqlite3
from datetime import datetime

user_visits_table_name = "db/users_visits"
admins_table_name = "db/admins"


def get_visits_connection():
    return sqlite3.connect(f"{user_visits_table_name}.db")


def get_admins_connection():
    return sqlite3.connect(f"{admins_table_name}.db")


def save_users_visit(user_id):
    get_visits_connection().cursor().execute(
        (
            "INSERT INTO "
            f"'{user_visits_table_name}' AS src (user_id, last_visit, counter) VALUES "
            f'(?, "{datetime.now().isoformat()}",  1) ON CONFLICT (user_id)'
            "DO UPDATE SET counter=excluded.counter+1;"
        ),
        (user_id,),
    )


def add_admin(user_id: int):
    get_admins_connection().cursor().execute(
        f"INSERT INTO '{admins_table_name}' VALUES (?)", (user_id,)
    )


def is_admin(message):
    user_id = message.from_user.id
    result = (
        get_admins_connection()
        .cursor()
        .execute(f"SELECT * FROM '{admins_table_name}' WHERE user_id = ?;", (user_id,))
    )
    return bool(result.fetchone())
