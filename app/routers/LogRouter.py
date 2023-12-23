from typing import List

from fastapi import APIRouter, Depends

from app.const import LOG_TAGS
from app.models.Log import Log
from app.responses.LogResponse import LogResponse
from app.services.LogService import LogService
from app.services.AuthService import AuthService

router = APIRouter(prefix="/log", tags=LOG_TAGS)


@router.get(
    "",
    response_description="Получить лог по id",
    response_model=LogResponse,
    response_model_by_alias=False,
)
async def get_log(log_id: str):
    return LogService.get_log(log_id)


@router.get(
    "/AllLogs",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить все логи",
    response_model=List[LogResponse],
    response_model_by_alias=False,
)
async def get_all_logs():
    return LogService.get_all_logs()


@router.get(
    "/search",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Поиск логов по полю",
    response_model=List[Log],
    response_model_by_alias=False
)
async def search_logs(sorting_field: str, data: str):
    return LogService.search_logs(sorting_field, data)
