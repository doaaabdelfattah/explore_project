"""
booking
"""

from os import getenv
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel


class Booking(BaseModel, Base):
    """booking"""

    __tablename__ = "bookings"

    # for database mapping

    package_id = Column(String(60), ForeignKey('packages.id'), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=True)

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    destination = Column(String(128), nullable=True)
    message = Column(String(500), nullable=True)
