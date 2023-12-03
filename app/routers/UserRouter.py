from typing import List

from fastapi import (
    APIRouter
)

from app.const import USER_TAGS
from app.models.User import User
from app.services.UserService import UserService

router = APIRouter(prefix="/user", tags=USER_TAGS)


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


@router.get(
    "/search/",
    response_description="Поиск преподователей по полю",
    response_model=List[User],
    response_model_by_alias=False
)
async def search_teachers(sorting_field: str, data: str):
    return UserService.search_teachers(sorting_field, data)
