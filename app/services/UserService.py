from datetime import datetime
from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models.User import User
from app.requests.user.AddTeacherRequest import AddTeacherRequest
from app.requests.user.EditAdminProfileRequest import EditAdminProfileRequest
from app.requests.user.EditTeacherProfileRequest import EditTeacherProfileRequest
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
    def get_users(user_ids: List[str]) -> List[User]:
        res = []
        for user_id in user_ids:
            user = db.Users.find_by_id(user_id)

            if user is None:
                raise HTTPException(status_code=404, detail=f"User {user_id} not found")

            res.append(user)

        return res

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
    def edit_admin_profile(request: EditAdminProfileRequest) -> User:
        user = db.Users.find_by_id(request.user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user.role == "Teacher":
            raise HTTPException(status_code=400, detail="Invalid user role")

        user.login = request.login
        if request.password != "":
            user.password = AuthService.bcrypt(request.password)
        user.username = request.username
        user.photoUrl = request.photoUrl
        db.Users.update(user)

        return user

    @staticmethod
    def edit_teacher_profile(request: EditTeacherProfileRequest) -> User:
        user = db.Users.find_by_id(request.user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user.role == "Admin":
            raise HTTPException(status_code=400, detail="Invalid user role")

        if request.userTg[0] != '@':
            raise HTTPException(status_code=400, detail="Invalid userTg")

        user.username = request.username
        user.position = request.position
        user.userTg = request.userTg
        db.Users.update(user)

        return user

    @staticmethod
    def delete_teacher(user_id: str) -> User:
        user = db.Users.find_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user.role == "Admin":
            raise HTTPException(status_code=400, detail="Invalid user role")

        db.Users.delete_by_id(user_id)

        return user

    @staticmethod
    def delete_teachers(user_ids: List[str]) -> List[User]:
        res = []
        for user_id in user_ids:
            user = db.Users.find_by_id(user_id)

            if user is None:
                raise HTTPException(status_code=404, detail=f"User {user_id} not found")

            if user.role == "Admin":
                raise HTTPException(status_code=400, detail=f"Invalid {user_id} user role")

            res.append(user)

        db.Users.delete_many(user_ids)

        return res
