import aioinject

from .....db.dependencies import create_database_session
from ..._types import Providers

PROVIDERS: Providers = (aioinject.Scoped(create_database_session),)
