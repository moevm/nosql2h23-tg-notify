from typing import List

from fastapi import (
    APIRouter,
    Body,
    Depends,
    Query
)

from app.const import USER_TAGS
from app.models.User import User
from app.requests.user.AddTeacherRequest import AddTeacherRequest
from app.requests.user.EditAdminProfileRequest import EditAdminProfileRequest
from app.requests.user.EditTeacherProfileRequest import EditTeacherProfileRequest
from app.services.AuthService import AuthService
from app.services.UserService import UserService

router = APIRouter(prefix="/user", tags=USER_TAGS)


@router.get(
    "",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить пользователя по id",
    response_model=User,
    response_model_by_alias=False,
)
async def get_user(user_id: str):
    return UserService.get_user(user_id)


@router.get(
    "/users",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить пользователей по id",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_users(user_ids: List[str] = Query(...)):
    return UserService.get_users(user_ids)


@router.get(
    "/AllUsers",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить всех пользователей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_all_users():
    return UserService.get_all_users()


@router.get(
    "/teachers",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Получить всех учителей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def get_all_teachers():
    return UserService.get_all_teachers()


@router.get(
    "/search",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Поиск преподователей по полю",
    response_model=List[User],
    response_model_by_alias=False
)
async def search_teachers(sorting_field: str, data: str):
    return UserService.search_teachers(sorting_field, data)


@router.post(
    "/addTeacher",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Добавить преподователя",
    response_model=User,
    response_model_by_alias=False
)
async def add_teacher(request: AddTeacherRequest = Body(...)):
    return UserService.add_teacher(request)


@router.put(
    "/editAdminProfile",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Изменить данные профиля админа",
    response_model=User,
    response_model_by_alias=False
)
async def edit_admin_profile(request: EditAdminProfileRequest = Body(...)):
    return UserService.edit_admin_profile(request)


@router.put(
    "/editTeacherProfile",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Изменить данные профиля преподавателя",
    response_model=User,
    response_model_by_alias=False
)
async def edit_teacher_profile(request: EditTeacherProfileRequest = Body(...)):
    return UserService.edit_teacher_profile(request)


@router.delete(
    "/deleteTeacher",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Удалить преподавателя",
    response_model=User,
    response_model_by_alias=False
)
async def delete_teacher(user_id: str):
    return UserService.delete_teacher(user_id)


@router.delete(
    "/deleteTeachers",
    dependencies=[Depends(AuthService.request_validate_token)],
    response_description="Удалить преподавателей",
    response_model=List[User],
    response_model_by_alias=False
)
async def delete_teachers(user_ids: List[str]):
    return UserService.delete_teachers(user_ids)
