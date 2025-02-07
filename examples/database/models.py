from sqlalchemy import Column, Integer, String

from .core import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password = Column(String)
    name = Column(String, unique=True)
    age = Column(Integer)
