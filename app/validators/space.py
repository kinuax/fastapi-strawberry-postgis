from typing import Any

from app.constants import LAT_MIN, LAT_MAX, LON_MIN, LON_MAX


def validate_lat(args: dict[str, Any]) -> dict[str, str]:
    errors = {}
    if "lat" in args:
        if not (LAT_MIN <= args["lat"] <= LAT_MAX):
            errors["lat"] = f"should be between {LAT_MIN} and {LAT_MAX}"
        if "lon" not in args:
            errors["lon"] = "missing"
    return errors


def validate_lon(args: dict[str, Any]) -> dict[str, str]:
    errors = {}
    if "lon" in args:
        if not (LON_MIN <= args["lon"] <= LON_MAX):
            errors["lon"] = f"should be between {LON_MIN} and {LON_MAX}"
        if "lat" not in args:
            errors["lat"] = "missing"
    return errors


def validate_radius(args: dict[str, Any]) -> dict[str, str]:
    errors = {}
    if "radius" in args:
        if args["radius"] <= 0:
            errors["radius"] = "should be positive"
        if "lat" not in args:
            errors["lat"] = "missing"
        if "lon" not in args:
            errors["lon"] = "missing"
    return errors
