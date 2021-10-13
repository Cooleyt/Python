from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_bcrypt import Bcrypt 

from flask_app.models.email import User

bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/email', methods=['POST'])
def create_email():
    
    if User.validate_email(request.form):
        data = {
            'email': request.form['email'],
        }
        User.create_email(data)
        flash("You've created an email'!")
        return redirect('/success')

    else: 
        flash("Email is invalid")
        return redirect('/')

@app.route('/success')
def success():

    email = User.get_all_emails()

    # if len(users) != 1:
    #     flash('Email is incorrect')
    #     return redirect('/')

    # User.create_email()
    # flash("Valid email, thank you'!")

    # email = users[0]

    return render_template('success.html', emails = email)




