from pydantic import BaseModel


class EditProfileRequest(BaseModel):
    user_id: str
    login: str
    password: str
    photoUrl: str
    username: str
