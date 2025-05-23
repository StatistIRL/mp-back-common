from contextvars import ContextVar

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from .dto import UserCredentials

ClientIdContextVar: ContextVar[UserCredentials] = ContextVar("ClientIdContextVar")


class ClientIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_id = int(request.headers.get("x-clientid", 1))
        user_creds = UserCredentials(client_id=client_id)
        ClientIdContextVar.set(user_creds)
        response = await call_next(request)
        return response
