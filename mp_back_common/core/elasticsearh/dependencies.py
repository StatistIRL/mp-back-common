import contextlib
from typing import AsyncIterator

from elasticsearch import AsyncElasticsearch
from ...settings import ElasticSettings


@contextlib.asynccontextmanager
async def create_elasticsearch_client(
    settings: ElasticSettings,
) -> AsyncIterator[AsyncElasticsearch]:
    """
    Dependency for managing an Elasticsearch client.

    Yields:
        AsyncIterator[AsyncElasticsearch]: An active Elasticsearch client opened within a context manager.
    """

    async with AsyncElasticsearch(settings.url) as es:
        yield es
