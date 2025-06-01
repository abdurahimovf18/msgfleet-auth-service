from typing import AsyncGenerator
from httpx import AsyncClient
from src.auth_service.infrastructure.clients.setup import UsersHTTPClient


async def users_client() -> AsyncGenerator[AsyncClient, None]:
    client = UsersHTTPClient()

    async with client:
        yield client
