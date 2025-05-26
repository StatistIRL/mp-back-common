from datetime import date, timedelta

from pydantic import field_validator

from ..schemas import BaseSchema
from ..topics import exceptions as topic_api_excs

# START CREATE TOPIC REQUEST


class TopicCreateRequestSchema(BaseSchema):
    topic_name: str
    include_search_query: str
    exclude_search_query: str | None = None
    collect_start_date: date

    @field_validator("collect_start_date")
    def validate_collect_start_date(cls, value):
        today = date.today()
        thirty_days_ago = today - timedelta(days=30)

        if value > today:
            raise topic_api_excs.CollectStartDateInFutureHTTPError()
        if value < thirty_days_ago:
            raise topic_api_excs.CollectStartDateTooOldHTTPError()

        return value

    @field_validator("topic_name")
    def validate_topic_name(cls, value):
        if not value.strip():
            raise topic_api_excs.InvalidTopicNameHTTPError()

        return value


# END CREATE TOPIC REQUEST

# START UPDATE TOPIC REQUEST


class TopicUpdateSchema(BaseSchema):
    topic_name: str

    @field_validator("topic_name")
    def validate_topic_name(cls, value):
        if not value.strip():
            raise topic_api_excs.InvalidTopicNameHTTPError()

        return value


# END UPDATE TOPIC REQUEST
