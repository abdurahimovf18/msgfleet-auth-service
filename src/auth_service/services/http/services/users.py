from ..dto.parameters import users as p
from ..dto.responses import users as r

from src.auth_service.infrastructure.http.clients import UsersHTTPClient


async def create(param: p.CreateDTO, client: UsersHTTPClient) -> r.CreateDTO:
    response = await client.post("/create", json=param.model_dump())
    return r.CreateDTO.model_validate(response.json())
