from typing import Any

from .uuids import validate_uuid


def validate_event_id(args: dict[str, Any]) -> dict[str, str]:
    return validate_uuid(args, "event_id")
