import strawberry

from app.api.resolvers import (
    get_town_resolver,
    get_towns_resolver,
    get_venue_resolver,
    get_venues_resolver,
    get_event_resolver,
    get_events_resolver,
)
from app.api.types import Town, Venue, Event


@strawberry.type
class Query:
    town: Town | None = strawberry.field(resolver=get_town_resolver)
    towns: list[Town] = strawberry.field(resolver=get_towns_resolver)
    venue: Venue | None = strawberry.field(resolver=get_venue_resolver)
    venues: list[Venue] = strawberry.field(resolver=get_venues_resolver)
    event: Event | None = strawberry.field(resolver=get_event_resolver)
    events: list[Event] = strawberry.field(resolver=get_events_resolver)


schema = strawberry.Schema(Query)
