from core.clients.base import BaseAPIClient
from settings import TopicServiceAPIClientSettings


class TopicsServiceAPIClient(BaseAPIClient[TopicServiceAPIClientSettings]):
    async def get_topic(self, topic_id):
        response = await self._base_request(
            method="GET",
            endpoint=f"/topics/{topic_id}",
            success_status_codes=[200, 404],
        )

        data = (await response.json()).get("data")
        return data
