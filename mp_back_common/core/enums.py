from enum import Enum


class ContentTypeEnum(str, Enum):
    text = "text"
    images = "images"
    videos = "videos"
    textEmpty = "textEmpty"


class MessageTypeEnum(str, Enum):
    review = 12
    question = 28
    answer = 13
    comment = 4


class OrderByEnum(str, Enum):
    createdDate = "Post.Date.CreatedDate"


class FieldsEnum(str, Enum):
    url = "Url"
