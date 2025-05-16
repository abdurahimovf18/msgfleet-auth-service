from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from src.auth_service.domain.models import enums


@dataclass
class Auth:
    id: int
    user_id: int

    username: int
    password: int

    role: enums.UserRole
