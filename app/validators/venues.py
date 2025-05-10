from typing import Any

from .uuids import validate_uuid, validate_uuids


def validate_venue_id(args: dict[str, Any]) -> dict[str, str]:
    return validate_uuid(args, "venue_id")


def validate_venue_ids(args: dict[str, Any]) -> dict[str, str]:
    return validate_uuids(args, "venue_ids")
