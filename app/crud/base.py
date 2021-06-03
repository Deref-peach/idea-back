from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from sqlalchemy.ext.asyncio import AsyncSession
from dataclasses import asdict
from app.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", )
UpdateSchemaType = TypeVar("UpdateSchemaType", )


class CrudBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A strawberry model (schema) class
        """
        self.model = model

    async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()


    async def create(self, db: AsyncSession, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = asdict(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        await db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
        

    async def update(# TODO
        self,
        db: AsyncSession,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = asdict(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = asdict(obj_in ) 
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field]) # TODO: тут может ноне прилететь, дыру запили, чмо
        await db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        await db.delete(obj)
        await db.commit()
        return obj
