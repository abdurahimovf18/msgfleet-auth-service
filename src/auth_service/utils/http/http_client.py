from typing import Self
from httpx import AsyncClient, Response, RequestError
from pydantic import HttpUrl
from urllib.parse import urljoin
from loguru import logger


class HTTPClient:
    def __init__(self, base_url: str | HttpUrl | None, **kw):
        if not base_url:
            logger.critical(
                f"HTTPClient base_url is missing. Check: {self.__module__}.{self.__qualname__}"
            )
            raise RuntimeError("Internal HTTPClient misconfiguration: base_url is not set.")

        timeout = kw.pop("timeout", 10.0)
        self._client = AsyncClient(base_url=str(base_url), timeout=timeout, **kw)

    async def _request(self, method: str, path: str, **kw) -> Response:
        full_url = urljoin(str(self._client.base_url), path)
        try:
            return await self._client.request(method, full_url, **kw)
        except RequestError as e:
            logger.error(f"{method} request to {full_url} failed: {e}")
            raise RuntimeError(f"HTTPClient failed during {method} to {full_url}") from e

    async def get(self, path: str, **kw) -> Response:
        return await self._request("GET", path, **kw)

    async def post(self, path: str, **kw) -> Response:
        return await self._request("POST", path, **kw)

    async def put(self, path: str, **kw) -> Response:
        return await self._request("PUT", path, **kw)

    async def patch(self, path: str, **kw) -> Response:
        return await self._request("PATCH", path, **kw)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_) -> None:
        await self._client.aclose()
