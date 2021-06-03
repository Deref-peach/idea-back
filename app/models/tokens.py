from app.db.base import Base
from sqlalchemy import VARCHAR, Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class ConfirmToken(Base):
    __tablename__ = "token"
    token = Column(VARCHAR(36), primary_key=True)
    username = Column(VARCHAR(32), ForeignKey('user.username'))
    action = Column(VARCHAR())
    user = relationship("User")
