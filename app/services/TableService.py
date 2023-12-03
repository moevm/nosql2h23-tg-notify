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

    @staticmethod
    def search_tables(sorting_field: str, data: str) -> List[Table]:
        if sorting_field == "Названию таблицы":
            return db.Tables.find_by_tableName(data)
        elif sorting_field == "Ссылке":
            return db.Tables.find_by_url(data)
        elif sorting_field == "Дате создания":
            return db.Tables.find_by_date(data)
        else:
            raise HTTPException(status_code=400, detail="Invalid sorting field")
