

from sqlalchemy import func
from os import getenv
from flask import Flask, redirect, render_template, request
from models import storage
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel
from models.data import Data

# Initialize Flask app
app = Flask(__name__)
#app.debug = True

# Routes
Data.user_data()
Data.package_data()
@app.route('/')
def index():
    # all packages
    packages = storage.all(Package).values()
    packages = sorted(packages, key=lambda k: k.package_name)

    #print(packages)
    return render_template('index.html', packages=packages)


""" @app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        packages = storage.all(Package).values()
        # Filter packages by name containing the search term
        filtered_packages = [package for package in packages if search_term.lower(
        ) in package.package_name.lower()]
        return render_template('index.html', packages=filtered_packages)
    return render_template('index.html') """


""" @app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']

        # Create a new user instance
        new_user = User(name=name, email=email, address=address, phone=phone)

        # Add the user to the database
        storage.new(new_user)
        storage.save()

        # Redirect to the home page or any other page after registration
        return redirect('register.html')

    return render_template('register.html') """

# print('main')
#user = User(
#    name='Alshimaa Mamdouh',
#    email='alshimaa.mamdouh.abdelaziz@gmail.com',
#   address='6th october',
#    phone='23447677878'
# )
# user.save()



if __name__ == '__main__':
   #app.run(host='0.0.0.0', port=5000)
   #storage.reload()
   app.run()
    
