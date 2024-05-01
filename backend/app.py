

from sqlalchemy import func
from os import getenv
from models import storage
from models.user import User


"""
 Objects creations
"""
#print('main')
user  = User(
        name = 'Alshimaa Mamdouh',
        email = 'alshimaa.mamdouh.abdelaziz@gmail.com',
        address = '6th october',
        phone = '23447677878' 
)
user.save()

if __name__ == '__main__':
        storage.reload()