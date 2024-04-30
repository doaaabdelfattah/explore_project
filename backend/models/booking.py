"""
booking
"""

from os import getenv
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel


class Booking(BaseModel,Base):
    """booking"""

    __tablename__ = "bookings"


    #for database mapping
    
    package_id = Column(String(60), ForeignKey('packages.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    