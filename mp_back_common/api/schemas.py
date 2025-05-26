from typing import Any

from pydantic import BaseModel, ConfigDict

from ..core.utils import snake_to_lower_camel


class BaseSchema(BaseModel):
    """
    Base class for all schemas in the project.
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=snake_to_lower_camel,
    )


class APIRequestSchema(BaseSchema):
    pass


class APISuccessResponseSchema(BaseSchema):
    data: Any
    meta: Any


class APIErrorSchema(BaseSchema):
    status: int
    name: str
    message: str


class APIErrorResponseSchema(BaseSchema):
    data: None = None
    error: APIErrorSchema
