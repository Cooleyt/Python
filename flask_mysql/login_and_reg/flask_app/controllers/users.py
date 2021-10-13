from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_bcrypt import Bcrypt 

from flask_app.models.user import User

bcrypt = Bcrypt(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def register_user():
    #first validate users names, emails, passwords.
    # print(User.validate_user(request.form)) -- to test
    if User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        (request.form['password'])
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        User.create_user(data)
        flash("You are now registered, you can log in!")
    #if user is valid then create it in the workbench
    #redirect back to index
    return redirect('/')

@app.route('/users/login', methods = ['POST'])
def login():

    users = User.get_user_by_first_name(request.form)

    if len(users) != 1:
        flash('First name or password is incorrect')
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect.')
        return redirect('/')

    flash('Name/password correct')
    return redirect('/wall')

@app.route('/user/logout')
def logout():
    session.clear()
    flash("You've logged out")
    return redirect('/')



