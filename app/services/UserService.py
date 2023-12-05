from datetime import datetime
from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models.User import User
from app.requests.AddTeacherRequest import AddTeacherRequest
from app.requests.EditProfileRequest import EditProfileRequest
from app.services.AuthService import AuthService


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

    @staticmethod
    def search_teachers(sorting_field: str, data: str) -> List[User]:
        if sorting_field == "ФИО":
            return db.Users.find_users_by_username(data)
        elif sorting_field == "Должности":
            return db.Users.find_users_by_position(data)
        elif sorting_field == "Никнейму Телеграмм":
            return db.Users.find_users_by_userTg(data)
        else:
            raise HTTPException(status_code=400, detail="Invalid sorting field")

    @staticmethod
    def add_teacher(request: AddTeacherRequest) -> User:
        user = User(
            userTg=request.userTg,
            username=request.username,
            position=request.position,
            role="Teacher",
            creationDate=datetime.utcnow()
        )
        db.Users.insert(user)

        return user

    @staticmethod
    def edit_profile(request: EditProfileRequest) -> User:
        user = db.Users.find_by_id(request.user_id)
        user.login = request.login
        user.password = AuthService.bcrypt(request.password)
        user.username = request.username
        user.photoUrl = request.photoUrl
        db.Users.update(user)

        return user
