from pydantic import BaseModel


class PongModel(BaseModel):
    """Response schema for the ping endpoint."""

    ping: str
