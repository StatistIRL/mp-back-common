from typing import Optional, Protocol

from api.schemas import BaseSchema
from fastapi import status


class APIErrorSchema(BaseSchema):
    status: int
    name: str
    message: str


class APIErrorResponseSchema(BaseSchema):
    data: Optional[None] = None
    error: APIErrorSchema


class BaseHTTPErrorProtocol(Protocol):
    status_code: int
    response_schema: APIErrorResponseSchema


class BaseHTTPError(BaseHTTPErrorProtocol, Exception):
    pass


class ServerHTTPError(BaseHTTPError):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="InternalServerError",
            message="(Внутренняя ошибка сервера)",
        )
    )
