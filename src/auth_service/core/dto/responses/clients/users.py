from src.auth_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    id: s.User.id
    language: s.User.language
    created_at: s.User.created_at
    updated_at: s.User.updated_at
