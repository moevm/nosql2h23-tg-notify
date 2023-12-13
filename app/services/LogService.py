from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models.Log import Log
from app.responses.LogResponse import LogResponse


class LogService:
    @staticmethod
    def get_log(log_id: str) -> LogResponse:
        log = db.Logs.find_by_id(log_id)
        admin = db.Users.find_by_id(log.adminId)
        table = db.Tables.find_by_id(log.tableId)

        if log is not None:
            return LogResponse(
                id=log.id,
                changeDate=log.changeDate,
                action=log.action,
                message=log.message,
                admin=admin,
                table=table
            )
        else:
            raise HTTPException(status_code=404, detail="Log not found")

    @staticmethod
    def get_all_logs() -> List[LogResponse]:
        logs = db.Logs.find_all()
        res = []
        for log in logs:
            admin = db.Users.find_by_id(log.adminId)
            table = db.Tables.find_by_id(log.tableId)
            print(log.id)
            res.append(LogResponse(
                id=log.id,
                changeDate=log.changeDate,
                action=log.action,
                message=log.message,
                admin=admin,
                table=table
            ))

        return res

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
