from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    photo_url: str
