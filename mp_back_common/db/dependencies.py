import contextlib
from typing import AsyncIterator

from db.engine import async_session_factory
from sqlalchemy.ext.asyncio import AsyncSession


@contextlib.asynccontextmanager
async def create_session() -> AsyncIterator[AsyncSession]:
    """
    Dependency for managing an SQLAlchemy session.

    Yields:
        AsyncIterator[AsyncSession]: An active SQLAlchemy session opened within a context manager.
    """
    async with async_session_factory.begin() as session:
        yield session
