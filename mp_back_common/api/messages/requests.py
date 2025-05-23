from datetime import datetime, timezone
from typing import Literal

from ...core import enums
from pydantic import Field, field_validator, model_validator

from ...core import utils as core_utils
from ...api import schemas as api_schemas

# START GET MESSAGES REQUEST

class PaginationRequestSchema(api_schemas.APIRequestSchema):
    page: int = Field(gt=0)
    page_size: Literal[25, 50, 100]


class SortingRequestSchema(api_schemas.APIRequestSchema):
    order_by: core_utils.get_literal_type_from_enum(enums.OrderByEnum)
    direction: Literal["asc", "desc"] = "desc"

    @field_validator("order_by")
    def validate_and_map_order_by(cls, value: str) -> str:
        mapped = enums.OrderByEnum[value].value
        return mapped


class FilterRequestSchema(api_schemas.APIRequestSchema):
    date_from: datetime
    date_to: datetime
    search_query: str | None
    message_type: list[core_utils.get_literal_type_from_enum(enums.MessageTypeEnum)] = []
    content_type: list[core_utils.get_literal_type_from_enum(enums.ContentTypeEnum)] = []

    @model_validator(mode="after")
    def validate_dates(cls, values):
        if values.date_from > values.date_to:
            raise ValueError(
                "Дата начала (date_from) не может быть позже даты окончания (date_to)."
            )
        if values.date_to > datetime.now(timezone.utc):
            raise ValueError(
                "Дата окончания (date_to) не может быть позже текущей даты."
            )
        return values

    @field_validator("message_type")
    def validate_and_map_message_type(cls, value: list[str]) -> list[int]:
        result = []
        for item in value:
            result.append(enums.MessageTypeEnum[item].value)
        return result


class GetMessagesByTopicIdRequestSchema(api_schemas.APIRequestSchema):
    pagination: PaginationRequestSchema
    sorting: SortingRequestSchema
    filter: FilterRequestSchema

# END GET MESSAGES REQUEST