from app.api.builders.venues import build_venue
from app.api.types import Event
from app.models import Town as TownModel, Venue as VenueModel, Event as EventModel
from app.utils import get_str_from_datetime


def build_event(town: TownModel, venue: VenueModel, event: EventModel) -> Event:
    """Convert event from model to type."""
    return Event(
        id=event.id,
        venue=build_venue(town, venue),
        name=event.name,
        start=get_str_from_datetime(event.start),
        end=get_str_from_datetime(event.end),
        desc=event.desc,
    )
