from typing import Any
from uuid import UUID


def validate_uuid(args: dict[str, Any], arg: str, values: list[str] | None = None) -> dict[str, str]:
    errors = {}
    if arg in args:
        id_ = args[arg]
        try:
            UUID(id_, version=4)
        except ValueError:
            errors[f"{arg}"] = "invalid uuid"
            return errors
        if values is not None and id_ not in values:
            errors[f"{arg}"] = f"should be {values}"
    return errors


def validate_uuids(args: dict[str, Any], arg: str, values: list[str] | None = None) -> dict[str, str]:
    errors = {}
    if arg in args:
        for id_ in args[arg]:
            try:
                UUID(id_, version=4)
            except ValueError:
                errors[f"{arg} - {id_}"] = "invalid uuid"
                continue
            if values is not None and id_ not in values:
                errors[f"{arg} - {id_}"] = f"should be {values}"
    return errors
