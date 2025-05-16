from enum import Enum


class STREnum(str, Enum): pass


class UserRole(STREnum):
    ADMIN = "ADMIN"
    USER = "USER"
    