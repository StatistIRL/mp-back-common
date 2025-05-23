import aioinject
from ..._types import Providers
from ....redis.dependencies import create_redis_client

PROVIDERS: Providers = (aioinject.Scoped(create_redis_client),)
