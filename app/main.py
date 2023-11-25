from fastapi import FastAPI

from app.routers import (
    test,
    user
)

app = FastAPI(
    title="nosql2h23-tg-notify API",
    description="UI for admin",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

print("Docs: http://127.0.0.1:8000/docs")

app.include_router(test.router)
app.include_router(user.router)
