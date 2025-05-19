from src.auth_service.utils.dto import BaseDTO, s


class Languages(s.STREnum):
    UZ = "UZ"
    RU = "RU"
    EN = "EN"


class RegisterDTO(BaseDTO):
    username: s.Auth.username
    password: s.Auth.password
    language: Languages 


class GenerateAccessTokenDTO(BaseDTO):
    username: s.Auth.username
    password: s.Auth.password


class IdentifyDTO(BaseDTO):
    access_token: str
    