from app.db.base import Base
from sqlalchemy import CHAR, Integer, VARCHAR, Column

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(20), nullable=False)
    hashed_password = Column(CHAR(128), nullable=False)

    def __repr__(self):
        return f"User<id={self.id}, username={self.username}>"
