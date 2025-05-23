import aioinject
from core.di._types import Providers
from core.elasticsearh.dependencies import create_elasticsearch_client

PROVIDERS: Providers = [aioinject.Scoped(create_elasticsearch_client)]
