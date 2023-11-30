from typing import List

from bson.objectid import ObjectId

from app.backend.db import db
from app.models import User


class UserService:
    @staticmethod
    def get_user(user_id: str) -> User:
        return db.collection_Users.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_all_users() -> List[User]:
        return list(db.collection_Users.find())
