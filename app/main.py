from fastapi import FastAPI

from app.routers import (
    UserRouter,
    AuthRouter
)

app = FastAPI(
    title="nosql2h23-tg-notify API",
    description="UI for admin",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
