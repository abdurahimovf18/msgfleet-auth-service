from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from fastapi import HTTPException, status
from src.auth_service.core import queries
from src.auth_service.core import clients
from src.auth_service.utils.auth import hash_password, verify_password, generate_jwt_token, GenerateJWTDTO
from src.auth_service.infrastructure.clients.setup import UsersHTTPClient

from src.auth_service.core.dto.parameters.flows import app as p
from src.auth_service.core.dto.responses.flows import app as r


async def register_user(
    param: p.RegisterUserDTO,
    session: AsyncSession,
    users_client: UsersHTTPClient
) -> r.RegisterUserDTO:

    # Check if username already exists
    user_exists = await queries.auth.exists(
        queries.auth.p.ExistsDTO(username=param.username), session
    )
    if user_exists.exists:
        raise HTTPException(
            status.HTTP_409_CONFLICT, detail="User with this username already exists."
        )
    
    # Hash password separately to avoid mutating the input DTO
    hashed_password = hash_password(param.password)

    # Create user via HTTP client
    user = await clients.users.create(
        clients.users.p.CreateDTO(language=param.language), users_client
    )

    # Create auth profile with hashed password
    profile = await queries.auth.create(
        queries.auth.p.CreateDTO(
            user_id=user.id,
            username=param.username,
            password=hashed_password
        ),
        session
    )

    await session.commit()

    return r.RegisterUserDTO.v(user, profile)


async def generate_access_token(param: p.GenerateAccessTokenDTO, session: AsyncSession) -> r.GenerateAccessTokenDTO:
    try:
        auth_identity = await queries.auth.get(
            queries.auth.p.GetDTO(username=param.username), session
        )
    except NoResultFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found.")

    hashed_password = auth_identity.password

    if not verify_password(param.password, hashed_password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Username and/or Password is invalid.")
    
    access_token = generate_jwt_token(
        GenerateJWTDTO(user_id=auth_identity.user_id, auth_id=auth_identity.id,
                       role=auth_identity.role, username=auth_identity.username)
    )
    
    return r.GenerateAccessTokenDTO(access_token=access_token)
