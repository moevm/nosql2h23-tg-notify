from typing import List

from fastapi import APIRouter, HTTPException

from app.models.User import User
from app.services import UserService

router = APIRouter(prefix="/api")


@router.get(
    "/user/{id}",
    response_description="Получить пользователя по id",
    response_model=User,
    response_model_by_alias=False,
)
def get_user(user_id: str):
    user = UserService.get_user(user_id)

    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")


@router.get(
    "/users/",
    response_description="Получить всех пользователей",
    response_model=List[User],
    response_model_by_alias=False,
)
async def list_students():
    return UserService.get_all_users()
