from sqlalchemy import text

from app.database import async_engine, Base, get_async_session


async def create_tables() -> None:
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def drop_tables(tables: list[str]) -> None:
    async with get_async_session() as session:
        for table in tables:
            drop_stmt = text(f"DROP TABLE {table}")
            await session.execute(drop_stmt)
        await session.commit()


async def truncate_tables(tables: list[str]) -> None:
    async with get_async_session() as session:
        for table in tables:
            truncate_stmt = text(f"TRUNCATE TABLE {table}")
            await session.execute(truncate_stmt)
        await session.commit()
