from src.auth_service.core.dto.parameters.clients import users as p
from src.auth_service.core.dto.responses.clients import users as r

from src.auth_service.infrastructure.clients.setup import UsersHTTPClient


async def create(param: p.CreateDTO, client: UsersHTTPClient) -> r.CreateDTO:
    response = await client.post("/create", json=param.model_dump())
    return r.CreateDTO.model_validate(response.json())
