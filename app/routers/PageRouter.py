from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="")


templates = Jinja2Templates(directory="app/templates")


@router.get("/auth", response_class=HTMLResponse)
async def get_auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})
    