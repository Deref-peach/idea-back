from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.api.deps import get_db, user
from sqlalchemy.orm import Session
from app.core import create_access_token



router = APIRouter()

@router.post("/login/access-token")
def login_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = user.authenticate(
        db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {
        "access_token": create_access_token({'userid': user.id}),
        "token_type": "bearer",
    }

