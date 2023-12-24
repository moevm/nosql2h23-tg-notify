from pydantic import BaseModel


class ExportResponse(BaseModel):
    users: list
    logs: list
    tables: list
