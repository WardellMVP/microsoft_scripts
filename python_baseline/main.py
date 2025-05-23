"""Entry point for baseline simulator."""

import argparse
from typing import List

from .auth import get_graph_client
from . import actions, scheduler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Baseline activity simulator")
    parser.add_argument("--tenant-id", required=True)
    parser.add_argument("--client-id", required=True)
    parser.add_argument("--client-secret", required=True)
    parser.add_argument("--duration", type=int, default=10, help="Total run time in minutes")
    parser.add_argument("--rate", type=int, default=6, help="Average actions per minute")
    parser.add_argument("--mail-to", required=True, help="Address to send test email")
    return parser.parse_args()


def main():
    args = parse_args()
    client = get_graph_client(args.tenant_id, args.client_id, args.client_secret)

    action_funcs: List = [
        lambda: actions.signin(client),
        lambda: actions.send_mail(client, args.mail_to),
        lambda: actions.read_inbox(client),
        lambda: actions.list_app_registrations(client),
        lambda: actions.create_or_update_group(client),
        lambda: actions.manage_storage_account("baselineacct", "demo-rg", args.tenant_id),
    ]

    scheduler.run(args.duration, args.rate, action_funcs)


if __name__ == "__main__":
    main()
