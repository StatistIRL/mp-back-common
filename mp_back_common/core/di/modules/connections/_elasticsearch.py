import aioinject
from ..._types import Providers
from ....elasticsearh.dependencies import create_elasticsearch_client

PROVIDERS: Providers = (aioinject.Scoped(create_elasticsearch_client),)
