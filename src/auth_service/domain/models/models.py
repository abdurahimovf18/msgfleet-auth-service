from uuid import UUID
from dataclasses import dataclass
from .enums import UserRole


@dataclass
class Auth:
    id: UUID
    user_id: UUID

    username: str
    password: str

    role: UserRole
