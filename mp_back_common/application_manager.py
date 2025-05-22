
from fastapi import Request
from fastapi.responses import JSONResponse
from api.exceptions import BaseHTTPError, ServerHTTPError
from fastapi.encoders import jsonable_encoder
from starlette.types import Lifespan

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

@contextlib.asynccontextmanager
async def _lifespan(
    app: FastAPI,
) -> AsyncIterator[None]:
    async with contextlib.aclosing(create_container()):
        yield

class ApplicationManger:
    def __init__(self, settings: ApplicationSettings):
        self._settings = settings
    
    def get_base_application(self, title: str, version: str, description: str, modified_lifespan: Lifespan = _lifespan)