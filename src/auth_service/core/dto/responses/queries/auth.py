from src.auth_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    id: s.Auth.id
    user_id: s.Auth.user_id

    username: s.Auth.username
    password: s.Auth.password

    role: s.Auth.role


class ExistsDTO(BaseDTO):
    exists: bool


class GetDTO(BaseDTO):
    id: s.Auth.id
    user_id: s.Auth.user_id

    username: s.Auth.username
    password: str

    role: s.Auth.role
