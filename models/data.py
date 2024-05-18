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
    
    # packages

    def package_data():
        path1 = 'static/images/rome.jpg'
        path2 = 'static/images/egypt.jpg'
        path3 = 'static/images/france.jpg'

        with open(path1, 'rb') as f:
            binary1 = f.read()

        with open(path2, 'rb') as f:
            binary2 = f.read()

        with open(path3, 'rb') as f:
            binary3 = f.read()

        package1 = Package(
            package_name='Italy',
            price='660$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary1
        )
        package1.save()

        package2 = Package(
            package_name='Egypt',
            price='300$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary2
        )
        package2.save()

        package3 = Package(
            package_name='France',
            price='300$',
            description1='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            description2='ghfhgfhfhjgjhghjghjghjgjhghgfhgfghfhgjgjhhjhghghhgghfg',
            image=binary3
        )
        package3.save()

# ------------------------------------------------------------------------
