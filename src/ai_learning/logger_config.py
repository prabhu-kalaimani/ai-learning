"""
Generic Logger Module

This module configures a shared application-wide logger. Log messages are sent both to the console (via StreamHandler)
and to a rotating log file. The log file is capped at 5 MB, and up to 5 backup files are maintained. This ensures that
the log directory remains clean and prevents uncontrolled log growth.
"""

import logging as logger
import os
from logging.handlers import RotatingFileHandler

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(LOG_FOLDER, "ai_learning.log")

# config the root logger
logger.basicConfig(
    level=logger.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logger.StreamHandler(),
        RotatingFileHandler(LOG_FILE, maxBytes=5000000, backupCount=5),
    ],
)


# get logger method that returns the logger object
def get_logger(name: str) -> logger.Logger:
    return logger.getLogger(name)
