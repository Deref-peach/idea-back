from app.db.base import Base
from sqlalchemy import VARCHAR, Column, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta


class ConfirmToken(Base):
    __tablename__ = "token"
    token = Column(VARCHAR(36), primary_key=True)
    id = Column(Integer, ForeignKey('user.id'))
    created_date = Column(DateTime, default=lambda _: datetime.utcnow() + timedelta(days=1))
    user = relationship("User")
