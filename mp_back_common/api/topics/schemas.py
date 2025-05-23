from datetime import date, datetime, timedelta

from pydantic import field_validator

from ..schemas import BaseSchema
from . import exceptions as api_topics_excs


class TopicCreateSchema(BaseSchema):
    topic_name: str
    include_search_query: str
    exclude_search_query: str | None = None
    collect_start_date: date

    @field_validator("collect_start_date")
    def validate_collect_start_date(cls, value):
        today = date.today()
        thirty_days_ago = today - timedelta(days=30)

        if value > today:
            raise api_topics_excs.CollectStartDateInFutureHTTPError()
        if value < thirty_days_ago:
            raise api_topics_excs.CollectStartDateTooOldHTTPError()

        return value

    @field_validator("topic_name")
    def validate_topic_name(cls, value):
        if not value.strip():
            raise api_topics_excs.InvalidTopicNameHTTPError()

        return value


class TopicReadIdSchema(BaseSchema):
    topic_id: int


class TopicItemReadSchema(BaseSchema):
    topic_id: int
    topic_name: str


class TopicReadSchema(BaseSchema):
    topic_id: int
    topic_name: str
    include_search_query: str
    exclude_search_query: str | None
    collect_start_date: str
    create_date: datetime
    modify_date: datetime | None

    @field_validator("collect_start_date", mode="before")
    def validate_and_convert_date(cls, value: date) -> str:
        return value.strftime("%Y-%m-%d")


class TopicUpdateSchema(BaseSchema):
    topic_name: str

    @field_validator("topic_name")
    def validate_topic_name(cls, value):
        if not value.strip():
            raise api_topics_excs.InvalidTopicNameHTTPError()

        return value
