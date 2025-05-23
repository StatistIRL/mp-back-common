from datetime import date, datetime

from pydantic import field_validator
from .. import schemas as api_schemas
from . import exceptions as api_topics_excs


# START CREATE TOPIC RESPONSE

class TopicReadIdSchema(api_schemas.BaseSchema):
    topic_id: int

class CreateTopicResponseSchema(api_schemas.APISuccessResponseSchema):
    data: TopicReadIdSchema
    meta: None = None


create_topic_error_classes = [
    api_topics_excs.CollectStartDateTooOldHTTPError,
    api_topics_excs.CollectStartDateInFutureHTTPError,
    api_topics_excs.TopicNameIsNotUniqueHTTPError,
]

# END CREATE TOPIC RESPONSE

# START GET TOPICS RESPONSE

class TopicItemReadSchema(api_schemas.BaseSchema):
    topic_id: int
    topic_name: str

class GetTopicsResponseSchema(api_schemas.APISuccessResponseSchema):
    data: list[TopicItemReadSchema]
    meta: None = None


get_topics_response_classes = []

# END GET TOPICS RESPONSE

# START GET TOPIC BY ID RESPONSE

class TopicReadSchema(api_schemas.BaseSchema):
    topic_id: int
    topic_name: str
    include_search_query: str
    exclude_search_query: str | None
    collect_start_date: str
    create_date: datetime
    modify_date: datetime | None

    @field_validator("collect_start_date", mode="before")
    def validate_and_convert_date(cls, value: date | str) -> str:
        if isinstance(value, str):
            return value
        return value.strftime("%Y-%m-%d")

class GetTopicByIdResponseSchema(api_schemas.APISuccessResponseSchema):
    data: TopicReadSchema
    meta: None = None


get_topic_by_id_response_classes = [api_topics_excs.TopicNotFoundHTTPError]

# END GET TOPIC BY ID RESPONSE

# START UPDATE TOPIC RESPONSE

update_topic_response_classes = [
    api_topics_excs.InvalidTopicNameHTTPError,
    api_topics_excs.TopicNotFoundHTTPError,
    api_topics_excs.TopicNameIsNotUniqueHTTPError,
]

# END UPDATE TOPIC RESPONSE

# START DELETE TOPIC RESPONSE

delete_topic_response_classes = [api_topics_excs.TopicNotFoundHTTPError]

# END DELETE TOPIC RESPONSE
