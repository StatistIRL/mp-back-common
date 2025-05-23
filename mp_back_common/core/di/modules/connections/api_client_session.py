import aioinject
from core.clients.dependencies import create_aiohttp_session
from core.di._types import Providers

PROVIDERS: Providers = [aioinject.Scoped(create_aiohttp_session)]
