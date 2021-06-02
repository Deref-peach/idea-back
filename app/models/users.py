from app.db.base import Base
from sqlalchemy import CHAR, Integer, VARCHAR, Column

class User(Base):
    __tablename__ = 'Users'
    username = Column(VARCHAR(32), primary_key=True, index=True)
    fullname = Column(VARCHAR(32), nullable=False)
    email = Column(VARCHAR(32), nullable=False)
    resume = Column(VARCHAR(255))
    # todo skills
    hashed_password = Column(CHAR(128), nullable=False)
    
    # def __repr__(self):
    #     return f"User<id={self.id}, username={self.username}>"
