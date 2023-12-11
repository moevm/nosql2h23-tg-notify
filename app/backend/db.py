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

    def find_by_id(self, user_id: str) -> User | None:
        user = self.collection.find_one({"_id": ObjectId(user_id)})

        if user is None:
            return user

        return User(**user)

    def find_by_login(self, login: str) -> User | None:
        user = self.collection.find_one({"login": login})

        if user is None:
            return user

        return User(**user)

    def find_users_by_username(self, username: str) -> List[User]:
        users = self.collection.find({"username": username})

        if not users:
            return users

        return self.create_json(users)

    def find_users_by_position(self, position: str) -> List[User]:
        users = self.collection.find({"position": position})

        if not users:
            return users

        return self.create_json(users)

    def find_users_by_userTg(self, userTg: str) -> List[User]:
        users = self.collection.find({"userTg": userTg})

        if not users:
            return users

        return self.create_json(users)

    def find_all(self) -> List[User]:
        users = self.collection.find()

        if not users:
            return users

        return self.create_json(users)

    def find_all_teachers(self) -> List[User]:
        teachers = self.collection.find({"role": "Teacher"})

        if not teachers:
            return teachers

        return self.create_json(teachers)

    def insert(self, user: User):
        self.collection.insert_one(user.model_dump(by_alias=True, exclude=["id"]))

    def export_users(self):
        users = self.collection.find()

        return users

    def update(self, user: User):
        self.collection.update_one({"_id": ObjectId(user.id)}, {"$set": user.model_dump(by_alias=True, exclude=["id"])})

    def delete_by_id(self, user_id: str):
        self.collection.delete_one({"_id": ObjectId(user_id)})

    def delete_many(self, user_ids: List[str]):
        for user_id in user_ids:
            self.delete_by_id(user_id)

    @staticmethod
    def create_json(users: []):
        res_list = []

        for u in users:
            res_list.append(User(**u))

        return res_list


class TablesCollection:
    def __init__(self, collection):
        self.collection = collection

    def find_by_id(self, table_id: str) -> Table | None:
        table = self.collection.find_one({"_id": ObjectId(table_id)})

        if table is None:
            return table

        return Table(**table)

    def find_by_tableName(self, tableName: str) -> List[Table]:
        tables = self.collection.find({"tableName": tableName})

        if not tables:
            return tables

        return self.create_json(tables)

    def find_by_url(self, url: str) -> List[Table]:
        tables = self.collection.find({"tableUrl": url})

        if not tables:
            return tables

        return self.create_json(tables)

    def find_by_date(self, date: str) -> List[Table]:
        tables = self.collection.find({"creationDate": date})

        if not tables:
            return tables

        return self.create_json(tables)

    def find_all(self) -> List[Table]:
        tables = self.collection.find()

        if not tables:
            return tables

        return self.create_json(tables)

    def insert(self, table: Table):
        self.collection.insert_one(table.model_dump(by_alias=True, exclude=["id"]))

    def export_tables(self):
        tables = self.collection.find()

        return tables

    def update(self, table: Table):
        self.collection.update_one({"_id": ObjectId(table.id)}, {"$set": table.model_dump(by_alias=True, exclude=["id"])})

    def delete_by_id(self, table_id: str):
        self.collection.delete_one({"_id": ObjectId(table_id)})

    def delete_many(self, table_ids: List[str]):
        for table_id in table_ids:
            self.delete_by_id(table_id)

    @staticmethod
    def create_json(tables: []):
        res_list = []

        for t in tables:
            res_list.append(Table(**t))

        return res_list


class LogsCollection:
    def __init__(self, collection):
        self.collection = collection

    def find_by_id(self, table_id: str) -> Log | None:
        log = self.collection.find_one({"_id": ObjectId(table_id)})

        if log is None:
            return log

        return Log(**log)

    def find_by_date(self, date: str) -> List[Log]:
        logs = self.collection.find({"changeDate": date})

        if not logs:
            return logs

        return self.create_json(logs)

    def find_by_action(self, action: str) -> List[Log]:
        logs = self.collection.find({"action": action})

        if not logs:
            return logs

        return self.create_json(logs)

    def find_by_tableId(self, tableId: str) -> List[Log]:
        logs = self.collection.find({"tableId": tableId})

        if not logs:
            return logs

        return self.create_json(logs)

    def find_by_adminId(self, adminId: str) -> List[Log]:
        logs = self.collection.find({"adminId": adminId})

        if not logs:
            return logs

        return self.create_json(logs)

    # TODO сделать ограничение на кол-во
    def find_all(self) -> List[Log]:
        logs = self.collection.find()

        if not logs:
            return logs

        return self.create_json(logs)

    def update(self, log: Log):
        self.collection.update_one({"_id": ObjectId(log.id)}, {"$set": log.model_dump(by_alias=True, exclude=["id"])})

    def export_logs(self):
        logs = self.collection.find()

        return logs

    def insert(self, log: Log):
        self.collection.insert_one(log.model_dump(by_alias=True, exclude=["id"]))

    def delete_by_id(self, log_id: str):
        self.collection.delete_one({"_id": ObjectId(log_id)})

    @staticmethod
    def create_json(logs: []):
        res_list = []

        for l in logs:
            res_list.append(Log(**l))

        return res_list


db = MongoDB(DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)
