from typing import Any

from .events import validate_event_id
from .space import validate_lat, validate_lon, validate_radius
from .towns import validate_town_id, validate_town_ids
from .time import validate_day, validate_start_time, validate_end_time
from .venues import validate_venue_id, validate_venue_ids


validators = {
    # Space.
    "lat": validate_lat,
    "lon": validate_lon,
    "radius": validate_radius,
    # Time.
    "day": validate_day,
    "start_time": validate_start_time,
    "end_time": validate_end_time,
    # Models.
    "town_id": validate_town_id,
    "town_ids": validate_town_ids,
    "venue_id": validate_venue_id,
    "venue_ids": validate_venue_ids,
    "event_id": validate_event_id,
}


def validate_args(args: dict[str, Any]) -> dict[str, str]:
    errors = {}
    for arg in args:
        errors.update(validators[arg](args))
    return errors
