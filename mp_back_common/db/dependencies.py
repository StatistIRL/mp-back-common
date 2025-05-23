import contextlib
from typing import AsyncIterator

from settings import DatabaseSettings
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)


@contextlib.asynccontextmanager
async def create_database_session(
    settings: DatabaseSettings,
) -> AsyncIterator[AsyncSession]:
    """
    Dependency for managing an SQLAlchemy session.

    Yields:
        AsyncIterator[AsyncSession]: An active SQLAlchemy session opened within a context manager.
    """
    engine = create_async_engine(url=settings.url)
    async with async_sessionmaker(bind=engine).begin() as session:
        yield session
