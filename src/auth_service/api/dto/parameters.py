from src.auth_service.utils.dto import BaseDTO, s


class RegisterDTO(BaseDTO):
    username: s.Auth.username
    password: s.Auth.password

    language: str

    role: s.Auth.role
