from datetime import datetime, timedelta, timezone

def get_modified_time():
    # I think best time for Bar4etverg is between next two times:
    # - 18:00+0300 (thursday) -> 06:00+0300 (friday)
    # Let's fix-move hours to -18h: 00:00 -> 12:00 (both thursday)
    tz_info = timezone(timedelta(hours=3))
    fix_timedelta = timedelta(hours=18)

    return datetime.now(tz_info) - fix_timedelta


def get_day_isoformat():
    modified_datetime = get_modified_time()
    return modified_datetime.strftime("%Y-%m-%d")


def is_bar_thursday():
    modified_datetime = get_modified_time()
    is_bar_time = modified_datetime.hour < 12

    thursday = 3
    tz_info = timezone(timedelta(hours=3))
    is_thursday = datetime.now(tz_info).weekday == thursday

    return is_thursday and is_bar_time
