from datetime import datetime, timedelta, timezone


def get_current_time() -> datetime:
    tz_info = timezone(timedelta(hours=3))
    return datetime.now(tz_info)


def get_current_weekday():
    return get_current_time().weekday()


def get_current_hour():
    return get_current_time().hour


def is_bar_thursday():
    weekday = get_current_weekday()
    hour = get_current_hour()
    is_thursday = (weekday == 3) and (hour > 18)
    is_friday_beginning = (weekday == 4) and (hour < 3)
    return is_thursday or is_friday_beginning
