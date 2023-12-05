from typing import List

from fastapi import APIRouter

from app.const import TABLE_TAGS
from app.models.Table import Table
from app.services.TableService import TableService
from app.requests.table.AddTableRequest import AddTableRequest
from app.requests.table.EditTableRequest import EditTableRequest

router = APIRouter(prefix="/table", tags=TABLE_TAGS)


@router.get(
    "/{id}",
    response_description="Получить таблицу по id",
    response_model=Table,
    response_model_by_alias=False,
)
async def get_table(table_id: str):
    return TableService.get_table(table_id)


@router.get(
    "/tables/",
    # dependencies=[Depends(AuthService.validate_token)], <- проверка на токен
    response_description="Получить все таблицы",
    response_model=List[Table],
    response_model_by_alias=False,
)
async def get_all_tables():
    return TableService.get_all_tables()


@router.get(
    "/search/",
    response_description="Поиск таблиц по полю",
    response_model=List[Table],
    response_model_by_alias=False
)
async def search_tables(sorting_field: str, data: str):
    return TableService.search_tables(sorting_field, data)


@router.post(
    "/addTable/",
    response_description="Добавление таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def add_table(request: AddTableRequest):
    return TableService.add_table(request)


@router.post(
    "/editTable/",
    response_description="Редактирование таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def edit_table(request: EditTableRequest):
    return TableService.edit_table(request)
