

import base64
import ssl
from sqlalchemy import func
import sys
import os
from os import getenv
from flask import Flask, redirect, render_template, request, flash, session, url_for
from models import storage
from models.user import User
from models.booking import Booking
from models.package import Package
from models.base_model import Base, BaseModel
from models.data import Data
from models.all_packages import GetData
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'abcdefg123456'
# app.debug = True


Data.package_data()
# Routes



@app.route('/', methods=['GET', 'POST'])
def index():
    # all packages
    packages = GetData.all()
    packages = sorted(packages, key=lambda k: k.package_name)

    # decode image
    image_list = GetData.decode(packages)

    #check username
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None

    if request.method == 'POST':
        search_term = request.form['destination']
        # Filter packages by name containing the search term
        filtered_packages = GetData.filtered(search_term)
        image_list2 = GetData.decode(filtered_packages)

        return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=packages, user_name=user_fname)

    return render_template('index.html', packages=image_list, pagetitle="Home", user_name=user_fname)


@app.route('/submit_booking', methods=['GET', 'POST'])
def submit_booking():
    # all packages
    packages_submit = GetData.all()
    packages_submit = sorted(packages_submit, key=lambda k: k.package_name)

    #check username
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None


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

           ############# Sending Email##########################

            # Email and password for Gmail account
            sender_email = "booking.online.alx@gmail.com"
            password = "glbg hlkl mlts urat"  # using app password
            # Recipient email

            receiver_email1 = "alshimaa.mamdouh.abdelaziz@gmail.com"
            receiver_email2 = "doaa.abdalfattah@gmail.com"
            # Create a multipart message and set headers
            message1 = MIMEMultipart()
            message1["From"] = sender_email
            message1["To"] = receiver_email1
            message1["Subject"] = "New Booking"
            message2 = MIMEMultipart()
            message2["From"] = sender_email
            message2["To"] = receiver_email2
            message2["Subject"] = "Confirm Booking"
            # Add body to email
            body1 = (
                "First Name: " + request.form['f-name'] + "\n" +
                "Last Name: " + request.form['l-name'] + "\n" +
                "Phone No: " + request.form['phone'] + "\n" +
                "Email: " + request.form['email'] + "\n" +
                "Choosed Package: " + request.form['destination'] + "\n" +
                "Message: " + request.form['message']
            )
            body2 = ("Your Booking confirmed please wait till the admin contact you" + "\n" +
                     "Regards," + "\n" + "Online Booking Admin")
            message1.attach(MIMEText(body1, "plain"))
            message2.attach(MIMEText(body2, "plain"))

            # Connect to the SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                # Encrypt the connection
                server.starttls()
                # Log in to the server
                server.login(sender_email, password)
                # Send email
                server.send_message(message1)
                server.send_message(message2)

       ######################## END Of Sending Email ###################

            # Flash a success message
            flash('Booking was successfully submitted')
    return render_template('submit_booking.html', packages_submit=packages_submit, user_name=user_fname)


@app.route('/packages', methods=['GET', 'POST'])
def packages():
    #check username
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None
    # all packages for the dropdown list
    packages_reg = GetData.all()
    packages_reg = sorted(packages_reg, key=lambda k: k.package_name)
    image_list1 = []
    image_list2 = []
    image_list1 = GetData.decode(packages_reg)

    if request.method == 'POST':
        search_term = request.form['destination']
        # Filter packages by name containing the search term
        filtered_packages = GetData.filtered(search_term)
        image_list2 = GetData.decode(filtered_packages)

        if not filtered_packages:
            image_list2 = image_list1


        return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=packages_reg, user_name=user_fname)

    return render_template('packages.html', pagetitle="Packages", filtered_packages=image_list2, packages=image_list1, user_name=user_fname)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    #check phone
    if 'user_phone' in session:
        user_phone = session['user_phone']
    else:
        user_phone = None
    
    #check email
    if 'user_email' in session:
        user_email = session['user_email']
    else:
        user_email = None
    
    #check fname and lname
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None

    if 'user_lname' in session:
        user_lname = session['user_lname']
    else:
        user_lname = None
    #check username
    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    if request.method == "POST":
        ############# Sending Email##########################

            # Email and password for Gmail account
            sender_email = "booking.online.alx@gmail.com"
            password = "glbg hlkl mlts urat"  # using app password
            # Recipient email
            print (request.form)

            receiver_email = request.form['email']
            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "Conact us request"
           
            # Add body to email
            body = (
                "First Name: " + request.form['f-name'] + "\n" +
                "Last Name: " + request.form['l-name'] + "\n" +
                "Phone No: " + request.form['phone'] + "\n" +
                "Message: " + request.form['message']
            )
            message.attach(MIMEText(body, "plain"))

            # Connect to the SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                # Encrypt the connection
                server.starttls()
                # Log in to the server
                server.login(sender_email, password)
                # Send email
                server.send_message(message)

       ######################## END Of Sending Email ###################
    return render_template('contact.html', pagetitle="Contact Us", user_name=user_fname, user_email=user_email, user_phone=user_phone,  user_lname= user_lname,  user_fname= user_fname)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #check username
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None

    if request.method == 'POST':
        if not request.form['f-name'] or not request.form['f-name'] or not request.form['phone'] or not request.form['email'] or not request.form['password'] or not request.form['username']:
            flash('Please enter all the fields', 'error')
        elif request.form['password'] != request.form['confirmPassword']:
            flash('password nt matched', 'error')

        else:
            #print("hello save user")
            user = User(
            fname=request.form['f-name'],
            lname=request.form['l-name'],
            username=request.form['username'],
            email=request.form['email'],
            address="any thing",
            password=request.form['password'],
            phone=request.form['phone'],
            is_admin=False
            )
            user.save()
            flash('Account created successfully. Please sign in.', 'success')
            return render_template('login.html', pagetitle="Login/Register")
    
    return render_template('signup.html', pagetitle="Sign Up", user_name=user_fname)


@app.route('/login', methods=['GET', 'POST'])
def login():
    #check username
    if 'user_fname' in session:
        user_fname = session['user_fname']
    else:
        user_fname = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Data.get_user(username)
        if user and user.password == password:
            session['user_id'] = user.id
            session['user_name'] = user.username
            session['user_email'] = user.email
            session['user_phone'] = user.phone
            session['user_fname'] = user.fname
            session['user_lname'] = user.lname
            
            flash('Logged in successfully!', 'success')
            # all packages
            packages = GetData.all()
            packages = sorted(packages, key=lambda k: k.package_name)
            # decode image
            image_list = GetData.decode(packages)
            return render_template('index.html', packages=image_list, pagetitle="Home", user_name=user.fname)
        else:
            flash('Invalid username or password. Please try again.', 'error')
    return render_template('login.html', pagetitle="Login/Register", user_name=user_fname)

@app.route('/logout')
def logout():
    # Clear the user's session
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    session.pop('user_phone', None)
    session.pop('user_fname', None)
    session.pop('user_lname', None)
    # all packages
    packages = GetData.all()
    packages = sorted(packages, key=lambda k: k.package_name)
    # decode image
    image_list = GetData.decode(packages)
    return render_template('index.html', packages=image_list, pagetitle="Home", user_name=None)


if __name__ == '__main__':
    # storage.reload()
    app.run()
