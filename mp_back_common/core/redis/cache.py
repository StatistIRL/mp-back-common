import json
from typing import Type, TypeVar

from redis.asyncio import Redis
from settings import BaseRedisCacheSettings

TBaseRedisCacheSettings = TypeVar(
    "TBaseRedisCacheSettings", bound=BaseRedisCacheSettings
)


class RedisCache:
    def __init__(self, redis: Redis, settings: Type[TBaseRedisCacheSettings]):
        self.__redis = redis
        self.settings = settings

    async def get(self, key: str) -> dict | None:
        cache_obj = await self.__redis.get(f"{self.settings.prefix}:{key}")
        if cache_obj:
            return json.loads(cache_obj.decode("utf-8"))

    async def set(self, key: str, data: dict) -> None:
        await self.__redis.set(
            f"{self.settings.prefix}:{key}",
            json.dumps(data),
            ex=self.settings.cache_ttl_seconds,
        )
