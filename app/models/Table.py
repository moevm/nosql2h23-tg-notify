from datetime import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, Field, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]


class Table(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    tableName: str
    tableUrl: str
    creationDate: datetime
    message: str
    columnName: str
