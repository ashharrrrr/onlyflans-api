from fastapi import FastAPI

from app.api.routes import health, users

app = FastAPI(title="OnlyFlans API")

app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["health"],
)

app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["users"],
)
