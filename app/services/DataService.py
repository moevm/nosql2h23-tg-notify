import json
import os.path
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os
from datetime import datetime

from bson.json_util import dumps
from bson.json_util import loads
from fastapi import HTTPException

from app.backend.db import db
from app.models.Log import Log
from app.models.Table import Table
from app.models.User import User
from app.responses.ExportResponse import ExportResponse
from app.requests.data.DataRequest import DataRequest
from app.utils import find_string, filter_date


class DataService:
    @staticmethod
    def export_database() -> ExportResponse:
        users = db.Users.find_all()
        tables = db.Tables.find_all()
        logs = db.Logs.find_all()
        #print(type(users), type(tables), type(logs))
        response = ExportResponse(users=users, tables=tables, logs=logs)
        print(response)
        save_path = "app/files/data.json"
        with open(save_path, 'w') as file:
            json.dump(json.loads(dumps(response)), file, ensure_ascii=False)
        return response


    @staticmethod
    def import_database(request: DataRequest):
        data = request.data

        for user in data[0][1]:
            db.Users.insert(User(
                    id=user[0][1],
                    login=user[1][1],
                    password=user[2][1],
                    userTg=user[3][1],
                    username=user[4][1],
                    position=user[5][1],
                    creationDate=filter_date(user[6][1]["$date"]),
                    photoUrl=user[7][1],
                    role=user[8][1]
                ))

        for log in data[1][1]:
            db.Logs.insert(Log(
                id=log[0][1],
                changeDate=filter_date(log[1][1]["$date"]),
                action=log[2][1],
                message=log[3][1],
                tableId=log[4][1],
                adminId=log[5][1]
            ))

        for table in data[2][1]:
            db.Tables.insert(Table(
                id=table[0][1],
                tableName=table[1][1],
                tableUrl=table[2][1],
                creationDate=filter_date(table[3][1]["$date"]),
                message=table[4][1],
                columnName=table[5][1]
            ))        

 