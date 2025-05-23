import functools
import itertools
from typing import Iterable

import aioinject
import settings
from core.di._types import Providers
from pydantic_settings import BaseSettings


class ContainerManger:
    @classmethod
    def _register_settings(
        cls,
        container: aioinject.Container,
        *,
        settings_classes: Iterable[type[BaseSettings]],
    ):
        for settings_cls in settings_classes:
            factory = functools.partial(settings.get_settings, settings_cls)
            container.register(aioinject.Singleton(factory, type_=settings_cls))

    @functools.lru_cache
    @classmethod
    def create_container(
        cls, settings: Iterable[type[BaseSettings]], providers: list[Providers]
    ) -> aioinject.Container:
        container = aioinject.Container()

        for provider in itertools.chain.from_iterable(providers):
            container.register(provider)

        cls._register_settings(container, settings_classes=settings)

        return container
