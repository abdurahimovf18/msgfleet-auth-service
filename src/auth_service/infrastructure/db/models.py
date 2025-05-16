from typing import Annotated
from uuid import uuid4, UUID

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import UUID as SQLUUID

from src.auth_service.config.settings import TIMEZONE
from src.auth_service.infrastructure.db.setup import Base
from src.auth_service.domain.models import enums


id_ = Annotated[UUID, mapped_column(SQLUUID(as_uuid=True), primary_key=True, default=lambda: uuid4())]


class Auth(Base):
    __tablename__ = "auth"
    
    id: Mapped[id_]

    username: Mapped[str]
    password: Mapped[str]

    role: Mapped[enums.UserRole]
