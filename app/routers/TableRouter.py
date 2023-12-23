from typing import List

from fastapi import APIRouter, Depends, Query

from app.const import TABLE_TAGS
from app.models.Table import Table
from app.requests.table.AddTableRequest import AddTableRequest
from app.requests.table.EditTableRequest import EditTableRequest
from app.services.AuthService import AuthService
from app.services.TableService import TableService

router = APIRouter(prefix="/table", tags=TABLE_TAGS)


@router.get(
    "",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить таблицу по id",
    response_model=Table,
    response_model_by_alias=False,
)
async def get_table(table_id: str):
    return TableService.get_table(table_id)


@router.get(
    "/tables",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить таблицы по id",
    response_model=List[Table],
    response_model_by_alias=False,
)
async def get_tables(table_ids: List[str] = Query(...)):
    return TableService.get_tables(table_ids)


@router.get(
    "/AllTables",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить все таблицы",
    response_model=List[Table],
    response_model_by_alias=False,
)
async def get_all_tables():
    return TableService.get_all_tables()


@router.get(
    "/search",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Поиск таблиц по полю",
    response_model=List[Table],
    response_model_by_alias=False
)
async def search_tables(sorting_field: str, data: str):
    return TableService.search_tables(sorting_field, data)


@router.post(
    "/addTable",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Добавление таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def add_table(request: AddTableRequest):
    return TableService.add_table(request)


@router.put(
    "/editTable",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Редактирование таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def edit_table(request: EditTableRequest):
    return TableService.edit_table(request)


@router.delete(
    "/deleteTable",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Удаление таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def delete_table(table_id: str):
    return TableService.delete_table(table_id)


@router.delete(
    "/deleteTables",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Удаление таблиц",
    response_model=List[Table],
    response_model_by_alias=False
)
async def delete_tables(table_ids: List[str]):
    return TableService.delete_tables(table_ids)

