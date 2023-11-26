from pymongo import MongoClient

from app.backend.config import DB_NAME, DB_HOST, DB_PASSWORD, DB_PORT, DB_USERNAME


class MongoDB:
    def __init__(self, db_name, username, password, host, port):
        CONNECTION_STRING = f"mongodb://{username}:{password}@{host}:{port}"

        self.db = MongoClient(CONNECTION_STRING)[db_name]

        self.collection_Users = self.db["Users"]
        self.collection_Tables = self.db["Tables"]
        self.collection_Logs = self.db["Logs"]


db = MongoDB(DB_NAME, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)
