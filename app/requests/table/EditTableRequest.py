from pydantic import BaseModel


class EditTableRequest(BaseModel):
    table_id: str
    tableName: str
    tableUrl: str
    message: str
    columnName: str
