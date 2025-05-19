from src.auth_service.utils.dto import BaseDTO, s


class RegisterUserDTO(BaseDTO):
    id: s.Auth.id
    user_id: s.Auth.user_id
    username: s.Auth.username
    password: s.Auth.password
    role: s.Auth.role
    created_at: s.User.created_at
    updated_at: s.User.updated_at
    language: s.User.language


class GenerateAccessTokenDTO(BaseDTO):
    access_token: str
    