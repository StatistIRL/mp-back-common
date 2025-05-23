from typing import Protocol

from fastapi import status

from .schemas import APIErrorResponseSchema, APIErrorSchema


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
