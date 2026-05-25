"""
Generic Logger Module

This module configures a shared application-wide logger. Log messages are sent both to the console (via StreamHandler)
and to a rotating log file. The log file is capped at 5 MB, and up to 5 backup files are maintained. This ensures that
the log directory remains clean and prevents uncontrolled log growth.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(LOG_FOLDER, "ai_learning.log")
LOGGER_LEVEL = logging.DEBUG

# config the root logger
logging.basicConfig(
    level=LOGGER_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(
            LOG_FILE, maxBytes=5_00_0000, backupCount=5, encoding="utf-8"
        ),
    ],
)


# get logger method that returns the logger object
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
