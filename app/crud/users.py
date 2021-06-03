from .base import CrudBase
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.core import verify_password
from typing import Optional
from app.schemas.user import  CreateUser, UpdateUser, DeleteUser
from dataclasses import asdict


class CrudUser(CrudBase[User, CreateUser, UpdateUser]):
    async def check_passwd_and_uname(self, db: AsyncSession, obj_in: DeleteUser):
        dct = asdict(obj_in)
        st = select(self.model).filter_by(**dct).exists()
        res = await db.execute(st)
        return res

    def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_by_username(self , db: AsyncSession, username: str):
        st = select(self.model).filter(self.model.username == username).first()
        return await db.execute(st)

    async def username_isexist(self, db: AsyncSession, username: str):
        stat = select(self.model.username).filter_by(username=username).exists()
        res = await db.execute(stat) 
        return res

    async def delete_by_username(self, db: AsyncSession, username: str):
        obj = select(self.model.username).filter_by(username=username)
        await db.delete(obj)
        await db.commit()
        return obj
    
    async def set_confirmed(self, db: AsyncSession, username: str):
        st = update(self.model).where(self.model.username == username).values(confirmed=True)
        await db.execute(st)

cruduser = CrudUser(User)
