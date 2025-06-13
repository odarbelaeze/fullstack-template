FROM node:20.18-alpine

# Change the working directory to the `app` directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache curl

# Install dependencies
RUN --mount=type=cache,target=/root/.npm \
    --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    npm ci

ADD . /app
