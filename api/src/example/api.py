from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from example.config import Config
from example.models.ping import PongModel

config = Config()  # type: ignore

pool = AsyncConnectionPool(str(config.db_dsn), open=False)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Open and close the connection pool."""
    await pool.open()
    yield
    await pool.close()


app = FastAPI(lifespan=lifespan, root_path="/api")


@app.get("/ping/")
async def ping() -> PongModel:
    """Ping endpoint to check if the server is up and running."""
    return PongModel(ping="pong")
