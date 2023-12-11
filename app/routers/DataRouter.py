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
    dependencies=[Depends(AuthService.validate_token)],
    response_description="Экспорт данных бд",
    response_model=ExportResponse,
    response_model_by_alias=False,
)
async def export_data() -> ExportResponse:
    return DataService.export_data()
