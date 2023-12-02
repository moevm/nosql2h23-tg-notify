from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from app.routers import (
    UserRouter,
    AuthRouter,
    PageRouter
)

app = FastAPI(
    title="nosql2h23-tg-notify API",
    description="UI for admin",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


print("http://127.0.0.1:8000/docs")
#uvicorn app.main:app


app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
app.include_router(PageRouter.router)
