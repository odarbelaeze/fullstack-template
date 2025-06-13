"""Models for this example."""

from pydantic import AwareDatetime, BaseModel


class CreateTaskPayload(BaseModel):
    """Payload for creating a task."""

    name: str
    description: str


class Task(BaseModel):
    """Task model."""

    id: int
    name: str
    description: str
    is_completed: bool
    created_at: AwareDatetime
    updated_at: AwareDatetime


class PaginatedTasks(BaseModel):
    """Paginated tasks."""

    tasks: list[Task]
    next: str | None


class PongModel(BaseModel):
    """Response schema for the ping endpoint."""

    ping: str
