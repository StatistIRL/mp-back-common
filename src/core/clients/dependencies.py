import contextlib
from typing import AsyncIterator
import aiohttp


@contextlib.asynccontextmanager
async def create_aiohttp_session() -> AsyncIterator[aiohttp.ClientSession]:
    """
    Dependency for managing an aiohttp.ClientSession.

    Yields:
        AsyncIterator[aiohttp.ClientSession]: An active ClientSession.
    """
    async with aiohttp.ClientSession() as session:
        yield session