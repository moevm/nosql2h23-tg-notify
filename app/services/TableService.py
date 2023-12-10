from datetime import datetime
from typing import List

from fastapi import HTTPException

from app.backend.db import db
from app.models.Table import Table
from app.requests.table.AddTableRequest import AddTableRequest
from app.requests.table.EditTableRequest import EditTableRequest


class TableService:
    @staticmethod
    def get_table(table_id: str) -> Table:
        table = db.Tables.find_by_id(table_id)

        if table is not None:
            return table
        else:
            raise HTTPException(status_code=404, detail="Table not found")

    @staticmethod
    def get_tables(table_ids: List[str]) -> List[Table]:
        res = []
        for table_id in table_ids:
            table = db.Tables.find_by_id(table_id)

            if table is None:
                raise HTTPException(status_code=404, detail=f"Table {table_id} not found")

            res.append(table)

        return res

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

    @staticmethod
    def add_table(request: AddTableRequest) -> Table:
        table = Table(
            tableName=request.tableName,
            tableUrl=request.tableUrl,
            creationDate=datetime.utcnow(),
            message=request.message,
            columnName=request.columnName
        )
        db.Tables.insert(table)

        return table

    @staticmethod
    def edit_table(request: EditTableRequest) -> Table:
        table = db.Tables.find_by_id(request.table_id)

        if table is None:
            raise HTTPException(status_code=404, detail="Table not found")

        table.tableName = request.tableName
        table.tableUrl = request.tableUrl
        table.message = request.message
        table.columnName = request.columnName
        db.Tables.update(table)

        return table

    @staticmethod
    def delete_table(table_id: str) -> Table:
        table = db.Tables.find_by_id(table_id)

        if table is None:
            raise HTTPException(status_code=404, detail="Table not found")

        db.Tables.delete_by_id(table_id)

        return table

    @staticmethod
    def delete_tables(table_ids: List[str]) -> List[Table]:
        res = []
        for table_id in table_ids:
            table = db.Tables.find_by_id(table_id)

            if table is None:
                raise HTTPException(status_code=404, detail=f"Table {table_id} not found")

            res.append(table)

        db.Tables.delete_many(table_ids)

        return res

