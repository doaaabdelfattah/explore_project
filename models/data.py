"""
insert data
"""

import base64
import os
from sqlalchemy import func
from os import getenv
from models import storage
import uuid
from models.booking import Booking
from models.package import Package
from models.user import User
from models.base_model import Base, BaseModel


class Data():
    @staticmethod
    def get_user(filter_email):
        users = storage.all(User)
        # Find the first user with email containing the filter email
        for user in users:
            if filter_email.lower() in user.email.lower():
                return user
        return None  # Return None if no user matches the filter criteria
    # users
    def user_data():
        user1 = User(
            # id = str(uuid.uuid4()),
            name='Alshimaa Mamdouh',
            email='alshimaa.mamdouh.abdelaziz@gmail.com',
            address='6th october',
            phone='23447677878'
        )
        user1.save()

        user2 = User(
            # id = str(uuid.uuid4()),
            name='Doaa Abdelfattah',
            email='doaa.abdelfattah@gmail.com',
            address='shorouk',
            phone='5555555'
        )
        user2.save()
    # -----------------------------------------------------
    # packages

    def package_data():
        path1 = 'static/images/rome.jpg'
        path2 = 'static/images/egypt.jpg'
        path3 = 'static/images/france.jpg'

        with open(path1, 'rb') as f:
            # binary1 = base64.b64encode(f.read())
            binary1 = f.read()

        with open(path2, 'rb') as f:
            # binary2 = base64.b64encode(f.read())
            binary2 = f.read()

        with open(path3, 'rb') as f:
            # binary3 = base64.b64encode(f.read())
            binary3 = f.read()

        package1 = Package(
            # id = str(uuid.uuid4()),
            package_name='Italy',
            price='660$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary1
        )
        package1.save()

        package2 = Package(
            # id = str(uuid.uuid4()),
            package_name='Egypt',
            price='300$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary2
        )
        package2.save()

        package3 = Package(
            # id = str(uuid.uuid4()),
            package_name='France',
            price='300$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary3
        )
        package3.save()

# ------------------------------------------------------------------------
