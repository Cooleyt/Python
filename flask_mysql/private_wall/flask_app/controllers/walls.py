from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models.wall import Wall

@app.route('/wall')
def dashboard():
    if 'user_id' not in session:
        flash('Log in to view this page')
        return redirect('/')

    return render_template('wall.html', user = Wall.get_all_messages())

@app.route('/create/message', methods=['POST'])
def create_message():
    if Wall.validate_message(request.form):
        data = {
            'message': request.form['message'],
            'users_id': session['user_id']
        }
        message_id = Wall.new_message(data)
        print(message_id)

        return redirect('/')
    return redirect('/wall')

