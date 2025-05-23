import aioinject

from ....redis.dependencies import create_redis_client
from ..._types import Providers

PROVIDERS: Providers = (aioinject.Scoped(create_redis_client),)
