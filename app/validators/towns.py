from typing import Any

from .uuids import validate_uuid, validate_uuids


def validate_town_id(args: dict[str, Any]) -> dict[str, str]:
    return validate_uuid(args, "town_id")


def validate_town_ids(args: dict[str, Any]) -> dict[str, str]:
    return validate_uuids(args, "town_ids")
