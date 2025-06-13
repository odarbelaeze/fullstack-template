# fullstack-template

A dev environment structured as a mono repo.

Here are the bits and pieces:

- `./api` a [FastAPI][fastapi] application
- `./migrations` a bunch of [migrate][migrate] migrations.
- `./proxy` an [nginx][nginx] proxy.
- `./ui` a [React][react] application.

## Getting Started

`docker compose up --watch` should get you started.

[fastapi]: https://fastapi.tiangolo.com/
[migrate]: https://github.com/golang-migrate/migrate
[nginx]: https://nginx.org/
[react]: https://react.dev/
