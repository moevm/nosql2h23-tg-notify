from typing import List

from fastapi import APIRouter

from app.const import LOG_TAGS
from app.models.Log import Log
from app.services.LogService import LogService
from app.services.AuthService import AuthService

router = APIRouter(prefix="/log", tags=LOG_TAGS)


@router.get(
    "/{id}",
    response_description="Получить лог по id",
    response_model=Log,
    response_model_by_alias=False,
)
async def get_log(log_id: str):
    return LogService.get_log(log_id)


@router.get(
    "/logs/",
    # dependencies=[Depends(AuthService.validate_token)], <- проверка на токен
    response_description="Получить все логи",
    response_model=List[Log],
    response_model_by_alias=False,
)
async def get_all_logs():
    return LogService.get_all_logs()


@router.get(
    "/search/",
    response_description="Поиск логов по полю",
    response_model=List[Log],
    response_model_by_alias=False
)
async def search_logs(sorting_field: str, data: str):
    return LogService.search_logs(sorting_field, data)
