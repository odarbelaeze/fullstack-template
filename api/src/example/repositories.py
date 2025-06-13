"""Repository classes for the example application."""

import logging

from psycopg import AsyncConnection
from psycopg.rows import class_row

from example.exceptions import CreateError, NotFoundError
from example.models import CreateTaskPayload, PaginatedTasks, Task
from example.utils import encode_next_id

logger = logging.getLogger(__name__)


class TaskRepository:
    """Repository for tasks."""

    def __init__(self, conn: AsyncConnection) -> None:
        self.conn = conn

    async def create(self, payload: CreateTaskPayload) -> Task:
        """Create a task."""
        async with self.conn.cursor(row_factory=class_row(Task)) as cursor:
            result = await cursor.execute(
                """INSERT INTO tasks (name, description)
                   VALUES (%(name)s, %(description)s)
                   RETURNING
                    id, name, description, is_completed, created_at, updated_at""",
                payload.model_dump(),
            )
            task = await result.fetchone()
            if task is None:
                message = "Failed to create task"
                logger.info(message)
                raise CreateError(message)
            return task

    async def get(self, id: int) -> Task:
        """Get a task by id."""
        async with self.conn.cursor(row_factory=class_row(Task)) as cursor:
            result = await cursor.execute(
                """SELECT id, name, description, is_completed, created_at, updated_at
                   FROM tasks
                   WHERE id = %s""",
                (id,),
            )
            task = await result.fetchone()
            if task is None:
                message = "Task not found"
                logger.info(message)
                raise NotFoundError(message)
            return task

    async def list(self, after: int = 0, limit: int = 100) -> PaginatedTasks:
        """List a page of tasks tasks."""
        async with self.conn.cursor(row_factory=class_row(Task)) as cursor:
            result = await cursor.execute(
                """SELECT id, name, description, is_completed, created_at, updated_at
                   FROM tasks
                   WHERE id > %(after)s
                   ORDER BY id
                   LIMIT %(limit)s""",
                {"after": after, "limit": limit},
            )
            tasks = await result.fetchall()
            _next = None
            if len(tasks) == limit:
                _next = encode_next_id(tasks[-1].id)
            return PaginatedTasks(tasks=tasks, next=_next)
