from ...api.topics import responses as api_topics_responses
from ...settings import TopicServiceAPIClientSettings
from .base import BaseAPIClient
from .decorators import validate_response


class TopicsServiceAPIClient(BaseAPIClient[TopicServiceAPIClientSettings]):
    @validate_response(
        success_model=api_topics_responses.GetTopicByIdResponseSchema,
        response_models=api_topics_responses.get_topic_by_id_response_classes,
    )
    async def get_topic_by_id(self, topic_id: int) -> api_topics_responses.GetTopicByIdResponseSchema | None:
        response = await self._base_request(
            method="GET",
            endpoint=f"/topics/{topic_id}",
            success_status_codes=[200, 404],
        )
        return await response.json()
