import aioinject
from core.di._types import Providers
from core.redis.dependencies import create_redis_client

PROVIDERS: Providers = [aioinject.Scoped(create_redis_client)]
