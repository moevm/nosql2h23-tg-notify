from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.AuthService import AuthService

router = APIRouter(prefix="/page")

templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/auth",
    response_class=HTMLResponse
)
async def get_auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@router.get(
    "/admin",
    dependencies=[Depends(AuthService.page_validate_token)],
    response_class=HTMLResponse
)
async def get_admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@router.get(
    "/tables",
    dependencies=[Depends(AuthService.page_validate_token)],
    response_class=HTMLResponse
)
async def get_tables_page(request: Request):
    return templates.TemplateResponse("tables.html", {"request": request})



@router.get("/teachers",
            response_class=HTMLResponse)
async def get_teachers_page(request: Request):
    return templates.TemplateResponse("teachers.html", {"request": request})
    
    