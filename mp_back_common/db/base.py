from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

meta = MetaData()


class Base(DeclarativeBase):
    metadata = meta
