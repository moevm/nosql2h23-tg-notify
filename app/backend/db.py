from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import List

from app.backend.config import DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USERNAME
from app.models.User import User


class MongoDB:
    def __init__(self, db_name, username, password, host, port):
        CONNECTION_STRING = f"mongodb://{username}:{password}@{host}:{port}"

        self.db = MongoClient(CONNECTION_STRING)[db_name]

        self.Users = UsersCollection(self.db["Users"])
        self.collection_Tables = self.db["Tables"]
        self.collection_Logs = self.db["Logs"]


class UsersCollection:
    def __init__(self, collection):
        self.collection = collection 

    def get_by_id(self, user_id: str) -> User:
        user_json = self.collection.find_one({"_id": ObjectId(user_id)})

        return User(**user_json)
    
    def get_by_login(self, login: str) -> User:
        user_json = self.collection.find_one({"login": login})

        return User(**user_json)

    def get_all(self) -> List[User]:
        
        list_users = []
        cursor_users = self.collection.find()

        for u in cursor_users:
            list_users.append(User(**u))

        return list_users

    def insert(self, user: User):
        self.collection.insert_one(user.model_dump(by_alias=True, exclude=["id"]))   

        

class TablesCollection:
    def __init__(self, collection):
        self.collection = collection

class LogsCollection:
    def __init__(self, collection):
        self.collection = collection


db = MongoDB(DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)

