"""Action stubs for baseline user activity."""

from typing import Tuple
import uuid

import requests

GRAPH_ROOT = "https://graph.microsoft.com/v1.0"


def _request_id(response: requests.Response) -> str:
    """Return request-id header or a generated uuid."""
    return response.headers.get("request-id", str(uuid.uuid4()))


def sign_in(session: requests.Session) -> Tuple[str, int, str]:
    """Perform a simple /me GET request."""
    resp = session.get(f"{GRAPH_ROOT}/me")
    return ("sign_in", resp.status_code, _request_id(resp))


def send_email(session: requests.Session, to: str, subject: str, body: str) -> Tuple[str, int, str]:
    """Send an email using /me/sendMail."""
    payload = {
        "message": {
            "subject": subject,
            "body": {"contentType": "Text", "content": body},
            "toRecipients": [{"emailAddress": {"address": to}}],
        },
        "saveToSentItems": "true",
    }
    resp = session.post(f"{GRAPH_ROOT}/me/sendMail", json=payload)
    return ("send_email", resp.status_code, _request_id(resp))


def read_inbox(session: requests.Session) -> Tuple[str, int, str]:
    """List messages in the inbox."""
    resp = session.get(f"{GRAPH_ROOT}/me/mailFolders/Inbox/messages")
    return ("read_inbox", resp.status_code, _request_id(resp))


def list_app_registrations(session: requests.Session) -> Tuple[str, int, str]:
    """List app registrations."""
    resp = session.get(f"{GRAPH_ROOT}/applications")
    return ("list_app_registrations", resp.status_code, _request_id(resp))


def create_or_update_group(session: requests.Session, name: str) -> Tuple[str, int, str]:
    """Create a group if it does not exist, otherwise update its display name."""
    # Simplified example - real implementation would query and update.
    payload = {
        "displayName": name,
        "mailEnabled": False,
        "mailNickname": name.replace(" ", "").lower(),
        "securityEnabled": True,
    }
    resp = session.post(f"{GRAPH_ROOT}/groups", json=payload)
    return ("create_or_update_group", resp.status_code, _request_id(resp))


def create_and_delete_storage_account(session: requests.Session, name: str) -> Tuple[str, int, str]:
    """Create and immediately delete an Azure Storage account (placeholder)."""
    # TODO: Implement using Azure management REST API
    # Placeholder response simulation
    resp = requests.Response()
    resp.status_code = 202
    return ("create_and_delete_storage_account", resp.status_code, str(uuid.uuid4()))
