from sqlalchemy import text

from app.database import Base, async_engine, get_async_session


async def create_tables() -> None:
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def load_tables(objs: list[Base]) -> None:
    async with get_async_session() as session:
        for obj in objs:
            session.add(obj)
            await session.commit()


async def truncate_tables(tables: list[str]) -> None:
    async with get_async_session() as session:
        for table in tables:
            truncate_stmt = text(f"TRUNCATE TABLE {table} CASCADE")
            await session.execute(truncate_stmt)
        await session.commit()


async def drop_tables(tables: list[str]) -> None:
    async with get_async_session() as session:
        for table in tables:
            drop_stmt = text(f"DROP TABLE {table}")
            await session.execute(drop_stmt)
        await session.commit()
