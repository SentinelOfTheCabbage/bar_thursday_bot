sqlite-utils migrate db/users_visits.db migrations/users_visits.py
sqlite-utils migrate db/admins.db migrations/admins.py

python3 -B bot.py
