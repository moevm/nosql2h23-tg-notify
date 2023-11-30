from datetime import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, Field, BeforeValidator
from pydantic.functional_validators import field_validator

PyObjectId = Annotated[str, BeforeValidator(str)]


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    login: Optional[str] = None
    password: Optional[str] = None
    userTg: Optional[str] = None
    username: str
    position: Optional[str] = None
    creationDate: datetime
    photoUrl: Optional[str] = None
    role: str

    # проверка на None для Admin и Teacher
    @field_validator('role')
    def check_role(cls, v, values):
        data = values.data

        if v == "Admin":
            if data.get('login') is None or data.get('password') is None or data.get('photoUrl') is None:
                raise ValueError('For a Admin login ,password, photoUrl must not be None')

            if data.get('userTg') is not None or data.get('position') is not None:
                raise ValueError('For a Admin userTg, position must  be None')

        if v == "Teacher":
            if data.get('login') is not None or data.get('password') is not None or data.get('photoUrl') is not None:
                raise ValueError('For a Teacher login ,password, photoUrl must be None')

            if data.get('userTg') is None or data.get('position') is None:
                raise ValueError('For a Teacher userTg, position must not be None')

        return v
