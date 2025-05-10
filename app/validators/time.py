from typing import Any

from app.constants import DATE_FORMAT_REPR, TIME_FORMAT_REPR
from app.utils import get_date_from_str, get_time_from_str


def validate_day(args: dict[str, Any]) -> dict[str, str]:
    errors = {}
    try:
        args["day"] = get_date_from_str(args["day"])
    except ValueError:
        errors["day"] = f"should have valid {DATE_FORMAT_REPR} format"
    return errors


def validate_time(args: dict[str, Any], time_arg: str) -> dict[str, str]:
    errors = {}
    if time_arg in args:
        try:
            args[time_arg] = get_time_from_str(args[time_arg])
        except ValueError:
            errors[time_arg] = f"should have valid {TIME_FORMAT_REPR} format"
    return errors


def validate_start_time(args: dict[str, Any]) -> dict[str, str]:
    return validate_time(args, "start_time")


def validate_end_time(args: dict[str, Any]) -> dict[str, str]:
    if errors := validate_time(args, "end_time"):
        return errors
    if "start_time" in args and not (args["start_time"] < args["end_time"]):
        errors["end_time"] = "should be greater than start_time"
    return errors
