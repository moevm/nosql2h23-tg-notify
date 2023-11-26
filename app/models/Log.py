from datetime import datetime

from pydantic import BaseModel


class Log(BaseModel):
    changeDate: datetime
    action: str
    tableId: str
    adminId: str
