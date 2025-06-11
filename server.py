from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="ServiceDesk Plus MCP")

class Ticket(BaseModel):
    title: str
    description: str

@app.get("/")
async def read_root():
    return {"status": "MCP operativo"}

@app.post("/tickets")
async def create_ticket(ticket: Ticket):
    # Aquí se integraría la lógica para crear tickets en SDP
    api_key = os.environ.get("SDP_API_KEY", "not-set")
    return {"message": "Ticket recibido", "title": ticket.title, "api_key": api_key}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
