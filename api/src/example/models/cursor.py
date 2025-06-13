"""Cursor model.

For cursor based pagination.
"""

import base64
from typing import Self

from pydantic import BaseModel


class Cursor(BaseModel):
    """Cursor model."""

    id: str

    def encode(self) -> str:
        """Encode the cursor as a base64 encoded string."""
        return base64.urlsafe_b64encode(self.model_dump_json().encode()).decode()

    @classmethod
    def decode(cls, encoded: str) -> Self:
        """Decode a cursor from a base64 encoded string."""
        return cls.parse_raw(base64.urlsafe_b64decode(encoded))
