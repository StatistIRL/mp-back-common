from typing import Literal

from pydantic import Field, field_validator

from ...core.products import enums as products_enums
from ...core.utils import get_literal_type_from_enum
from ..schemas import BaseSchema
from . import exceptions as products_excs

# START GET PRODUCTS REQUEST


class PaginationRequestSchema(BaseSchema):
    page: int = Field(gt=0)
    page_size: Literal[25, 50, 100]


class SortingRequestSchema(BaseSchema):
    order_by: Literal[get_literal_type_from_enum(products_enums.OrderByEnum)]  # type: ignore
    direction: Literal["asc", "desc"] = "desc"

    @field_validator("order_by")
    def validate_and_map_order_by(cls, value: str) -> str:
        mapped = products_enums.OrderByEnum[value]
        return mapped


class ProductsReadRequestSchema(BaseSchema):
    pagination: PaginationRequestSchema
    sorting: SortingRequestSchema


# END GET PRODUCTS REQUEST

# START CREATE PRODUCT REQUEST


class ProductCreateRequestSchema(BaseSchema):
    urls: list[str]


# END CREATE PRODUCTS REQUEST

# START UPDATE PRODUCT REQUEST


class ProductUpdateRequestSchema(BaseSchema):
    product_name: str

    @field_validator("product_name")
    def validate_product_name(cls, value: str):
        if not value.strip():
            raise products_excs.EmptyProductNameHTTPError()
        return value


# END UPDATE PRODUCTS REQUEST

# START DELETE PRODUCT REQUEST


class ProductDeleteRequestSchema(BaseSchema):
    topic_product_ids: list[str]


# END DELETE PRODUCTS REQUEST
