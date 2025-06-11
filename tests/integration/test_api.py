from fastapi.testclient import TestClient
from server import app
from unittest.mock import patch

client = TestClient(app)


def test_get_ticket():
    response = client.get("/tickets/1")
    assert response.status_code == 200
    data = response.json()
    assert data["ticket_id"] == 1
    assert "status" in data


def test_close_ticket():
    response = client.post("/tickets/1/close", json={"technician": "Ismael"})
    assert response.status_code == 200
    data = response.json()
    assert data["ticket_id"] == 1
    assert data["status"] == "cerrado"


def test_assign_ticket():
    response = client.post("/tickets/1/assign", json={"technician": "Ismael"})
    assert response.status_code == 200
    data = response.json()
    assert data["ticket_id"] == 1
    assert data["assigned_to"] == "Ismael"


def test_create_ticket():
    with patch("server.ServiceDeskClient") as mock_client_cls:
        mock_client = mock_client_cls.return_value
        mock_client.create_ticket.return_value = {"request_id": 123}
        response = client.post(
            "/tickets",
            json={"title": "Ejemplo", "description": "Prueba"},
        )
        assert response.status_code == 200
        assert response.json() == {"request_id": 123}
        mock_client.create_ticket.assert_called_once_with("Ejemplo", "Prueba")
