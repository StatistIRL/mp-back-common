import functools
import itertools
from typing import Iterable

import aioinject
from pydantic_settings import BaseSettings

from ... import settings
from ..di._types import Providers


class ContainerManager:
    @classmethod
    def create_container(
        cls,
        settings_classes: Iterable[type[BaseSettings]],
        providers: list[Providers],
    ) -> aioinject.Container:
        return cls._create_container_cached(tuple(settings_classes), tuple(providers))

    @staticmethod
    @functools.lru_cache
    def _create_container_cached(
        settings_classes: tuple[type[BaseSettings]],
        providers: tuple[Providers],
    ) -> aioinject.Container:
        container = aioinject.Container()

        for provider in itertools.chain.from_iterable(providers):
            container.register(provider)

        for settings_cls in settings_classes:
            factory = functools.partial(settings.get_settings, settings_cls)
            container.register(aioinject.Singleton(factory, type_=settings_cls))

        return container
