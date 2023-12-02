from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models import Table


class TableService:
    @staticmethod
    def get_table(table_id: str) -> Table:
        table = db.Tables.find_by_id(table_id)

        if table is not None:
            return table
        else:
            raise HTTPException(status_code=404, detail="Table not found")

    @staticmethod
    def get_all_tables() -> List[Table]:
        return db.Tables.find_all()
