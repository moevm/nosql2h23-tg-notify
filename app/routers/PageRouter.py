from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.TableService import TableService
from app.services.UserService import UserService
from app.services.AuthService import AuthService

router = APIRouter(prefix="/page")

router_auth = APIRouter(prefix="")

templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/add_table",
    dependencies=[Depends(AuthService.page_validate_token)],
    response_class=HTMLResponse    
)
async def get_add_table_page(request: Request):
    return templates.TemplateResponse("add_table.html", {"request": request})


@router.get(
    "/add_teacher",
    dependencies=[Depends(AuthService.page_validate_token)],
    response_class=HTMLResponse    
)
async def get_add_table_page(request: Request):
    return templates.TemplateResponse("add_teacher.html", {"request": request})


@router_auth.get(
    "/",
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
            dependencies=[Depends(AuthService.page_validate_token)],
            response_class=HTMLResponse)
async def get_teachers_page(request: Request):
    return templates.TemplateResponse("teachers.html", {"request": request})


@router.get("/logs",
            response_class=HTMLResponse,
            dependencies=[Depends(AuthService.page_validate_token)])
async def get_logs_page(request: Request):
    return templates.TemplateResponse("logs.html", {"request": request})


@router.get(
    "/setting_table/{table_id}",
    response_class=HTMLResponse,
    dependencies=[Depends(AuthService.page_validate_token)]
)
async def get_setting_table_page(request: Request, table_id: str):
    table = TableService.get_table(table_id)
    return templates.TemplateResponse("edit_table.html", {"request": request, "table": table})


@router.get(
    "/setting_teacher/{teacher_id}",
    response_class=HTMLResponse,
    dependencies=[Depends(AuthService.page_validate_token)]
)
async def get_setting_table_page(request: Request, teacher_id: str):
    teacher = UserService.get_user(teacher_id)
    return templates.TemplateResponse("edit_teacher.html", {"request": request, "teacher": teacher})


@router.get(
    "/import_export",
    response_class=HTMLResponse,
    dependencies=[Depends(AuthService.page_validate_token)]
)
async def get_setting_table_page(request: Request):
    return templates.TemplateResponse("import_export.html", {"request": request})


@router.get(
    "/import",
    response_class=HTMLResponse,
    dependencies=[Depends(AuthService.page_validate_token)]
)
async def get_setting_table_page(request: Request):
    return templates.TemplateResponse("import.html", {"request": request})


@router.get(
    "/export",
    response_class=HTMLResponse,
    dependencies=[Depends(AuthService.page_validate_token)]
)
async def get_setting_table_page(request: Request):
    return templates.TemplateResponse("export.html", {"request": request})



