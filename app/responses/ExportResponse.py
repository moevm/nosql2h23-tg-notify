from typing import List

from pydantic import BaseModel

from app.models.Log import Log
from app.models.Table import Table
from app.models.User import User


class ExportResponse(BaseModel):
    users: list#List[User]
    logs: list#List[Log]
    tables: list#List[Table]
