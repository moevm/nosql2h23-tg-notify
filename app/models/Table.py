from datetime import datetime

from pydantic import BaseModel


class Log(BaseModel):
    tableName: str
    tableUrl: str
    creationDate: datetime
    message: str
    columnName: str
