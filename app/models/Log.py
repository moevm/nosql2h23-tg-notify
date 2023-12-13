from datetime import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class Log(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    changeDate: datetime
    action: str
    message: str
    tableId: Optional[str] = None
    adminId: Optional[str] = None
