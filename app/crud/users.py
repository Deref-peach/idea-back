from .base import CrudBase
from app.models import User
from sqlalchemy.orm import Session
from app.core import verify_password
from typing import Optional
from app.schemas.user import  CreateUser, 

class CrudUser(CrudBase[User, CreateUser, UpdateUser]):
    def delete(self, db: Session, obj_in: DeleteUser):
        obj = db.query(self.model).filter_by(**obj_in.dict(exclude_unset=True))
        db.delete(obj)
        db.commit()
        return obj

    def authenticate(self, db: Session, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_by_username(self , db: Session, username: str):
        return db.query(self.model).filter(self.model.username == username).first()

    def check_username(self, db: Session, username: str):
        return db.query(self.model) # TODO

cruduser = CrudUser(User)
