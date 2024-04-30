"""
base_model
"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

#for database mapping
Base = declarative_base()


class BaseModel:
    """docstring for BaseModel"""

    #for database mapping
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    createdDate = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updatedDate = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4)
        self.createdDate = datetime.now()
        self.updatedDate = datetime.now()
        if kwargs:
            if kwargs.get('__class__', None):
                del kwargs['__class__']
            for k, v in kwargs.items():
                if k == 'createdDate' or k == 'updatedDate':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__.update({k: v})

    def reload(self):
        """reload"""
        # print('baseModel reload')
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def save(self):
        """Save"""
        #print('baseModel Save')
        self.updatedDate = datetime.now
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)


    