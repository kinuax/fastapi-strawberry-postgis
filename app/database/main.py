from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from app.settings import get_settings


class Base(MappedAsDataclass, DeclarativeBase):
    pass


settings = get_settings()
postgres_settings = {setting.removeprefix("postgres_"): value for setting, value in settings.model_dump().items()
                     if setting.startswith("postgres_")}
postgres_url = URL.create(**postgres_settings)
async_engine_args = {
    "url": postgres_url,
    "pool_recycle": 3600,
    "future": True,
}
if settings.debug:
    async_engine_args.update({"echo": True})
async_engine = create_async_engine(**async_engine_args)
async_session_factory = async_sessionmaker(async_engine, autoflush=False, expire_on_commit=False)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
