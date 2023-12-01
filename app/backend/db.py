from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import List

from app.backend.config import DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USERNAME
from app.models.User import User
from app.models.Table import Table
from app.models.Log import Log


class MongoDB:
    def __init__(self, db_name, username, password, host, port):
        CONNECTION_STRING = f"mongodb://{username}:{password}@{host}:{port}"

        self.db = MongoClient(CONNECTION_STRING)[db_name]

        self.Users = UsersCollection(self.db["Users"])
        self.Tables = TablesCollection(self.db["Tables"])
        self.Logs = LogsCollection(self.db["Logs"])


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

    def delete(self, id: str):
        self.collection.delete_one({"_id": ObjectId(id)})
        

class TablesCollection:
    def __init__(self, collection):
        self.collection = collection

    def get_by_id(self, id: str) -> Table:
        table_json = self.collection.find_one({"_id": ObjectId(id)})

        return Table(**table_json)
    
    def get_all(self) -> List[Table]:
        list_tables = []
        cursor_tables = self.collection.find()

        for t in cursor_tables:
            list_tables.append(Table(**t))

        return list_tables

    def insert(self, table: Table):
        self.collection.insert_one(table.model_dump(by_alias=True, exclude=["id"]))   
    
    def delete(self, id: str):
        self.collection.delete_one({"_id": ObjectId(id)})


class LogsCollection:
    def __init__(self, collection):
        self.collection = collection

    def get_by_id(self, id: str) -> Log:
        log_json = self.collection.find_one({"_id": ObjectId(id)})

        return Log(**log_json)
    
    # TODO сделать ограничение на кол-во
    def get_all(self) -> List[Log]:
        list_logs = []
        cursor_logs = self.collection.find()

        for l in cursor_logs:
            list_logs.append(Log(**l))

        return list_logs

    def insert(self, log: Log):
        self.collection.insert_one(log.model_dump(by_alias=True, exclude=["id"]))   

    def delete(self, id: str):
        self.collection.delete_one({"_id": ObjectId(id)})


db = MongoDB(DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)
