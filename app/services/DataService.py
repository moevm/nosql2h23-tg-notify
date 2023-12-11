import os.path
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg

from bson.json_util import dumps
from bson.json_util import loads
from fastapi import HTTPException

from app.backend.db import db
from app.responses.ExportResponse import ExportResponse


class DataService:
    @staticmethod
    def export_data() -> ExportResponse:
        users = db.Users.find_all()
        tables = db.Tables.find_all()
        logs = db.Logs.find_all()

        response = ExportResponse(users=users, tables=tables, logs=logs)

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
                file.write("{\n")
                file.write("users: ")
                file.write(str(loads(dumps(db.Users.export_users()))))
                file.write(",")
                file.write("\n")
                file.write("tables: ")
                file.write(str(loads(dumps(db.Tables.export_tables()))))
                file.write(",")
                file.write("\n")
                file.write("logs: ")
                file.write(str(loads(dumps(db.Logs.export_logs()))))
                file.write("\n")
                file.write("}")

        except OSError:
            msg.showerror(title="Ошибка", message='Не удалось создать файл')
            raise HTTPException(status_code=400, detail="Cannot create file")

        return response
