"""
dbStorage
"""
import pyodbc # for sql server
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from dotenv import load_dotenv, dotenv_values
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
load_dotenv()
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
		self.__engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(getenv('SQL_USER'),getenv('SQL_PASS'),getenv('SQL_HOST'),getenv('SQL_DB')),echo=True)
		
		# self.__engine = create_engine(uri,echo=True)

		if getenv('ENV') == 'test':
			Base.metadata.drop_all(self.__engine)
	
	

	def all(self, cls=None):
		"""query on the current database session"""
		new_dict = {}
		for clss in all_classes:
			if cls is None or cls is all_classes[clss] or cls is clss:
				objs = self.__session.query(all_classes[clss]).all()
				for obj in objs:
					key = obj.__class__.__name__ + '.' + obj.id
					new_dict[key] = obj
					return (new_dict)
	
	
	def reload(self):
		"""Create tables and current database session"""
		# print(self.__engine)
		# print('dbStorage-reload')
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		Session = scoped_session(session_factory)
		self.__session = Session()		
	
	
	def save(self):
		"""Commit changes to the current databases session"""
		# print('dbStorage-Save')
		self.__session.commit()
	

	def close(self):
		""" call close on private session. """
		self.__session.close()
        

	def new(self, obj):
		"""new"""
		self.__session.add(obj)