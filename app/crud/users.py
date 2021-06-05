from .base import CrudBase
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.core import verify_password
from typing import Optional
from app.schemas.user import  CreateUser, UpdateUser, DeleteUser
from dataclasses import asdict

class Container:
    pass

class CrudUser(CrudBase[User, CreateUser, UpdateUser]):
    async def check_passwd_and_uname(self, db: AsyncSession, obj_in: DeleteUser):
        dct = asdict(obj_in)
        st = select(self.model).filter_by(**dct).exists()
        res = await db.execute(st)
        return res

    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        user = await self.get_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_by_username(self , db: AsyncSession, username: str):
        st = select(self.model).filter(self.model.username == username)
        res = await db.execute(st)
        return res.first()

    async def username_isexist(self, db: AsyncSession, username: str):
        stat = select(self.model.username).filter_by(username=username).exists()
        res = await db.execute(stat) 
        return res

    async def delete_by_username(self, db: AsyncSession, username: str):
        st = delete(self.model).where(username==username)
        await db.execute(st)
        await db.commit()

    async def set_confirmed(self, db: AsyncSession, username: str, val: bool = True):
        st = update(self.model).where(self.model.username == username).values(confirmed=val)
        await db.execute(st)
        await db.commit()

    async def get_user(self, db: AsyncSession, username: str, fields):
        fields = map(lambda el: el.name.value, fields)
        st = select(getattr(self.model, field) for field in fields).filter_by(username=username)
        res = await db.execute(st)
        user = res.first()
        c = Container()
        c.__dict__.update(zip(fields, user)) # hack to describe field: value
        return c

cruduser = CrudUser(User)
