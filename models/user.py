"""
user
"""

from os import getenv
from sqlalchemy import Boolean, Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """user"""

    __tablename__ = "users"

    # for database mapping
    # for database mapping

    fname = Column(String(128), nullable=True)
    lname = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    bookings = relationship("Booking", backref="user", cascade="all,delete")
