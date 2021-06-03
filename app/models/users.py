from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from app.db.base import Base
from sqlalchemy import CHAR, Integer, VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid


class User(Base):
    __tablename__ = 'user'
    username = Column(VARCHAR(32), primary_key=True, index=True)
    fullname = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(32), nullable=False)
    resume = Column(VARCHAR(255))
    # todo skills
    hashed_password = Column(CHAR(128), nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    token = relationship("ConfirmToken", cascade="all, delete")

    # def __repr__(self):
    #     return f"User<id={self.id}, username={self.username}>"

class ConfirmToken(Base):
    __tablename__ = "token"
    token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(VARCHAR(32), ForeignKey('user.username'))
    user = relationship("User")
