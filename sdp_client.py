import os
import requests

class ServiceDeskClient:
    """Cliente sencillo para la API v3 de ServiceDesk Plus."""

    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        self.base_url = (base_url or os.environ.get("SDP_BASE_URL", "")).rstrip("/")
        self.api_key = api_key or os.environ.get("SDP_API_KEY")
        if not self.base_url or not self.api_key:
            raise ValueError("SDP_BASE_URL and SDP_API_KEY must be set")

    def create_ticket(self, title: str, description: str) -> dict:
        url = f"{self.base_url}/requests"
        headers = {
            "authtoken": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        payload = {"request": {"subject": title, "description": description}}
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
