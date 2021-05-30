from sqlalchemy import Column, String, Integer, VARCHAR, ForeignKey, Boolean
from app.db.base import Base

class Task(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True, index=True)
    public = Column(Boolean, default=False)
    completed = Column(Boolean, default=False)
    uid = Column(Integer, ForeignKey('Users.id'))
    text = Column(String, default='None', nullable=False)
    name = Column(VARCHAR(30), nullable=False)

    def __repr__(self):
        return f'Task<id={self.id}, recordname={self.name}>'
