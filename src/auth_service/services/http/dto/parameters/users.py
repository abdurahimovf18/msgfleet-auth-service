from src.auth_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    language: s.User.language
    
