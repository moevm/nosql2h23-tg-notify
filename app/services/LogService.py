from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models import Log


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
