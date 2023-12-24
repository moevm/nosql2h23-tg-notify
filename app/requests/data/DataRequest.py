from pydantic import BaseModel


class DataRequest(BaseModel):
    data: list
    