from models import storage
from models.user import User

from os import getenv


"""
 Objects creations
"""
print('main')
user  = User(code = 'AB',
        name = 'ABC',
        email = '8989999999999999999999999999999',
        address = 'hjhghjgjhg',
        phone = 'fhgfhgfhf')
user.save()
if __name__ == '__main__':
        storage.reload()