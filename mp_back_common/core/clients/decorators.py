from functools import wraps
from typing import Any, Callable

from pydantic import BaseModel, ValidationError
from result import Ok, Err, Result

from ...api.exceptions import BaseHTTPErrorProtocol
from ...api.schemas import BaseSchema


def validate_response(
    success_model: type[BaseSchema],
    response_models: list[type[BaseHTTPErrorProtocol]],
) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Result[BaseSchema, BaseHTTPErrorProtocol]:
            result: Any = await func(*args, **kwargs)

            try:
                return Ok(success_model.model_validate(result))
            except ValidationError:
                pass

            for error_model in response_models:
                try:
                    return Err(error_model.response_schema.model_validate(result))
                except ValidationError:
                    continue

            raise ValueError(
                f"Ответ не соответствует ни success_model, ни одной из response_models. Ответ: {result}"
            )

        return wrapper

    return decorator
