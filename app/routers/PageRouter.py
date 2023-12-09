from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import datetime

from app.services.TableService import TableService

router = APIRouter(prefix="/page")


templates = Jinja2Templates(directory="app/templates")


@router.get("/auth", response_class=HTMLResponse)
async def get_auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@router.get("/tables", response_class=HTMLResponse)
async def get_auth_page(request: Request):
    return templates.TemplateResponse("tables.html", {"request": request})
    