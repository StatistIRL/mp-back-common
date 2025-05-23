from .exceptions import BaseHTTPError
from .responses import base_responses


def build_error_responses(errors: list[type[BaseHTTPError]]) -> dict:
    errors += base_responses
    result = {}
    for error in errors:
        if error.status_code not in result:
            result[error.status_code] = {
                "content": {
                    "application/json": {
                        "examples": {
                            error.response_schema.error.name: {
                                "value": error.response_schema
                            }
                        }
                    }
                }
            }
        else:
            result[error.status_code]["content"]["application/json"]["examples"][
                error.response_schema.error.name
            ] = {"value": error.response_schema}
    return result
