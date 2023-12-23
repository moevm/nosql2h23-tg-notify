import json
import os.path
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import os

from bson.json_util import dumps
from bson.json_util import loads
from fastapi import HTTPException

from app.backend.db import db
from app.models.Log import Log
from app.models.Table import Table
from app.models.User import User
from app.responses.ExportResponse import ExportResponse


class DataService:
    @staticmethod
    def export_data() -> ExportResponse:
        users = db.Users.find_all()
        tables = db.Tables.find_all()
        logs = db.Logs.find_all()

        response = ExportResponse(users=users, tables=tables, logs=logs)
        
        if os.environ.get('DISPLAY','') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        tk = Tk()
        tk.withdraw()
        tk.attributes('-topmost', True)
        type_files = [('Json', '*.json')]
        path = fd.asksaveasfilename(title="Сохранить как...", filetypes=type_files, defaultextension=".json")

        _, ext = os.path.splitext(path)
        if ext not in [".json"]:
            msg.showerror(title="Ошибка", message='Файл должен быть только с разрешением .json')
            raise HTTPException(status_code=400, detail="Invalid file type")

        try:
            with open(path, 'w') as file:
                json.dump(json.loads(dumps(response)), file, ensure_ascii=False)

        except OSError:
            msg.showerror(title="Ошибка", message='Не удалось создать файл')
            raise HTTPException(status_code=400, detail="Cannot create file")

        return response

    @staticmethod
    def import_data():
        if os.environ.get('DISPLAY','') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')

        tk = Tk()
        tk.withdraw()
        tk.attributes('-topmost', True)
        type_files = [('Json', '*.json')]
        path = fd.askopenfilename(title="Выберете файл", filetypes=type_files, parent=None)

        _, ext = os.path.splitext(path)
        if ext not in [".json"]:
            msg.showerror(title="Ошибка", message='Файл должен быть только с разрешением .json')
            raise HTTPException(status_code=400, detail="Invalid file type")

        try:
            with open(path, 'r') as file:
                data = loads(file.read())

        except OSError:
            msg.showerror(title="Ошибка", message='Не удалось создать файл')
            raise HTTPException(status_code=400, detail="Cannot create file")

        for user in data[0][1]:
            db.Users.insert(User(
                    id=user[0][1],
                    login=user[1][1],
                    password=user[2][1],
                    userTg=user[3][1],
                    username=user[4][1],
                    position=user[5][1],
                    creationDate=user[6][1],
                    photoUrl=user[7][1],
                    role=user[8][1]
                ))

        for log in data[1][1]:
            db.Logs.insert(Log(
                id=log[0][1],
                changeDate=log[1][1],
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
                creationDate=table[3][1],
                message=table[4][1],
                columnName=table[5][1]
            ))
