from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool

from example.config import Config
from example.models import CreateTaskPayload, PaginatedTasks, PongModel, Task
from example.repositories import TaskRepository
from example.utils import decode_next_id

config = Config()  # type: ignore

pool = AsyncConnectionPool(str(config.db_dsn), open=False)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Open and close the connection pool."""
    await pool.open()
    yield
    await pool.close()


app = FastAPI(lifespan=lifespan)


async def get_db_connection() -> AsyncGenerator[AsyncConnection, None]:
    """Get a database connection."""
    async with pool.connection() as conn:
        yield conn


async def get_task_repository(
    conn: Annotated[AsyncConnection, Depends(get_db_connection)],
) -> TaskRepository:
    """Get a task repository."""
    return TaskRepository(conn)


@app.get("/ping/")
async def ping() -> PongModel:
    """Ping endpoint to check if the server is up and running."""
    return PongModel(ping="pong")


@app.get("/tasks/")
async def list_tasks(
    repo: Annotated[TaskRepository, Depends(get_task_repository)],
    after: str | None = None,
    limit: Annotated[int, Query(ge=1, lte=100)] = 25,
) -> PaginatedTasks:
    """List tasks."""
    _after = 0
    if after is not None:
        _after = decode_next_id(after)
    return await repo.list(_after, limit)


@app.post("/tasks/", status_code=201)
async def create_task(
    repo: Annotated[TaskRepository, Depends(get_task_repository)],
    payload: CreateTaskPayload,
) -> Task:
    """Create a task."""
    return await repo.create(payload)


@app.get("/tasks/{id}/")
async def get_task(
    repo: Annotated[TaskRepository, Depends(get_task_repository)],
    id: int,
) -> Task:
    """Get a task by id."""
    return await repo.get(id)
