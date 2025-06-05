from datetime import date

from ..schemas import APISuccessResponseSchema, BaseSchema
from ..topics import exceptions as topics_excs
from . import exceptions as products_excs

# START GET PRODUCTS RESPONSE


class PaginationResponseSchema(BaseSchema):
    page: int
    page_size: int
    page_count: int
    total: int


class ProductReadResponseSchema(BaseSchema):
    url: str
    url_hash: str
    created_date: date
    original_name: str | None
    platform: str
    brand_name: str | None
    name: str | None


class MetaSchema(BaseSchema):
    pagination: PaginationResponseSchema


class GetProductsSuccessResponseSchema(APISuccessResponseSchema):
    data: list[ProductReadResponseSchema]
    meta: MetaSchema


get_products_response_classes = [topics_excs.TopicNotFoundHTTPError]

# END GET PRODUCTS RESPONSE

# START CREATE PRODUCT RESPONSE


class ProductCreateResponseSchema(BaseSchema):
    duplicate_urls: list[str]
    valid_urls: list[str]
    error_urls: list[str]


class CreateProductSuccessResponseSchema(APISuccessResponseSchema):
    data: ProductCreateResponseSchema
    meta: None = None


create_product_response_classes = [topics_excs.TopicNotFoundHTTPError]

# END CREATE PRODUCT RESPONSE

# START DELETE PRODUCT RESPONSE

delete_product_response_classes = [topics_excs.TopicNotFoundHTTPError]

# END DELETE PRODUCT RESPONSE

# START UPDATE PRODUCT RESPONSE

update_product_response_classes = [
    topics_excs.TopicNotFoundHTTPError,
    products_excs.EmptyProductNameHTTPError,
    products_excs.ProductNotFoundHTTPError,
]

# END UPDATE PRODUCT RESPONSE
