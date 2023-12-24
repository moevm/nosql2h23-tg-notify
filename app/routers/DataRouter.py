
from fastapi import (
    APIRouter,
    Depends
)

from app.const import DATA_TAGS
from app.requests.data.DataRequest import DataRequest
from app.responses.ExportResponse import ExportResponse
from app.services.AuthService import AuthService
from app.services.DataService import DataService

router = APIRouter(prefix="/data", tags=DATA_TAGS)


@router.get(
    "/export",
    dependencies=[Depends(AuthService.request_validate_token)],
    description="Экспорт данных бд",
    #response_model=ExportResponse,
    response_model_by_alias=False,
)
async def export_data() -> dict:
    DataService.export_database()

    return {"status": "success"}


@router.put(
    "/import",
    dependencies=[Depends(AuthService.request_validate_token)],
    description="Импорт данных в бд"
)
async def import_data(request: DataRequest) -> dict:
    DataService.import_database(request)

    return {"status": "success"}



"""
@router.put(
    "/editTable",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Редактирование таблицы",
    response_model=Table,
    response_model_by_alias=False
)
async def edit_table(request: EditTableRequest):
    return TableService.edit_table(request)

"""

