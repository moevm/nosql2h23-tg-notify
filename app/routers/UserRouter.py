from typing import List

from fastapi import APIRouter

from app.models.User import User
from app.services.UserService import UserService
from app.services.AuthService import AuthService

router = APIRouter(prefix="/user")


@router.get(
    "/{id}",
    response_description="Получить пользователя по id",
    response_model=User,
    response_model_by_alias=False,
)
async def get_user(user_id: str):
    return UserService.get_user(user_id)


@router.get(
    "/users/",
    # dependencies=[Depends(AuthService.validate_token)], <- проверка на токен
    response_description="Получить всех пользователей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_all_users():
    return UserService.get_all_users()


@router.get(
    "/teachers/",
    # dependencies=[Depends(AuthService.validate_token)], <- проверка на токен
    response_description="Получить всех учителей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_all_teachers():
    return UserService.get_all_teachers()
