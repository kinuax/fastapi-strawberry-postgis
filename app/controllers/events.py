from datetime import date, time
from uuid import UUID

from geoalchemy2 import WKTElement
from sqlalchemy import Integer, cast, select
from sqlalchemy.orm import with_expression
from sqlalchemy.sql.selectable import Select

from app.constants import TIME_MIN, TIME_MAX
from app.database import get_async_session
from app.models import Town, Venue, Event
from app.settings import get_settings
from app.utils import get_datetime_from_date_and_time, get_point_from_lat_lon


select_town_venue_events = select(Town, Venue, Event).join_from(Town, Venue).join_from(Venue, Event)


async def get_event(event_id: str) -> tuple[Town, Venue, Event] | None:
    async with get_async_session() as session:
        select_town_venue_event_by_id = select_town_venue_events.where(Event.id == UUID(event_id))
        try:
            row = next(await session.execute(select_town_venue_event_by_id))
        except StopIteration:
            return
        else:
            return row[0], row[1], row[2]


async def get_events(
    day: date,
    town_ids: list[str] | None = None,
    venue_ids: list[str] | None = None,
    lat: float | None = None,
    lon: float | None = None,
    radius: int | None = None,
    start_time: time | None = None,
    end_time: time | None = None,
) -> list[tuple[Town, Venue, Event]]:
    async with get_async_session() as session:
        select_filtered_town_venue_events = select_town_venue_events.order_by(Event.start, Event.end)
        if town_ids is not None:
            select_filtered_town_venue_events = get_events_by_town_ids(select_filtered_town_venue_events, town_ids)
        if venue_ids is not None:
            select_filtered_town_venue_events = get_events_by_venue_ids(select_filtered_town_venue_events, venue_ids)
        if lat is not None and lon is not None:
            point = get_point_from_lat_lon(lat, lon)
            select_filtered_town_venue_events = select_filtered_town_venue_events.options(
                with_expression(Venue.distance, cast(Venue.point.ST_Distance(point), Integer))
            )
            if radius is not None:
                select_filtered_town_venue_events = get_events_by_radius(
                    select_filtered_town_venue_events, point, radius
                )
        select_filtered_town_venue_events = get_events_by_time(
            select_filtered_town_venue_events, day, start_time, end_time
        )

        if get_settings().debug:
            query = str(select_filtered_town_venue_events.compile(compile_kwargs={"literal_binds": True}))
            print("########### QUERY ###########")
            print(query)
            print("#############################")

        results = []
        for row in await session.execute(select_filtered_town_venue_events):
            results.append((row[0], row[1], row[2]))
        return results


def get_events_by_town_ids(select_filtered_town_venue_events: Select, town_ids: list[str]) -> Select:
    town_ids = [UUID(town_id) for town_id in town_ids]
    return select_filtered_town_venue_events.where(Town.id.in_(town_ids))


def get_events_by_venue_ids(select_filtered_town_venue_events: Select, venue_ids: list[str]) -> Select:
    venue_ids = [UUID(venue_id) for venue_id in venue_ids]
    return select_filtered_town_venue_events.where(Venue.id.in_(venue_ids))


def get_events_by_radius(select_filtered_town_venue_events: Select, point: WKTElement, radius: int) -> Select:
    return select_filtered_town_venue_events.where(Venue.point.ST_DWithin(point, radius))


def get_events_by_time(
    select_filtered_town_venue_events: Select,
    day: date,
    start_time: time | None = None,
    end_time: time | None = None,
) -> Select:
    if start_time is None:
        start_time = TIME_MIN
    start = get_datetime_from_date_and_time(day, start_time)
    if end_time is None:
        end_time = TIME_MAX
    end = get_datetime_from_date_and_time(day, end_time)
    return select_filtered_town_venue_events.where(start <= Event.start, Event.start <= end)
