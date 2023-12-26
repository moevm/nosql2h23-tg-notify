from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import (
    UserRouter,
    AuthRouter,
    PageRouter,
    LogRouter,
    TableRouter,
    DataRouter
)

app = FastAPI(
    title="nosql2h23-tg-notify API",
    description="UI for admin",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.mount("/files", StaticFiles(directory="app/files"), name="static_files")

app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
app.include_router(PageRouter.router)
app.include_router(PageRouter.router_auth)
app.include_router(LogRouter.router)
app.include_router(TableRouter.router)
app.include_router(DataRouter.router)
