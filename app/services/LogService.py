from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models.Log import Log


class LogService:
    @staticmethod
    def get_log(log_id: str) -> Log:
        log = db.Logs.find_by_id(log_id)

        if log is not None:
            return log
        else:
            raise HTTPException(status_code=404, detail="Log not found")

    @staticmethod
    def get_all_logs() -> List[Log]:
        return db.Logs.find_all()

    @staticmethod
    def search_logs(sorting_field: str, data: str) -> List[Log]:
        if sorting_field == "Дате":
            return db.Logs.find_by_date(data)
        elif sorting_field == "Действию":
            return db.Logs.find_by_action(data)
        elif sorting_field == "Пользователю":
            return db.Logs.find_by_adminId(data)
        elif sorting_field == "Таблице":
            return db.Logs.find_by_tableId(data)
        else:
            raise HTTPException(status_code=400, detail="Invalid sorting field")
