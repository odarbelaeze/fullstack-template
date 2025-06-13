# Install uv
FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:0.5.13-alpine /usr/local/bin/uv /usr/local/bin/uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache curl

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Copy the project into the image
ADD . /app

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen
