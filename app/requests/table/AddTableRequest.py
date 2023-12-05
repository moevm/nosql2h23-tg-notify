from pydantic import BaseModel


class AddTableRequest(BaseModel):
    tableName: str
    tableUrl: str
    message: str
    columnName: str
