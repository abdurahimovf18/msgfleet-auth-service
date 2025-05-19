from uuid import UUID
from pydantic import BaseModel


class Identity(BaseModel):
    auth_id: UUID
    user_id: UUID
    username: str
    role: str
