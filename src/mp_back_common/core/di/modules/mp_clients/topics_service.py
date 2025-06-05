import aioinject

from ....clients.topics_service_client import TopicsServiceAPIClient
from ..._types import Providers

PROVIDERS: Providers = (aioinject.Scoped(TopicsServiceAPIClient),)
