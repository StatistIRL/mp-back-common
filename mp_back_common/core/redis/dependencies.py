import contextlib
from typing import AsyncIterator

from redis.asyncio import Redis
from ...settings import RedisSettings


@contextlib.asynccontextmanager
async def create_redis_client(redis_settings: RedisSettings) -> AsyncIterator[Redis]:
    """
    Dependency for managing an Redis client.

    Yields:
        AsyncIterator[Redis]: An active Redis client opened within a context manager.
    """

    async with Redis(
        username=redis_settings.username,
        password=redis_settings.password,
        host=redis_settings.host,
        port=redis_settings.port,
    ) as redis:
        yield redis
