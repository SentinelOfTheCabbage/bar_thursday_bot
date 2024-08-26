import os
from sqlite_migrate import Migrations
from sqlite3 import Connection


table_name = "admins"
migration = Migrations(table_name)

ENV_MASTER_ADMIN_ID_KEY = "ADMIN_ID"
MASTER_ADMIN_ID = int(os.getenv(ENV_MASTER_ADMIN_ID_KEY))


@migration()
def m01_create_admins_table(db: Connection):
    db[f"db/{table_name}"].create(
        {
            "user_id": int,
        },
        pk="user_id",
    )

    db[f"db/{table_name}"].insert({"user_id": MASTER_ADMIN_ID})
