from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from typing import List

from app.models.User import User
from app.backend.db import db

router = APIRouter(prefix="/api")

@router.get(
    "/user/{id}",
    response_description="Get a single user",
    response_model=User,
    response_model_by_alias=False,
)
def get_user(id: str):
    """
    Get the record for a specific user, looked up by `id`.
    """
    
    user =  db.collection_Users.find_one({"_id": ObjectId(id)})
    
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    

@router.get(
    "/users/",
    response_description="List all Users",
    response_model=List[User],
    response_model_by_alias=False,
)
async def list_students():
    """
    List all of the Users data in the database.
    """
    return  list(db.collection_Users.find())