from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator

from app.models.Table import Table
from app.models.User import User

PyObjectId = Annotated[str, BeforeValidator(str)]


class LogResponse(BaseModel):
    id: PyObjectId
    changeDate: datetime
    action: str
    message: str
    table: Table | None
    admin: User | None
