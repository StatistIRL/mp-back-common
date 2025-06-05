import aioinject

from ....elasticsearh.dependencies import create_elasticsearch_client
from ..._types import Providers

PROVIDERS: Providers = (aioinject.Scoped(create_elasticsearch_client),)
