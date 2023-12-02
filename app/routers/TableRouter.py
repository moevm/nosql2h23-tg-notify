from typing import List

from fastapi import APIRouter

from app.models.Table import Table
from app.services.TableService import TableService
from app.services.AuthService import AuthService

router = APIRouter(prefix="/table")


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
