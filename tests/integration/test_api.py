from fastapi.testclient import TestClient
from server import app

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
