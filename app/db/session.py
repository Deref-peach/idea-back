from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.POSTGRES_DSN, pool_pre_ping=True, echo=settings.DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, class_=AsyncSession, bind=engine)

def get_session() -> AsyncSession:
    return SessionLocal()
