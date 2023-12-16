from fastapi import (
    APIRouter,
    Depends
)

from app.const import DATA_TAGS
from app.responses.ExportResponse import ExportResponse
from app.services.AuthService import AuthService
from app.services.DataService import DataService

router = APIRouter(prefix="/data", tags=DATA_TAGS)


@router.get(
    "/export",
    dependencies=[Depends(AuthService.request_validate_token)],
    description="Экспорт данных бд",
    response_model=ExportResponse,
    response_model_by_alias=False,
)
async def export_data() -> dict:
    DataService.export_data()

    return {"status": "success"}


@router.get(
    "/import",
    dependencies=[Depends(AuthService.request_validate_token)],
    description="Импорт данных в бд"
)
async def import_data() -> dict:
    DataService.import_data()

    return {"status": "success"}
