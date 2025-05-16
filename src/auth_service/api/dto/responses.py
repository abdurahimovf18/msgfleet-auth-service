from pydantic import field_validator

from src.auth_service.utils.dto import BaseDTO, s


class RegisterDTO(BaseDTO):
    id: s.Auth.id
    user_id: s.Auth.user_id

    username: s.Auth.username
    password: s.Auth.password

    role: s.Auth.role

    @field_validator("password")
    def normalize_password(cls, v: str) -> str:
        return f"{v[:5]}...{v[-5:]}"
    