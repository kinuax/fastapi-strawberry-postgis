from app.api.builders import build_event
from app.api.types import Event
from app.validators import validate_args
from app.controllers import get_event, get_events


async def get_event_resolver(event_id: str) -> Event | None:
    if errors := validate_args({"event_id": event_id}):
        raise Exception(errors)
    if town_place_event := await get_event(event_id):
        return build_event(*town_place_event)


async def get_events_resolver(
    day: str,
    town_ids: list[str] | None = None,
    venue_ids: list[str] | None = None,
    lat: float | None = None,
    lon: float | None = None,
    radius: int | None = None,
    start_time: str | None = None,
    end_time:  str | None = None,
) -> list[Event]:
    args = {arg: value for arg, value in locals().items() if value is not None}
    if errors := validate_args(args):
        raise Exception(errors)
    events = []
    for town, place, event in await get_events(**args):
        events.append(build_event(town, place, event))
    return events
