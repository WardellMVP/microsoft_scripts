"""Scheduler for executing random baseline actions."""

import argparse
import random
import time
from typing import Callable, List, Tuple

from actions import (
    sign_in,
    send_email,
    read_inbox,
    list_app_registrations,
    create_or_update_group,
    create_and_delete_storage_account,
)
from logger import JsonActionLogger

ActionFunc = Callable[[], Tuple[str, int, str]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Baseline activity scheduler")
    parser.add_argument("--duration", type=int, default=300, help="Run time in seconds")
    parser.add_argument("--rate", type=int, default=2, help="Approximate actions per minute")
    return parser.parse_args()


def run(session, logger: JsonActionLogger, duration: int, rate: int) -> None:
    actions: List[ActionFunc] = [
        lambda: sign_in(session),
        lambda: read_inbox(session),
        lambda: list_app_registrations(session),
        lambda: create_or_update_group(session, "Baseline Demo Group"),
        lambda: create_and_delete_storage_account(session, "baselinedemostorage"),
        lambda: send_email(session, "user@example.com", "Hello", "Baseline message"),
    ]

    end_time = time.time() + duration
    while time.time() < end_time:
        action = random.choice(actions)
        name, status, resp_id = action()
        logger.log(name, status, resp_id)
        # Sleep between 30 and 120 seconds
        sleep_for = random.randint(30, 120)
        time.sleep(sleep_for)
