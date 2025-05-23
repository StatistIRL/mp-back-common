from functools import wraps
from typing import Any, Callable

from pydantic import ValidationError

from ...api.exceptions import BaseHTTPError
from ...api.schemas import BaseSchema


def validate_response(
    success_model: type[BaseSchema],
    response_models: list[type[BaseHTTPError]],
) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> BaseSchema | None:
            result: Any = await func(*args, **kwargs)

            try:
                return success_model.model_validate(result)
            except ValidationError:
                pass

            for response_model in response_models:
                try:
                    response_model.response_schema.model_validate(result)
                    raise response_model
                except ValidationError:
                    continue

            raise ValueError(
                f"Ответ не соответствует ни success_model, ни одной из response_models. Ответ: {result}"
            )

        return wrapper

    return decorator
