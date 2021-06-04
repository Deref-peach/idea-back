from sqlalchemy.sql.sqltypes import Boolean, Integer
from app.db.base import Base
from sqlalchemy import CHAR, VARCHAR, Column
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(VARCHAR(32), unique=True, nullable=False)
    fullname = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(32), nullable=False, unique=True)
    resume = Column(VARCHAR(255))
    # todo skills
    hashed_password = Column(CHAR(128), nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    token = relationship("ConfirmToken", cascade="all, delete")

    # def __repr__(self):
    #     return f"User<id={self.id}, username={self.username}>"

