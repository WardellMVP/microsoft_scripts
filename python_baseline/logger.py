"""Logging utilities for baseline simulator."""

import json
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


LOG_FILE = "baseline.log"

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("baseline")
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=1024*1024, backupCount=5)
    logger.addHandler(handler)
    return logger

logger = setup_logger()


def log_action(data: dict) -> None:
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        **data,
    }
    logger.info(json.dumps(record))
