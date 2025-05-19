"""
auth.py

Password hashing utilities using Argon2.

Provides secure password hashing and verification functions
with configurable performance parameters.

This module should be the central place for password hashing logic
in the auth-service and be imported wherever password hashing is needed.
"""

from datetime import datetime, timedelta
from argon2 import PasswordHasher
from jwt import encode

from time import perf_counter

from src.auth_service.utils.dto import BaseDTO, s
from src.auth_service.config.settings import JWT_ALGORITHM, JWT_EXP, JWT_ISS, JWT_PRIVATE_KEY, TIMEZONE


ph = PasswordHasher(
    time_cost=1,  # Number of iterations
    memory_cost=8192,  # Memory usage in kibibytes (8 MiB)
    parallelism=2  # Number of parallel threads
)


class GenerateJWTDTO(BaseDTO):
    user_id: s.Auth.user_id
    role: s.Auth.role
    username: s.Auth.username
    auth_id: s.Auth.id


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using Argon2.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The Argon2 hashed password string.
    """
    return ph.hash(password=password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against an Argon2 hashed password.

    Args:
        password (str): The plaintext password to verify.
        hashed_password (str): The Argon2 hashed password to check against.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    return ph.verify(hashed_password, password)

def generate_jwt_token(param: GenerateJWTDTO) -> str:
    now = datetime.now(TIMEZONE)
    exp = timedelta(seconds=JWT_EXP)

    payload = {
        "sub": str(param.user_id),
        "role": param.role.value,
        "auth_id": str(param.auth_id),
        "username": param.username,
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int((now + exp).timestamp()),
        "iss": JWT_ISS
    }
    token = encode(payload, JWT_PRIVATE_KEY, algorithm=JWT_ALGORITHM)
    return token
