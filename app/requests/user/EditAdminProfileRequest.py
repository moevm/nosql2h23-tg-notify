from pydantic import BaseModel


class EditAdminProfileRequest(BaseModel):
    user_id: str
    login: str
    password: str
    photoUrl: str
    username: str
