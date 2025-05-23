from typing import Sequence

from .exceptions import BaseHTTPError


def get_responses(errors: Sequence[BaseHTTPError]) -> dict:
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
