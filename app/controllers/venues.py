from uuid import UUID

from sqlalchemy import select

from app.database import get_async_session
from app.models import Town, Venue


select_town_venues = select(Town, Venue).join_from(Town, Venue)


async def get_venue(venue_id: str) -> tuple[Town, Venue] | None:
    async with get_async_session() as session:
        select_town_venue_by_id = select_town_venues.where(Venue.id == UUID(venue_id))
        try:
            row = next(await session.execute(select_town_venue_by_id))
        except StopIteration:
            return
        else:
            return row[0], row[1]


async def get_venues(town_id: str | None = None) -> list[tuple[Town, Venue]]:
    async with get_async_session() as session:
        select_filtered_town_venues = select_town_venues
        if town_id is not None:
            select_filtered_town_venues = select_filtered_town_venues.where(Town.id == UUID(town_id))
        results = []
        for row in await session.execute(select_filtered_town_venues):
            results.append((row[0], row[1]))
        return results
