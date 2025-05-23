import contextlib
from typing import AsyncIterator

from aioinject.ext.fastapi import AioInjectMiddleware
from api.exceptions import BaseHTTPError
from api.router import router
from core.di.container import create_container
from core.middlewares import ClientIDMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mp_back_common.logger import get_logger
from mp_back_common.settings import ApplicationSettings, get_settings

logger = get_logger(__name__)
application_settings: ApplicationSettings = get_settings(ApplicationSettings)


@contextlib.asynccontextmanager
async def _lifespan(
    app: FastAPI,
) -> AsyncIterator[None]:
    async with contextlib.aclosing(create_container()):
        yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="Messages Service",
        version="1.0.0",
        description="API для работы с сообщениями",
        docs_url=application_settings.swagger_path,
        lifespan=_lifespan,
    )
    app.include_router(router=router, prefix="/api")

    app.exception_handlers[BaseHTTPError] = http_exception_handler
    app.exception_handlers[Exception] = common_exception_handler

    app.add_middleware(ClientIDMiddleware)
    app.add_middleware(AioInjectMiddleware, container=create_container())
    app.add_middleware(
        CORSMiddleware,
        allow_origins=application_settings.allow_origins,
        allow_credentials=True,
        allow_origin_regex=application_settings.allow_origin_regex,
        allow_methods=application_settings.allow_methods,
        allow_headers=application_settings.allow_headers,
    )

    return app
