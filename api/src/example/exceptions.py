"""Custom exceptions for this example."""


class ExampleError(Exception):
    """Base exception for this example."""

    pass


class CreateError(ExampleError, ValueError):
    """Raised when a creation fails."""

    pass


class NotFoundError(ExampleError):
    """Raised when a resource is not found."""

    pass


class InvalidCursorError(ExampleError, ValueError):
    """Raised when a cursor is invalid."""

    pass
