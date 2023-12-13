from bson.objectid import ObjectId
from pymongo import MongoClient

from config import DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

user_id = ObjectId()
user_1 = {
    "_id": user_id,
    "login": "vasia",
    "password": "$2b$12$fY/mEvyT8P/mkvsMXINhLeF5.xTDordepTfJKr0lx.BMqqhPwtd6K",  # 12345678
    "userTg": None,
    "username": "Василий Иванович Пупкин",
    "position": None,
    "creationDate": "2012-04-23T18:25:43.511Z",
    "role": "Admin",
    "photoUrl": "https://www.w3schools.com/w3css/img_snowtops.jpg"
}

user_2 = {
    "_id": ObjectId(),
    "login": None,
    "password": None,
    "userTg": "@tg_max",
    "username": "Максим Максимыч",
    "position": "ректор",
    "creationDate": "2012-04-23T18:25:43.511Z",
    "role": "Teacher",
    "photoUrl": None
}

table_id = ObjectId()
table_1 = {
    "_id": table_id,
    "tableName": "ИДЗ 0999",
    "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8SrBND8HQyPcK2po8QYdHQ0G_27Rvh2jU/edit?resourcekey#gid=1186562930",
    "creationDate": "2012-04-23T18:25:43.511Z",
    "message": "Произошли измениния в таблице \"ИДЗ 0999\"",
    "columnName": "A3"
}

table_2 = {
    "_id": ObjectId(),
    "tableName": "ИДЗ 666",
    "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8Shsidgodigdiodhgidogod=drgxgd",
    "creationDate": "2012-04-23T18:25:43.511Z",
    "message": "Произошло что-то ужасное в \"ИДЗ 666\"",
    "columnName": "A4"
}

log_1 = {
    "_id": ObjectId(),
    "changeDate": "2012-04-23T18:25:43.511Z",
    "action": "Добавление таблицы",
    "message": "Была добавлена таблица апофис",
    "tableId": str(table_id),
    "adminId": None
}

log_2 = {
    "_id": ObjectId(),
    "changeDate": "2012-04-23T18:25:43.511Z",
    "action": "Удаление таблицы",
    "message": "Была удалена таблица с учителями",
    "tableId": str(table_id),
    "adminId": str(user_id)
}

if __name__ == "__main__":
    CONNECTION_STRING = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}"

    db = MongoClient(CONNECTION_STRING)[DB_NAME]

    collection_Users = db["Users"]
    collection_Tables = db["Tables"]
    collection_Logs = db["Logs"]

    collection_Users.insert_many([user_1, user_2])
    collection_Tables.insert_many([table_1, table_2])
    collection_Logs.insert_many([log_1, log_2])
