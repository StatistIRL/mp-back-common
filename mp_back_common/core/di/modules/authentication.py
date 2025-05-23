import aioinject
from .._types import Providers
from ...middlewares.authentication import ClientIdContextVar
from ...middlewares.dto import UserCredentials

PROVIDERS: Providers = (
    aioinject.Scoped(lambda: ClientIdContextVar.get(), UserCredentials),
)