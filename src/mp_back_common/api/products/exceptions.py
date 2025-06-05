from fastapi import status

from ..exceptions import APIErrorResponseSchema, APIErrorSchema, BaseHTTPError


class EmptyProductNameHTTPError(BaseHTTPError):
    status_code = status.HTTP_400_BAD_REQUEST
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="EmptyProductName",
            message="Не указано название продукта",
        )
    )


class ProductNotFoundHTTPError(BaseHTTPError):
    status_code = status.HTTP_404_NOT_FOUND
    response_schema = APIErrorResponseSchema(
        error=APIErrorSchema(
            status=status_code,
            name="ProductNotFound",
            message="Не верный идентификатор продукта",
        )
    )
