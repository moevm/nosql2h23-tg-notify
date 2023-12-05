from fastapi import (
    APIRouter,
    Body
)

from app.const import (
    AUTH_TAGS,
    AUTH_URL,
)
from app.requests.auth.AuthRequest import AuthRequest
from app.responses.TokenResponse import TokenResponse
from app.services.AuthService import AuthService

router = APIRouter(prefix="" + AUTH_URL, tags=AUTH_TAGS)


@router.post(
    "",
    response_model=TokenResponse,
    response_description="Авторизация пользователя"
)
async def authenticate_user(request: AuthRequest = Body(...)) -> TokenResponse | None:
    return AuthService.authenticate_user(request)
