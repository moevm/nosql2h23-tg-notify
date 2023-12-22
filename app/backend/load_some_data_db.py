from bson.objectid import ObjectId
from pymongo import MongoClient

from config import DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

user_id_1 = ObjectId()
user_1 = {
    "_id": user_id_1,
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

user_3 = {
    "_id": ObjectId(),
    "login": None,
    "password": None,
    "userTg": "@apofeoz",
    "username": "Вадим Александрович",
    "position": "Преподаватель ИТ",
    "creationDate": "2012-04-27T19:25:43.511Z",
    "role": "Teacher",
    "photoUrl": None
}

user_4 = {
    "_id": ObjectId(),
    "login": None,
    "password": None,
    "userTg": "@begemotxd",
    "username": "Александр Кимович",
    "position": "Преподаватель МГУ",
    "creationDate": "2012-02-27T19:25:43.511Z",
    "role": "Teacher",
    "photoUrl": None
}

user_id_5 = ObjectId()
user_5 = {
    "_id": user_id_5,
    "login": "maxim",
    "password": "$2b$12$oZgxl81nnIIxPV6vJm8bc.3SJQVXxDdvnY2ZtM7kSKEmaPp10bgIm",  #1234
    "userTg": None,
    "username": "Анатолий Анатольевич Кирпич",
    "position": None,
    "creationDate": "2012-01-23T18:25:43.511Z",
    "role": "Admin",
    "photoUrl": "https://www.w3schools.com/w3css/img_snowtops.jpg"
}

table_id_1 = ObjectId()
table_1 = {
    "_id": table_id_1,
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

table_id_3 = ObjectId()
table_3 = {
    "_id": table_id_3,
    "tableName": "Таблица квазиопургинальных переменных",
    "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8Shsidgodigdiodhgidogodasdfasdf",
    "creationDate": "2012-06-27T15:25:43.511Z",
    "message": "Произошло что-то ужасное",
    "columnName": "A1"
}

log_1 = {
    "_id": ObjectId(),
    "changeDate": "2012-04-23T18:25:43.511Z",
    "action": "Добавление таблицы",
    "message": "Была добавлена таблица апофис",
    "tableId": str(table_id_1),
    "adminId": None
}

log_2 = {
    "_id": ObjectId(),
    "changeDate": "2012-04-23T18:25:43.511Z",
    "action": "Удаление таблицы",
    "message": "Была удалена таблица с учителями",
    "tableId": str(table_id_1),
    "adminId": str(user_id_1)
}

log_3 = {
    "_id": ObjectId(),
    "changeDate": "2012-07-23T18:25:43.511Z",
    "action": "Добавление таблицы",
    "message": "Была добавлена таблица с Барбусями",
    "tableId": str(table_id_3),
    "adminId": str(user_id_1)
}

log_4 = {
    "_id": ObjectId(),
    "changeDate": "2012-07-23T18:25:43.511Z",
    "action": "Добавление преподавателя",
    "message": "Был добавлен преподаватель Александр Кимович",
    "tableId": None,
    "adminId": str(user_id_5)
}

log_5 = {
    "_id": ObjectId(),
    "changeDate": "2012-07-24T18:25:43.511Z",
    "action": "Добавление преподавателя",
    "message": "Был добавлен преподаватель Вадим Александрович",
    "tableId": None,
    "adminId": str(user_id_5)
}

if __name__ == "__main__":
    CONNECTION_STRING = f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}"

    db = MongoClient(CONNECTION_STRING)[DB_NAME]

    collection_Users = db["Users"]
    collection_Tables = db["Tables"]
    collection_Logs = db["Logs"]

    collection_Users.insert_many([user_1, user_2, user_3, user_4, user_5])
    collection_Tables.insert_many([table_1, table_2, table_3])
    collection_Logs.insert_many([log_1, log_2, log_3, log_4, log_5])
