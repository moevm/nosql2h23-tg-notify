from datetime import (
    datetime,
    timedelta,
)
from typing import Annotated

from fastapi import HTTPException, Body, Depends
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.backend.config import TOKEN_KEY
from app.backend.db import db
from app.const import (
    TOKEN_ALGORITHM,
    TOKEN_EXPIRE_MINUTES
)
from app.const import apikey_scheme_page, apikey_scheme_request
from app.requests.auth.AuthRequest import AuthRequest
from app.responses.TokenResponse import (
    TokenResponse
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def authenticate_user(request: AuthRequest = Body(...)) -> TokenResponse | None:
        user_login = request.login
        user = db.Users.find_by_login(user_login)

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if user.password is None:
            raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            if not AuthService.verify(user.password, request.password):
                raise HTTPException(status_code=401, detail="Incorrect password")
            else:
                access_token = AuthService._create_access_token(user.id, user_login, user.photoUrl)
                return TokenResponse(access_token=access_token)

    @staticmethod
    def _create_access_token(user_id: str, login: str, photo_url: str) -> str:
        payload = {
            "id": user_id,
            "login": login,
            "expires_at": AuthService._expiration_time(),
            "photo_url": photo_url
        }

        return jwt.encode(payload, TOKEN_KEY, algorithm=TOKEN_ALGORITHM)

    @staticmethod
    def _expiration_time() -> str:
        expires_at = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
        return expires_at.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def is_expired(expires_at: str) -> bool:
        return datetime.strptime(expires_at, "%Y-%m-%d %H:%M:%S") < datetime.utcnow()

    @staticmethod
    async def page_validate_token(token: Annotated[str, Depends(apikey_scheme_page)]):
        if token is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        try:
            payload = jwt.decode(token, TOKEN_KEY, algorithms=[TOKEN_ALGORITHM])

            login: str = payload.get("login")
            expires_at: str = payload.get("expires_at")

            if login is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")

            user = db.Users.find_by_login(login)
            if login != user.login:
                raise HTTPException(status_code=401, detail="Invalid token")

            if AuthService.is_expired(expires_at):
                raise HTTPException(status_code=401, detail="Token expired")

        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    @staticmethod
    async def request_validate_token(token: Annotated[str, Depends(apikey_scheme_request)]):
        if token is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        try:
            payload = jwt.decode(token, TOKEN_KEY, algorithms=[TOKEN_ALGORITHM])

            login: str = payload.get("login")
            expires_at: str = payload.get("expires_at")

            if login is None:
                raise HTTPException(status_code=401, detail="Invalid credentials")

            user = db.Users.find_by_login(login)
            if login != user.login:
                raise HTTPException(status_code=401, detail="Invalid token")

            if AuthService.is_expired(expires_at):
                raise HTTPException(status_code=401, detail="Token expired")

        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid credentials")
