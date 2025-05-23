"""Action library using Microsoft Graph."""

import random
from typing import Any, Dict

from msgraph.core import GraphClient


def signin(client: GraphClient) -> Dict[str, Any]:
    """Simulate sign in by calling /me."""
    response = client.get("/me")
    return {"action": "signin", "status": response.status_code, "response_id": response.json().get("id")}


def send_mail(client: GraphClient, to_address: str) -> Dict[str, Any]:
    """Send an email via /me/sendMail."""
    # Implement Graph call here
    message = {
        "message": {
            "subject": "Baseline simulator message",
            "body": {"contentType": "Text", "content": "Hello from baseline simulator"},
            "toRecipients": [{"emailAddress": {"address": to_address}}],
        }
    }
    response = client.post("/me/sendMail", json=message)
    return {"action": "send_mail", "status": response.status_code, "response_id": response.headers.get("request-id")}


def read_inbox(client: GraphClient) -> Dict[str, Any]:
    """Read messages from inbox."""
    response = client.get("/me/mailFolders/Inbox/messages")
    return {"action": "read_inbox", "status": response.status_code, "response_id": response.headers.get("request-id")}


def list_app_registrations(client: GraphClient) -> Dict[str, Any]:
    """List all app registrations."""
    response = client.get("/applications")
    return {"action": "list_app_registrations", "status": response.status_code, "response_id": response.headers.get("request-id")}


def create_or_update_group(client: GraphClient, group_id: str = None) -> Dict[str, Any]:
    """Create or update a group."""
    # If group_id provided, update; else create
    if group_id:
        body = {"description": "Updated by baseline simulator"}
        response = client.patch(f"/groups/{group_id}", json=body)
    else:
        body = {
            "displayName": f"BaselineGroup-{random.randint(1000,9999)}",
            "mailEnabled": False,
            "mailNickname": f"baseline{random.randint(1000,9999)}",
            "securityEnabled": True,
        }
        response = client.post("/groups", json=body)
    return {"action": "create_or_update_group", "status": response.status_code, "response_id": response.json().get("id")}


def manage_storage_account(account_name: str, resource_group: str, subscription_id: str) -> Dict[str, Any]:
    """Create and delete a storage account using Azure SDK."""
    # Placeholder for Azure resource management calls
    # Use azure-mgmt-storage SDK here to create and delete a storage account
    return {"action": "manage_storage_account", "status": 200, "response_id": account_name}
