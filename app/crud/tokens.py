from app.models import ConfirmToken
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class CrudToken:
    def __init__(self, model):
        self.model = model

    async def create(self, db: AsyncSession, uuid: str, username: str) -> ConfirmToken:
        db_obj = self.model(username=username, token=uuid)
        await db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)

    async def get_username(self, db: AsyncSession, token: str):
        st = select(self.model).filter_by(token=token).first()
        res = await db.execute(st)
        username = res.username
        await res.delete()
        return username

crudtoken = CrudToken(ConfirmToken)
