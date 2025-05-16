from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import load_only

from src.auth_service.infrastructure.db import models
from src.auth_service.domain.models import enums


from ..dto.parameters import auth as p
from ..dto.responses import auth as r



async def create(param: p.CreateDTO, session: AsyncSession) -> r.CreateDTO:
    auth = models.Auth()
    session.add(auth)
    await session.flush(auth)
    return r.CreateDTO.model_validate(auth)
