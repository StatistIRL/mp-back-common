from pydantic import BaseModel, ConfigDict


def snake_to_lower_camel(snake_str: str) -> str:
    words = snake_str.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


class BaseSchema(BaseModel):
    """
    Base class for all schemas in the project.
    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=snake_to_lower_camel,
    )
