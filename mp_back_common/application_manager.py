import contextlib
from typing import AsyncIterator

import aioinject
from aioinject.ext.fastapi import AioInjectMiddleware
from api.exceptions import BaseHTTPError, ServerHTTPError
from fastapi import APIRouter, FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.types import Lifespan

from mp_back_common.core.middlewares.authentication import ClientIDMiddleware
from mp_back_common.logger import get_logger
from mp_back_common.settings import ApplicationSettings

logger = get_logger(__name__)


async def http_exception_handler(
    request: Request,
    exc: BaseHTTPError,
) -> JSONResponse:
    return JSONResponse(
        content=jsonable_encoder(exc.response_schema.model_dump(by_alias=True)),
        status_code=exc.status_code,
    )


async def common_exception_handler(request: Request, exc: Exception):
    logger.exception("Error: ", exc_info=True)
    exc = ServerHTTPError()
    return JSONResponse(
        content=jsonable_encoder(exc.response_schema.model_dump(by_alias=True)),
        status_code=exc.status_code,
    )


class ApplicationManger:
    def __init__(
        self,
        application_settings: ApplicationSettings,
        di_container: aioinject.Container,
        lifespan: Lifespan | None = None,
    ):
        self.di_container = di_container
        self.lifespan = lifespan
        self._application_settings = application_settings

    def create_base_application(
        self,
    ) -> FastAPI:
        lifespan = self.wrap_lifespan_with_container(
            self.lifespan or self.default_lifespan,
            self.di_container,
        )

        app = FastAPI(
            title=self._application_settings.title,
            version=self._application_settings.version,
            description=self._application_settings.description,
            docs_url=self._application_settings.swagger_path,
            lifespan=lifespan,
        )

        return app

    def wrap_lifespan_with_container(
        self,
        lifespan: Lifespan,
        di_container: aioinject.Container,
    ) -> Lifespan:
        @contextlib.asynccontextmanager
        async def wrapped(app: FastAPI) -> AsyncIterator[None]:
            async with contextlib.aclosing(di_container):
                app.state.container = di_container
                async with lifespan(app):
                    yield

        return wrapped

    @staticmethod
    @contextlib.asynccontextmanager
    async def default_lifespan(app: FastAPI) -> AsyncIterator[None]:
        yield

    def configure_app(self, app: FastAPI, base_router: APIRouter) -> FastAPI:
        app.include_router(router=base_router, prefix="/api")

        app.exception_handlers[BaseHTTPError] = http_exception_handler
        app.exception_handlers[Exception] = common_exception_handler

        app.add_middleware(ClientIDMiddleware)
        app.add_middleware(AioInjectMiddleware, container=self.di_container)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=self._application_settings.allow_origins,
            allow_credentials=True,
            allow_origin_regex=self._application_settings.allow_origin_regex,
            allow_methods=self._application_settings.allow_methods,
            allow_headers=self._application_settings.allow_headers,
        )

        return app
