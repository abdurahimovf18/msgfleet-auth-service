from typing import Self
from httpx import AsyncClient, Response



class HTTPClient:
    def __init__(self, base_url: str, **kw):
        self._client = AsyncClient(base_url=base_url, **kw)

    async def get(self, path: str, **kw) -> Response:
        return await self._client.get(path, **kw)
    
    async def post(self, path: str, **kw) -> Response:
        return await self._client.post(path, **kw)
    
    async def put(self, path: str, **kw) -> Response:
        return await self._client.put(path, **kw)
    
    async def patch(self, path: str, **kw) -> Response:
        return await self._client.patch(path, **kw)
    
    async def __aenter__(self, *ar, **kw) -> Self:
        return self
    
    async def __aexit__(self, *ar, **kw) -> None:
        await self._client.aclose()

