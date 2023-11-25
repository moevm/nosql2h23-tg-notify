from typing import Optional
from datetime import datetime
from pydantic import BaseModel, field_validator, Field


class User(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
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
    def check_role(cls, v, values, **kwargs):
        data = values.data
        
        print(data)

        
        if v == "Admin":
            if data.get('login') is None or data.get('password') is  None or data.get('photoUrl') is  None:
                raise ValueError('For a Admin login ,password, photoUrl must not be None')
            
            if data.get('userTg') is not None or data.get('position') is not None:
                raise ValueError('For a Admin userTg, position must  be None') 
        
        if v == "Teacher":  
            if data.get('login') is not None or data.get('password') is not None or data.get('photoUrl') is not None:
                raise ValueError('For a Teacher login ,password, photoUrl must be None')
            
            if data.get('userTg') is None or data.get('position') is None:
                raise ValueError('For a Teacher userTg, position must not be None') 
            

"""
как это работатет
user_1 = {
  "login": "vasi",
  "password": "12345678",
  "username": "Василий Иванович Пупкин",
  "creationDate": "2012-04-23T18:25:43.511Z",
  "role": "Admin",
  "photoUrl": "https://2021-02/1614282221_80-p-chernii-fon-laika-98.jpg"
}

u = User(**user_1)

"""