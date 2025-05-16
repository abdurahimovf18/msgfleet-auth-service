from sqlalchemy.ext.asyncio import AsyncSession

from .dto import p, r
from src.auth_service.services import queries
from src.auth_service.services import http
from src.auth_service.utils.session import session

from src.auth_service.infrastructure.http.clients import UsersHTTPClient


async def register_user(param: p.RegisterUserDTO, 
                        session: AsyncSession, 
                        users_client: UsersHTTPClient) -> r.RegisterUserDTO:
    
    user = await http.users.create(
        http.users.p.CreateDTO(language=param.language), users_client)
    
    profile = await queries.auth.create(
        queries.auth.p.CreateDTO(user_id=user.id, language=param.language), session)
    
    await session.commit()
    
    return r.RegisterUserDTO.v(user, profile) 
