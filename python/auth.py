"""Authentication utilities for Microsoft Graph."""

import os
from typing import Dict

import msal
import requests


def get_graph_client(config: Dict[str, str]) -> requests.Session:
    """Return an authenticated requests.Session for Microsoft Graph.

    The `config` dictionary must include `tenant_id`, `client_id` and either
    `client_secret` for client credentials auth or `username`/`password` for
    user credential auth. Set `auth_type` to ``client_credentials`` or
    ``password``.
    """
    authority = f"https://login.microsoftonline.com/{config['tenant_id']}"

    if config.get("auth_type") == "password":
        app = msal.PublicClientApplication(
            client_id=config["client_id"],
            authority=authority,
        )
        result = app.acquire_token_by_username_password(
            username=config["username"],
            password=config["password"],
            scopes=["https://graph.microsoft.com/.default"],
        )
    else:
        app = msal.ConfidentialClientApplication(
            client_id=config["client_id"],
            client_credential=config["client_secret"],
            authority=authority,
        )
        result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" not in result:
        raise RuntimeError(f"Could not obtain token: {result.get('error_description')}")

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {result['access_token']}",
        "Content-Type": "application/json",
    })
    return session
