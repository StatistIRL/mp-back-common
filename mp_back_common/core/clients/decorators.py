from functools import wraps
from typing import Any, Callable

from pydantic import BaseModel, ValidationError

from ...api.exceptions import BaseHTTPErrorProtocol
from ...api.schemas import BaseSchema


def validate_response(
    success_model: type[BaseSchema],
    response_models: list[type[BaseHTTPErrorProtocol]],
) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> BaseModel:
            result: Any = await func(*args, **kwargs)

            try:
                return success_model.model_validate(result)
            except ValidationError:
                pass

            for error_model in response_models:
                try:
                    return error_model.response_schema.model_validate(result)
                except ValidationError:
                    continue

            raise ValueError(
                f"Ответ не соответствует ни success_model, ни одной из response_models. Ответ: {result}"
            )

        return wrapper

    return decorator
