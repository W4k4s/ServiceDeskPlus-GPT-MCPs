"""Esquemas JSON para las herramientas expuestas por el MCP."""
from pydantic import BaseModel

class CreateTicketSchema(BaseModel):
    title: str
    description: str

class GetTicketSchema(BaseModel):
    ticket_id: int
