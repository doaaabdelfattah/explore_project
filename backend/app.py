

import base64
import ssl
from sqlalchemy import func
import sys
import os
from os import getenv
from flask import Flask, redirect, render_template, request, flash
from models import storage
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel
from models.data import Data
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'abcdefg123456'
# app.debug = True


Data.user_data()
Data.package_data()
# Routes


@app.route('/', methods=['GET', 'POST'])
def index():
    # all packages
    packages = storage.all(Package)
    packages = sorted(packages, key=lambda k: k.package_name)

    # decode image
    image_list = []

    for package in packages:
        if hasattr(package, 'image') and package.image:
            image_list.append({'image': base64.b64encode(package.image).decode('utf-8'),
                               'description1': package.description1,
                               'package_name': package.package_name,
                               'price': package.price})
            
    if request.method == 'POST':
        search_term = request.form['destination']
        # Filter packages by name containing the search term
        filtered_packages = [package for package in packages if search_term.lower(
        ) in package.package_name.lower()]

        image_list2 = []

        for pc in filtered_packages:
            if hasattr(pc, 'image') and pc.image:
                image_list2.append({'image': base64.b64encode(pc.image).decode('utf-8'),
                               'description1': pc.description1,
                               'package_name': pc.package_name,
                               'price': pc.price})


        
        return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=packages  )

    return render_template('index.html', packages=image_list, pagetitle="Home")


@app.route('/submit_booking', methods=['GET', 'POST'])
def submit_booking():
    # all packages
    packages_submit = storage.all(Package)
    packages_submit = sorted(packages_submit, key=lambda k: k.package_name)

    if request.method == 'POST':
        if not request.form['f-name'] or not request.form['phone'] or not request.form['email'] or not request.form['destination']:
            flash('Please enter all the fields', 'error')
        else:
            booking = Booking(

                first_name=request.form['f-name'],
                last_name=request.form['l-name'],
                phone=request.form['phone'],
                email=request.form['email'],
                package_id=request.form['destination'],  # Added comma here
                message=request.form['message']
            )
            # Add the Booking object to the database session & save

            booking.save()

            """ ############# Sending Email##########################

            # Email and password for Gmail account
            sender_email = "bookingonline265@gmail.com"
            password = "glbg hlkl mlts urat"
            # Recipient email
            
            receiver_email = "alshimaa.mamdouh.abdelaziz@gmail.com"
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "New Booking"
            # Add body to email
            body = "first_name"+ request.form['f-name']+"last_name"+request.form['l-name']+"phone"+request.form['phone']+"email"+request.form['email']+"package_id"+request.form['destination']+"message"+request.form['message']
            
            message.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                # Encrypt the connection
                server.starttls()
                # Log in to the server
                server.login(sender_email, password)
                # Send email
                server.send_message(message) """
            # Flash a success message
            flash('Booking was successfully submitted')
    return render_template('submit_booking.html', packages_submit=packages_submit)


@app.route('/packages')
def packages():
    #all packages for the dropdown list
    packages_reg = storage.all(Package)
    packages_reg = sorted(packages_reg, key=lambda k: k.package_name)
    image_list2 = []

    if request.method == 'POST':
        #take search item
        search_term = request.form['destination']
        # Filter packages by name containing the search term
        filtered_packages = [package for package in packages if search_term.lower(
        ) in package.package_name.lower()]

        #decode image
        for pc in filtered_packages:
            if hasattr(pc, 'image') and pc.image:
                image_list2.append({'image': base64.b64encode(pc.image).decode('utf-8'),
                               'description1': pc.description1,
                               'package_name': pc.package_name,
                               'price': pc.price})


        
        return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=packages_reg )
    
    return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=packages_reg)


@app.route('/contact')
def contact():
    return render_template('contact.html', pagetitle="Contact Us")


    
        
    
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


if __name__ == '__main__':
    # storage.reload()
    app.run()
