from src.auth_service.utils.dto import BaseDTO, s


class Languages(s.STREnum):
    UZ = "UZ"
    RU = "RU"
    EN = "EN"


class RegisterUserDTO(BaseDTO):
    language: Languages
    username: s.Auth.username
    password: s.Auth.password


class GenerateAccessTokenDTO(BaseDTO):
    username: s.Auth.username
    password: s.Auth.password
    