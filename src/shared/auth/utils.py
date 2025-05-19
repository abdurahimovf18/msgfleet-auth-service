from typing import Any

from jwt import decode, ExpiredSignatureError, InvalidTokenError, PyJWTError
from jwt.exceptions import ExpiredSignatureError

from loguru import logger

from .settings import JWT_ISS, JWT_PUBLIC_KEY, JWT_ALGORITHM


def get_jwt_data(jwt_token: str) -> dict[str, Any]:
    try:
        payload = decode(
            jwt=jwt_token,
            key=JWT_PUBLIC_KEY,
            algorithms=[JWT_ALGORITHM],
            options={"verify_signature": True, "verify_exp": True},
            issuer=JWT_ISS,
        )
        return payload
    except ExpiredSignatureError:
        raise ValueError("JWT token has expired.")
    except InvalidTokenError:
        raise ValueError("JWT token is invalid or signature verification failed.")
    except PyJWTError as e:
        # catch any other JWT-related exceptions
        raise ValueError(f"JWT error: {str(e)}")
    except Exception as e:
        logger.exception("Jwt decoding error.")
        raise RuntimeError("Jwt decoding error.") from e
    