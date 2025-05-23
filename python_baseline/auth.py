"""Authentication utilities for baseline simulator."""

from msal import ConfidentialClientApplication
from msgraph.core import GraphClient


def get_graph_client(tenant_id: str, client_id: str, client_secret: str) -> GraphClient:
    """Return an authenticated Microsoft Graph client."""
    app = ConfidentialClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret,
    )
    token_result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    if "access_token" not in token_result:
        raise RuntimeError(f"Authentication failed: {token_result}")
    return GraphClient(credential=lambda req: req.headers.__setitem__("Authorization", f"Bearer {token_result['access_token']}"))
