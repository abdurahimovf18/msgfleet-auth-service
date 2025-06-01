from pydantic import Field, model_validator
from src.auth_service.utils.dto import BaseDTO, s


class CreateDTO(BaseDTO):
    username: s.Auth.username
    password: s.Auth.password
    user_id: s.Auth.user_id

    def d(self, *a, **k):
        data = super().d(*a, **k, recursive=False)
        data.setdefault("role", s.Auth.role.USER)
        return data


class ExistsDTO(BaseDTO):
    id: s.Auth.id | None = Field(default=None)
    username: s.Auth.username | None = Field(default=None)

    @model_validator(mode="after")
    def validate(self):
        if self.id is None and self.username is None:
            raise ValueError("Either 'id' or 'username' must be provided, but not both.")
        if self.id is not None and self.username is not None:
            raise ValueError("'id' and 'username' cannot both be provided at the same time.")
        return self
    

class GetDTO(BaseDTO):
    id: s.Auth.id | None = Field(default=None)
    username: s.Auth.username | None = Field(default=None)

    @model_validator(mode="after")
    def validate(self):
        if self.id is None and self.username is None:
            raise ValueError("Either 'id' or 'username' must be provided, but not both.")
        if self.id is not None and self.username is not None:
            raise ValueError("'id' and 'username' cannot both be provided at the same time.")
        return self
    