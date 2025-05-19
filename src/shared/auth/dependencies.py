from typing import Any

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from .utils import get_jwt_data
from .dto import Identity


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def auth_identity(token: str = Depends(oauth2_scheme)) -> Identity:
    try:
        token_data = get_jwt_data(token)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc)
        )
    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authorization error"
        )

    # Validate presence of required fields
    missing_fields = [field for field in ("sub", "role", "username", "auth_id") if field not in token_data]
    if missing_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"JWT token is missing required fields: {', '.join(missing_fields)}"
        )

    try:
        return Identity(
            user_id=token_data["sub"],
            username=token_data["username"],
            role=token_data["role"],
            auth_id=token_data["auth_id"]
        )
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Failed to parse identity: {str(exc)}"
        )
