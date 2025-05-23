from fastapi import status

from ..exceptions import APIErrorResponseSchema, APIErrorSchema, BaseHTTPError


class CollectStartDateInFutureHTTPError(BaseHTTPError):
    status_code = status.HTTP_400_BAD_REQUEST
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="CollectStartDateInFuture",
            message="Дата начала сбора позже текущей даты.",
        )
    )


class CollectStartDateTooOldHTTPError(BaseHTTPError):
    status_code = status.HTTP_400_BAD_REQUEST
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="CollectStartDateTooOld",
            message="Дата начала сбора не может быть раньше чем 30 дней от текущей даты.",
        )
    )


class TopicNotFoundHTTPError(BaseHTTPError):
    status_code = status.HTTP_404_NOT_FOUND
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="TopicNotFound",
            message="Не верный идентификатор темы",
        )
    )


class InvalidTopicNameHTTPError(BaseHTTPError):
    status_code = status.HTTP_400_BAD_REQUEST
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="InvalidTopicName",
            message="Имя темы должно быть заполнено",
        )
    )


class TopicNameIsNotUniqueHTTPError(BaseHTTPError):
    status_code = status.HTTP_400_BAD_REQUEST
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="TopicNameIsNotUnique",
            message="Тема {TopicName} уже существует",
        )
    )
