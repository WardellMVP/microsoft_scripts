"""Scheduler for executing random actions."""

import random
import time
from datetime import datetime, timedelta
from typing import Callable, List

from . import actions
from .logger import log_action

ActionCallable = Callable[[], dict]


def run(duration_minutes: int, rate_per_minute: int, action_funcs: List[ActionCallable]):
    """Run actions at random intervals for a given duration."""
    end_time = datetime.utcnow() + timedelta(minutes=duration_minutes)
    interval = 60 / rate_per_minute
    while datetime.utcnow() < end_time:
        action = random.choice(action_funcs)
        result = action()
        log_action(result)
        sleep_time = random.randint(30, 120)
        time.sleep(max(interval, sleep_time))
