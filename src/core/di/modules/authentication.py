import aioinject

from ...middlewares.authentication import ClientIdContextVar
from ...middlewares.dto import UserCredentials
from .._types import Providers

PROVIDERS: Providers = (
    aioinject.Scoped(lambda: ClientIdContextVar.get(), UserCredentials),
)
