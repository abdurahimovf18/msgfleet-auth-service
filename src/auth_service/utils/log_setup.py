"""
Logging Configuration Module

Sets up the application's logging system using Python's built-in `logging` module.

Usage:
    from src.auth_service.utils.log_setup import setup_logging
    setup_logging()  # Call once at startup
"""

import logging.config
from src.auth_service.config.logging import LOGGING_CONFIG


def setup_logging() -> None:
    """Applies the logging configuration to the application."""
    logging.config.dictConfig(LOGGING_CONFIG)
    logging.getLogger(__name__).debug("Logging has been configured.")
