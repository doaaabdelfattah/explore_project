


import base64
from sqlalchemy import func
import sys, os
from os import getenv
from flask import Flask, redirect, render_template, request, flash
from models import storage
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel
from models.data import Data

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'abcdefg123456'
# app.debug = True

# Routes
Data.user_data()
Data.package_data()

@app.route('/')
def index():
    
   
     #all packages
    packages = storage.all(Package)
    length = len(storage.all(Package))
    packages = sorted(packages, key=lambda k: k.package_name)
    # print("Number of packages:", length)
    image_list = []
    
    for package in packages:
        if hasattr(package, 'image') and package.image:
            image_list.append({'image':base64.b64encode(package.image).decode('utf-8'),
                               'description1':package.description1,
                               'package_name':package.package_name,
                               'price':package.price})

            
 
    return render_template('index.html', packages=image_list, pagetitle="Home")


# @app.route('/submit_booking.html', methods=['GET', 'POST'])
# def submit_booking():
#     if request.method == 'POST':
#         if not request.form['f-name'] or not request.form['phone'] or not request.form['email'] or not request.form['destination']:
#             flash('Please enter all the fields', 'error')
#         else:
#             booking = Booking(
#                 first_name=request.form['f-name'],
#                 last_name=request.form['l-name'],
#                 phone=request.form['phone'],
#                 email=request.form['email'],
#                 destination=request.form['destination'],  # Added comma here
#                 message=request.form['message']
#             )
#             # Add the Booking object to the database session & save
#             try:
#                 booking.save()
#             except Exception as e:
#                 print(e)

            
#             # Flash a success message
#             flash('Booking was successfully submitted')
#     return render_template('submit_booking.html')
@app.route('/submit_booking', methods=['GET', 'POST'])
def submit_booking():
    if request.method == 'POST':
        if not request.form['f-name'] or not request.form['phone'] or not request.form['email'] or not request.form['destination']:
            flash('Please enter all the fields', 'error')
        else:
            booking = Booking(

                first_name=request.form['f-name'],
                last_name=request.form['l-name'],
                phone=request.form['phone'],
                email=request.form['email'],
                destination=request.form['destination'],  # Added comma here
                message=request.form['message']
            )
            # Add the Booking object to the database session & save
            try:
                booking.save()
            except Exception as e:
                print(e)
                print('Catch Error')
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)

            
            # Flash a success message
            flash('Booking was successfully submitted')
    return render_template('submit_booking.html')



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
# user = User(
#    name='Alshimaa Mamdouh',
#    email='alshimaa.mamdouh.abdelaziz@gmail.com',
#   address='6th october',
#    phone='23447677878'
# )
# user.save()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    # storage.reload()
    app.run()