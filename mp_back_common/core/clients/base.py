from abc import ABC
from typing import Generic, TypeVar

import aiohttp
from core._types import UserCredentials
from logger import get_logger
from settings import BaseAPIClientSettings

logger = get_logger(__name__)

TClientSettings = TypeVar("TClientSettings", bound=BaseAPIClientSettings)


class BaseAPIClient(ABC, Generic[TClientSettings]):
    def __init__(
        self,
        api_settings: TClientSettings,
        session: aiohttp.ClientSession,
        user_credentials: UserCredentials,
    ):
        self._api_settings = api_settings
        self.__session = session
        self._user_credentials = user_credentials

    async def _base_request(
        self,
        method: str = "GET",
        endpoint: str = "",
        success_status_codes: list[int] = [200],
        **kwargs,
    ):
        url = f"{self._api_settings.base_url}{self._api_settings.api_version}{endpoint}"
        response = None

        headers = kwargs.get("headers", {})
        headers["x-clientid"] = str(self._user_credentials.client_id)
        kwargs["headers"] = headers

        try:
            response = await self.__session.request(method=method, url=url, **kwargs)

            if response.status not in success_status_codes:
                body = await response.text()
                logger.error(
                    f"Unexpected status code {response.status} for URL {url}\nResponse body: {body}",
                    exc_info=True,
                )
                response.raise_for_status()

            return response

        except aiohttp.ClientError as exc:
            request_url = url
            request_body = kwargs.get("json") or kwargs.get("data") or None

            response_body = None
            if response is not None:
                try:
                    response_body = await response.text()
                except Exception:
                    response_body = "<failed to read response>"

            logger.error(
                f"Request error '{exc}': {request_url}\n"
                f"Body - {request_body}\n"
                f"Response for error: {response_body}",
                exc_info=True,
            )

            if (response is None) or (response.status not in success_status_codes):
                raise

            return response
