import aioinject
from ..._types import Providers
from .....db.dependencies import create_database_session

PROVIDERS: Providers = (aioinject.Scoped(create_database_session),)
