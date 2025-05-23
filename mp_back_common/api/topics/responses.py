from ..schemas import APISuccessResponseSchema
from . import exceptions as api_topics_excs
from . import schemas as topics_schemas


class CreateTopicResponseSchema(APISuccessResponseSchema):
    data: topics_schemas.TopicReadIdSchema
    meta: None = None


create_topic_error_classes = [
    api_topics_excs.CollectStartDateTooOldHTTPError,
    api_topics_excs.CollectStartDateInFutureHTTPError,
    api_topics_excs.TopicNameIsNotUniqueHTTPError,
]


class GetTopicsResponseSchema(APISuccessResponseSchema):
    data: list[topics_schemas.TopicItemReadSchema]
    meta: None = None


get_topics_response_classes = []


class GetTopicByIdResponseSchema(APISuccessResponseSchema):
    data: topics_schemas.TopicReadSchema
    meta: None = None


get_topic_by_id_response_classes = [api_topics_excs.TopicNotFoundHTTPError]

update_topic_response_classes = [
    api_topics_excs.InvalidTopicNameHTTPError,
    api_topics_excs.TopicNotFoundHTTPError,
    api_topics_excs.TopicNameIsNotUniqueHTTPError,
]

delete_topic_response_classes = [api_topics_excs.TopicNotFoundHTTPError]
