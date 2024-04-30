"""
user
"""

from os import getenv
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class User(BaseModel,Base):
    """user"""

    __tablename__ = "users"


    #for database mapping
    
    username = Column(String(128), nullable=True)
    name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    
 