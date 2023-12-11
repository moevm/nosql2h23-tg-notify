from typing import List

from pydantic import BaseModel

from app.models.Log import Log
from app.models.Table import Table
from app.models.User import User


class ExportResponse(BaseModel):
    users: List[User]
    logs: List[Log]
    tables: List[Table]
