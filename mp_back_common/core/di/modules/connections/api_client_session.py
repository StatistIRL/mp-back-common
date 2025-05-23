import aioinject
from ....clients.dependencies import create_aiohttp_session
from ..._types import Providers

PROVIDERS: Providers = [aioinject.Scoped(create_aiohttp_session)]
