from pydantic import field_validator

from src.auth_service.utils.dto import BaseDTO, s


class RegisterDTO(BaseDTO):
    id: s.Auth.id
    user_id: s.Auth.user_id
    username: s.Auth.username
    password: s.Auth.password
    role: s.Auth.role
    created_at: s.User.created_at
    updated_at: s.User.updated_at
    language: s.User.language

    @field_validator("password")
    def normalize_password(cls, v: str) -> str:
        return f"{v[:2]}...{v[-5:]}"
    

class GenerateAccessTokenDTO(BaseDTO):
    access_token: str


class IdentifyDTO(BaseDTO):
    auth_id: s.Auth.id
    user_id: s.Auth.user_id
    username: s.Auth.username
    role: s.Auth.role
