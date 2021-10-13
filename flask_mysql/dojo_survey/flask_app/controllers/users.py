from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.survey import Survey

@app.route("/")
def index():
    return render_template("dojo_survey.html")


@app.route('/create', methods=['POST'])
def validate_name():
    
    if not Survey.validate_name(request.form):
        return redirect('/')

    Survey.save(request.form)

    return redirect("/")


@app.route('/show/<int:survey_id>')
def sumbitted_info(survey_id):

    data = {
        'id': survey_id
    }

    survey = Survey.get_single_survey(data)

    return render_template('results.html', surveys = survey)

