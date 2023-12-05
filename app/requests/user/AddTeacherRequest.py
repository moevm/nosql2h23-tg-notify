from pydantic import BaseModel


class AddTeacherRequest(BaseModel):
    username: str
    position: str
    userTg: str
