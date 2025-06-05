import math
from enum import Enum
from typing import Literal


def snake_to_lower_camel(snake_str: str) -> str:
    words = snake_str.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def get_pagination(total: int, page: int, page_size: int):
    page_count = math.ceil(total / page_size)
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "page_count": page_count,
    }


def get_literal_type_from_enum(enum: Enum) -> Literal:
    return Literal[*[item.name for item in enum]]
