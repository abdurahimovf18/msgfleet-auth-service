from uuid import UUID
from datetime import datetime

from src.auth_service.utils.dto import BaseDTO


class CreateDTO(BaseDTO):
    id: UUID
    language: str
    created_at: datetime
    updated_at: datetime
