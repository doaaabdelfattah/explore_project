"""
insert data
"""

import base64
import os
from sqlalchemy import func
from os import getenv
from models import storage
import uuid
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel



class Data():
    # users
    def user_data():
        user1 = User(
            #id = str(uuid.uuid4()),
            name='Alshimaa Mamdouh',
            email='alshimaa.mamdouh.abdelaziz@gmail.com',
            address='6th october',
            phone='23447677878'
            )
        user1.save()
        
        user2 = User(
            #id = str(uuid.uuid4()),
            name = 'Doaa Abdelfattah',
            email = 'doaa.abdelfattah@gmail.com',
            address = 'shorouk',
            phone = '5555555'
            )
        user2.save()
    #-----------------------------------------------------
    # packages
    def package_data():
        path1 = 'layout/images/rome.jpg'
        path2 = 'layout/images/egypt.jpg'
        path3 = 'layout/images/france.jpg'
        
        with open(path1, 'rb') as f:
            binary1 = base64.b64encode(f.read())
        
        with open(path2, 'rb') as f:
            binary2 = base64.b64encode(f.read())
        
        with open(path3, 'rb') as f:
            binary3 = base64.b64encode(f.read())
            
            
        package1 = Package(
            #id = str(uuid.uuid4()),
            package_name = 'Italy',
            price = '300$',
            description1 = 'fhgfhfhfhf',
            description2 = 'ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image = binary1
            )
        package1.save()
            
        package2 = Package(
            #id = str(uuid.uuid4()),
            package_name = 'Egypt',
            price = '300$',
            description1 = 'fhgfhfhfhf',
            description2 = 'ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image = binary2
            )
        package2.save()

        package3 = Package(
            #id = str(uuid.uuid4()),
            package_name = 'France',
            price = '300$',
            description1 = 'fhgfhfhfhf',
            description2 = 'ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image = binary3
            )
        package3.save()

#------------------------------------------------------------------------

