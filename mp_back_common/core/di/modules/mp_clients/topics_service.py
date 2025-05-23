import aioinject
from ..._types import Providers
from ....clients.topics_service_client import TopicsServiceAPIClient

PROVIDERS: Providers = (
    aioinject.Scoped(TopicsServiceAPIClient),
)