from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.user import User


@app.route("/")
def index():
    users = User.get_all_users()
    print(users)
    return render_template("index.html", users = users)

@app.route('/users/<int:user_id>/userinfo')    
def user_info(user_id):
    data = {
        'id': user_id
    }
    user = User.users_info(data)
    print(user)
    return render_template('user_info.html', one_user = user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.users_info(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:user_id>/update', methods = ['POST'])    
def edit(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    user = User.edit(data)
    print(user)
    # return redirect('/')
    return redirect(f'/users/{user_id}/userinfo')


@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect('/')
