"""JSON rotating logger for baseline actions."""

import json
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from typing import Optional


class JsonActionLogger:
    """Logger that writes JSON action records to a rotating file."""

    def __init__(self, path: str = "baseline.log"):
        self.logger = logging.getLogger("baseline")
        self.logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(path, maxBytes=1024 * 1024, backupCount=5)
        self.logger.addHandler(handler)

    def log(self, action: str, status: int, response_id: str):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "baseline": True,
            "action": action,
            "status": status,
            "response_id": response_id,
        }
        self.logger.info(json.dumps(record))
