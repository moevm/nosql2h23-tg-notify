db = db.getSiblingDB('admin')
db.auth('root', 'root')
db = db.getSiblingDB('Database')

db.createCollection('Users')
let user_id_1 = ObjectId("658ac73b66691d23a0a8d7a5");
let user_id_5 = ObjectId("658ac73b66691d23a0a8d7a4");

db.Users.insertMany([
    {
        "_id": user_id_1,
        "login": "vasia",
        "password": "$2b$12$fY/mEvyT8P/mkvsMXINhLeF5.xTDordepTfJKr0lx.BMqqhPwtd6K",  // 12345678
        "userTg": null,
        "username": "Василий Иванович Пупкин",
        "position": null,
        "creationDate": "2012-04-23T18:25:43.511Z",
        "role": "Admin",
        "photoUrl": "https://www.w3schools.com/w3css/img_snowtops.jpg"
    },
    { 
        "login": null,
        "password": null,
        "userTg": "@tg_max",
        "username": "Максим Максимыч",
        "position": "ректор",
        "creationDate": "2012-04-23T18:25:43.511Z",
        "role": "Teacher",
        "photoUrl": null
    },
    { 
        "login": null,
        "password": null,
        "userTg": "@apofeoz",
        "username": "Вадим Александрович",
        "position": "Преподаватель ИТ",
        "creationDate": "2012-04-27T19:25:43.511Z",
        "role": "Teacher",
        "photoUrl": null
    },
    {
        "login": null,
        "password": null,
        "userTg": "@begemotxd",
        "username": "Александр Кимович",
        "position": "Преподаватель МГУ",
        "creationDate": "2012-02-27T19:25:43.511Z",
        "role": "Teacher",
        "photoUrl": null
    },
    {
        "_id": user_id_5,
        "login": "maxim",
        "password": "$2b$12$oZgxl81nnIIxPV6vJm8bc.3SJQVXxDdvnY2ZtM7kSKEmaPp10bgIm",  //1234
        "userTg": null,
        "username": "Анатолий Анатольевич Кирпич",
        "position": null,
        "creationDate": "2012-01-23T18:25:43.511Z",
        "role": "Admin",
        "photoUrl": "https://www.w3schools.com/w3css/img_snowtops.jpg"
    }
])



let table_id_1 = ObjectId("658ac73b66691d23a0a8d7a3");
let table_id_3 = ObjectId("658ac73b66691d23a0a8d7a2");

db.createCollection('Tables')
db.Tables.insertMany([
    {
        "_id": table_id_1,
        "tableName": "ИДЗ 0999",
        "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8SrBND8HQyPcK2po8QYdHQ0G_27Rvh2jU/edit?resourcekey#gid=1186562930",
        "creationDate": "2012-04-23T18:25:43.511Z",
        "message": "Произошли измениния в таблице \"ИДЗ 0999\"",
        "columnName": "A3"
    },
    {

        "tableName": "ИДЗ 666",
        "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8Shsidgodigdiodhgidogod=drgxgd",
        "creationDate": "2012-04-23T18:25:43.511Z",
        "message": "Произошло что-то ужасное в \"ИДЗ 666\"",
        "columnName": "A4"
    },
    {
        "_id": table_id_3,
        "tableName": "Таблица квазиопургинальных переменных",
        "tableUrl": "https://docs.google.com/spreadsheets/d/1mOdWylUHkB8Shsidgodigdiodhgidogodasdfasdf",
        "creationDate": "2012-06-27T15:25:43.511Z",
        "message": "Произошло что-то ужасное",
        "columnName": "A1"
    }

])


db.createCollection('Logs')
db.Logs.insertMany([
    { 
        "changeDate": "2012-04-23T18:25:43.511Z",
        "action": "Добавление таблицы",
        "message": "Была добавлена таблица апофис",
        "tableId": table_id_1.toString(),
        "adminId": null
    },
    {
        "changeDate": "2012-04-23T18:25:43.511Z",
        "action": "Удаление таблицы",
        "message": "Была удалена таблица с учителями",
        "tableId": table_id_1.toString(),
        "adminId": user_id_1.toString()
    },
    {
        "changeDate": "2012-07-23T18:25:43.511Z",
        "action": "Добавление таблицы",
        "message": "Была добавлена таблица с Барбусями",
        "tableId": table_id_3.toString(),
        "adminId": user_id_1.toString()
    },
    {
        "changeDate": "2012-07-23T18:25:43.511Z",
        "action": "Добавление преподавателя",
        "message": "Был добавлен преподаватель Александр Кимович",
        "tableId": null,
        "adminId": user_id_5.toString()
    },
    {
        "changeDate": "2012-07-24T18:25:43.511Z",
        "action": "Добавление преподавателя",
        "message": "Был добавлен преподаватель Вадим Александрович",
        "tableId": null,
        "adminId": user_id_5.toString()
    }
])