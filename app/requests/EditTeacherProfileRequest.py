from pydantic import BaseModel


class EditTeacherProfileRequest(BaseModel):
    user_id: str
    username: str
    position: str
    userTg: str
