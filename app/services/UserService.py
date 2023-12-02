from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models import User


class UserService:
    @staticmethod
    def get_user(user_id: str) -> User:
        user = db.Users.find_by_id(user_id)

        if user is not None:
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def get_all_users() -> List[User]:
        return db.Users.find_all()

    @staticmethod
    def get_all_teachers() -> List[User]:
        return db.Users.find_all_teachers()
