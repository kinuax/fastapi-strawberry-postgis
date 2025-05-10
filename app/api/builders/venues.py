from app.api.builders.towns import build_town
from app.api.types import Point, Venue
from app.models import Town as TownModel, Venue as VenueModel
from app.utils import get_lat_lon_from_point


def build_venue(town: TownModel, venue: VenueModel) -> Venue:
    """Convert venue from model to type."""
    lat, lon = get_lat_lon_from_point(venue.point)
    return Venue(
        id=venue.id,
        town=build_town(town),
        name=venue.name,
        point=Point(lat=lat, lon=lon),
        address=venue.address,
        distance=venue.distance,
    )
