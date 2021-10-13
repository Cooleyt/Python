from flask import render_template, request, redirect

from flask_app import app

from flask_app.model.ninja import Ninja
from flask_app.model.dojos import Dojo

@app.route("/dojos")
def index():
    dojo = Dojo.get_all()
    print(dojo)
    return render_template("home.html", dojos = dojo)

@app.route('/show/<int:dojo_id>/dojos')    
def dojo_info(dojo_id):
    dojo = Dojo.get_one_with_ninjas({'id': dojo_id})
    return render_template('dojo_show.html', dojo = dojo)


@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    dojo_id = int(request.form['dojo_id'])
    Ninja.create_ninja(data)

    return redirect(f'/show/{dojo_id}/dojos')

@app.route('/ninja/new')
def new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')


@app.route('/ninjas/<int:ninja_id>')
def ninja_info(ninja_id):

    data = {
        'id': ninja_id
    }

    ninja = Ninja.get_single_ninja(data)

    dojos = Dojo.get_all_dojos()

    return render_template('dojo_show.html', ninja = ninja, dojos = dojos)