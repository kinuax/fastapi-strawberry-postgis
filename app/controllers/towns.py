from uuid import UUID

from sqlalchemy import select

from app.database import get_async_session
from app.models import Town


select_towns = select(Town)


async def get_town(town_id: str) -> Town | None:
    async with get_async_session() as session:
        select_town_by_id = select_towns.where(Town.id == UUID(town_id))
        try:
            return next(await session.scalars(select_town_by_id))
        except StopIteration:
            return


async def get_towns() -> list[Town]:
    async with get_async_session() as session:
        return await session.scalars(select_towns)
