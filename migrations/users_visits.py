from sqlite_migrate import Migrations
from datetime import datetime

table_name = "users_visits"
migration = Migrations(table_name)


@migration()
def m01_create_users_table(db):
    db[f'db/{table_name}'].create(
        {
            "user_id": int,
            "last_visit": datetime,
            "counter": int ,
        },
        pk="user_id",
    )
