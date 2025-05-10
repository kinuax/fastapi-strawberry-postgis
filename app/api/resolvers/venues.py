from app.api.builders import build_venue
from app.api.types import Venue
from app.validators import validate_args
from app.controllers import get_venue, get_venues


async def get_venue_resolver(venue_id: str) -> Venue | None:
    if errors := validate_args({"venue_id": venue_id}):
        raise Exception(errors)
    if town_venue := await get_venue(venue_id):
        return build_venue(*town_venue)


async def get_venues_resolver(town_id: str | None = None) -> list[Venue]:
    if town_id is not None and (errors := validate_args({"town_id": town_id})):
        raise Exception(errors)
    venues = []
    for town, venue in await get_venues(town_id):
        venues.append(build_venue(town, venue))
    return venues
