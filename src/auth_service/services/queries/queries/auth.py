from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy.orm import load_only

from src.auth_service.infrastructure.db import models
from src.auth_service.domain.models import enums


from ..dto.parameters import auth as p
from ..dto.responses import auth as r



async def create(param: p.CreateDTO, session: AsyncSession) -> r.CreateDTO:
    auth = models.Auth(**param.d())
    session.add(auth)
    await session.flush([auth])
    return r.CreateDTO.model_validate(auth)


async def exists(param: p.ExistsDTO, session: AsyncSession) -> r.ExistsDTO:
    query = (
        sa.select(
            sa.exists(models.Auth)
            .where(
                models.Auth.id == param.id 
                if param.id is not None else
                models.Auth.username == param.username
            )
        )
    )
    response = await session.execute(query)
    return r.ExistsDTO(exists=response.scalar_one())


async def get(param: p.GetDTO, session: AsyncSession) -> r.GetDTO: 
    query = (
        sa.select(models.Auth)
        .where(
            models.Auth.id == param.id 
            if param.id is not None else
            models.Auth.username == param.username
        )
    )
    response = await session.execute(query)
    return r.GetDTO.model_validate(response.scalar_one())
