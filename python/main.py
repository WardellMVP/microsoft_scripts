"""Entry point for the baseline activity simulator."""

import os
import yaml

from auth import get_graph_client
from logger import JsonActionLogger
import scheduler


CONFIG_FILE = "config.yaml"


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    # Fallback to environment variables
    return {
        "tenant_id": os.environ.get("TENANT_ID"),
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET"),
        "username": os.environ.get("USERNAME"),
        "password": os.environ.get("PASSWORD"),
        "auth_type": os.environ.get("AUTH_TYPE", "client_credentials"),
    }


def main() -> None:
    args = scheduler.parse_args()
    config = load_config()
    session = get_graph_client(config)
    log = JsonActionLogger()
    scheduler.run(session, log, args.duration, args.rate)


if __name__ == "__main__":
    main()
