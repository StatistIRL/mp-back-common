import aioinject
from core.di._types import Providers
from core.clients.topics_service_client import TopicsServiceAPIClient

PROVIDERS: Providers = [
    aioinject.Scoped(TopicsServiceAPIClient),
]
