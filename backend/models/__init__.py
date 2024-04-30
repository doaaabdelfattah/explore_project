from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()