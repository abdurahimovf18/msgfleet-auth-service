from typing import Annotated, Any
from uuid import UUID
import re

from pydantic import Field
from pydantic_core import core_schema

from src.auth_service.domain.models import enums


class PasswordStr:
    @classmethod
    def __get_pydantic_core_schema__(cls, _source: Any, _handler: Any) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(cls._validate, core_schema.str_schema())
    
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: core_schema.CoreSchema, handler: Any) -> dict:
        field_schema = handler(core_schema)
        field_schema.update({
            "type": "string",
            "minlength": 8,
            "pattern": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).+$",
            "description": "Password must be at least 8 characters and contain an uppercase letter, lowercase letter, digit, and special character.",
            "example": "StrongP@ss1"
        })
        return field_schema

    @classmethod
    def _validate(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Password must be a string")

        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")

        return value


class UsernameStr:
    @classmethod
    def __get_pydantic_core_schema__(cls, _source: Any, _handler: Any) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(cls._validate, core_schema.str_schema())
    
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: core_schema.CoreSchema, handler: Any) -> dict:
        field_schema = handler(core_schema)
        field_schema.update({
            "type": "string",
            "minLength": 3,
            "maxLength": 32,
            "pattern": r"^[a-zA-Z][a-zA-Z0-9_-]*$",
            "description": "Username must start with a letter and only contain letters, numbers, underscores, or hyphens.",
            "example": "john_doe123"
        })
        return field_schema
    
    @classmethod
    def _validate(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Username must be a string")

        if len(value) < 3 or len(value) > 32:
            raise ValueError("Username must be between 3 and 32 characters")

        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_-]*$", value):
            raise ValueError("Username must start with a letter and only contain letters, numbers, underscores, or hyphens")

        return value


class Auth:
    id = Annotated[UUID, Field()]
    user_id = Annotated[UUID, Field()]

    username = UsernameStr
    password = PasswordStr

    role = Annotated[enums.UserRole, Field()]
