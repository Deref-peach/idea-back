from app.db import SessionLocal
from app.models import User
from app.crud import CrudUser
from fastapi import Depends, HTTPException
from app.core import settings
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
import app.core.security as security

user =  CrudUser(User)

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"api/v1/login/access-token"
)

async def get_db():
    async with SessionLocal() as session:
        yield session


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    payload = jwt.decode(
        token, settings.JWT_SECRET_KEY, algorithms=[security.ALGORITHM]
    )
    user = user.get(db, id=payload['userid'])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


