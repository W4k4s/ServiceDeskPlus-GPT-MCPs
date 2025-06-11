from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from sdp_client import ServiceDeskClient

app = FastAPI(title="ServiceDesk Plus MCP")

class Ticket(BaseModel):
    title: str
    description: str

class TechnicianPayload(BaseModel):
    technician: str

@app.get("/")
async def read_root():
    return {"status": "MCP operativo"}


@app.get("/tickets/{ticket_id}")
async def get_ticket(ticket_id: int):
    """Devuelve la información de un ticket por su ID."""
    # Aquí se integraría la llamada a SDP para obtener el ticket
    return {"ticket_id": ticket_id, "status": "pendiente"}


@app.post("/tickets/{ticket_id}/close")
async def close_ticket(ticket_id: int, payload: TechnicianPayload):
    """Cierra un ticket registrando el técnico responsable."""
    return {
        "ticket_id": ticket_id,
        "closed_by": payload.technician,
        "status": "cerrado",
    }


@app.post("/tickets/{ticket_id}/assign")
async def assign_ticket(ticket_id: int, payload: TechnicianPayload):
    """Asigna un ticket a un técnico."""
    return {
        "ticket_id": ticket_id,
        "assigned_to": payload.technician,
    }

@app.post("/tickets")
async def create_ticket(ticket: Ticket):
    """Crea un ticket en ServiceDesk Plus utilizando la API v3."""
    try:
        client = ServiceDeskClient()
        result = client.create_ticket(ticket.title, ticket.description)
    except Exception as exc:  # pragma: no cover - errores inesperados
        raise HTTPException(status_code=500, detail=str(exc))
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
