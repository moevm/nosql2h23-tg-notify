from typing import List

from fastapi import (
    APIRouter,
    Body,
    Depends
)

from app.const import USER_TAGS
from app.models.User import User
from app.requests.AddTeacherRequest import AddTeacherRequest
from app.requests.EditProfileRequest import EditProfileRequest
from app.services.UserService import UserService
from app.services.AuthService import AuthService


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
    # dependencies=[Depends(AuthService.validate_token)], # <- проверка на токен
    response_description="Получить всех пользователей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_all_users():
    return UserService.get_all_users()


@router.get(
    "/teachers/",
    # dependencies=[Depends(AuthService.validate_token)], # <- проверка на токен
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


@router.post(
    "/addTeacher/",
    response_description="Добавить преподователя",
    response_model=User,
    response_model_by_alias=False
)
async def add_teacher(request: AddTeacherRequest = Body(...)):
    return UserService.add_teacher(request)


@router.post(
    "/editProfile/",
    response_description="Изменить данные профиля",
    response_model=User,
    response_model_by_alias=False
)
async def edit_profile(request: EditProfileRequest = Body(...)):
    return UserService.edit_profile(request)
