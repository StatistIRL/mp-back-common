from functools import lru_cache
from pathlib import Path
from typing import Type, TypeVar

import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

TSettings = TypeVar("TSettings", bound=BaseSettings)
BASE_DIR = Path(__file__).parent.parent


@lru_cache
def get_settings(cls: Type[TSettings]) -> TSettings:
    """
    Factory function for creating instances of settings classes with environment variables loaded from a .env file.

    Args:
        cls (Type[TSettings]): The class type to instantiate after loading environment variables.

    Returns:
        TSettings: An instance of the provided settings class.
    """
    dotenv.load_dotenv()
    return cls()


class ApplicationSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="app_")

    title: str = "Application"
    version: str = "1.0.0"
    description: str = "Application"

    host: str = "0.0.0.0"
    port: int = 8011
    reload: bool = True

    allow_origins: list[str] = ["*"]
    allow_origin_regex: str = ""
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    swagger_path: str = "/"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="database_")

    driver: str = "postgresql+asyncpg"
    username: str = "postgres"
    password: str = "postgres"
    host: str = "mp-database"
    port: int = 5432
    name: str = "test"

    @property
    def url(self) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"


class ElasticSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="elastic_")

    url: str = "http://elasticsearch:9200"


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(str_strip_whitespace=True, env_prefix="redis_")

    username: str = ""
    password: str = ""

    host: str = "redis"
    port: int = 6379


class BaseRedisCacheSettings(BaseSettings):
    prefix: str
    cache_ttl_seconds: int = 60


class BaseAPIClientSettings(BaseSettings):
    base_url: str = ""
    api_version: str = ""


class TopicServiceAPIClientSettings(BaseAPIClientSettings):
    model_config = SettingsConfigDict(
        str_strip_whitespace=True, env_prefix="topics_service_api_client_"
    )
