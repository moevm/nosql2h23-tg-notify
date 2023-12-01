from datetime import datetime

from pydantic import BaseModel


class Table(BaseModel):
    tableName: str
    tableUrl: str
    creationDate: datetime
    message: str
    columnName: str
