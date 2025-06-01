from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth_service.infrastructure.db.setup import session_factory


async def session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


async def transaction() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory.begin() as transaction:
        yield transaction
