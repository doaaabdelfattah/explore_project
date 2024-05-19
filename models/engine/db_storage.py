"""
dbStorage
"""
#import pyodbc  # for sql server
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
#from dotenv import load_dotenv, dotenv_values
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel

all_classes = {"BaseModel": BaseModel, "User": User, "booking": Booking,
               "package": Package}

# import MySQLdb

# print('load_dot')
#load_dotenv()
# print(getenv('SQL_PASS') )
# print(getenv('SQL_USER') )

class DBStorage:
    """DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """__init__"""
        # import PyMySQL

        # uri = 'mysql+pymysql://root@localhost/'+getenv('SQL_DB')
        # print('mysql+pymysql://{}:{}@{}/{}'.format(getenv('SQL_USER'),getenv('SQL_PASS'),getenv('SQL_HOST'),getenv('SQL_DB')))
        self.__engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(
            'porto_dev', 'porto_dev_pwd', 'localhost', 'explore_project_db', echo=True)

        # self.__engine = create_engine(uri,echo=True)
        #if getenv('ENV') == 'test':
            #Base.metadata.drop_all(self.__engine)

    def all(self, cls):
        """Query all objects from the current database session"""
        objs = self.__session.query(cls).all()
        #print(objs)
        return objs

    def reload(self):
        """Create tables and current database session"""
        # print(self.__engine)
        # print('dbStorage-reload')
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def save(self):
        """Commit changes to the current databases session"""
        # print('dbStorage-Save')
        # try:
        self.__session.commit()
        """ except Exception as e:
            self.__session.rollback()
            print (str(e)) """

    def close(self):
        """ call close on private session. """
        self.__session.close()

    def new(self, obj):
        """new"""
        self.__session.add(obj)
