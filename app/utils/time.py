from datetime import date, datetime, time

from app.constants import DATE_FORMAT, DATETIME_FORMAT, TIME_FORMAT


def get_date_from_str(d_str: str) -> date:
    return datetime.strptime(d_str, DATE_FORMAT).date()


def get_time_from_str(t_str: str) -> time:
    return datetime.strptime(t_str, TIME_FORMAT).time()


def get_datetime_from_str(dt_str: str) -> datetime:
    return datetime.strptime(dt_str, DATETIME_FORMAT)


def get_datetime_from_date_and_time(d: date, t: time) -> datetime:
    return datetime.combine(d, t)


def get_str_from_date(d: date) -> str:
    return d.strftime(DATE_FORMAT)


def get_str_from_time(t: time) -> str:
    return t.strftime(TIME_FORMAT)


def get_str_from_datetime(dt: datetime) -> str:
    return dt.strftime(DATETIME_FORMAT)
