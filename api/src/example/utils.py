"""Utility functions for the example application."""

import base64
import binascii

from example.exceptions import InvalidCursorError

_NUM_AFTER_PARTS = 2


def encode_next_id(after: int) -> str:
    """Encode the next cursor."""
    return base64.b64encode(f"id:{after}".encode()).decode()


def decode_next_id(next: str) -> int:
    """Decode the next cursor."""
    try:
        data = base64.b64decode(next.encode()).decode().split(":")
    except binascii.Error as e:
        message = "Invalid cursor"
        raise InvalidCursorError(message) from e
    if len(data) != _NUM_AFTER_PARTS or data[0] != "id":
        message = "Invalid cursor"
        raise ValueError(message)
    return int(data[1])
