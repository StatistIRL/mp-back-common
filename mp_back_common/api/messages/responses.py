from datetime import datetime
from mp_back_common.api.topics import exceptions as api_topics_excs
from .. import schemas as api_schemas

# START GET MESSAGES RESPONSE

class PaginationResponseSchema(api_schemas.BaseSchema):
    page: int
    page_size: int
    page_count: int
    total: int


class MetaSchema(api_schemas.BaseSchema):
    pagination: PaginationResponseSchema

class MessagePlatformReadSchema(api_schemas.BaseSchema):
    id: str | None
    name: str | None
    favicon_url: str | None


class MessageAuthorReadSchema(api_schemas.BaseSchema):
    name: str
    url: str


class MessageGeoReadSchema(api_schemas.BaseSchema):
    city: str | None
    region: str | None
    country: str | None


class MessageImageReadSchema(api_schemas.BaseSchema):
    url: str


class MessageVideoReadSchema(api_schemas.BaseSchema):
    url: str


class MessageReadSchema(api_schemas.BaseSchema):
    platform: MessagePlatformReadSchema
    id: str
    url: str
    create_date: datetime
    body: str | None
    pluses: str | None
    minuses: str | None
    type: int
    author: MessageAuthorReadSchema
    geo: MessageGeoReadSchema
    images: list[MessageImageReadSchema]
    videos: list[MessageVideoReadSchema]
    product_name: str
    rating: int | None


class GetMessageByTopicIdResponseSchema(api_schemas.APISuccessResponseSchema):
    data: list[MessageReadSchema]
    meta: MetaSchema


get_messages_by_topic_id_response_classes = [api_topics_excs.TopicNotFoundHTTPError]

# END GET MESSAGES RESPONSE