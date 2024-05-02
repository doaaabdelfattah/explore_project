"""
package
"""

from os import getenv
from sqlalchemy import Column, String, LargeBinary
from models.base_model import Base, BaseModel


class Package(BaseModel,Base):
    """package"""

    __tablename__ = "packages"


    #for database mapping
    
    package_name = Column(String(128), nullable=False)
    price = Column(String(128), nullable=False)
    description1 = Column(String(128), nullable=False)
    description2 = Column(String(128), nullable=False)
    image = Column(LargeBinary, nullable=True)
    